from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import openpyxl
import numpy as np

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        # 1st image

        img_top = Image.open(r"D:\SmartAttends\face-detection\img\face.jpg")
        img_top = img_top.resize((710, 625))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=710, height=625)

        # 2st image

        img_bottom = Image.open(r"D:\SmartAttends\face-detection\img\scan.jpg")
        img_bottom = img_bottom.resize((900, 625))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=500, y=45, width=900, height=625)

        # button 

        b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=350,y=527,width=200,height=40)

        #----- attendance------

    def mark_attendance(self, student_id, student_rank, student_name, student_department):
            # Load or create the attendance workbook
            try:
                workbook = openpyxl.load_workbook("attendance.xlsx")
                worksheet = workbook.active
            except FileNotFoundError:
                workbook = openpyxl.Workbook()
                worksheet = workbook.active
                worksheet.append(["ID", "Rank", "Name", "Dept", "Time", "Date", "Status"])

            # Check for duplicates using student IDs (more reliable than names)
            student_ids_in_excel = [row[0] for row in worksheet.values]
            if student_id not in student_ids_in_excel:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")

                # Write attendance data
                worksheet.append([student_id, student_rank, student_name, student_department, dtString, d1, "Present"])

            workbook.save("attendance.xlsx")




        #face recognition

    def face_recog(self):
       def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

         coord = []

         for (x, y, w, h) in features:
             cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
             id, predict = clf.predict(gray_image[y:y+h, x:x+w])
             confidence = int((100*(1-predict/300)))

             conn = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="",
                 database="face_recognizer",
                 auth_plugin='mysql_native_password'  # Specify the authentication plugin
             )
             my_cursor = conn.cursor()

             my_cursor.execute("select nom from employes where Matricule="+str(id))

             n = my_cursor.fetchone()

             if n is not None:
                 n = "+".join(n)
             else:
                 n = "Unknown"

             my_cursor.execute("select functions from employes where Matricule="+str(id))

             r = my_cursor.fetchone()

             if r is not None:
                 r = "+".join(r)
             else:
                 r = "Unknown"

             my_cursor.execute("select service from employes where Matricule="+str(id))

             d = my_cursor.fetchone()

             if d is not None:
                 d = "+".join(d)
             else:
                 d = "Unknown"

             my_cursor.execute("select Matricule from employes where Matricule="+str(id))

             i = my_cursor.fetchone()

             if i is not None:
                 i = str(i[0])
             else:
                 i = "Unknown"

             if confidence > 77:
                 cv2.putText(img, f"Matricule:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Function:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 cv2.putText(img, f"Service:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                 self.mark_attendance(i,r,n,d)
               
             else:
                 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                 cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

             coord = [x, y, w, h]

         return img, coord

                    
       def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
       
       faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
       clf=cv2.face.LBPHFaceRecognizer.create()
       clf.read("classifier.xml")

       video_cap=cv2.VideoCapture(0)

       while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

       video_cap.release()
       cv2.destroyAllWindows()

       
                    



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()

