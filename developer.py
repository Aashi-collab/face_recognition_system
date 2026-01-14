from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Developer")
        
        # Gradient background effect
        title_frame = Frame(self.root, bg="#1a5490", height=60)
        title_frame.place(x=0, y=0, width=1530, height=60)
        
        title_lbl = Label(title_frame, text="👨‍💻 DEVELOPER PROFILE", 
                         font=("Segoe UI", 38, "bold"), bg="#1a5490", fg="white")
        title_lbl.place(x=0, y=5, width=1530, height=50)
        
        # Background image with overlay
        img_top = Image.open("college_images/dev.jpg")
        img_top = img_top.resize((1530, 730), Image.LANCZOS)
        # Apply slight blur for aesthetic effect
        img_top = img_top.filter(ImageFilter.GaussianBlur(radius=1))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=60, width=1530, height=730)
        
        # Semi-transparent overlay
        overlay_frame = Frame(f_lbl, bg="#000000")
        overlay_frame.place(x=0, y=0, width=1530, height=730)
        overlay_frame.configure(bg="#000000")
        
        # Main card with shadow effect
        main_frame = Frame(f_lbl, bd=0, bg="white", relief=FLAT)
        main_frame.place(x=400, y=30, width=730, height=670)
        
        # Shadow effect (multiple frames)
        shadow_frame1 = Frame(f_lbl, bg="#d0d0d0")
        shadow_frame1.place(x=405, y=35, width=730, height=670)
        shadow_frame2 = Frame(f_lbl, bg="#e0e0e0")
        shadow_frame2.place(x=410, y=40, width=730, height=670)
        
        # Raise main frame to top
        main_frame.lift()
        
        # Header section with gradient
        header_frame = Frame(main_frame, bg="#2c5aa0", height=80)
        header_frame.place(x=0, y=0, width=730, height=80)
        
        header_label = Label(header_frame, text="MEET THE DEVELOPER", 
                           font=("Segoe UI", 24, "bold"), bg="#2c5aa0", fg="white")
        header_label.place(x=0, y=20, width=730, height=40)
        
        # Profile image section with circular frame
        img_inner = Image.open(r"C:\Users\Lenovo\Downloads\20251003_0639261.jpg")
        img_inner = img_inner.resize((240, 240), Image.LANCZOS)
        
        # Create circular mask
        mask = Image.new('L', (240, 240), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 240, 240), fill=255)
        
        # Apply circular mask
        output = Image.new('RGBA', (240, 240), (255, 255, 255, 0))
        output.paste(img_inner, (0, 0))
        output.putalpha(mask)
        
        self.photoimg_inner = ImageTk.PhotoImage(output)
        
        # Image container with border
        img_container = Frame(main_frame, bg="#2c5aa0", bd=5, relief=FLAT)
        img_container.place(x=245, y=100, width=250, height=250)
        
        img_lbl = Label(img_container, image=self.photoimg_inner, bg="white")
        img_lbl.place(x=0, y=0, width=240, height=240)
        
        # Name section
        name_frame = Frame(main_frame, bg="#f8f9fa")
        name_frame.place(x=30, y=370, width=670, height=60)
        
        name_label = Label(name_frame, text="MONTI BUNDELA", 
                         font=("Segoe UI", 28, "bold"), bg="#f8f9fa", fg="#1a5490")
        name_label.pack(pady=5)
        
        subtitle_label = Label(name_frame, text="AI & Data Analytics Developer", 
                             font=("Segoe UI", 12, "italic"), bg="#f8f9fa", fg="#666666")
        subtitle_label.pack()
        
        # Info cards section
        info_y = 450
        
        # Education Card
        self.create_info_card(main_frame, "🎓 EDUCATION", 
                            "Final Year B.C.A. - AI & Data Analytics\nLNCT University, Bhopal",
                            30, info_y, "#e3f2fd", "#1976d2")
        
        # Project Card
        self.create_info_card(main_frame, "🚀 CURRENT PROJECT", 
                            "ML Based Face Recognition\n& Attendance System",
                            380, info_y, "#f3e5f5", "#7b1fa2")
        
        # Skills section
        skills_frame = Frame(main_frame, bg="#fff3e0", bd=2, relief=SOLID)
        skills_frame.place(x=30, y=560, width=670, height=50)
        
        skills_title = Label(skills_frame, text="💻 TECHNICAL SKILLS", 
                           font=("Segoe UI", 11, "bold"), bg="#fff3e0", fg="#e65100")
        skills_title.place(x=10, y=5)
        
        skills_text = Label(skills_frame, text="Python • OpenCV • Machine Learning • TensorFlow • MySQL • Tkinter", 
                          font=("Segoe UI", 10), bg="#fff3e0", fg="#424242")
        skills_text.place(x=10, y=28)
        
        # Contact section
        contact_frame = Frame(main_frame, bg="#e8f5e9")
        contact_frame.place(x=30, y=620, width=320, height=40)
        
        email_label = Label(contact_frame, text="📧 rajamonti31@gmail.com", 
                          font=("Segoe UI", 10), bg="#e8f5e9", fg="#2e7d32")
        email_label.pack(pady=10)
        
        phone_frame = Frame(main_frame, bg="#e8f5e9")
        phone_frame.place(x=380, y=620, width=320, height=40)
        
        phone_label = Label(phone_frame, text="📱 +91 XXXXXXXXXX", 
                          font=("Segoe UI", 10), bg="#e8f5e9", fg="#2e7d32")
        phone_label.pack(pady=10)
        
    def create_info_card(self, parent, title, content, x, y, bg_color, title_color):
        """Create a styled information card"""
        card = Frame(parent, bg=bg_color, bd=2, relief=SOLID)
        card.place(x=x, y=y, width=320, height=90)
        
        card_title = Label(card, text=title, font=("Segoe UI", 11, "bold"), 
                         bg=bg_color, fg=title_color)
        card_title.place(x=10, y=8)
        
        card_content = Label(card, text=content, font=("Segoe UI", 9), 
                           bg=bg_color, fg="#424242", justify=LEFT)
        card_content.place(x=10, y=35)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()