# 🧠 Advanced Facial Recognition Attendance System

### A Python-based Smart Attendance Solution using OpenCV, Tkinter GUI & MySQL

This project is a complete **Facial Recognition Attendance System** developed in Python.
It automates attendance marking using real-time face detection and recognition, providing an efficient alternative to manual or RFID-based attendance processes.

The system includes a full-featured **Tkinter GUI**, student management module, face dataset generation, model training, real-time recognition, and attendance report generation.

---

## 🚀 Features

### 🔹 1. User Authentication

* Secure Login Page
* Admin Dashboard Access
* Password validation & error handling

### 🔹 2. Student Management System

* Add, Update, Delete, Search students
* Store details like Roll No, Name, Branch, Year, etc.
* Capture **photo samples** (face dataset) through webcam
* Automatically stores images in structured folders

### 🔹 3. Face Dataset Generation

* Capture multiple face samples using OpenCV
* Preprocessing for higher model accuracy
* Stores unique ID-mapped images

### 🔹 4. Model Training

* Uses LBPH (Local Binary Pattern Histogram) Face Recognizer
* Trains model on captured images
* Saves trained model as `.xml` file
* Accuracy improves as dataset grows

### 🔹 5. Real-Time Face Recognition

* Webcam-based detection
* Marks attendance automatically when face is recognized
* Prevents duplicate entries
* Displays name, ID, time & date

### 🔹 6. Attendance Management

* Records attendance with timestamp
* Saves attendance in **CSV/Excel format**
* Stores attendance records in **MySQL database**
* Allows exporting reports

### 🔹 7. Modern Tkinter GUI

* Clean button-based interface
* Student Details Window
* Train Data Window
* Face Detection Window
* Attendance Report Window

---

## 🛠️ Tech Stack

| Component            | Technology Used                |
| -------------------- | ------------------------------ |
| Programming Language | **Python**                     |
| GUI Framework        | **Tkinter**                    |
| Face Recognition     | **OpenCV, Haarcascades, LBPH** |
| Database             | **MySQL**                      |
| Data Storage         | CSV / Excel                    |
| Additional Tools     | Numpy, Pillow, OS, datetime    |

---

## 📁 Project Structure

```
📦 Facial-Recognition-Attendance-System
├── 📁 student_images/         # Stored face samples
├── 📁 attendance_reports/     # CSV/Excel attendance files
├── 📁 training_data/          # Trained model files
├── main.py                    # Launch GUI
├── student.py                 # Student management module
├── train.py                   # Model training script
├── attendance.py              # Attendance detection
├── login.py                   # Authentication system
├── database.py                # Database connection
└── requirements.txt
```

---

## 📸 Screens & Workflow

1️⃣ Login →
2️⃣ Dashboard →
3️⃣ Add Student →
4️⃣ Capture Face Samples →
5️⃣ Train Model →
6️⃣ Take Attendance →
7️⃣ View Attendance Reports

---

## 💡 Future Enhancements (Optional to add)

* Web-based attendance dashboard
* Cloud database (Firebase / AWS)
* Email/SMS attendance alerts
* Mobile app integration
* Deep Learning-based FaceNet model

---

## 📜 License

This project is open-source and free to use for academic and learning purposes.

