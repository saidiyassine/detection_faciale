from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        img_top = Image.open(r"D:\SmartAttends\face-detection\img\Developer.jpg")
        img_top = img_top.resize((1290, 680))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1290, height=680)

#--------------------------frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=780,y=0,width=500,height=500)

        img_top1 = Image.open(r"D:\SmartAttends\face-detection\img\cv.jpg")
        img_top1 = img_top1.resize((190, 190))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=10, width=190, height=190)

        #developer info
        
        dev_label = Label(main_frame, text="Yassine Es-saidi", font=("times new roman", 20, "bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am a fullstack developer", font=("times new roman", 20, "bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=40)

        img = Image.open(r"D:\SmartAttends\face-detection\img\py.jpg")
        img = img.resize((500, 300))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(main_frame, image=self.photoimg)
        f_lbl.place(x=0, y=200, width=500, height=300)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
