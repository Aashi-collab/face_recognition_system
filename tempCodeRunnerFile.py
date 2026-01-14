from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from datetime import datetime
import os
import cv2
import mysql.connector
import csv

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.state('zoomed')  # Maximize window
        
        # Configure style
        self.configure_styles()
        
        # Header Images
        img = Image.open("college_images/Stanford.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open("college_images/facialrecognition.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        img2 = Image.open("college_images/u.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # Background
        img3 = Image.open("college_images/bg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title with date/time
        title_frame = Frame(bg_img, bg="white")
        title_frame.place(x=0, y=0, width=1530, height=70)
        
        title_lbl = Label(title_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", 
                         font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.pack(side=TOP, pady=5)
        
        # Date/Time display
        self.datetime_label = Label(title_frame, text="", 
                                    font=("times new roman", 12, "bold"), 
                                    bg="white", fg="blue")
        self.datetime_label.pack(side=TOP)
        self.update_datetime()

        # Dashboard Frame
        dashboard_frame = Frame(bg_img, bg="white", bd=2, relief=RIDGE)
        dashboard_frame.place(x=50, y=80, width=1430, height=100)
        
        Label(dashboard_frame, text="DASHBOARD", 
              font=("times new roman", 20, "bold"), bg="white", fg="darkgreen").pack()
        
        stats_frame = Frame(dashboard_frame, bg="white")
        stats_frame.pack(pady=10)
        
        # Statistics
        self.total_students_var = StringVar()
        self.present_today_var = StringVar()
        self.absent_today_var = StringVar()
        self.attendance_rate_var = StringVar()
        
        self.create_stat_box(stats_frame, "Total Students", self.total_students_var, 0)
        self.create_stat_box(stats_frame, "Present Today", self.present_today_var, 1)
        self.create_stat_box(stats_frame, "Absent Today", self.absent_today_var, 2)
        self.create_stat_box(stats_frame, "Attendance Rate", self.attendance_rate_var, 3)
        
        self.update_statistics()

        # Main buttons container
        button_container = Frame(bg_img, bg="white")
        button_container.place(x=50, y=200, width=1430, height=480)

        # Row 1 - Main Functions
        # Student Details Button
        self.create_button(button_container, "college_images/stu.jpg", 
                          "Student Details", self.student_details, 50, 20)

        # Face Detector Button
        self.create_button(button_container, "college_images/face_detector1.jpg", 
                          "Face Detector", self.face_data, 350, 20)

        # Attendance Button
        self.create_button(button_container, "college_images/attendance.jpg", 
                          "Attendance", self.attendance_data, 650, 20)

        # Help Desk Button
        self.create_button(button_container, "college_images/help-desk.jpg", 
                          "Help Desk", self.help_desk, 950, 20)

        # Row 2 - Training & Data
        # Train Data Button
        self.create_button(button_container, "college_images/Train.jpg", 
                          "Train Data", self.train_data, 50, 260)

        # Photos Button
        self.create_button(button_container, "college_images/photos.jpg", 
                          "Photos", self.open_img, 350, 260)

        # Developer Button
        self.create_button(button_container, "college_images/developer.jpg", 
                          "Developer Info", self.developer_info, 650, 260)

        # Exit Button
        self.create_button(button_container, "college_images/exit.jpg", 
                          "Exit System", self.exit_system, 950, 260)

        # Status bar
        self.status_bar = Label(self.root, text="Ready", 
                               font=("times new roman", 10), 
                               bg="lightgray", anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)

    def configure_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')

    def create_stat_box(self, parent, title, var, col):
        """Create a statistics box"""
        frame = Frame(parent, bg="lightblue", bd=2, relief=RIDGE)
        frame.grid(row=0, column=col, padx=20, pady=5)
        
        Label(frame, text=title, font=("Arial", 10, "bold"), 
              bg="lightblue").pack(padx=20, pady=2)
        Label(frame, textvariable=var, font=("Arial", 16, "bold"), 
              bg="lightblue", fg="darkblue").pack(padx=20, pady=2)

    def update_statistics(self):
        """Update dashboard statistics"""
        try:
            # Get total students
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="6394",
                database="face_recognition_system"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM student")
            total = cursor.fetchone()[0]
            self.total_students_var.set(str(total))
            conn.close()

            # Get today's attendance
            today = datetime.now().strftime("%d/%m/%Y")
            present = 0
            
            if os.path.exists("attendance.csv"):
                with open("attendance.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) >= 6 and row[5] == today and row[6] == "Present":
                            present += 1
            
            self.present_today_var.set(str(present))
            absent = total - present
            self.absent_today_var.set(str(absent))
            
            # Calculate attendance rate
            if total > 0:
                rate = (present / total) * 100
                self.attendance_rate_var.set(f"{rate:.1f}%")
            else:
                self.attendance_rate_var.set("0%")
                
        except Exception as e:
            print(f"Error updating statistics: {e}")
            self.total_students_var.set("N/A")
            self.present_today_var.set("N/A")
            self.absent_today_var.set("N/A")
            self.attendance_rate_var.set("N/A")

    def update_datetime(self):
        """Update date and time display"""
        now = datetime.now()
        date_time = now.strftime("%A, %d %B %Y | %I:%M:%S %p")
        self.datetime_label.config(text=date_time)
        self.root.after(1000, self.update_datetime)

    def create_button(self, parent, img_path, text, command, x, y):
        """Create a styled button with image"""
        try:
            img = Image.open(img_path)
            img = img.resize((220, 180), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            # Store reference to prevent garbage collection
            if not hasattr(self, 'button_images'):
                self.button_images = []
            self.button_images.append(photo)
            
            btn = Button(parent, image=photo, command=command, 
                        cursor="hand2", bd=2, relief=RAISED)
            btn.image = photo
            btn.place(x=x, y=y, width=220, height=180)

            btn_text = Button(parent, text=text, command=command, 
                            cursor="hand2", font=("times new roman", 15, "bold"),
                            bg="darkblue", fg="white", bd=2, relief=RAISED)
            btn_text.place(x=x, y=y+180, width=220, height=40)
            
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

    def open_img(self):
        """Open photos directory"""
        try:
            if os.path.exists("Data"):
                os.startfile("Data")
            else:
                messagebox.showwarning("Warning", "Data folder not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open folder: {str(e)}")

    def student_details(self):
        """Open student details window"""
        self.status_bar.config(text="Opening Student Details...")
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        self.root.after(500, lambda: self.status_bar.config(text="Ready"))

    def train_data(self):
        """Open train data window"""
        self.status_bar.config(text="Opening Training Module...")
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        self.root.after(500, lambda: self.status_bar.config(text="Ready"))

    def face_data(self):
        """Open face recognition window"""
        self.status_bar.config(text="Opening Face Recognition...")
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        self.root.after(500, lambda: self.status_bar.config(text="Ready"))

    def attendance_data(self):
        """Open attendance window"""
        self.status_bar.config(text="Opening Attendance Management...")
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        self.root.after(500, lambda: self.status_bar.config(text="Ready"))

    def help_desk(self):
        """Show help information"""
        help_window = Toplevel(self.root)
        help_window.title("Help Desk")
        help_window.geometry("600x500")
        help_window.resizable(False, False)

        # Title
        Label(help_window, text="HELP & SUPPORT", 
              font=("times new roman", 20, "bold"), 
              bg="darkblue", fg="white").pack(fill=X)

        # Help content
        help_text = Text(help_window, font=("Arial", 11), wrap=WORD, padx=10, pady=10)
        help_text.pack(fill=BOTH, expand=True, padx=10, pady=10)

        help_content = """
FACE RECOGNITION ATTENDANCE SYSTEM - USER GUIDE

1. STUDENT DETAILS
   - Add new student information
   - Update existing student records
   - Delete student records
   - Take photo samples for training

2. TRAIN DATA
   - Train the face recognition model
   - Required before face recognition
   - Use after adding new students

3. FACE DETECTOR
   - Real-time face recognition
   - Automatic attendance marking
   - Shows recognition confidence

4. ATTENDANCE
   - View attendance records
   - Import/Export CSV files
   - Search and filter records
   - Update attendance status

5. PHOTOS
   - View captured student photos
   - Stored in 'Data' folder

TROUBLESHOOTING:

• Camera not working?
  - Check camera connections
  - Try restarting the application
  - Check camera permissions

• Recognition not working?
  - Ensure you've trained the model
  - Check if photos exist in Data folder
  - Verify database connectivity

• Database errors?
  - Check MySQL service is running
  - Verify credentials in code
  - Ensure database exists

CONTACT SUPPORT:
Email: support@facesystem.com
Phone: +1234567890

© 2024 Face Recognition System
        """
        help_text.insert(1.0, help_content)
        help_text.config(state=DISABLED)

    def developer_info(self):
        """Show developer information"""
        dev_window = Toplevel(self.root)
        dev_window.title("Developer Information")
        dev_window.geometry("500x400")
        dev_window.resizable(False, False)

        # Title
        Label(dev_window, text="DEVELOPER INFO", 
              font=("times new roman", 20, "bold"), 
              bg="darkgreen", fg="white").pack(fill=X)

        info_frame = Frame(dev_window, bg="white")
        info_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        dev_info = """
        
FACE RECOGNITION ATTENDANCE SYSTEM
Version 2.0 Enhanced

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEVELOPMENT TEAM:
• Lead Developer: [Your Name]
• UI/UX Designer: [Designer Name]
• Database Admin: [DBA Name]

TECHNOLOGIES USED:
• Python 3.x
• OpenCV (Computer Vision)
• MySQL Database
• Tkinter (GUI)
• PIL/Pillow (Image Processing)
• LBPH Face Recognizer

FEATURES:
✓ Real-time Face Recognition
✓ Automated Attendance
✓ Student Management
✓ Report Generation
✓ Data Import/Export

SYSTEM REQUIREMENTS:
• Python 3.7+
• MySQL Server
• Webcam
• 4GB RAM minimum
• Windows/Linux/MacOS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

© 2024 All Rights Reserved
        """
        
        Label(info_frame, text=dev_info, font=("Courier", 10), 
              bg="white", justify=LEFT).pack()

    def exit_system(self):
        """Exit the application"""
        result = messagebox.askyesno("Exit", 
                                     "Are you sure you want to exit the system?",
                                     parent=self.root)
        if result:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()