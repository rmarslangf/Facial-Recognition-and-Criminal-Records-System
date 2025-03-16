import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import subprocess
import os, cv2
import signal

def run_app1():
    global process1
    process1 = subprocess.Popen(["python", "dataSetGen.py"])

def run_app2():
    global process2
    process2 = subprocess.Popen(["python", "trainner.py"])

def run_app3():
    global process3
    process3 = subprocess.Popen(["python", "detector.py"])

def exit_program():
    
    if 'process1' in globals():
        os.kill(process1.pid, signal.SIGTERM)  
    if 'process2' in globals():
        os.kill(process2.pid, signal.SIGTERM)  
    if 'process3' in globals():
        os.kill(process3.pid, signal.SIGTERM)  
    
    
    cv2.destroyAllWindows()

    
    

root = tk.Tk()
root.title("Face Recognition Main Menu")
root.geometry("600x400")  
root.configure(bg="#f0f0f0")  


bg_image = Image.open("background.jpg")  
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  


info_box_frame = tk.Frame(root)
info_box_frame.pack(pady=10)


scrollbar = tk.Scrollbar(info_box_frame)
scrollbar.pack(side="right", fill="y")

info_box = Text(info_box_frame, height=8, width=60, wrap="word", bg="white", fg="black", yscrollcommand=scrollbar.set)
info_box.pack(padx=5, pady=5)
info_box.insert("1.0", "This app tracks faces for public interest.\n1- Create a Person DataSet / Tek Kişilik Veri Seti Yarat.\n2- Train it / Modeli eğitin.\n3- Detect it / Algılama yapın.\n 4- Kill detector task with exit Button / Exit tuşuyla Detektör Penceresini kapat")
info_box.config(state="disabled")  


btn1 = tk.Button(root, text="Create DataSet", command=run_app1, width=20, height=2, bg="#006400", fg="white", font=("Arial", 12, "bold"))
btn2 = tk.Button(root, text="Train Data", command=run_app2, width=20, height=2, bg="#00008B", fg="white", font=("Arial", 12, "bold"))
btn3 = tk.Button(root, text="Run Detector", command=run_app3, width=20, height=2, bg="#8B0000", fg="white", font=("Arial", 12, "bold"))
btn_exit = tk.Button(root, text="Exit", command=exit_program, width=20, height=2, bg="#808080", fg="white", font=("Arial", 12, "bold"))


btn1.place(x=20, y=350)  
btn_exit.place(x=240, y=350)  
btn2.place(x=460, y=350)  
btn3.place(x=240, y=300)  

root.mainloop()
