import json
import tkinter as tk
from tkinter import ttk

# ฟังก์ชันสำหรับการดึงข้อมูลจากไฟล์ user.json
def get_user_data():
    with open('user.json') as file:
        user_data = json.load(file)
        return user_data

# ฟังก์ชันสำหรับการดึงข้อมูลคอร์สจากไฟล์ course.json
def get_course_data(subject):
    with open(f'{subject}_course.json') as file:
        course_data = json.load(file)
        return course_data

# ฟังก์ชันสำหรับแสดงข้อมูลใน Tkinter GUI
def show_data():
    user_data = get_user_data()
    subject = user_data['subject']
    course_data = get_course_data(subject)

    root = tk.Tk()
    root.title("ข้อมูลคอร์ส")

    tab_control = ttk.Notebook(root)

    for course_code, course_info in course_data.items():
        tab1 = tk.Frame(tab_control)
        tab_control.add(tab1, text=course_info['course'])

        label1 = tk.Label(tab1, text=f"ราคา: {course_info['price']} บาท")
        label1.pack(pady=10)
        label2 = tk.Label(tab1, text=f"ระยะเวลา: {course_info['time(hr)']} ชั่วโมง")
        label2.pack(pady=10)

    tab_control.pack(expand=1, fill="both")
    root.mainloop()

# เรียกใช้ฟังก์ชัน show_data() เพื่อแสดงข้อมูล
show_data()