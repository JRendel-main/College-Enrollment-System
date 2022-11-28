import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sl
import random
import smtplib
from tkinter import messagebox as mb
import math

def main():
    print('main')
    root.destroy()


def enrollmentform():
    def addStudent():
        mb.showinfo("OTP Verification", "OTP has been sent to your registered email address.")
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]
        print(OTP)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("hirotoshitest@gmail.com", "nhqdiwtariodmlxy")
        message = "Your OTP and Student No is " + OTP
        s.sendmail("hirotoshitest@gmail.com", entry_6.get(), message)
        s.quit()
        mb.showinfo("OTP Verification", "OTP has been sent to your registered email address.")
        #create table students and insert into database
        conn = sl.connect('college.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, course TEXT, address TEXT, email TEXT, password TEXT)")
        c.execute("INSERT INTO students VALUES (:student_id, :first_name, :last_name, :course, :address, :email, :password)", {
            'student_id': int(OTP),
            'first_name': entry_3.get(),
            'last_name': entry_4.get(),
            'course': combobox_1.get(),
            'address': entry_5.get(),
            'email': entry_6.get(),
            'password': 'pass'
        })
        conn.commit()
        conn.close()
        mb.showinfo("Success", "Student Added")
        toplevel, toplevel_2.destroy()
        newStudent()

    def cancel():
        toplevel_2.withdraw()

    toplevel_2 = tk.Toplevel()
    toplevel_2.geometry("640x480")
    frame_2 = ttk.Frame(toplevel_2)
    frame_2.configure(height=200, width=200)
    label_3 = ttk.Label(frame_2)
    label_3.configure(
        font="{Arial Rounded MT Bold} 20 {bold}",
        text='Enrollment Form')
    label_3.place(anchor="center", relx=0.5, rely=0.5, x=0, y=0)
    frame_2.place(
        anchor="center",
        relheight=0.1,
        relwidth=1.0,
        relx=0.5,
        rely=0.05,
        x=0,
        y=0)
    frame_3 = ttk.Frame(toplevel_2)
    frame_3.configure(height=200, width=200)
    label_4 = ttk.Label(frame_3)
    label_4.configure(font="{Britannic Bold} 12 {}", text='First Name')
    label_4.place(anchor="n", relx=0.5, rely=0.05, x=0, y=0)
    entry_3 = ttk.Entry(frame_3)
    entry_3.place(anchor="n", relx=0.5, rely=0.13, x=0, y=0)
    label_5 = ttk.Label(frame_3)
    label_5.configure(font="{Britannic Bold} 12 {}", text='Last Name')
    label_5.place(anchor="n", relx=0.5, rely=0.21, x=0, y=0)
    entry_4 = ttk.Entry(frame_3)
    entry_4.place(anchor="n", relx=0.5, rely=0.28, x=0, y=0)
    
    combobox_1 = ttk.Combobox(frame_3)
    combobox_1['values'] = ('BSIT', 'BSBA', 'BSMA', 'BIT')
    combobox_1.configure(state="normal")
    combobox_1.place(anchor="nw", relx=0.29, rely=0.45, x=0, y=0)
    label_6 = ttk.Label(frame_3)
    label_6.configure(font="{Britannic Bold} 12 {}", text='Course')
    label_6.place(anchor="n", relx=0.5, rely=0.37, x=0, y=0)
    label_7 = ttk.Label(frame_3)
    label_7.configure(font="{Britannic Bold} 12 {}", text='Address')
    label_7.place(anchor="n", relx=0.5, rely=0.53, x=0, y=0)
    entry_5 = ttk.Entry(frame_3)
    entry_5.place(anchor="n", relx=0.5, rely=0.6, x=0, y=0)
    label_8 = ttk.Label(frame_3)
    label_8.configure(font="{Britannic Bold} 12 {}", text='Email')
    label_8.place(anchor="n", relx=0.5, rely=0.67, x=0, y=0)
    entry_6 = ttk.Entry(frame_3)
    entry_6.place(anchor="n", relx=0.5, rely=0.73, x=0, y=0)
    button_1 = tk.Button(frame_3, command=addStudent)
    button_1.configure(background="#52ef66", text='Send OTP')
    button_1.place(anchor="n", relx=0.2, rely=0.85, x=0, y=0)
    button_2 = tk.Button(frame_3, command=cancel)
    button_2.configure(background="#fa474b", text='Cancel')
    button_2.place(anchor="n", relx=0.8, rely=0.85, x=0, y=0)
    frame_3.place(
        anchor="center",
        relheight=0.7,
        relwidth=0.5,
        relx=0.5,
        rely=0.5,
        x=0,
        y=0)
    toplevel_2.mainloop()

def login():
    conn = sl.connect('college.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE student_id = ? AND password = ?", (entry_1.get(), entry_2.get()))
    if c.fetchone() is not None:
        print("Login Successful")
        toplevel.destroy()
        main()
    else:
        print("Login Failed")

def newStudent():
    root = tk.Tk()
    # hide root
    root.withdraw()
    # remove root window
    toplevel = tk.Toplevel(root)
    toplevel.geometry("1024x576")
    toplevel.configure(background='gray')
    label_1 = ttk.Label(toplevel)
    label_1.configure(
        font="{Arial Rounded MT Bold} 24 {}",
        relief="flat",
        text='College Enrollment System\n')
    label_1.place(
        anchor="center",
        bordermode="outside",
        relheight=0.081,
        relx=0.5,
        rely=0.13,
        x=0,
        y=0)
    frame_1 = ttk.Frame(toplevel)
    frame_1.configure(height=200, width=200)
    label_2 = ttk.Label(frame_1)
    label_2.configure(
        font="{Arial Rounded MT Bold} 24 {}",
        relief="flat",
        text='Verify')
    label_2.place(anchor="center", relx=0.5, rely=0.14, x=0, y=0)
    entry_1 = ttk.Entry(frame_1)
    entry_1.place(anchor="center", relx=0.6, rely=0.42, x=0, y=0)
    entry_2 = ttk.Entry(frame_1, show='*')
    entry_2.place(anchor="center", relx=0.6, rely=0.64, x=0, y=0)
    label_3 = ttk.Label(frame_1)
    label_3.configure(font="{@Malgun Gothic} 16 {}", text='OTP/Student No: ')
    label_3.place(anchor="nw", relx=0.1, rely=0.35, x=0, y=0)
    label_4 = ttk.Label(frame_1)
    label_4.configure(font="{@Malgun Gothic} 16 {}", text='Password: ')
    label_4.place(anchor="nw", relx=0.1, rely=0.57, x=0, y=0)
    button_1 = ttk.Button(frame_1)
    button_1.configure(text='Verify', command=login)
    button_1.place(anchor="center", relx=0.5, rely=0.79, x=0, y=0)
    frame_1.place(
        anchor="nw",
        relheight=0.47,
        relwidth=0.39,
        relx=0.3,
        rely=0.31,
        x=0,
        y=0)

root = tk.Tk()
# hide root
root.withdraw()
# remove root window
toplevel = tk.Toplevel(root)
toplevel.geometry("1024x576")
toplevel.configure(background='gray')
label_1 = ttk.Label(toplevel)
label_1.configure(
    font="{Arial Rounded MT Bold} 24 {}",
    relief="flat",
    text='College Enrollment System\n')
label_1.place(
    anchor="center",
    bordermode="outside",
    relheight=0.081,
    relx=0.5,
    rely=0.13,
    x=0,
    y=0)
frame_1 = ttk.Frame(toplevel)
frame_1.configure(height=200, width=200)
label_2 = ttk.Label(frame_1)
label_2.configure(
    font="{Arial Rounded MT Bold} 24 {}",
    relief="flat",
    text='Login')
label_2.place(anchor="center", relx=0.5, rely=0.14, x=0, y=0)
entry_1 = ttk.Entry(frame_1)
entry_1.place(anchor="center", relx=0.6, rely=0.42, x=0, y=0)
entry_2 = ttk.Entry(frame_1, show='*')
entry_2.place(anchor="center", relx=0.6, rely=0.64, x=0, y=0)
label_3 = ttk.Label(frame_1)
label_3.configure(font="{@Malgun Gothic} 16 {}", text='Student No: ')
label_3.place(anchor="nw", relx=0.1, rely=0.35, x=0, y=0)
label_4 = ttk.Label(frame_1)
label_4.configure(font="{@Malgun Gothic} 16 {}", text='Password: ')
label_4.place(anchor="nw", relx=0.1, rely=0.57, x=0, y=0)
button_1 = ttk.Button(frame_1)
button_1.configure(text='Login', command=login)
button_1.place(anchor="center", relx=0.5, rely=0.79, x=0, y=0)
label_5 = ttk.Label(frame_1)
label_5.configure(
    font="{Arial} 7 {}",
    justify="center",
    takefocus=True,
    text='New enrollee? Click here to enroll')
label_5.place(anchor="center", relx=.5, rely=0.91, x=0, y=0)
frame_1.place(
    anchor="nw",
    relheight=0.47,
    relwidth=0.39,
    relx=0.3,
    rely=0.31,
    x=0,
    y=0)
# run function when label_5 is clicked
label_5.bind("<Button-1>", lambda event: enrollmentform())
root.mainloop()
