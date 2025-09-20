from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition System")
        self.root.geometry("1550x800+0+0")
        
        #bg image
        self.bg = ImageTk.PhotoImage(Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\mainpage.jpg").resize((1550,800)))
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        title_lbl=Label(lbl_bg,text="SMARTATTEND-FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        #student button
        img1=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\student.jpg")
        img1=img1.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(lbl_bg,image=self.photoimg1,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=250,height=230)
        
        b1_1=Button(lbl_bg,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="#144911",fg="white",command=self.student_details)
        b1_1.place(x=200,y=300,width=250,height=40)
        
        #detect image
        img2=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\face_detector.jpg")
        img2=img2.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(lbl_bg,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=250,height=230)
        
        b1_2=Button(lbl_bg,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_2.place(x=500,y=300,width=250,height=40)
        
        #Attendance system
        img3=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\attendance.png")
        img3=img3.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(lbl_bg,image=self.photoimg3,cursor="hand2")
        b3.place(x=800,y=100,width=250,height=230)
        
        b1_3=Button(lbl_bg,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_3.place(x=800,y=300,width=250,height=40)
        
        #help desk
        img4=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\help.jpg")
        img4=img4.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(lbl_bg,image=self.photoimg4,cursor="hand2")
        b4.place(x=1100,y=100,width=250,height=230)
        
        b1_4=Button(lbl_bg,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_4.place(x=1100,y=300,width=250,height=40)
        
        #Train Data
        img5=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\train.png")
        img5=img5.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(lbl_bg,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=400,width=250,height=230)
        
        b1_5=Button(lbl_bg,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_5.place(x=200,y=600,width=250,height=40)
        
        #Photos
        img6=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\people.jpg")
        img6=img6.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(lbl_bg,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=400,width=250,height=230)
        
        b1_6=Button(lbl_bg,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_6.place(x=500,y=600,width=250,height=40)
        
        #Developer
        img7=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\developer.webp")
        img7=img7.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b3=Button(lbl_bg,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=400,width=250,height=230)
        
        b1_3=Button(lbl_bg,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_3.place(x=800,y=600,width=250,height=40)
        
        #Exit
        img8=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\exit.webp")
        img8=img8.resize((250,230),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b3=Button(lbl_bg,image=self.photoimg8,cursor="hand2")
        b3.place(x=1100,y=400,width=250,height=230)
        
        b1_3=Button(lbl_bg,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="#144911",fg="white")
        b1_3.place(x=1100,y=600,width=250,height=40)
        
    def open_img(self):
        os.startfile("data")
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    
        
if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
    