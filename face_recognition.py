from tkinter import*
from tkinter import ttk
# upr vali line ke bina screen generate nahi hori thii error dera tha vo dimensions ka
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x760+0+0")
        self.root.title("Face Recognition Attendence System (by atul)")

        img = Image.open(r"C:\Users\91955\Desktop\ATUL-5SEM\face_recognition_system\project_images\facial-recognition2.jpg")
        img = img.resize((1530,760),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height = 760)

        title_lbl = Label(self.root,text = "Face Recognition",font = ("times new roman",35,"bold"),bg ="blue",fg="white")
        title_lbl.place(x=0,y=0,width =1530, height = 61)

        # button
        b1_1 = Button(self.root,text="FACE RECOGNITION", cursor = "hand2",command = self.face_recog,font = ("times new roman",21,"bold"),bg ="white",fg="red")
        b1_1.place(x=611,y=718,width=309,height=31)



    # --------------  attendance -----------

    def mark_attendance(self,si,ro,na,de):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((si not in name_list) and (ro not in name_list) and (na not in name_list) and (de not in name_list) ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{si},{ro},{na},{de},{dtString},{d1},Present")







    # ------------- face recognition -------------

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="atuluniyal")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where Student_Id=" + str(id))
                n = my_cursor.fetchone()
                na= ''.join(n)

                my_cursor.execute("select Roll from student where Student_Id=" + str(id))
                r = my_cursor.fetchone()
                ro= ''.join(r)

                my_cursor.execute("select Dep from student where Student_Id=" + str(id))
                d = my_cursor.fetchone()
                de= ''.join(d)

                my_cursor.execute("select Student_Id from student where Student_Id=" + str(id))
                s = my_cursor.fetchone()
                si= ''.join(s)


                if confidence > 75:
                    cv2.putText(img,f"Id:  {si}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:  {ro}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:  {na}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:  {de}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(si,ro,na,de)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord = [x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)

            # press any key to exit

            if cv2.waitKey(1)== 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()