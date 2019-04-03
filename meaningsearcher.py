import pyautogui as py
import cv2
import csv
import pytesseract
from PIL import Image,ImageGrab
import numpy as np
from win10toast import ToastNotifier
toaster=ToastNotifier()
#import socket
#import os
#os.startfile("Project1.exe")
#s = socket.socket()
#port = 1234
#s.bind(('', port))
#s.listen(5)
#c, addr = s.accept()
#uio=input()
q1=42
q2=639#py.position()
#uio=input()
m1=1776
m2=1060
#py.position()
fgfg='k'
intx=6
inty=2
def imageGrab():
   box = (q1,q2,m1,m2)
   image = ImageGrab.grab(box)
   return  image
while True:
 #c.recv(1024).decode('ascii')
 #c.send("hg".encode('ascii'))
 img=cv2.inRange(np.array(imageGrab()),(250,250,250),(256,256,256))
 ker=np.ones((2,2),np.uint8)
 kil=cv2.dilate(img,ker,iterations=1)
 x,y=py.position()
 if (x<q1 or x > m1) or (y<q2 or y>m2):
  x=0
  y=0
  try:
   root.destroy()
  except:
   pass
  continue
 else :
  x=x-q1
  y=y-q2
 lenx=m1-q1
 leny=m2-q2
 if (x-270<0):
  xs=0
 else:
  xs=x-270
 if x+270>lenx:
  xe=lenx-1
 else:
  xe=x+270
 y1=0
 for y1 in range(y,leny):
  for d1 in range(xs,xe):
   if kil[y1,d1]!=0:
     break
  if d1==xe-1:
   break
 y2=y1
 d1=0
 if y==len(kil):
  continue
 for y1 in range(y,0,-1):
  for d1 in range(xs,xe):
   if kil[y1,d1]!=0:
     break
  if d1==xe-1:
   break
 count=0
 for x1 in range(x,0,-1):
  if count > intx :
   break
  for y in range(y1,y2+1):
   if kil[y,x1]!=0:
    break
  if y==y2:
   count=count+1
  else:
   count=0
 count=0
 for xd in range(x,lenx,1):
  if count>intx:
   break
  for y in range(y1,y2+1):
   if kil[y,xd]!=0:
    break
  if y==y2:
   count=count+1
  else:
   count=0
 #print(j)
 dda=kil[y1:y2+1,x1:xd]
 cv2.imshow('k',dda)
 cv2.waitKey(200)
 jkl=pytesseract.image_to_string(dda)
 #c.send(jkl.encode('ascii'))
 if (jkl=="" or jkl==fgfg) :
  continue
 #print(jkl)
 try:
  if not(jkl[-1].isalpha()):
   z=jkl[0].capitalize()+jkl[1:-1].lower()+" "
  else:
   z=jkl[0].capitalize()+jkl[1:].lower()+" "
  #print(z)
  with open(z[0].capitalize()+".csv",mode='r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for j in csv_reader:
     if j!=[]:
      if z in j[0][0:len(z)+1]:
       print(j[0])
       toaster.show_toast("",j[0])
       #c.send(j[0].encode('ascii'))
  #print(time.time()-t)
 except:
  #c.send("k".endcode("ascii"))
  continue
 fgfg=jkl