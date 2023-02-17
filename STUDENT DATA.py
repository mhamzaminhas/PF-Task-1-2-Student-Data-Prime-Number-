def stddata():
  input_numb = int(input("Total number of students in the class:\t"))
  math_std = int(input("Number of students with mathematics is\t"))
  bio_std = int(input("Number of Students with Bio\t"))
  print("Calculate the number of students without Math and Bio is:", input_numb-(math_std+bio_std))
  print("Calculate the number of students with Math and Bio is:", (math_std + bio_std))
stddata()