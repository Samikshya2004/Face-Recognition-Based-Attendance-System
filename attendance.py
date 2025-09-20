from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Attendance System")
        self.root.geometry("1550x800+0+0")
        
        img1=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\student1.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        l_lbl=Label(self.root,image=self.photoimg1)
        l_lbl.place(x=5,y=0,width=715,height=200)
        
        img2=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\student1.jpg")
        img2=img2.resize((720,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        
        l_lbl=Label(self.root,image=self.photoimg1)
        l_lbl.place(x=5,y=0,width=715,height=200)
        
if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()