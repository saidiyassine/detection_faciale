from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1290,height=45)

        img_top = Image.open(r"D:\SmartAttends\face-detection\img\Service-Help-Desk.png")
        img_top = img_top.resize((1290, 680))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1290, height=680)

        dev_label = Label(f_lbl, text="Email:saidiyassine791@gmail.com", font=("times new roman", 20, "bold"),fg="blue",bg="white")
        dev_label.place(x=422,y=5)






if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
