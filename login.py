from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from register import Register
import subprocess

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\Login_Background.jpg").resize((1550,800)))
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="#144911")
        frame.place(x=900, y=170, width=340, height=450)
        
        img1=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\login.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="#144911",borderwidth=0)
        lblimg1.place(x=1020,y=175,width=100,height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="#144911")
        get_str.place(x=95, y=100)

        username = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="#144911")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="#144911")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)
        
        img2 = Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\user.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="#144911", borderwidth=0)
        lblimg1.place(x=940, y=323, width=25, height=25)
        
        img3 = Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\padlock.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="#144911", borderwidth=0)
        lblimg1.place(x=940, y=395, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="black", bg="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="#144911")
        registerbtn.place(x=15, y=350, width=160)
        
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="#144911", activeforeground="black", activebackground="#144911")
        forgetbtn.place(x=10, y=370, width=160)
    

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
        self.new_window.grab_set()               
        self.root.wait_window(self.new_window)   


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Sriya@2004", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (  # fixed 'pasword' typo
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            conn.close()  # good practice
            if row == None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                messagebox.showinfo("Success", "Welcome!")
                self.root.destroy()
                subprocess.Popen(["python", "main.py"]) 
                
    #reset password
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select a security question",parent=self.root2)
        elif self.txt_sanswer.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Sriya@2004", database="face_recognition")
            my_cursor = conn.cursor()
            query=("select * from register where email = %s and squestion=%s and sanswer=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_sanswer.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has beem reset, please login with new password",parent=self.root2)
                self.root2.destroy()
    
    # forget password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Sriya@2004", database="face_recognition")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                squestion=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                squestion.place(x=50,y=80)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your BestFriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                sanswer=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                sanswer.place(x=50,y=150)
                
                self.txt_sanswer=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_sanswer.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
                
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="darkgreen")
                btn.place(x=100,y=290)

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
