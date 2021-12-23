from tkinter import*
from tkinter import ttk
# upr vali line ke bina screen generate nahi hori thii error dera tha vo dimensions ka
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition Attendence System (by atul)")

        # ---------- variables ---------

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()



        # TOP-img
        top_img = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\student_top.jpg")
        top_img = top_img.resize((1530, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(top_img)
        top_img = Label(self.root, image=self.photoimg)
        top_img.place(x=0, y=0, width=1530, height=150)

        # title 
        student_title_lbl = Label(top_img, text="Attendance System", font=(
            "times new roman", 25, "bold"), bg="DARKBLUE", fg="white")
        student_title_lbl.place(x=551, y=40, width=450, height=61)

        # bg-img
        img = Image.open(
            r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\student_bg.jpg")
        img = img.resize((1530, 609), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=151, width=1530, height=609)

        main_frame = Frame(bg_img, bd=0, bg="lightblue")
        main_frame.place(x=15, y=21, height=551, width=1492)

        # Left label frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="black", relief=RIDGE, text="Student information", font=(
            "times new roman", 11, "bold"), fg="white")
        Left_Frame.place(x=0, y=0, height=571, width=691)

        # img2 = Image.open(
        #     r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\students_infor.jpg")
        # img2 = img2.resize((671, 121), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img2)
        # bg_img = Label(Left_Frame, image=self.photoimg3)
        # bg_img.place(x=5, y=9, width=671, height=121)

        left_inside_frame = Frame(Left_Frame, bd=2, bg="white")
        left_inside_frame.place(x=11, y=15, height=471, width=651)

        # labels and entries

        attendanceId_label = Label(left_inside_frame, text="Attendance ID", font=(
            "times new roman", 14, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=61,pady = 16)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=(
            "times new roman", 14, "bold"), foreground="blue")
        attendanceId_entry.grid(row=0, column=1, padx=21, pady=8, sticky=W)

        
        # roll
        rolllabel = Label(left_inside_frame, text="Roll no. ", font=(
            "times new roman", 14, "bold"), bg="white")
        rolllabel.grid(row=1, column=0, padx=61,pady = 16)

        atten_roll = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll, font=(
            "times new roman", 14, "bold"), foreground="blue")
        atten_roll.grid(row=1, column=1, padx=21, pady=8, sticky=W)

        # name
        namelabel = Label(left_inside_frame, text="Name. ", font=(
            "times new roman", 14, "bold"), bg="white")
        namelabel.grid(row=2, column=0, padx=61,pady = 16)

        attenname = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=(
            "times new roman", 14, "bold"), foreground="blue")
        attenname.grid(row=2, column=1, padx=21, pady=8, sticky=W)

        # dep
        deplabel = Label(left_inside_frame, text="Department ", font=(
            "times new roman", 14, "bold"), bg="white")
        deplabel.grid(row=3, column=0, padx=61,pady = 16)

        atten_dep = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=(
            "times new roman", 14, "bold"), foreground="blue")
        atten_dep.grid(row=3, column=1, padx=21, pady=8, sticky=W)

        # time
        timelabel = Label(left_inside_frame, text="Time ", font=(
            "times new roman", 12, "bold"), bg="white")
        timelabel.grid(row=4, column=0, padx=61,pady = 16)

        atten_time = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=(
            "times new roman", 14, "bold"), foreground="blue")
        atten_time.grid(row=4, column=1, padx=21, pady=8, sticky=W)

        # date
        datelabel = Label(left_inside_frame, text="Date ", font=(
            "times new roman", 14, "bold"), bg="white")
        datelabel.grid(row=5, column=0, padx=61,pady = 16)

        atten_date = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=(
            "times new roman", 14, "bold"), foreground="blue")
        atten_date.grid(row=5, column=1, padx=21, pady=8, sticky=W)

        # status
        attendancelabel = Label(left_inside_frame, text="Status ", font=(
            "times new roman", 14, "bold"), bg="white")
        attendancelabel.grid(row=6, column=0, padx=61,pady = 16)

        atten_attendance = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font=(
            "times new roman", 14, "bold"), foreground="blue")
        atten_attendance.grid(row=6, column=1, padx=21, pady=8, sticky=W)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=418, width=631, height=31)

        save_btn = Button(btn_frame, text="Import csv",command = self.importCsv, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command =self.exportCsv,width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command = self.reset_data, width=17, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right label frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="black", relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 11, "bold"), fg="white")
        Right_Frame.place(x=731, y=0, height=571, width=761)

        table_frame = Frame(Right_Frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=11, y=15, width=741, height=471)


        # ----------- scroll bar table

        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient = VERTICAL)

        self.AttendanceReportTable= ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill = BOTH,expand = 1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # ----------------- fetch data ---------

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1 :
                messagebox.showerror("NoData","No Data found to be export",parent = self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent = self.root)
            with open(fln,mode="w",newline ="") as myfile:
                exp_write = csv.writer(myfile,delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data exported","Your data exported successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


 
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
