from tkinter import*
from tkinter import ttk
from PIL import Image 
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

from student import Student

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Developer", font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("college_images/dev.jpg")
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=745)

        # Main frame with padding
        main_frame=Frame(f_lbl,bd=3,bg="white",relief=RIDGE)
        main_frame.place(x=750,y=50,width=750,height=650)

        # Inner image with border
        img_inner = Image.open(r"C:\Users\Lenovo\Downloads\20251003_0639261.jpg")
        img_inner = img_inner.resize((220,220), Image.LANCZOS)
        self.photoimg_inner = ImageTk.PhotoImage(img_inner)

        img_frame = Frame(main_frame, bd=3, relief=RIDGE, bg="white")
        img_frame.place(x=265, y=20, width=220, height=220)

        img_lbl = Label(img_frame, image=self.photoimg_inner)
        img_lbl.place(x=0, y=0, width=220, height=220)

        # Developer info - Name
        dev_label=Label(main_frame,text="Hello, I am Monti", font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        dev_label.place(x=20,y=260,width=710,height=40)

        # Developer info - Description
        dev_label1=Label(main_frame,text="I am a final year student of B.C.A. AI & Data Analytics", font=("times new roman",14,"bold"),bg="white",fg="black")
        dev_label1.place(x=20,y=310,width=710,height=35)

        # Contact Information
        contact_label=Label(main_frame,text="📧 Email: monti@example.com", font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        contact_label.place(x=20,y=355,width=710,height=25)

        # Phone Information
        phone_label=Label(main_frame,text="📱 Phone: +91 XXXXXXXXXX", font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        phone_label.place(x=20,y=385,width=710,height=25)

        # Skills Section
        skills_label=Label(main_frame,text="🛠️ Skills: Python, OpenCV, Machine Learning, Face Recognition", font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        skills_label.place(x=20,y=415,width=710,height=25)

        # College Information
        college_label=Label(main_frame,text="🏫 College: XYZ Institute of Technology", font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        college_label.place(x=20,y=445,width=710,height=25)

        # Project Information
        project_label=Label(main_frame,text="📚 Project: AI-Based Face Recognition & Attendance System", font=("times new roman",12,"bold"),bg="white",fg="darkblue")
        project_label.place(x=20,y=475,width=710,height=25)

if __name__ == "__main__":
            root = Tk()
            obj = Developer(root)
            root.mainloop()