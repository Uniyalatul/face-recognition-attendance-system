from tkinter import*
from tkinter import ttk
# upr vali line ke bina screen generate nahi hori thii error dera tha vo dimensions ka
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition Attendence System (by atul)")

        # -----------------  variables   --------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # TOP-img
        top_img = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\student_top.jpg")
        top_img = top_img.resize((1530, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(top_img)
        top_img = Label(self.root, image=self.photoimg)
        top_img.place(x=0, y=0, width=1530, height=150)

        # title student details
        student_title_lbl = Label(top_img, text="STUDENT  MANAGEMENT", font=(
            "times new roman", 25, "bold"), bg="DARKBLUE", fg="white")
        student_title_lbl.place(x=551, y=40, width=450, height=61)

        # bg-img
        img = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\student_bg.jpg")
        img = img.resize((1530, 609), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=151, width=1530, height=609)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=11, y=11, height=589, width=1507)

        # Left label frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student information", font=(
            "times new roman", 11, "bold"), fg="brown")
        Left_Frame.place(x=10, y=5, height=571, width=691)

        img2 = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\students_infor.jpg")
        img2 = img2.resize((671, 121), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        bg_img = Label(Left_Frame, image=self.photoimg3)
        bg_img.place(x=5, y=9, width=671, height=121)

        # current course information
        curr_cour_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course information", font=(
            "times new roman", 11, "bold"), fg="brown")
        curr_cour_Frame.place(x=5, y=135, height=105, width=671)

        # department
        dep_label = Label(curr_cour_Frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=21)

        dep_combo = ttk.Combobox(curr_cour_Frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer Science", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=8)

        # Course
        cour_label = Label(curr_cour_Frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        cour_label.grid(row=0, column=2, padx=25)

        cour_combo = ttk.Combobox(curr_cour_Frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        cour_combo["values"] = (
            "Select Course", "Diploma", "Btech", "Mtech", "Phd.")
        cour_combo.current(0)
        cour_combo.grid(row=0, column=3, padx=0, pady=8, sticky=W)

        # year
        year_label = Label(curr_cour_Frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=15)

        year_combo = ttk.Combobox(curr_cour_Frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = (
            " ", "2020-21", "2021-22", "2021-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=0, pady=8, sticky=W)

        # Semester
        sem_label = Label(curr_cour_Frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=25)

        sem_combo = ttk.Combobox(curr_cour_Frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=0, pady=8, sticky=W)

        # Class Student Information
        class_Student_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student information", font=("times new roman", 11, "bold"), fg="brown")
        class_Student_Frame.place(x=5, y=247, width=671, height=294)

        # student ID
        studID_label = Label(class_Student_Frame, text="Student ID", font=(
            "times new roman", 12, "bold"), bg="white")
        studID_label.grid(row=0, column=0, padx=15)

        studId_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        studId_entry.grid(row=0, column=1, padx=0, pady=8, sticky=W)

        # student Name
        stud_Name_label = Label(class_Student_Frame, text="Student Name", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_Name_label.grid(row=0, column=2, padx=25)

        stud_NAME_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_NAME_entry.grid(row=0, column=3, padx=0, pady=8, sticky=W)

        # student Division
        stud_div_label = Label(class_Student_Frame, text="Student Division", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_div_label.grid(row=1, column=0, padx=25)

        stud_div_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_div, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_div_entry.grid(row=1, column=1, padx=0, pady=8, sticky=W)

        # student rollno
        stud_roll_label = Label(class_Student_Frame, text="Roll No", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_roll_label.grid(row=1, column=2, padx=25)

        stud_Roll_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_Roll_entry.grid(row=1, column=3, padx=0, pady=8, sticky=W)

        # student Gender
        stud_gend_label = Label(class_Student_Frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_gend_label.grid(row=2, column=0, padx=25)

        stud_Gend_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_gender, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_Gend_entry.grid(row=2, column=1, padx=0, pady=8, sticky=W)

        # student D.O.B
        stud_dob_label = Label(class_Student_Frame, text="Student D.O.B", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_dob_label.grid(row=2, column=2, padx=25)

        stud_dob_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_dob_entry.grid(row=2, column=3, padx=0, pady=8, sticky=W)

        # student Email
        stud_ema_label = Label(class_Student_Frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_ema_label.grid(row=3, column=0, padx=25)

        stud_ema_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_ema_entry.grid(row=3, column=1, padx=0, pady=8, sticky=W)

        # student Phoneno
        stud_phn_label = Label(class_Student_Frame, text="Phoneno", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_phn_label.grid(row=3, column=2, padx=25)

        stud_phn_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_phn_entry.grid(row=3, column=3, padx=0, pady=8, sticky=W)

        # student Address
        stud_adr_label = Label(class_Student_Frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_adr_label.grid(row=4, column=0, padx=25)

        stud_adr_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_adr_entry.grid(row=4, column=1, padx=0, pady=8, sticky=W)

        # Teacher Name
        stud_tname_label = Label(class_Student_Frame, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg="white")
        stud_tname_label.grid(row=4, column=2, padx=25)

        stud_tname_entry = ttk.Entry(class_Student_Frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        stud_tname_entry.grid(row=4, column=3, padx=0, pady=8, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_Student_Frame, variable=self.var_radio1, text="Take Photo ", value="Yes")
        radiobtn1.grid(row=6, column=0)

        # self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            class_Student_Frame, variable=self.var_radio1, text="Do Not Take Photo ", value="No")
        radiobtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(class_Student_Frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=221, width=651, height=26)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command = self.update_data, width=17, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command= self.delete_data, width=17, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command= self.reset_data, width=17, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # button frame 2

        btn_frame2 = Frame(class_Student_Frame, bd=2, relief=RIDGE)
        btn_frame2.place(x=5, y=249, width=651, height=26)

        take_photo_btn = Button(btn_frame2,command= self.generate_dataset , text="Take Photo", width=35, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame2, text="Update Photo", width=35, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student information", font=(
            "times new roman", 11, "bold"), fg="brown")
        Right_Frame.place(x=731, y=5, height=571, width=761)

        img_right = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\stud_class.jpg")
        img_right = img_right.resize((744, 121), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        right_img = Label(Right_Frame, image=self.photoimg_right)
        right_img.place(x=5, y=9, width=744, height=121)

        # search system

        search_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 11, "bold"), fg="brown")
        search_Frame.place(x=5, y=135, width=744, height=71)

        search_label = Label(search_Frame, text="Search By :", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_Frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select ", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=7, pady=8, sticky=W)

        search_entry = ttk.Entry(search_Frame, width=20, font=(
            "times new roman", 11, "bold"), foreground="blue")
        search_entry.grid(row=0, column=2, padx=7, pady=8, sticky=W)

        search_btn = Button(search_Frame, text="Search", width=14, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=7)

        showAll_btn = Button(search_Frame, text="Show All", width=14, font=(
            "times new roman", 11, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=7)

        # table frame

        table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_Frame.place(x=5, y=211, width=744, height=331)

        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_Frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll",
                                          "gender","dob","email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B.")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ------------ function declaration ------------

    def add_data(self):
        if self.var_dep.get() == "Select Deapartment" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror(
                "ERROR", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="12345", database="atuluniyal")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

    # ----------  fetch data ------------

    def fetch_data(self):
        conn = mysql.connector.connect(
        host="localhost", username="root", password="12345", database="atuluniyal")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ---------- get cursor(for updation) ---------

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # ----------- update function
    def update_data(self):
        if self.var_dep.get() == "Select Deapartment" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror(
                "ERROR", "All fields are required", parent=self.root)
        else:
            try:
                updatE = messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)
                if updatE > 0:
                    conn = mysql.connector.connect(
                    host="localhost", username="root", password="12345", database="atuluniyal")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s ,Course=%s,Year=%s,Semester =%s,Division=%s,Roll=%s,Gender=%s,dob=%s,Email=%s,Phoneno=%s,Address=%s,Teacher=%s,PhotoSample=%s  where Student_Id = %s ",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),                
                    # self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))

                else:
                    if not updatE:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    # delete function

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required")
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent = self.root)
                if delete >0:
                    conn = mysql.connector.connect(
                    host="localhost", username="root", password="12345", database="atuluniyal")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details successfully deleted ",parent = self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


    # --------------- RESET

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    # ------  GENERATE DATA SET OR TAKE PHOTO SAMPLES

    def generate_dataset(self):
        if self.var_dep.get() == "Select Deapartment" or self.var_std_name.get() == "" or self.var_std_id == "":
            messagebox.showerror(
                "ERROR", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost", username="root", password="12345", database="atuluniyal")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult =my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set Dep=%s ,Course=%s,Year=%s,Semester =%s,Division=%s,Roll=%s,Gender=%s,dob=%s,Email=%s,Phoneno=%s,Address=%s,Teacher=%s,PhotoSample=%s  where Student_Id = %s ",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),                
                # self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_std_id.get() == id+1
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ---------- load predefined data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.3
                    # Minimum neighbour = 5

                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed !!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
