import os
import zipfile
from embeddings import get_embeddings
import psycopg2
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import psycopg2
import psycopg2.extras


UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['zip'])


app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "Learning"
DB_USER = "postgres"
DB_PASS = "H@mza1122"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            zip_ref = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
            zip_ref.extractall(UPLOAD_FOLDER)
            zip_ref.close()

            # fetch one image from the extracted images
            images_folder = os.path.join(UPLOAD_FOLDER, 'test')  # the folder where the extracted images are stored
            images = os.listdir(images_folder)  # list all the files in the folder
            if len(images) > 0:  # if there is at least one image file
                image_path = os.path.join(images_folder, images[0])  # get the path of the first image file
                embed = get_embeddings(image_path)
                img_name = image_path.split('\\')[-1]
                cursor.execute("INSERT INTO upload (title,embedding, name) VALUES (%s,%s,%s)", (image_path, str(embed), img_name))
                conn.commit()

                return render_template('image.html', image_path=image_path)  # display the first image file

            else:  # if there is no image file in the folder
                flash('No image file found in the uploaded zip file')
                return redirect(request.url)
        else:  # if the uploaded file is not a zip file
            flash('Allowed file type is zip')
            return redirect(request.url)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
