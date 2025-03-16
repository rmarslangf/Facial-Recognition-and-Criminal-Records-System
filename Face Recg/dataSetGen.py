import cv2
import os
import sqlite3
import tkinter as tk
from tkinter import simpledialog

#=====================Create Detector/Detector Yarta=====================================
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#=====================Get info popup/Bilgileri Al popupı=====================================
def get_user_info():
    root = tk.Tk()
    root.withdraw()  

  
    id = simpledialog.askstring("ID", "Enter your ID:")
    name = simpledialog.askstring("Name", "Enter your Name:")
    
    root.quit()
    return id, name

#=====================Save To Database/Database e Kaydet=====================================
def InsertOrUpdate(ID, Name):
    conn = sqlite3.connect("FaceBase.db")
    cursor = conn.execute(f"SELECT * FROM People WHERE ID={ID}")
    
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1

    if isRecordExist == 1:
        cmd = f"UPDATE People SET Name='{Name}' WHERE ID={ID}"
    else:
        cmd = f"INSERT INTO People (ID, Name) VALUES ({ID}, '{Name}')"

    conn.execute(cmd)
    conn.commit()
    conn.close()

#=====================Get info/Bilgileri Al=====================================
id, name = get_user_info()
InsertOrUpdate(id, name)

#=====================Get Faces/Yüz verilerini Topla=====================================
sampleNum = 0
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite(f"dataSet/User.{id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)

    cv2.imshow("Face", im)
    cv2.waitKey(1)

    if sampleNum > 20:
        break

cam.release()
cv2.destroyAllWindows()
