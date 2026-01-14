from tkinter import *
from tkinter import ttk
from PIL import Image 
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import threading
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.stop_recognition = False
        self.video_cap = None

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image 
        img_top = Image.open("college_images/face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\face_ml\face_recognition_system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_right = Label(self.root, image=self.photoimg_bottom)
        f_lbl_right.place(x=650, y=55, width=950, height=700)

        # Button frame - positioned at bottom center of right image
        btn_frame = Frame(f_lbl_right, bg="black", relief=FLAT, bd=0)
        btn_frame.place(x=340, y=610, width=240, height=40)

        # Start button
        self.b1_1 = Button(btn_frame, text="Start", cursor="hand2", 
                          command=self.start_recognition, 
                          font=("Arial", 10, "bold"), 
                          bg="#00AA00", fg="black", activebackground="#00FF00", bd=0)
        self.b1_1.place(x=0, y=0, width=120, height=40)
        
        # Stop button
        self.b1_2 = Button(btn_frame, text="Stop", cursor="hand2", 
                          command=self.stop_face_recog, 
                          font=("Arial", 10, "bold"), 
                          bg="#CC0000", fg="black", state=DISABLED, activebackground="#FF0000", bd=0)
        self.b1_2.place(x=121, y=0, width=120, height=40)
    
    def start_recognition(self):
        """Start face recognition in a separate thread"""
        self.stop_recognition = False
        self.b1_1.config(state=DISABLED)
        self.b1_2.config(state=NORMAL)
        
        # Run face recognition in separate thread so GUI remains responsive
        thread = threading.Thread(target=self.face_recog, daemon=True)
        thread.start()
    
    def stop_face_recog(self):
        """Stop face recognition"""
        print("Stop button clicked!")
        self.stop_recognition = True
        self.b1_1.config(state=NORMAL)
        self.b1_2.config(state=DISABLED)

    # ==================Attendance===================

    def mark_attendace(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    # ===============Face Recognition================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, txt, clf):
            if img is None:
                return []

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict/300))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="6394", database="face_recognition_system")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n else "Unknown"

                    my_cursor.execute("select roll from student where Student_id="+str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r else "Unknown"

                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d else "Unknown"

                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if d else "Unknown"


                    conn.close()

                    if confidence > 77:
                        cv2.putText(img, f"ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendace(i,r,n,d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                except Exception as e:
                    print(f"Database error: {e}")
                
                coord = [x, y, w, h]
            
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        # Use full path to Haar Cascade
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(cascade_path)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        self.video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not self.video_cap.isOpened():
            messagebox.showerror("Error", "Camera not detected")
            self.b1_1.config(state=NORMAL)
            self.b1_2.config(state=DISABLED)
            return

        try:
            print("Face recognition started. Press 'q' or click Stop button to exit.")
            while True:
                # Check stop flag from GUI button
                if self.stop_recognition:
                    print("Stopping recognition...")
                    break
                    
                ret, img = self.video_cap.read()
                
                if not ret or img is None:
                    print("Failed to capture frame")
                    break

                img = recognize(img, clf, faceCascade)
                cv2.imshow("Face Recognition - Press 'q' to quit", img)
                
                key = cv2.waitKey(1) & 0xFF
                
                # Exit with 'q' or ESC key
                if key == ord('q') or key == 27:
                    break
                
                # Check if window was closed
                try:
                    if cv2.getWindowProperty("Face Recognition - Press 'q' to quit", cv2.WND_PROP_VISIBLE) < 1:
                        break
                except:
                    break
        
        finally:
            # Cleanup
            if self.video_cap is not None:
                self.video_cap.release()
            cv2.destroyAllWindows()
            
            # Force flush OpenCV event queue
            for i in range(10):
                cv2.waitKey(1)
            
            print("Camera released successfully")
            
            # Re-enable start button
            self.b1_1.config(state=NORMAL)
            self.b1_2.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()