from tkinter import*
from tkinter import ttk
from PIL import Image 
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Train Dataset", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("college_images/facialrecognition.png")
        img_top = img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)


        b1_1= Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)


        img_bottom = Image.open("college_images/photos.jpg")
        img_bottom = img_bottom.resize((1530,325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)
        
    def train_classifier(self):
        data_dir = "Data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, file))]    
        
        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L') 
                imageNp = np.array(img, 'uint8')
                
                filename = os.path.basename(image)
                parts = filename.split('.')
                
                # Use -2 to get the ID regardless of how many dots are in the name
                # as long as the ID is right before the extension (e.g. .1.jpg)
                id = int(parts[-2])

                faces.append(imageNp)
                ids.append(id)
                
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
                
            except Exception as e:
                print(f"Error processing {image}: {e}")
                continue
        
        if len(ids) > 0:
            ids = np.array(ids)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write('classifier.xml')
            cv2.destroyAllWindows()
            messagebox.showinfo('Result', 'Training Datasets completed!!')
        else:
            messagebox.showerror("Error", "No valid data found to train!")
if __name__ == "__main__":
            root = Tk()
            obj = Train(root)
            root.mainloop()        