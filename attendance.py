from tkinter import*
from tkinter import ttk
from PIL import Image 
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ===========variables===========
        self.attend_id=StringVar()
        self.roll=StringVar()
        self.name=StringVar()
        self.department=StringVar()
        self.time=StringVar()
        self.date=StringVar()
        self.attendance=StringVar()
        

        # 1st
        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # 2nd
        img1 = Image.open("college_images/student.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        #bg image
        img3=Image.open("college_images/bg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=650)

         #left label frame

        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("college_images/attendance.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=20, y=140, width=720, height=370)

        #lebels and entry

           #attendance id

        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.attend_id,font=("times new roman",13,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)

        #roll

        roll_no_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=4, pady=8)

        roll_no_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.roll, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=0, column=3, pady=8)


        #Name
        Name_label = Label(left_inside_frame, text="Name:",font=("times new roman", 13, "bold"),bg="white")
        Name_label.grid(row=1, column=0)

        Name_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.name, font=("comicsansns 11 bold", 13, "bold"))
        Name_entry.grid(row=1, column=1, pady=8)

        #Department

        dep_label=Label(left_inside_frame, text="Department:",font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=1, column=2,pady=8)

        dept_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.department, font=("comicsansns 11 bold", 13, "bold"))
        dept_entry.grid(row=1, column=3, pady=8)

        #time

        time_label=Label(left_inside_frame, text="Time:",font=("times new roman", 13, "bold"),bg="white")
        time_label.grid(row=2, column=0)

        time_entry = ttk.Entry(left_inside_frame, width=22,textvariable=self.time, font=("comicsansns 11 bold", 13, "bold"))
        time_entry.grid(row=2, column=1, pady=8)

        #date

        date_label=Label(left_inside_frame, text="Date",font=("times new roman", 13, "bold"),bg="white")
        date_label.grid(row=2, column=2)

        date_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.date, font=("comicsansns 11 bold", 13, "bold"))
        date_entry.grid(row=2, column=3, pady=8)

        # attendance
        date_label=Label(left_inside_frame, text="Attendance Status",font=("times new roman", 13, "bold"),bg="white")
        date_label.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status['values']=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        
#button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief= RIDGE, bg="white")
        btn_frame.place(x=0,y=300,width=710,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=17,font=("times of roman",13,"bold"),bg="blue" ,fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV",command=self.export_csv, width=17, font=("times of roman", 13, "bold"), bg="blue",fg = "white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=("times of roman", 13, "bold"), bg="blue" ,fg = "white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,width=17, font=("times of roman", 13, "bold"), bg="blue" ,fg = "white")
        reset_btn.grid(row=0, column=3)


 #right label frame

        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student attendance Details",font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=680, height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=5,width=660,height=445)

        # ==========scroll bar table===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable['show']='headings'

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # =============fetch data========
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#     import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(filetypes=(("CSV File","*.csv"),("All File","*.*")),initialdir=os.getcwd(),title="Open CSV",parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

# export csv
    def export_csv(self):
        try:
             if len(mydata)==0:
                  messagebox.showerror("No Data","No Data found to export",parent=self.root)
                  return False
             fln=filedialog.asksaveasfilename(filetypes=(("CSV File","*.csv"),("All File","*.*")),initialdir=os.getcwd(),title="Open CSV",parent=self.root)
             with open(fln,mode="w",newline="") as myfile:
                  exp_write=csv.writer(myfile,delimiter=",")
                  for i in mydata:
                       exp_write.writerow(i)
                  messagebox.showinfo("Data Exported","Your Data Exported to "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es: 
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.attend_id.set(rows[0])
        self.roll.set(rows[1])
        self.name.set(rows[2])
        self.department.set(rows[3])
        self.time.set(rows[4])
        self.date.set(rows[5])
        self.attendance.set(rows[6])

    def reset_data(self):
        self.attend_id.set("")
        self.roll.set("")
        self.name.set("")
        self.department.set("")
        self.time.set("")
        self.date.set("")
        self.attendance.set("")
        
if __name__ == "__main__":
            root = Tk()
            obj = Attendance(root)
            root.mainloop()