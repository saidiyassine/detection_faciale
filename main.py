from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from employe import Employe
from train import Train
from face_recognition import Face_recognition
import os
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Constants for width and height
        img_width, img_height = 430, 130

        # first image
        img = Image.open(r"D:\SmartAttends\face-detection\img\4.png")
        img = img.resize((img_width, img_height))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=img_width, height=img_height)

        # second image
        img1 = Image.open(r"D:\SmartAttends\face-detection\img\2.png")
        img1 = img1.resize((img_width, img_height))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=img_width, y=0, width=img_width, height=img_height)

        # third image
        img2 = Image.open(r"D:\SmartAttends\face-detection\img\1.png")
        img2 = img2.resize((img_width, img_height))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=2 * img_width, y=0, width=img_width, height=img_height)

       # bg image
        img3 = Image.open(r"D:\SmartAttends\face-detection\img\3.png")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1290, height=520)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFT",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        #time----------------------
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(bg_img,font=('times new roman',14,"bold"),background="white",foreground='blue')
        lbl.place(x=2,y=50,width=110,height=28)
        time()

       #employees button 
        img4 = Image.open(r"D:\SmartAttends\face-detection\img\Employee Details.png")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
       
        b1=Button(bg_img,image=self.photoimg4,command=self.employe_details,cursor="hand2")
        b1.place(x=60,y=85,width=200,height=180)

        b1_1=Button(bg_img,text="Employees Details",command=self.employe_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=60,y=245,width=200,height=40)

        #Detect face button 
        img5 = Image.open(r"D:\SmartAttends\face-detection\img\Face Detector.png")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
       
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=360,y=85,width=200,height=180)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=360,y=245,width=200,height=40)

        #Attendance face button 
        img6 = Image.open(r"D:\SmartAttends\face-detection\img\Attendance.png")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
       
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=660,y=85,width=200,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=660,y=245,width=200,height=40)

        #chat button 
        img7 = Image.open(r"D:\SmartAttends\face-detection\friendly-chatbot.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
       
        b1=Button(bg_img,image=self.photoimg7,command=self.chatbot,cursor="hand2")
        b1.place(x=960,y=85,width=200,height=180)

        b1_1=Button(bg_img,text="ChatBot",command=self.chatbot,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=960,y=245,width=200,height=40)

        #Train Data button 
        img8 = Image.open(r"D:\SmartAttends\face-detection\img\Rapport.png")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
       
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=60,y=305,width=200,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=60,y=465,width=200,height=40)

        #Photos Face button 
        img9 = Image.open(r"D:\SmartAttends\face-detection\img\Image.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
       
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image,)
        b1.place(x=360,y=305,width=200,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=360,y=465,width=200,height=40)

         #Developer face button 
        img10 = Image.open(r"D:\SmartAttends\face-detection\img\Developer.png")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
       
        b1=Button(bg_img,image=self.photoimg10,command=self.developer,cursor="hand2")
        b1.place(x=660,y=305,width=200,height=180)

        b1_1=Button(bg_img,text="Developer",command=self.developer,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=660,y=465,width=200,height=40)

        #Exit face button 
        img11 = Image.open(r"D:\SmartAttends\face-detection\img\Exit.png")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
       
        b1=Button(bg_img,image=self.photoimg11,command=self.Exit,cursor="hand2")
        b1.place(x=960,y=305,width=200,height=180)

        b1_1=Button(bg_img,text="Exit",command=self.Exit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=960,y=465,width=200,height=40)

    

    def open_image(self):
        os.startfile("data")

    def Exit(self):
        self.iExit=tkinter.messagebox.askyesno("Face recognizer","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 
#-------------------function----------------------#
    def employe_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employe(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    # def Help(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)
        
    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import ttk
# from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import cv2
# import os
# import numpy as np
# import openpyxl

# class Face_recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
#         title_lbl.place(x=0,y=0,width=1290,height=45)

#         # 1st image

#         img_top = Image.open(r"D:\SmartAttends\face-detection\img\face.jpg")
#         img_top = img_top.resize((710, 625))
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl = Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=45, width=710, height=625)

#         # 2st image

#         img_bottom = Image.open(r"D:\SmartAttends\face-detection\img\scan.jpg")
#         img_bottom = img_bottom.resize((900, 625))
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
#         f_lbl = Label(self.root, image=self.photoimg_bottom)
#         f_lbl.place(x=500, y=45, width=900, height=625)

#         # button 

#         b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",command=self.face_recog,font=("times new roman",13,"bold"),bg="darkgreen",fg="white")
#         b1_1.place(x=350,y=527,width=200,height=40)

#         #----- attendance------
        
#     def mark_attendance(self, student_id, student_rank, student_name, student_department):

#             # Load or create the attendance workbook
#             try:
#                 workbook = openpyxl.load_workbook("attendance.xlsx")
#                 worksheet = workbook.active
#             except FileNotFoundError:
#                 workbook = openpyxl.Workbook()
#                 worksheet = workbook.active
#                 worksheet.append(["ID", "Rank", "Name", "Dept", "Time", "Date", "Status"])  # Write headers only here

#             # Check for duplicates using student IDs (more reliable than names)
#             student_ids_in_excel = [row[0] for row in worksheet.values]
#             if student_id not in student_ids_in_excel:
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")

#                 # Write attendance data
#                 worksheet.append([student_id, student_rank, student_name, student_department, dtString, d1, "Present"])

#             workbook.save("attendance.xlsx")
#                 #face recognition

#     def face_recog(self):
#        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#          gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#          features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

#          coord = []

#          for (x, y, w, h) in features:
#              cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#              id, predict = clf.predict(gray_image[y:y+h, x:x+w])
#              confidence = int((100*(1-predict/300)))

#              conn = mysql.connector.connect(
#                  host="localhost",
#                  user="root",
#                  password="yassinedev",
#                  database="face_recognizer",
#                  auth_plugin='mysql_native_password'  # Specify the authentication plugin
#              )
#              my_cursor = conn.cursor()

#              my_cursor.execute("select nom from employes where Matricule="+str(id))

#              n = my_cursor.fetchone()

#              if n is not None:
#                  n = "+".join(n)
#              else:
#                  n = "Unknown"

#              my_cursor.execute("select functions from employes where Matricule="+str(id))

#              r = my_cursor.fetchone()

#              if r is not None:
#                  r = "+".join(r)
#              else:
#                  r = "Unknown"

#              my_cursor.execute("select service from employes where Matricule="+str(id))

#              d = my_cursor.fetchone()

#              if d is not None:
#                  d = "+".join(d)
#              else:
#                  d = "Unknown"

#              my_cursor.execute("select Matricule from employes where Matricule="+str(id))

#              i = my_cursor.fetchone()

#              if i is not None:
#                  i = str(i[0])
#              else:
#                  i = "Unknown"

#              if confidence > 77:
#                  cv2.putText(img, f"Matricule:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                  cv2.putText(img, f"Function:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                  cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                  cv2.putText(img, f"Service:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
#                  self.mark_attendance(i,r,n,d)
#              else:
#                  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
#                  cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

#              coord = [x, y, w, h]

#          return img, coord

                    
#        def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
       
#        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#        clf=cv2.face.LBPHFaceRecognizer.create()
#        clf.read("classifier.xml")

#        video_cap=cv2.VideoCapture(0)

#        while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Welcome To face Recognition", img)

#             if cv2.waitKey(1) == 13:
#                 break

#        video_cap.release()
#        cv2.destroyAllWindows()

       
                    



# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()

