from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import subprocess

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_squestion=StringVar()
        self.var_sanswer=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        
        #bg image
        self.bg = ImageTk.PhotoImage(Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\RegisterBackground.jpg").resize((1600,900)))
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        self.bg1 = ImageTk.PhotoImage(Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\leftimage.jpg").resize((490,530)),Image.Resampling.LANCZOS)
        left_bg=Label(self.root,image=self.bg1)
        left_bg.place(x=50,y=100,width=490,height=530)
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=540,y=100,width=800,height=530)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #labels and entry
        #-----row1-----
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #-----row2-----
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #-----row3-----
        squestion=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        squestion.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_squestion,font=("times new roman",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your BestFriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        sanswer=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        sanswer.place(x=370,y=240)
        
        self.txt_sanswer=ttk.Entry(frame,textvariable=self.var_sanswer,font=("times new roman",15))
        self.txt_sanswer.place(x=370,y=270,width=250)
        
        #-----row4-----
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250) 
        
        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        cpassword.place(x=370,y=310)
        
        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_cpassword,font=("times new roman",15))
        self.txt_cpassword.place(x=370,y=340,width=250) 
        
        #checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new   roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons
        registerbtn=Button(frame,text="Register",command=self.register_data,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="darkgreen",activeforeground="black",activebackground="white")
        registerbtn.place(x=100,y=420,width=120,height=35)
        
        loginbtn=Button(frame,text="Login",command=self.open_login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="darkgreen",activeforeground="black",activebackground="white")
        loginbtn.place(x=420,y=420,width=120,height=35)
        
        
    def open_login(self):
        self.root.destroy()
        subprocess.Popen(["python", "login.py"])
        
        
        
        #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_squestion.get()=="Select" or self.var_contact.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
            return
        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
            return
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
            return
        elif self.var_password.get()=="":
            messagebox.showerror("Error","Please provide a password")
            return
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Sriya@2004",database="face_recognition")
            my_cursor=conn.cursor()
        query=("select * from register where email=%s")
        value=(self.var_email.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row!=None:
            messagebox.showerror("Error","User already exist, please try another email")
        else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_squestion.get(),
                self.var_sanswer.get(),
                self.var_password.get(),
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")
            self.root.destroy() 
            subprocess.Popen(["python","main.py"])
    def on_close(self):
        self.root.destroy()

        
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()