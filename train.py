from tkinter import*
from tkinter import ttk
# upr vali line ke bina screen generate nahi hori thii error dera tha vo dimensions ka
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition Attendence System (by atul)")

        # background image =================


        img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\student_top.jpg")
        img = img.resize((1530,760),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height = 760)

        title_lbl = Label(self.root,text = "Train Data Set",font = ("times new roman",35,"bold"),bg ="black",fg="white")
        title_lbl.place(x=0,y=0,width =1530, height = 61)
        

        # button
        b1_1 = Button(self.root,text="START\n TRAINING",command = self.train_classifier, cursor = "hand2",font = ("times new roman",21,"bold"),bg ="blue",fg="white")
        b1_1.place(x=651,y=351,width=200,height=81)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)    # to improve performance we use numpy arrays


        # ========= train the classifier and save ==================

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed !!")




# object

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
