import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3

#=====================================Create Detector/Detektörü Yarat=============================================
recognizer = cv2.face.LBPHFaceRecognizer_create() if hasattr(cv2, 'face') else cv2.face.createLBPHFaceRecognizer()
recognizer.read('Face Recg/trainingData.yml')
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
path = 'dataSet'

#=====================================Found from IDs/ID'lerden bul=============================================
def getProfile (id) :
    conn=sqlite3.connect ("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str (id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close ()
    return profile

#=======================Use Detector and Write Infos to Screen/Detektörü Kullan ve Verileri Ekrana Yaz==========================
cam = cv2.VideoCapture (0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read ()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])  
        profile = getProfile(id)  
        
        cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)

        if profile is not None:
            cv2.putText(im, f"Name: {profile[1]}", (x, y + h + 30), font, 0.8, (255, 255, 255), 2)
            cv2.putText(im, f"Age: {profile[2]}", (x, y + h + 60), font, 0.8, (255, 255, 255), 2)
            cv2.putText(im, f"Gender: {profile[3]}", (x, y + h + 90), font, 0.8, (255, 255, 255), 2)
            cv2.putText(im, f"City: {profile[4]}", (x, y + h + 120), font, 0.8, (255, 255, 255), 2)
        
       
    cv2.imshow('im',im)
    cv2.waitKey(10)