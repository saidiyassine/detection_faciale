from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

class Employe:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


#-------------------variables----------------------#
        
        self.var_dep=StringVar()
        self.var_fun=StringVar()
        self.var_year=StringVar()
        self.var_month=StringVar()
        self.var_mat=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_cin=StringVar()
        self.var_service=StringVar()
        self.var_status=StringVar()
        self.var_cat=StringVar()
        self.var_phone=StringVar()
        self.var_mail=StringVar()
        self.var_addr=StringVar()
        self.var_radio1=StringVar()
       # Constants for width and height
        img_width, img_height = 430, 130

        # first image
        img = Image.open(r"D:\SmartAttends\face-detection\img\EMPLOYEES MANAGEMENT SYSTEM.png")
        img = img.resize((1290, img_height))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1290, height=img_height)


         # bg image
        img3 = Image.open(r"D:\SmartAttends\face-detection\img\3.png")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1290, height=520)

        

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=7,width=1260,height=740)

        #Left label fram
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employees Details",font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=7,width=610,height=490)

        #img_left = Image.open(r"C:\Users\hp\Desktop\SmartAttends\img\1.png")
        #img_left = img_left.resize((610, 90))
        #self.photoimg_left = ImageTk.PhotoImage(img_left)
        #f_lbl = Label(Left_frame, image=self.photoimg_left)
        #f_lbl.place(x=5, y=0, width=600, height=130)

        #current cours
        current=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current",font=("times new roman",12,"bold"))
        current.place(x=5,y=5,width=600,height=120)

        #dep
        dep_label = Label(current, text="Departement", font=("times new roman", 12, "bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Departement","finition","apprenti","ouvrier")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #function
        dep_label = Label(current, text="Function", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current,textvariable=self.var_fun,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Function","finition","apprenti","ouvrier")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        dep_label = Label(current, text="Year", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","finition","apprenti","ouvrier")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #month
        dep_label = Label(current, text="Month", font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current,textvariable=self.var_month,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Month","finition","apprenti","ouvrier")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #current informations
        current_informations=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Employe informations",font=("times new roman",12,"bold"))
        current_informations.place(x=5,y=135,width=600,height=370)

        #matricule employe
        studentId_label = Label(current_informations, text="Matricule:", font=("times new roman", 13, "bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studntID_entry=ttk.Entry(current_informations,textvariable=self.var_mat,width=18,font=("times new roman", 13, "bold"))
        studntID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name employe
        studentName_label = Label(current_informations, text="Name:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_name,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #sexe employe
        studentName_label = Label(current_informations, text="Gender:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # studentName_entry=ttk.Entry(current_informations,textvariable=self.var_gender,width=18,font=("times new roman", 13, "bold"))
        # studentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(current_informations,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #cin employe
        studentName_label = Label(current_informations, text="Cin:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_cin,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #function employe
        studentId_label = Label(current_informations, text="Service:", font=("times new roman", 13, "bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studntID_entry=ttk.Entry(current_informations,textvariable=self.var_service,width=18,font=("times new roman", 13, "bold"))
        studntID_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #statut employe
        studentName_label = Label(current_informations, text="Status:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_status,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=2,column=3,padx=10,sticky=W)

        #category employe
        studentName_label = Label(current_informations, text="Category:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_cat,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone employe
        studentName_label = Label(current_informations, text="Phone:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_phone,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

          #email employe
        studentName_label = Label(current_informations, text="E-mail:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_mail,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #adress employe
        studentName_label = Label(current_informations, text="Adress:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(current_informations,textvariable=self.var_addr,width=18,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobtn1
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(current_informations,variable=self.var_radio1,text="Take Photo",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(current_informations,variable=self.var_radio1,text="No Photo",value="No")
        radionbtn2.grid(row=6,column=1)

        #btn
        btn_frame=Frame(current_informations,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=596,height=70)

        #save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #btn
        btn_frame1=Frame(current_informations,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=596,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo",width=29,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update photo",width=29,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        #Right label fram
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employees Details",font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=635,y=7,width=610,height=490)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=600,height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 14, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Name","Number","Function")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showallt_btn=Button(search_frame,text="Show All",width=8,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        showallt_btn.grid(row=0,column=4,padx=3)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=77,width=600,height=383)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employes_table=ttk.Treeview(table_frame,column=("Matricule","Name","Gender","Cin","Function","Status","Category"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employes_table.xview)
        scroll_y.config(command=self.employes_table.yview)

        self.employes_table.heading("Matricule",text="Matricule")
        self.employes_table.heading("Name",text="Name")
        self.employes_table.heading("Gender",text="Gender")
        self.employes_table.heading("Cin",text="Cin")
        self.employes_table.heading("Function",text="Function")
        self.employes_table.heading("Status",text="Status")
        self.employes_table.heading("Category",text="Category")
        self.employes_table["show"]="headings"

        self.employes_table.column("Matricule",width=100)
        self.employes_table.column("Name",width=100)
        self.employes_table.column("Gender",width=100)
        self.employes_table.column("Cin",width=100)
        self.employes_table.column("Function",width=100)
        self.employes_table.column("Status",width=100)
        self.employes_table.column("Category",width=100)
        self.employes_table.pack(fill=BOTH,expand=1)
        self.employes_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


#--------------function---------------------#
   
    def add_data(self):
        if (
            self.var_dep.get() == "" or
            self.var_fun.get() == "" or
            self.var_year.get() == "" or
            self.var_month.get() == "" or
            self.var_mat.get() == "" or
            self.var_name.get() == "" or
            self.var_gender.get() == "" or
            self.var_cin.get() == "" or
            self.var_service.get() == "" or
            self.var_status.get() == "" or
            self.var_cat.get() == "" or
            self.var_phone.get() == "" or
            self.var_mail.get() == "" or
            self.var_addr.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="face_recognizer",
                    auth_plugin='mysql_native_password'  # Specify the authentication plugin
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO employes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_mat.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_cin.get(),
                        self.var_fun.get(),
                        self.var_status.get(),
                        self.var_cat.get(),
                        self.var_year.get(),
                        self.var_month.get(),
                        self.var_dep.get(),
                        self.var_service.get(),
                        self.var_phone.get(),
                        self.var_mail.get(),
                        self.var_addr.get(),
                        self.var_radio1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee details have been added successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

#--------------fetch data---------#
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="face_recognizer",
                    auth_plugin='mysql_native_password'  # Specify the authentication plugin
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employes")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employes_table.delete(*self.employes_table.get_children())
            for i in data:
                self.employes_table.insert("",END,values=i)
            conn.commit()
        conn.close()
#-------------get cursor----------------#
    def get_cursor(self,event=""):
        cursor_focus=self.employes_table.focus()
        content=self.employes_table.item(cursor_focus)
        data=content["values"]

        self.var_mat.set(data[0]),
        self.var_name.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_cin.set(data[3]),
        self.var_fun.set(data[4]),
        self.var_status.set(data[5]),
        self.var_cat.set(data[6]),
        self.var_year.set(data[7]),
        self.var_month.set(data[8]),
        self.var_dep.set(data[9]),
        self.var_service.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_mail.set(data[12]),
        self.var_addr.set(data[13]),
        self.var_radio1.set(data[14])

#---------------update function ---------------#
    def update_data(self):
            if (
                self.var_dep.get() == "" or
                self.var_fun.get() == "" or
                self.var_year.get() == "" or
                self.var_month.get() == "" or
                self.var_mat.get() == "" or
                self.var_name.get() == "" or
                self.var_gender.get() == "" or
                self.var_cin.get() == "" or
                self.var_service.get() == "" or
                self.var_status.get() == "" or
                self.var_cat.get() == "" or
                self.var_phone.get() == "" or
                self.var_mail.get() == "" or
                self.var_addr.get() == ""
            ):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                try:
                    update=messagebox.askyesno("Update","Do you want to update this employe details",parent=self.root)
                    if update>0:
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="face_recognizer",
                            auth_plugin='mysql_native_password'  # Specify the authentication plugin
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute("update employes set nom=%s,gender=%s,cin=%s,functions=%s,statut=%s,categorie=%s,years=%s,months=%s,departement=%s,service=%s,phone=%s,mail=%s,adresse=%s,radio=%s where Matricule=%s",
                                        (
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_cin.get(),
                                            self.var_fun.get(),
                                            self.var_status.get(),
                                            self.var_cat.get(),
                                            self.var_year.get(),
                                            self.var_month.get(),
                                            self.var_dep.get(),
                                            self.var_service.get(),
                                            self.var_phone.get(),
                                            self.var_mail.get(),
                                            self.var_addr.get(),
                                            self.var_radio1.get(),
                                            self.var_mat.get()
                                        )
                                    )
                    else:
                        if not update:
                            return
                    messagebox.showinfo("Success","Employe details successfully update completed",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    
#----------------delete function -------------#
    def delete_data(self):
        if(self.var_mat.get()==""):
            messagebox.showerror("Error","Employe matricule must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employe Delete page","Do you want to delete this employe",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="face_recognizer",
                            auth_plugin='mysql_native_password'  # Specify the authentication plugin
                        )
                    my_cursor = conn.cursor()
                    sql="delete from employes where Matricule=%s"
                    val=(self.var_mat.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted employe details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#--------------------reset-----------------
    def reset_data(self):
        self.var_dep.set("Select Departement")
        self.var_fun.set("Select Function")
        self.var_year.set("Select Year")
        self.var_month.set("Select Month")
        self.var_mat.set("")
        self.var_name.set("")
        self.var_gender.set("Male")
        self.var_cin.set("")
        self.var_service.set("")
        self.var_status.set("")
        self.var_cat.set("")
        self.var_phone.set("")
        self.var_mail.set("")
        self.var_addr.set("")
        self.var_radio1.set("")

#-----------------generate data set or take photo sample----------------
    def generate_dataset(self):
            if (
                self.var_dep.get() == "Select Departement" or
                self.var_fun.get() == "Select Function" or
                self.var_year.get() == "Select Year" or
                self.var_month.get() == "Select Month" or
                self.var_mat.get() == "" or
                self.var_name.get() == "" or
                self.var_gender.get() == "" or
                self.var_cin.get() == "" or
                self.var_service.get() == "" or
                self.var_status.get() == "" or
                self.var_cat.get() == "" or
                self.var_phone.get() == "" or
                self.var_mail.get() == "" or
                self.var_addr.get() == ""
            ):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="face_recognizer",
                            auth_plugin='mysql_native_password'  # Specify the authentication plugin
                        )
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from employes")
                    my_result=my_cursor.fetchall()
                    id=0
                    for x in my_result:
                        id+=1
                    my_cursor.execute("update employes set nom=%s,gender=%s,cin=%s,functions=%s,statut=%s,categorie=%s,years=%s,months=%s,departement=%s,service=%s,phone=%s,mail=%s,adresse=%s,radio=%s where Matricule=%s",
                                        (
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_cin.get(),
                                            self.var_fun.get(),
                                            self.var_status.get(),
                                            self.var_cat.get(),
                                            self.var_year.get(),
                                            self.var_month.get(),
                                            self.var_dep.get(),
                                            self.var_service.get(),
                                            self.var_phone.get(),
                                            self.var_mail.get(),
                                            self.var_addr.get(),
                                            self.var_radio1.get(),
                                            self.var_mat.get()==id+1
                                        )
                                    )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    #-----------load predifiend data on face frontals from open cv

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scalingfactor=1.3
                        #Minimum=5
                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Crooped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets compled!!!")
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Employe(root)
    root.mainloop()
