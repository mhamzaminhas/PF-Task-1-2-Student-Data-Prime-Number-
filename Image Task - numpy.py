#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from PIL import Image
img = cv2.imread(r"C:\Users\Minhas\Downloads\baboon.png")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask=cv2.inRange(hsv,lower_red,upper_red)
img[mask>0]=[0,0,0]

cv2.imshow('Modified.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




