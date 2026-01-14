from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Help Desk")
        
        # Header Section
        title_lbl = Label(self.root, text="🆘 HELP DESK & SUPPORT CENTER", 
                         font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Main background
        bg_frame = Frame(self.root, bg="#f0f4f8")
        bg_frame.place(x=0, y=45, width=1530, height=745)
        
        # Quick Help Section (Left)
        quick_frame = LabelFrame(bg_frame, text="⚡ QUICK HELP", 
                                font=("times new roman", 16, "bold"),
                                bg="white", fg="red", bd=2, relief=RIDGE)
        quick_frame.place(x=30, y=20, width=450, height=500)
        
        # Quick Help Items
        help_items = [
            ("📸 Camera Issues", "Check camera permissions\nRestart application"),
            ("👤 Face Not Detected", "Ensure good lighting\nFace camera directly"),
            ("💾 Database Errors", "Verify MySQL connection\nCheck credentials"),
            ("⚙️ System Requirements", "Python 3.7+, OpenCV 4.5+\nMySQL 8.0+, 4GB RAM"),
            ("🔄 Update Issues", "Clear cache and restart\nReinstall if needed")
        ]
        
        y_pos = 30
        for title, desc in help_items:
            title_label = Label(quick_frame, text=title, 
                              font=("times new roman", 12, "bold"),
                              bg="white", fg="red", anchor=W)
            title_label.place(x=20, y=y_pos, width=400)
            
            desc_label = Label(quick_frame, text=desc, 
                             font=("times new roman", 10),
                             bg="white", fg="black", anchor=W, justify=LEFT)
            desc_label.place(x=20, y=y_pos + 25, width=400)
            
            y_pos += 90
        
        # FAQ Section (Right)
        faq_frame = LabelFrame(bg_frame, text="❓ FREQUENTLY ASKED QUESTIONS", 
                              font=("times new roman", 16, "bold"),
                              bg="white", fg="blue", bd=2, relief=RIDGE)
        faq_frame.place(x=500, y=20, width=1000, height=500)
        
        # Create scrollable text widget for FAQs
        faq_scroll = Scrollbar(faq_frame)
        faq_scroll.pack(side=RIGHT, fill=Y)
        
        faq_text = Text(faq_frame, wrap=WORD, yscrollcommand=faq_scroll.set,
                       font=("times new roman", 11), bg="white", fg="black",
                       padx=15, pady=15)
        faq_text.pack(fill=BOTH, expand=True)
        faq_scroll.config(command=faq_text.yview)
        
        # FAQ Content
        faqs = """
Q1: How do I add a new student?
A: Navigate to Student Details → Fill all fields → Click 'Save'. Capture 10-15 face samples for better accuracy.

Q2: Why is face recognition not working?
A: Check: Poor lighting, camera connection, training data. Solution: Good lighting, check camera, train with 50+ images.

Q3: How to train the face recognition model?
A: Go to Train Data → Click 'Train'. System processes all images (2-5 minutes).

Q4: Can I use multiple cameras?
A: Yes, specify camera index in settings. Default is 0 (built-in), external cameras use 1 or 2.

Q5: What database is required?
A: MySQL 8.0+. Create database 'face_recognizer' and table 'student'. Check database_schema.sql file.

Q6: How to export attendance records?
A: Attendance section → Select date range → Click 'Export to CSV'. Saved in 'attendance' folder.

Q7: System running slow?
A: Reduce image resolution, close apps, ensure 4GB+ RAM, update OpenCV.

Q8: How to backup data?
A: Export MySQL database using phpMyAdmin. Copy 'data' folder. Recommended: Weekly backups.
        """
        
        faq_text.insert(1.0, faqs)
        faq_text.config(state=DISABLED)
        
        # Contact Section (Bottom)
        contact_frame = LabelFrame(bg_frame, text="📞 NEED MORE HELP?", 
                                  font=("times new roman", 14, "bold"),
                                  bg="white", fg="red", bd=2, relief=RIDGE)
        contact_frame.place(x=30, y=540, width=1470, height=170)
        
        info_label = Label(contact_frame, 
                          text="Contact our support team for personalized assistance",
                          font=("times new roman", 12), bg="white", fg="black")
        info_label.place(x=20, y=10, width=1400)
        
        # Contact Buttons
        email_btn = Button(contact_frame, text="📧 Email Support", 
                          font=("times new roman", 12, "bold"), 
                          bg="red", fg="white", cursor="hand2",
                          command=self.open_email)
        email_btn.place(x=100, y=50, width=250, height=50)
        
        phone_btn = Button(contact_frame, text="📱 Call: +91 9696618056", 
                          font=("times new roman", 12, "bold"), 
                          bg="blue", fg="white", cursor="hand2",
                          command=self.show_phone)
        phone_btn.place(x=400, y=50, width=250, height=50)
        
        docs_btn = Button(contact_frame, text="📚 Documentation", 
                         font=("times new roman", 12, "bold"), 
                         bg="green", fg="white", cursor="hand2",
                         command=self.open_docs)
        docs_btn.place(x=700, y=50, width=250, height=50)
        
        video_btn = Button(contact_frame, text="🎥 Video Tutorials", 
                          font=("times new roman", 12, "bold"), 
                          bg="orange", fg="white", cursor="hand2",
                          command=self.open_tutorials)
        video_btn.place(x=1000, y=50, width=250, height=50)
        
        # Footer
        footer_label = Label(contact_frame, 
                            text="💡 Tip: Press F1 anytime in the application for context-sensitive help", 
                            font=("times new roman", 10, "italic"), bg="white", fg="gray")
        footer_label.place(x=0, y=115, width=1450)
    
    def open_email(self):
        """Open email client"""
        try:
            webbrowser.open("mailto:rajamonti31@gmail.com?subject=Face Recognition System - Support")
            messagebox.showinfo("Email", "Opening your default email client...")
        except:
            messagebox.showinfo("Email", "Email: rajamonti31@gmail.com")
    
    def show_phone(self):
        """Show phone contact"""
        self.root.clipboard_clear()
        self.root.clipboard_append("+91 9696618056")
        messagebox.showinfo("Contact", "📱 Phone: +91 9696618056\n\n✓ Number copied to clipboard!")
    
    def open_docs(self):
        """Open documentation"""
        messagebox.showinfo("Documentation", 
                          "📚 Documentation Features:\n\n"
                          "• Installation Guide\n"
                          "• User Manual\n"
                          "• API Reference\n"
                          "• Troubleshooting Guide\n"
                          "• Video Tutorials\n\n"
                          "Check the 'docs' folder.")
    
    def open_tutorials(self):
        """Open video tutorials"""
        messagebox.showinfo("Video Tutorials", 
                          "🎥 Available Tutorials:\n\n"
                          "1. System Setup\n"
                          "2. Adding Students\n"
                          "3. Training Model\n"
                          "4. Face Recognition\n"
                          "5. Managing Attendance\n\n"
                          "Access from 'tutorials' folder.")


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()