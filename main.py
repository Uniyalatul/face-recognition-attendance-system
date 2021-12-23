from tkinter import*
from tkinter import ttk
# from tkinter.ttk import*
# from tkinter import Tk
# import tkinter as tk
# upr vali line ke bina screen generate nahi hori thii error dera tha vo dimensions ka
from PIL import Image,ImageTk
from tkinter.messagebox import askyesno
# importing student.py file
from student import Student
import cv2
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition Attendence System (by atul)")

        # bg-img
        img = Image.open(r"project_images\bg-img.jpeg")
        img = img.resize((1530,760),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height = 760)

        #title
        title_lbl = Label(bg_img,text = "FACE  RECOGNITION  ATTENDANCE  SYSTEM",font = ("times new roman",35,"bold"),bg ="black",fg="white")
        title_lbl.place(x=0,y=0,width =1530, height = 61)

        #student button
        student_btn_img = Image.open(r"project_images\student_new.jpg")
        student_btn_img = student_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(student_btn_img)

        b1 = Button(bg_img,image=self.photoimg2,command = self.student_details,cursor = "hand2")
        b1.place(x=30,y=100,width=180,height=145)

        b1_1 = Button(bg_img,text="STUDENT DETAILS",command = self.student_details,cursor = "hand2",font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b1_1.place(x=30,y=245,width=181,height=25)

        #detect face button
        face_dtct_btn_img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\detect_face_new.jpg")
        face_dtct_btn_img = face_dtct_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(face_dtct_btn_img)

        b2 = Button(bg_img,image=self.photoimg3,cursor = "hand2",command=self.face_data)
        b2.place(x=30,y=320,width=180,height=145)

        b2_1 = Button(bg_img,text="DETECT FACE",cursor = "hand2",command=self.face_data,font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b2_1.place(x=30,y=460,width=181,height=25)


        #Attendence button
        atten_btn_img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\attendance.jpg")
        atten_btn_img = atten_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(atten_btn_img)

        b3 = Button(bg_img,image=self.photoimg4,cursor = "hand2",command = self.attendance_data)
        b3.place(x=30,y=540,width=180,height=145)

        b3_1 = Button(bg_img,text="Attendance",cursor = "hand2",command = self.attendance_data,font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b3_1.place(x=30,y=680,width=181,height=26)


        #Train Data button
        train_btn_img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\train.jpg")
        train_btn_img = train_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(train_btn_img)

        b4 = Button(bg_img,image=self.photoimg5,cursor = "hand2",command = self.train_data)
        b4.place(x=1300,y=100,width=180,height=145)

        b4_1 = Button(bg_img,text="Train Data",cursor = "hand2",command = self.train_data,font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b4_1.place(x=1300,y=245,width=181,height=26)


        #photos button
        photos_btn_img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\photos.png")
        photos_btn_img = photos_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(photos_btn_img)

        b5 = Button(bg_img,image=self.photoimg6,cursor = "hand2",command = self.open_img)
        b5.place(x=1300,y=320,width=180,height=145)

        b5_1 = Button(bg_img,text="PHOTOS",cursor = "hand2",command = self.open_img,font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b5_1.place(x=1300,y=460,width=181,height=26)


        #Exit button
        exit_btn_img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\exit.jpg")
        exit_btn_img = exit_btn_img.resize((180,145),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(exit_btn_img)

        b6 = Button(bg_img,image=self.photoimg7,cursor = "hand2",command = self.iExit)
        b6.place(x=1300,y=540,width=180,height=145)

        b6_1 = Button(bg_img,text="Exit",cursor = "hand2",command = self.iExit,font = ("times new roman",10,"bold"),bg ="blue",fg="white")
        b6_1.place(x=1300,y=680,width=181,height=26)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = askyesno("Face Recognition","Are you sure , you want to exit")
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ----------------------  Functions Buttons  ------------------  #

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app= Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app= Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app= Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app= Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()