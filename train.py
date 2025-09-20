from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.title("Train Data Samples")
        self.root.geometry("1550x800+0+0")
        
        title_lbl=Label(self.root,text="TRAIN DATA SAMPLES",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        img1=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\facerecognition.jpg")
        img1=img1.resize((1550,330),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        l_lbl=Label(self.root,image=self.photoimg1)
        l_lbl.place(x=0,y=55,width=1550,height=330)
        
        #button
        b1_6=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="#144911",fg="white")
        b1_6.place(x=0,y=385,width=1530,height=60)
        
        img2=Image.open(r"C:\Users\samik\Downloads\face_recognition\Images\student2.webp")
        img2=img2.resize((1550,330),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        l_lbl=Label(self.root,image=self.photoimg2)
        l_lbl.place(x=0,y=440,width=1550,height=330)
        
    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray sacle image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")
            

        
        
if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()