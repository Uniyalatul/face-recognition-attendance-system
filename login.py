from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
from face_recognition import Face_Recognition

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img = Image.open(r"project_images\bkground.jpg")
        img = img.resize((1530,771),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width = 1530 , height = 771)


        frame = Frame(self.root,bg= "white")
        frame.place(x= 21,y=51,width = 320,height = 451)

        img1 = Image.open(r"project_images\admin.jpg")
        img1 = img1.resize((201,81),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimage1,bg="white",borderwidth=0)
        lbl_img1.place(x=76,y=61,width = 201,height = 81)


        #label

        username_lbl = Label(frame,text = "Username : ",font = ("times new roman",15,"bold"),fg="brown",bg="white")
        username_lbl.place(x= 21, y=135)

        self.txtuser = Entry(frame,font=("times new roman",15,"bold"),bg="cyan")
        self.txtuser.place(x= 125,y=135,width=152)

        password_lbl = Label(frame,text = "Password : ",font = ("times new roman",15,"bold"),fg="brown",bg="white")
        password_lbl.place(x= 21, y=201)

        self.txtpass = Entry(frame,font=("times new roman",15,"bold"),bg="cyan")
        self.txtpass.place(x= 125,y=201,width=152)

        loginbtn = Button(frame,text="Login",font=("times new roman",15,"bold"),command=self.login,cursor = "hand2",bd = 3,relief=RIDGE,fg="white",bg="brown")
        loginbtn.place(x=116,y =275,width=101,height=41)

        or_lbl = Label(frame,text = "----  OR  ---- ",font = ("times new roman",15,"bold"),fg="brown",bg="white")
        or_lbl.place(x= 110, y=341)

        userstd_lbl = Label(frame,text = " Student :",font = ("times new roman",15,"bold"),fg="brown",bg="white")
        userstd_lbl.place(x= 21, y=391)

        loginstd_btn = Button(frame,text="Login",font=("times new roman",15,"bold"),command=self.face_data,cursor = "hand2",bd = 3,relief=GROOVE,fg="white",bg="blue")
        loginstd_btn.place(x=142,y =391,width=61,height=26)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="jmd" and self.txtpass.get()=="12345":
            self.new_window = Toplevel(self.root)
            self.app= Face_Recognition_System(self.new_window)
        else:
            messagebox.showerror("Sorry","Invalid credentials")

    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app= Face_Recognition(self.new_window)
        

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()