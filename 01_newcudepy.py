import json
from tkinter import *
from tkinter import messagebox  
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk, filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk
import re
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import subprocess
from reportlab.lib import fonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from sys import platform
import qrcode
from PIL import Image, ImageTk
from datetime import datetime

#common
userPath = "02_user.json"
subjectPath = "02_course.json"
userNameCache = ""
isLogin = False
isAdmin = False
addstd = None
signstd = None
processaddco = None
prowithdraw = None
domain =[".com",".net",".co.th",".ac.th",".go.th",".or.th",".in.th",".mil",".int",".net",".edu",".gov",".org",".biz",".info",".mobi",".name",".tv",".ws",".asia",".xxx",".idv.tw",".me",".co",".cc",".bz",".de",".tw",".eu",".us",".uk",".ca",".cn",".fr",".in",".jp",".kr",".ru",".sg",".vn",".com.tw",".net.tw",".org.tw",".com.cn",".net.cn",".org.cn",".gov.cn",".co.jp",".co.uk",".co.kr",".co.th",".co.in",".co.id",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve"]
def common(status,operation):
    operation(status)
def setUserName(name):
    global userNameCache
    userNameCache = name
def getUserName():
    global userNameCache
    return userNameCache
def setAdmin(status):
    global isAdmin
    isAdmin = status
def setLogin(status):
    global isLogin
    isLogin = status
def getLogin():
    global isLogin
    return isLogin
def getAdmin():
    global isAdmin
    return isAdmin
def passwordStrength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)
    is_length_valid = len(password) >= 8
    return has_upper and has_lower and has_digit and is_length_valid and has_special
def emailStrength(email):
    domain = [".com", ".co.th", ".net"]  # ระบุรายการของโดเมนที่อนุญาต
    hasDomain = False  # กำหนดค่าเริ่มต้นของ hasDomain เป็น False
    for i in domain:
        if i in email:
            hasDomain = True
            break
    hasAt = "@" in email
    hasDot = "." in email
    return hasDomain and hasAt and hasDot


root = Tk()
root.title("Login")
root.geometry("1000x500+50+50")  #กำหนดขนาดจอ

bglogin = Image.open('Login.png')
login_bg = ImageTk.PhotoImage(bglogin)
BG = Label(root, image = login_bg)
BG.pack()

def admin():
    admin_desk = Toplevel(root)
    admin_desk.title("For Admin")
    admin_desk.geometry("1000x500+50+50")  #กำหนดขนาดจอ

    adminbg = Image.open('Bgmenuadmin.png')
    root.add_menu = ImageTk.PhotoImage(adminbg)
    addmenu = Label(admin_desk,image=root.add_menu)
    addmenu.pack()

    def addSubject():
        def processaddco():
            global processaddco
            id = id_entry.get()
            course = course_entry.get()
            time = time_entry.get()
            price = price_entry.get()

            try:
                with open(subjectPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    messagebox.showerror("Error","รหัสวิชามีอยู่ในระบบแล้ว")
                    return
                newData = {id: {"course":course,"time(hr)":time, "price" : price}}
                data.update(newData)
                with open(subjectPath, "w") as file:
                    json.dump(data, file, indent=4)
                    admin_desk.grab_set()
                    messagebox.showinfo(0,f"เพิ่ม {course} สำเร็จแล้ว")
                    admin_desk.grab_release()
            except Exception as e:
                print(e)
            addsub_desk.destroy()
            
            

        addsub_desk = Toplevel(root)
        addsub_desk.title("Add new course")
        addsub_desk.geometry("1000x500+50+50")  #กำหนดขนาดจอ

        bgaddsub = Image.open('Bgadcourse.png')
        root.addcobg = ImageTk.PhotoImage(bgaddsub)
        bg_addcourse = Label(addsub_desk,image=root.addcobg)
        bg_addcourse.pack()

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(addsub_desk,image=root.back_but,bg='#5398f6',command=addsub_desk.destroy)
        backbutton.place(x=10, y=420)
           
        id_entry = Entry(addsub_desk,font=20,borderwidth=0)
        id_entry.place(x=360,y=115)

        course_entry = Entry(addsub_desk,font=20,borderwidth=0)
        course_entry.place(x=360,y=185)

        time_entry = Entry(addsub_desk,font=20,borderwidth=0)
        time_entry.place(x=360,y=270)

        price_entry = Entry(addsub_desk,font=20,borderwidth=0)
        price_entry.place(x=360,y=335)

        addbut = Image.open('ButtonAdd.png')
        root.add_but = ImageTk.PhotoImage(addbut)
        addbutton = Button(addsub_desk,image=root.add_but,bg="#6617ff",command=processaddco)
        addbutton.place(x=465, y=400)

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(addsub_desk, image=root.home_but,bg='#5398f6',command=addsub_desk.destroy)
        homebutton.place(x=826,y=22)

    def deleteSubject():
        def delsubprocess():
                id = iddel_entry.get()
                try:
                    with open(subjectPath, "r") as file:
                        data = json.load(file)
                    if id in data:
                        del data[id]
                        with open(subjectPath, "w") as file:
                            json.dump(data, file, indent=4)
                        messagebox.showinfo(0,f"ลบ {id} สำเร็จแล้ว\n\n")
                    else:
                        admin_desk.grab_set()
                        messagebox.showerror(0,f"ไม่พบรหัสวิชา {id} ในระบบ\n\n")
                        admin_desk.grab_release()
                except Exception as e:
                    print(e)
                delsub_desk.destroy()

        delsub_desk = Toplevel(root)
        delsub_desk.title("Delete course")
        delsub_desk.geometry("1000x500+50+50")  #กำหนดขนาดจอ

        bgdeldsub = Image.open('Bgdeletecourse.png')
        root.delcobg = ImageTk.PhotoImage(bgdeldsub)
        bg_delcourse = Label(delsub_desk,image=root.delcobg)
        bg_delcourse.pack()

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(delsub_desk,image=root.back_but,bg='#5398f6',command=delsub_desk.destroy)
        backbutton.place(x=10, y=420)

        iddel_entry =Entry(delsub_desk,font=20,borderwidth=0)
        iddel_entry.place(x=320,y=235)

        delbut = Image.open('ButtonDelete.png')
        root.del_but = ImageTk.PhotoImage(delbut)
        delbutton =Button(delsub_desk,image=root.del_but,bg="#66a7ff",command=delsubprocess)
        delbutton.place(x=450,y=290)

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(delsub_desk, image=root.home_but,bg='#5398f6',command=delsub_desk.destroy)
        homebutton.place(x=826,y=22)

    def addStudent():
        def addstd():
            global addstd
            fname = name_signEntry.get()
            lname = lname_signEntry.get()
            nickname = nickname_signEntry.get()
            email = email_signEntry.get()
            phoneNumber = tel_signEntry.get()
            userName = username_signEntry.get()
            password = password_signEntry.get()

            with open(userPath, "r") as file:
                data = json.load(file)
            newData = {userName: {"fname": fname, "lname": lname, "nickname": nickname, "email": email, "phoneNumber": phoneNumber, "password": password, "isAdmin": False, "subject": []}}
            if userName in data:
                messagebox.showerror(0, "มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว")
                return 
            
            elif userName not in data:
                if not emailStrength(email):  # ตรวจสอบความถูกต้องของอีเมล
                    if email_signEntry == '':  # ตรวจสอบว่าอีเมลถูกป้อนหรือไม่
                        messagebox.showerror(0, "กรุณาป้อนอีเมล")
                        
                    else:
                        messagebox.showerror(0, "อีเมลไม่ถูกต้อง")
                        
                elif not passwordStrength(password):  # ตรวจสอบความซับซ้อนของรหัสผ่าน
                    if password_signEntry == '':
                        messagebox.showerror(0, "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร")
                        
                    else:
                        messagebox.showerror(0, "รหัสผ่านไม่ถูกต้อง")
                        addStudent()
                elif len(phoneNumber) != 10 or not phoneNumber.isdigit():  # ตรวจสอบความถูกต้องของหมายเลขโทรศัพท์
                    messagebox.showerror(0, "โปรดป้อนหมายเลขโทรศัพท์ ให้ครบ 10 ตัว และป้อนเฉพาะตัวเลขเท่านั้น")
                    
                else:
                    with open(userPath, "r") as file:
                        data = json.load(file)  
                    newData = {userName:{"fname":fname,"lname":lname,"nickname":nickname,"email":email,"phoneNumber":phoneNumber,"password":password,"isAdmin":False,"subject":[]}}
                    
                    if userName in data:
                        return messagebox.showerror(0,"มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว")
                    data.update(newData) 
                    with open(userPath, "w") as file:
                        json.dump(data, file, indent=4)
                    admin_desk.grab_set
                    messagebox.showinfo(0,"สมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ")
                    admin_desk.grab_release()
            addstd_desk.destroy()
                    
        addstd_desk = Toplevel()
        addstd_desk.title("Add new student")
        addstd_desk.geometry("1000x500+50+50")  # กำหนดขนาดจอ

        bgaddsub = Image.open('Bgadstd.png')
        root.addcobg = ImageTk.PhotoImage(bgaddsub)
        bg_addcourse = Label(addstd_desk, image=root.addcobg)
        bg_addcourse.pack()

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(addstd_desk, image=root.back_but, bg='#5398f6', command=addstd_desk.destroy)
        backbutton.place(x=10, y=420)

        name_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        name_signEntry.place(x=130, y=105)

        lname_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        lname_signEntry.place(x=580, y=105)

        nickname_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        nickname_signEntry.place(x=120, y=175)

        tel_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        tel_signEntry.place(x=580, y=175)

        email_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        email_signEntry.place(x=340, y=240)

        username_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        username_signEntry.place(x=340, y=302)

        password_signEntry = Entry(addstd_desk, font=20, borderwidth=0)
        password_signEntry.place(x=340, y=355)

        addbut = Image.open('ButtonAdd.png')
        root.add_but = ImageTk.PhotoImage(addbut)
        addbutton = tk.Button(addstd_desk, image=root.add_but, bg="#6617ff", command=addstd)
        addbutton.place(x=465, y=400)

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(addstd_desk, image=root.home_but,bg='#5398f6',command=addstd_desk.destroy)
        homebutton.place(x=826,y=22)

    def deleteStudent():
        def delstd():
            id = iddel_entry.get()
            try:
                with open(userPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    del data[id]
                    with open(userPath, "w") as file:
                        json.dump(data, file, indent=4)
                    messagebox.showinfo(0, f"ลบ {id} สำเร็จแล้ว")
                else:
                    admin_desk.grab_set()
                    messagebox.showerror(0, f"ไม่พบชื่อผู้ใช้ {id} ในระบบ")
                    admin_desk.grab_release()
            except Exception as e:
                print(e)
            delstd_desk.destroy()

        delstd_desk = Toplevel(root)
        delstd_desk.title("Delete student")
        delstd_desk.geometry("1000x500+50+50")  # กำหนดขนาดจอ

        bgaddsub = Image.open('Bgdelstd.png')
        root.addcobg = ImageTk.PhotoImage(bgaddsub)
        bg_addcourse = Label(delstd_desk, image=root.addcobg)
        bg_addcourse.pack()

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(delstd_desk, image=root.back_but, bg='#5398f6', command=delstd_desk.destroy)
        backbutton.place(x=10, y=420)

        iddel_entry = Entry(delstd_desk, font=20, borderwidth=0)
        iddel_entry.place(x=320, y=235)

        delbut = Image.open('ButtonDelete.png')
        root.del_but = ImageTk.PhotoImage(delbut)
        delbutton = Button(delstd_desk, image=root.del_but, bg="#66a7ff", command=delstd)
        delbutton.place(x=450, y=290)

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(delstd_desk, image=root.home_but,bg='#5398f6',command=delstd_desk.destroy)
        homebutton.place(x=826,y=22)

    def setAd():
        setadmin_desk = Toplevel(root)
        setadmin_desk.title("Set Admin")
        setadmin_desk.geometry("1000x500+50+50")

        setadmin = Image.open('Bgdelstd.png')  
        root.setadmin_bg = ImageTk.PhotoImage(setadmin)
        setadminbg = Label(setadmin_desk, image=root.setadmin_bg)
        setadminbg.pack()

        def setad():
            id = idsetadmin_entry.get()
            try:
                with open(userPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    data[id]["isAdmin"] = True
                    with open(userPath, "w") as file:
                        json.dump(data, file, indent=4)
                    messagebox.showinfo(0,f"เพิ่มสิทธิ์แอดมิน {id} สำเร็จแล้ว\n\n")
                else:
                    admin_desk.grab_set()
                    messagebox.showerror(0,f"ไม่พบชื่อผู้ใช้ {id} ในระบบ\n\n")
                    admin_desk.grab_release()
            except Exception as e:
                print(e)
            setadmin_desk.destroy()

        idsetadmin_entry = Entry(setadmin_desk, font=20,borderwidth=0)
        idsetadmin_entry.place(x=320, y=235)

        setadmin = Image.open('ButtonAdd.png')  
        root.setadmin_but = ImageTk.PhotoImage(setadmin)
        setadminbutton = Button(setadmin_desk, image=root.setadmin_but,bg='#66a7ff',command=setad)
        setadminbutton.place(x=450,y=300)

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(setadmin_desk, image=root.home_but,bg='#5398f6',command=setadmin_desk.destroy)
        homebutton.place(x=826,y=22)

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(setadmin_desk,image=root.back_but,bg='#5398f6',command=setadmin_desk.destroy)
        backbutton.place(x=10,y=420)

    def allStd():
        allstudent_desk = Toplevel(root)
        allstudent_desk.title("All sesult students")
        allstudent_desk.geometry("1000x500+50+50")

        allstudent = Image.open('Bgshowstudent.png')
        root.allstudent_bg = ImageTk.PhotoImage(allstudent)
        allstudentbg = Label(allstudent_desk, image=root.allstudent_bg)
        allstudentbg.pack()

        def user_data():
            with open('02_user.json') as f:
                data = json.load(f)
                return data

        def display_data(allstudent_desk, data_dict):
            y_coordinate = 130
            for person_name, person_info in data_dict.items():
                if not person_info['isAdmin']:  # Check if isAdmin is False
                    info = ('ชื่อ : {:<15} {:^20} \t\tชื่อเล่น : {} \t\tEmail : {} \t\tหมายเลขโทรศัพท์ : {}'.format(person_info['fname'], person_info['lname'], person_info['nickname'], person_info['email'], person_info['phoneNumber']))  
                    label = tk.Label(allstudent_desk, text=info)
                    label.place(x=110, y=y_coordinate)
                    y_coordinate += 30
                    # label.place(x=110, y=130)
                    # label.pack()

        # Load data from JSON file
        data = user_data()

        # Call the display function automatically
        display_data(allstudent_desk, data)

        result_label = tk.Label(allstudent_desk, text="")
        result_label.pack()

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(allstudent_desk, image=root.back_but, bg='#5398f6', command=allstudent_desk.destroy)
        backbutton.place(x=10, y=420)

        homebut = Image.open('Home.png')
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(allstudent_desk, image=root.home_but, bg='#5398f6', command=allstudent_desk.destroy)
        homebutton.place(x=826, y=22)

    def allCourses():
        allcourses_desk = Toplevel(root)
        allcourses_desk.title("All Courses")
        allcourses_desk.geometry("1000x500+50+50")

        allcourses_bg = Image.open('Bgshowcourse.png')  # กำหนด path รูปภาพ
        root.allcourses_bg = ImageTk.PhotoImage(allcourses_bg)
        allcoursesbg = Label(allcourses_desk, image=root.allcourses_bg)
        allcoursesbg.pack()

        def course_data():
            with open('02_course.json') as f:
                data = json.load(f)
                return data

        def display_data(allcourses_desk, data_dict):
            y_coordinate = 130
            for course_code, course_info in data_dict.items():
                info = f"Course Code : {course_code} \t "
                info += ('ชื่อคอร์ส : {} \t\tเวลา : {} ชั่วโมง \t\tราคา : {} บาท'.format(course_info['course'], course_info['time(hr)'], course_info['price']))
                # for key, value in course_info.items():
                #     info += f"{key}: {value}\t"
                label = tk.Label(allcourses_desk, text=info)
                label.place(x=110, y=y_coordinate)
                y_coordinate += 30

        # Load data from JSON file
        data = course_data()

        # Call the display function automatically
        display_data(allcourses_desk, data)

        result_label = tk.Label(allcourses_desk, text="")
        result_label.pack()

        butback = Image.open('Back.png')  # กำหนด path รูปภาพ
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(allcourses_desk, image=root.back_but, bg='#5398f6', command=allcourses_desk.destroy)
        backbutton.place(x=10, y=420)

        homebut = Image.open('Home.png')  # กำหนด path รูปภาพ
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(allcourses_desk, image=root.home_but, bg='#5398f6', command=allcourses_desk.destroy)
        homebutton.place(x=826, y=22)

    def deleteAdmin():
        delAdmin_desk = Toplevel(root)
        delAdmin_desk.title("Remove Admin")
        delAdmin_desk.geometry("1000x500+50+50")  # กำหนดขนาดจอ

        bgdelAdmin = Image.open('Bgdelstd.png')
        root.delAdminbg = ImageTk.PhotoImage(bgdelAdmin)
        bg_delAdmin = Label(delAdmin_desk, image=root.delAdminbg)
        bg_delAdmin.pack()

        userdel_entry = Entry(delAdmin_desk, font=20, borderwidth=0)
        userdel_entry.place(x=320, y=235)

        def delad():
            user = userdel_entry.get()
            try:
                with open(userPath, "r") as file:
                    data = json.load(file)
                if user in data:
                    data[user]["isAdmin"] = False
                    with open(userPath, "w") as file:
                        json.dump(data, file, indent=4)
                    messagebox.showinfo(0, f"ลบสิทธิ์แอดมิน {user} สำเร็จแล้ว\n\n")
                else:
                    admin_desk.grab_set()
                    messagebox.showerror(0, f"ไม่พบชื่อผู้ใช้ {user} ในระบบ\n\n")
                    admin_desk.grab_release()
            except Exception as e:
                print(e)
            delAdmin_desk.destroy()

        delbut = Image.open('ButtonDelete.png')
        root.del_but = ImageTk.PhotoImage(delbut)
        delbutton = Button(delAdmin_desk, image=root.del_but, bg="#66a7ff", command=delad)
        delbutton.place(x=450, y=290)

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(delAdmin_desk, image=root.back_but, bg='#5398f6',command=delAdmin_desk.destroy)
        backbutton.place(x=10, y=420)

        homebut = Image.open('Home.png')
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(delAdmin_desk, image=root.home_but, bg='#5398f6', command=delAdmin_desk.destroy)
        homebutton.place(x=826, y=22)

    def editcourse():
        edit_desk = Toplevel(root)
        edit_desk.title("Edit Courses")
        edit_desk.geometry("1000x500+50+50")

        editCourse_deskbg = Image.open('Bgupdate.png')  
        root.editCourse_bg = ImageTk.PhotoImage(editCourse_deskbg)
        editCourse = Label(edit_desk, image=root.editCourse_bg)
        editCourse.pack()

        homebut = Image.open('Home.png')  
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(edit_desk, image=root.home_but,bg='#5398f6',command=edit_desk.destroy)
        homebutton.place(x=826,y=22)

        courseid_entry = Entry(edit_desk, font=20,borderwidth=0)
        courseid_entry.place(x=330, y=118)

        ncourse_entry = Entry(edit_desk, font=20,borderwidth=0)
        ncourse_entry.place(x=330, y=188)

        time_entry = Entry(edit_desk, font=20,borderwidth=0)
        time_entry.place(x=330, y=273)

        price_entry = Entry(edit_desk, font=20,borderwidth=0)
        price_entry.place(x=330, y=343)

        def editcourse():
            with open('02_course.json') as f:
                course_name = courseid_entry.get()
                data = json.load(f)
                if course_name in data:
                    ncourse_entry.insert(0,data[course_name]["course"])
                    time_entry.insert(0,data[course_name]["time(hr)"])
                    price_entry.insert(0,data[course_name]["price"])
                else:
                    messagebox.showerror(0,f"ไม่พบรหัสวิชา {course_name} ในระบบ")

            def up(): 
                new_price = price_entry.get()
                new_time = time_entry.get()
                new_subject_name = ncourse_entry.get() 
                if new_price:
                    data[course_name]["course"] = new_subject_name
                if new_time:
                    data[course_name]["time(hr)"] = new_time
                if new_subject_name:
                    data[course_name]["price"] = new_price
                with open(subjectPath, "w") as file:
                    json.dump(data, file, indent=4)  
                    admin_desk.grab_set() 
                    messagebox.showinfo(0,f"แก้ไขรหัสวิชา {course_name} สำเร็จแล้ว")
                    admin_desk.grab_release()
                edit_desk.destroy()

            backbut = Image.open('Buttonupdate.png')  
            root.back_but = ImageTk.PhotoImage(backbut)
            backbutton = Button(edit_desk, image=root.back_but,bg='#66a7ff',command=up)
            backbutton.place(x=440,y=395)

        backbu = Image.open('Back.png')  
        root.back_bu = ImageTk.PhotoImage(backbu)
        backbu = Button(edit_desk, image=root.back_bu,bg='#66a7ff',command=edit_desk.destroy)
        backbu.place(x=10,y=420)

        searchbut = Image.open('ButtonSearch.png')  
        root.search_but = ImageTk.PhotoImage(searchbut)
        searchbutton = Button(edit_desk, image=root.search_but,bg='#66a7ff',command=editcourse)
        searchbutton.place(x=700,y=105)

    def edituser():
        edituser_desk = Toplevel(root)
        edituser_desk.title("Edit Users")
        edituser_desk.geometry("1000x500+50+50")

        edituser_deskbg = Image.open('Bgeditstd.png')
        root.edituser_bg = ImageTk.PhotoImage(edituser_deskbg)
        edituser = Label(edituser_desk, image=root.edituser_bg)
        edituser.pack()

        homebut = Image.open('Home.png')
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(edituser_desk, image=root.home_but, bg='#5398f6',command=edituser_desk.destroy)
        homebutton.place(x=826, y=22)

        username_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        username_Entry.place(x=360, y=117)

        name_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        name_Entry.place(x=130, y=180)

        lname_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        lname_Entry.place(x=575, y=180)

        nickname_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        nickname_Entry.place(x=130, y=250)

        tel_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        tel_Entry.place(x=575, y=250)

        email_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        email_Entry.place(x=330, y=315)

        password_Entry = Entry(edituser_desk, font=20, borderwidth=0)
        password_Entry.place(x=330, y=380)

        def editUser():
            person_name = username_Entry.get()
            with open('02_user.json') as f:
                data = json.load(f)
                if person_name in data:
                    name_Entry.insert(0, data[person_name]["fname"])
                    lname_Entry.insert(0, data[person_name]["lname"])
                    nickname_Entry.insert(0, data[person_name]["nickname"])  # Added 0 for index
                    tel_Entry.insert(0, data[person_name]["phoneNumber"])  # Added 0 for index
                    email_Entry.insert(0, data[person_name]["email"])  # Added 0 for index
                    password_Entry.insert(0, data[person_name]["password"])
                else:
                    messagebox.showerror(0, f"ไม่พบชื่อผู้ใช้\n {person_name} \nในระบบ")

            def dataupdate():
                new_fname = name_Entry.get()
                new_lname = lname_Entry.get()
                new_nickname = nickname_Entry.get()
                new_email = email_Entry.get()
                new_phoneNumber = tel_Entry.get()
                new_password = password_Entry.get()
                if new_fname:
                    data[person_name]["fname"] = new_fname
                if new_lname:
                    data[person_name]["lname"] = new_lname
                if new_nickname:
                    data[person_name]["nickname"] = new_nickname
                if new_email:
                    data[person_name]["email"] = new_email
                if new_phoneNumber:
                    data[person_name]["phoneNumber"] = new_phoneNumber
                if new_password:
                    data[person_name]["password"] = new_password
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                    messagebox.showinfo(0, f"แก้ไขรายการของคุณ\n {person_name} \nสำเร็จแล้ว")
                edituser_desk.destroy()

            updatebut = Image.open('Buttonupdate.png')
            root.update_but = ImageTk.PhotoImage(updatebut)
            updatebutton = Button(edituser_desk, image=root.update_but, bg='#66a7ff', command=dataupdate)  # Fixed function call
            updatebutton.place(x=440, y=420)

        backbuttoo = Image.open('Back.png')
        root.back_buttoo = ImageTk.PhotoImage(backbuttoo)
        backbuttoo = Button(edituser_desk, image=root.back_buttoo, bg='#66a7ff', command=edituser_desk.destroy)
        backbuttoo.place(x=10, y=420)

        searchbut = Image.open('ButtonSearch.png')
        root.search_but = ImageTk.PhotoImage(searchbut)
        searchbutton = Button(edituser_desk, image=root.search_but, bg='#66a7ff', command=editUser)
        searchbutton.place(x=730, y=101)

    def logout():
        admin_desk.destroy()

    butout  =Image.open('Logout.png')
    root.out_but = ImageTk.PhotoImage(butout)
    outbutton = Button(admin_desk, image = root.out_but,bg = "#5398f6",command=logout )
    outbutton.place(x=815,y=15)

    butaddcourse  =Image.open('ButAddcourse.png')
    root.addcourse_but = ImageTk.PhotoImage(butaddcourse)
    addcoursebutton = Button(admin_desk, image = root.addcourse_but,bg = "#66a7ff",command=addSubject)
    addcoursebutton.place(x=63,y=120)

    butaddstudent  =Image.open('ButAddStd.png')
    root.addstudent_but = ImageTk.PhotoImage(butaddstudent)
    addcoursebutton = Button(admin_desk, image = root.addstudent_but,bg = "#66a7ff",command=addStudent)
    addcoursebutton.place(x=63,y=210)

    buteditcourse =Image.open('ButEditCourse.png')
    root.editcourse_but = ImageTk.PhotoImage(buteditcourse)
    editcoursebutton = Button(admin_desk, image = root.editcourse_but,bg = "#66a7ff",command=editcourse)
    editcoursebutton.place(x=309,y=120)
    
    buteditstudent =Image.open('ButEditstd.png')
    root.editstudent_but = ImageTk.PhotoImage(buteditstudent)
    editstudentbutton = Button(admin_desk, image = root.editstudent_but,bg = "#66a7ff",command=edituser)
    editstudentbutton.place(x=309,y=210)

    butdeletecourse =Image.open('DeleteC.png')
    root.deletecourse_but = ImageTk.PhotoImage(butdeletecourse)
    deletecoursebutton = Button(admin_desk, image = root.deletecourse_but,bg = "#66a7ff",command=deleteSubject)
    deletecoursebutton.place(x=560,y=120)

    butdeletestudent =Image.open('DeleteStd.png')
    root.deletestudent_but = ImageTk.PhotoImage(butdeletestudent)
    deletestudentbutton = Button(admin_desk, image = root.deletestudent_but,bg = "#66a7ff",command=deleteStudent)
    deletestudentbutton.place(x=560,y=210)

    butdeleteadmin =Image.open('DeleteAd.png')
    root.deleteadmin_but = ImageTk.PhotoImage(butdeleteadmin)
    deleteadminbutton = Button(admin_desk, image = root.deleteadmin_but,bg = "#66a7ff",command=deleteAdmin)
    deleteadminbutton.place(x=560,y=330)

    butallcourse =Image.open('Showcourse.png')
    root.allcourse_but = ImageTk.PhotoImage(butallcourse)
    allcoursebutton = Button(admin_desk, image = root.allcourse_but,bg = "#66a7ff",command=allCourses)
    allcoursebutton.place(x=793,y=120)

    butallstudent =Image.open('ShowStd.png')
    root.allstudent_but = ImageTk.PhotoImage(butallstudent)
    allstudentbutton = Button(admin_desk, image = root.allstudent_but,bg = "#66a7ff",command=allStd)
    allstudentbutton.place(x=793,y=210)

    buttosetadmin = Image.open('Setadmin.png')
    root.setadmin_butto = ImageTk.PhotoImage(buttosetadmin)
    setadminbutto = Button(admin_desk,image=root.setadmin_butto,bg='#5398f6',command=setAd)
    setadminbutto.place(x=309,y=330)

    butAbout = Image.open('About.png')
    root.about_button = ImageTk.PhotoImage(butAbout)
    aboutbutton  =Button(admin_desk,image=root.about_button,bg="#66A7FF",command=developper)
    aboutbutton.place(x=910,y=420)

# Menu user    
def userMenu():

    
    usermenu_desk = Toplevel(root)
    usermenu_desk.title("Menu For User")
    usermenu_desk.geometry("1000x500+50+50")  #กำหนดขนาดจอ

    usermenubg = Image.open('Bgmenuuser.png')
    root.usermenu_menu = ImageTk.PhotoImage(usermenubg)
    usermenu = Label(usermenu_desk,image=root.usermenu_menu)
    usermenu.pack()
            
    def get_user_data(username_to_login):
        with open('02_user.json') as file:
            user_data = json.load(file)
            return user_data.get(username_to_login, {})

    def get_course_data():
        with open('02_course.json') as file:
            course_data = json.load(file)
            return course_data

    def show_data():
        username_to_login = username_loginEntry.get()
        user_data = get_user_data(username_to_login)
        
        course_codes = user_data.get("subject", [])
        if course_codes:
            course_data = get_course_data()
            show_data_desk = Toplevel()
            show_data_desk.title("show data")
            show_data_desk.geometry("1000x500+50+50")

            label00 = Label(show_data_desk, text="ใบเสร็จชำระเงิน", font=("Arial", 40))
            label00.pack(pady=10)
            y_control = 170
            total_price = 0
            for code in course_codes:
                course_info = course_data.get(code)
                if code in course_data:
                    info2 = course_data[code]
                    label0 = Label(show_data_desk, text=f"รหัสวิชา : {code} \tชื่อคอร์ส: {info2['course']}  \tจำนวนชั่วโมง : {info2['time(hr)']} ชั่วโมง \tราคา: {info2['price']} บาท", font=("Arial", 12))
                    label0.place(x=50, y=y_control)
                    y_control += 25
                    total_price += int(course_info['price'])

                    with open('02_user.json') as file:
                        user_data = json.load(file)    

                    user_info = user_data[username_to_login]
                    label01 = Label(show_data_desk, text=f"ชื่อผู้ใช้ : {username_to_login} \tชื่อ : {user_info['fname']} {user_info['lname']}\n", font=("Arial", 12))
                    label01.place(x=20, y=130)
            label02 = Label(show_data_desk, text=f"ราคารวม : \t{total_price} \tบาท", font=("Arial", 12))
            label02.place(x=727, y=450)

            # แสดงวันที่
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            date_label = Label(show_data_desk, text=f"วันที่: {current_date}", font=("Arial", 12))
            date_label.place(x=20, y=100)  # ปรับตำแหน่งตามที่ต้องการ

            # อ่านไฟล์รูปภาพ QR และย่อขนาดลง
            qr_image = Image.open("QrPython.png")
            qr_photo = ImageTk.PhotoImage(qr_image)
            qr_label = Label(show_data_desk, image=qr_photo)
            qr_label.image = qr_photo  # อย่าลืมรักษาอ้างอิงภาพ
            qr_label.place(x=690, y=100)  # ปรับตำแหน่งตามที่ต้องการ
        else: 
            messagebox.showerror(0,"คุณไม่มีรายการลงทะเบียน")
        
        
    def enroll():
        enroll_desk = Toplevel(root)
        enroll_desk.title("Select course")
        enroll_desk.geometry("1000x500+50+50")  # กำหนดขนาดจอ

        selectbg = Image.open('Bgselect.png')
        root.select_bg = ImageTk.PhotoImage(selectbg)
        selectBg = Label(enroll_desk, image=root.select_bg)
        selectBg.pack()

        def course_data():
            with open('02_course.json') as file:
                data = json.load(file)
            return data
        
        def showresult():
            def course_data():
                with open('02_course.json') as file:
                    data = json.load(file)
                return data

            def display_data(enroll_desk, data_dict):
                with open('02_course.json') as file:
                    data = json.load(file)
                y_coordinate = 130
                for course_code, course_info in data_dict.items():
                    info = f"Course Code : {course_code} \t "
                    info += ('ชื่อคอร์ส : {} \t\tเวลา : {} ชั่วโมง \t\tราคา : {} บาท'.format(course_info['course'], course_info['time(hr)'], course_info['price']))
                    # for key, value in course_info.items():
                    #     info += f"{key}: {value}\t"
                    label = tk.Label(enroll_desk, text=info)
                    label.place(x=110, y=y_coordinate)
                    y_coordinate += 30

            # Load data from JSON file
            data = course_data()

            # Call the display function automatically
            display_data(enroll_desk, data)

            result_label = tk.Label(enroll_desk, text="")
            result_label.pack()

        def penroll():
            data = course_data()   # ตรวจสอบว่ามีการนิยามฟังก์ชัน course_data และคืนค่าอย่างไร
            try:
                subject = subject_entryadd.get()  # Make sure subject_entryadd.get() is properly defined
                if subject in data:
                    with open("02_user.json") as file:
                        user_data = json.load(file)
                    if subject in user_data[getUserName()]["subject"]:  # Make sure getUserName() is properly defined
                        usermenu_desk.grab_set()
                        result = messagebox.askquestion("คุณลงทะเบียนคอร์สนี้ไปแล้ว", "คุณต้องการลงทะเบียนต่อหรือไม่?")
                        
                        if result == 'yes':
                            enroll()
                        else:
                            userMenu()
                    else:
                        user_data[getUserName()]["subject"].append(subject)  # Make sure getUserName() is properly defined
                        with open(userPath, "w") as file:
                            json.dump(user_data, file, indent=4)
                        result = messagebox.askquestion("ลงทะเบียนสำเร็จแล้ว", "คุณต้องการลงทะเบียนเพิ่มหรือไม่?")
                        if result == 'yes':
                            enroll_desk.destroy()
                        else:
                            result = messagebox.askquestion("ออกจากระบบลงทะเบียน", "คุณต้องการดูใบเสร็จของคุณหรือไม่?")
                            if result == 'yes':
                                show_data()
                            else:
                                userMenu()
                else:
                    result = messagebox.askquestion("ไม่มีรหัสวิชานี้ในระบบ", "คุณต้องการลงทะเบียนต่อหรือไม่?")
                    if result == 'yes':
                        enroll_desk.destroy()
                    else:
                        userMenu()
            except Exception as e:
                print(e)
        

        subject_entryadd = tk.Entry(enroll_desk, font=20, borderwidth=0)
        subject_entryadd.place(x=335, y=350)

        showre_button = tk.Button(enroll_desk,text="แสดงข้อมูล", bg="#5398f6",command=showresult)
        showre_button.place(x=470, y=307)  # ปรับตำแหน่งของปุ่มตามที่คุณต้องการ

        addbut = Image.open('ButtonAdd.png')
        enroll_desk.add_but = ImageTk.PhotoImage(addbut)
        addbutton = tk.Button(enroll_desk, image=enroll_desk.add_but, bg="#5398f6", command=penroll)
        addbutton.place(x=460, y=400)

        butback = Image.open('Back.png')
        enroll_desk.back_but = ImageTk.PhotoImage(butback)
        backbutton = tk.Button(enroll_desk, image=enroll_desk.back_but, bg='#5398f6',command=enroll_desk.destroy)
        backbutton.place(x=10, y=420)

        homebut = Image.open('Home.png')
        enroll_desk.home_but = ImageTk.PhotoImage(homebut)
        homebutton = tk.Button(enroll_desk, image=enroll_desk.home_but, bg='#5398f6', command=enroll_desk.destroy)
        homebutton.place(x=826, y=22)

    def withdraw():
        withdraw_desk = Toplevel(root)
        withdraw_desk.title("Cancel course")
        withdraw_desk.geometry("1000x500+50+50")  #กำหนดขนาดจอ

        selectbg = Image.open('Bgselect.png')
        root.select_bg = ImageTk.PhotoImage(selectbg)
        selectBg = Label(withdraw_desk,image=root.select_bg)
        selectBg.pack()

        def p_course_data():
            with open('02_user.json') as file:
                data = json.load(file)
            return data
        
        def userresult():

            def p_course_data():
                with open('02_user.json') as file:
                    data = json.load(file)
                return data
            
            def display_data(withdraw_desk, data_dict, username_to_display):
                y_coordinate = 120
                if username_to_display in data_dict:  # Check if the username exists in the data_dict
                    person_info = data_dict[username_to_display]
                    info = f"USER : {username_to_display} \t "
                    info = ('ชื่อ : {:<15} {:^20} \t\tชื่อเล่น : {}  \t\tหมายเลขโทรศัพท์ : {} \tรหัสวิชา : {}'.format(person_info['fname'], person_info['lname'], person_info['nickname'], person_info['phoneNumber'], person_info['subject']))
                    label = tk.Label(withdraw_desk, text=info)
                    label.place(x=110, y=y_coordinate)
                else:
                    not_found_label = tk.Label(withdraw_desk, text="ไม่พบข้อมูลสำหรับผู้ใช้นี้")
                    not_found_label.place(x=110, y=y_coordinate)

            # Assuming the username is obtained from the login process
            username_to_login =  username_loginEntry.get()

            # Load data from JSON file
            data = p_course_data()

            # Call the display function with the username_to_login
            display_data(withdraw_desk, data, username_to_login)

            result_label = tk.Label(withdraw_desk, text="")
            result_label.pack()

        def pwithdraw():
            data = p_course_data()
            try:
                with open(userPath, "r") as file:
                    data = json.load(file)

                subject = subject_entrycancel.get()

                if subject in data[getUserName()]["subject"]:
                    data[getUserName()]["subject"].remove(subject)
                    with open(userPath, "w") as file:
                        json.dump(data, file, indent=4)
                    result = messagebox.askquestion(f"ยกเลิกคอร์ส {subject} สำเร็จแล้ว", "คุณต้องการยกเลิกการลงทะเบียนต่อหรือไม่")
                    if result == 'yes':
                        withdraw_desk.destroy()
                    else:
                        result = messagebox.askquestion("ออกจากระบบลงทะเบียน", "คุณต้องการดูใบเสร็จของคุณหรือไม่?")
                        if result == 'yes':
                            show_data()
                        else:
                            userMenu()
                else:
                    result = messagebox.askquestion("คุณไม่ได้ลงทะเบียนคอร์สนี้","คุณต้องการยกเลิกการลงทะเบียนต่อหรือไม่")
                    if result == 'yes':
                        withdraw()
                    else:
                        userMenu()
            except Exception as e:
                print(e)
                

        showre_button = tk.Button(withdraw_desk,text="แสดงข้อมูล", bg="#5398f6",command=userresult)
        showre_button.place(x=470, y=307)  # ปรับตำแหน่งของปุ่มตามที่คุณต้องการ

        subject_entrycancel = Entry(withdraw_desk,font=20,borderwidth=0)
        subject_entrycancel.place(x=335,y=350)

        delbut = Image.open('ButtonDelete.png')
        root.del_but = ImageTk.PhotoImage(delbut)
        delbutton = Button(withdraw_desk,image=root.del_but,bg="#6617ff",command=pwithdraw)
        delbutton.place(x=460,y=400)

        butback = Image.open('Back.png')
        root.back_but = ImageTk.PhotoImage(butback)
        backbutton = Button(withdraw_desk, image=root.back_but, bg='#5398f6',command=withdraw_desk.destroy)
        backbutton.place(x=10, y=420)

        homebut = Image.open('Home.png')
        root.home_but = ImageTk.PhotoImage(homebut)
        homebutton = Button(withdraw_desk, image=root.home_but, bg='#5398f6', command=withdraw_desk.destroy)
        homebutton.place(x=826, y=22)

    showre_button = tk.Button(usermenu_desk,text="แสดงข้อมูล", bg="#5398f6", font=("Arial", 20),command=show_data)
    showre_button.place(x=430, y=250)

    butAbout = Image.open('About.png')
    root.about_button = ImageTk.PhotoImage(butAbout)
    aboutbutton  =Button(usermenu_desk,image=root.about_button,bg="#66A7FF")
    aboutbutton.place(x=910,y=420)

    butout  =Image.open('Logout.png')
    root.out_but = ImageTk.PhotoImage(butout)
    outbutton = Button(usermenu_desk, image = root.out_but,bg = "#5398f6",command=usermenu_desk.destroy)
    outbutton.place(x=830,y=16)

    slectco = Image.open('ButtonSelect.png')
    root.slectco_but = ImageTk.PhotoImage(slectco)
    slectcobutton = Button(usermenu_desk, image=root.slectco_but, bg="#5398f6", command=enroll)
    slectcobutton.place(x=140, y=190)

    cancelco  =Image.open('ButtonCancel.png')
    root.cancelco_but = ImageTk.PhotoImage(cancelco)
    cancelcobutton = Button(usermenu_desk, image = root.cancelco_but,bg = "#5398f6",command=withdraw)
    cancelcobutton.place(x=600,y=190)

    buttoback = Image.open('Back.png')
    root.back_butto = ImageTk.PhotoImage(buttoback)
    backbutto = Button(usermenu_desk,image=root.back_butto,bg='#5398f6',command=usermenu_desk.destroy)
    backbutto.place(x=10,y=420)

    butAbouto = Image.open('About.png')
    root.abouto_button = ImageTk.PhotoImage(butAbouto)
    aboutobutton  =Button(usermenu_desk,image=root.abouto_button,bg="#66A7FF",command=developper)
    aboutobutton.place(x=910,y=420)
#ล็อคอิน
def login(userName, password):
    try:
        with open(userPath, "r") as file:
            data = json.load(file)
        if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == True:
            
            common(True,setAdmin)
            common(True,setLogin)
            common(userName, setUserName)
            admin()
        if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == False:
            messagebox.showinfo(0,"ยินดีต้อนรับคุณ", data[userName]["fname"], data[userName]["lname"])
            common(True,setLogin)
            common(userName, setUserName)
            userMenu()
        elif userName not in data:
            messagebox.showerror(0,"ไม่มีชื่อผู้ใช้ในระบบ กรุณาลองใหม่อีกครั้ง")
        elif data[userName]["password"] != password:
            messagebox.showerror(0,"รหัสผ่านผิด กรุณาลองใหม่อีกครั้ง")
        else:
            messagebox.showerror(0,"กรุณา Login อีกครั้ง")
    except Exception as e:
        print(e)

def developper():
    dv = Toplevel(root)
    dv.title("Developer")
    dv.geometry("1000x500+50+50")  #กำหนดขนาดจอ

    bgdv = Image.open('Bgabout.png')
    root.dvbg = ImageTk.PhotoImage(bgdv)
    BG = Label(dv, image = root.dvbg)
    BG.pack()

    butback = Image.open('Back.png')
    root.back_button = ImageTk.PhotoImage(butback)
    backbutton = Button(dv,image=root.back_button,bg="#66A7FF",command=dv.destroy)
    backbutton.place(x=14,y=420)

def loginmain():
        attemps = 0
        userName = username_loginEntry.get()
        password = password_loginEntry.get()
        login(userName, password)
        if attemps == 3:
            messagebox.showerror(0,"คุณใส่กรอกผิดเกินกว่าที่กำหนด โปรดลองใหม่อีกครั้งในภายหลัง")
            attemps = 0

def signin():
    def signupProcess():
        global signstd
        fname = fname_entry.get()
        lname = lname_entry.get()
        nickname = nickname_entry.get()
        email = mail_entry.get()
        phoneNumber = telNum_entry.get()
        userName = userName_entry.get()
        password = password_entry.get()

        with open(userPath, "r") as file:
            data = json.load(file)
        newData = {userName: {"fname": fname, "lname": lname, "nickname": nickname, "email": email, "phoneNumber": phoneNumber, "password": password, "isAdmin": False, "subject": []}}
        if userName in data:
            messagebox.showerror(0, "มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว")
            return 
        
        elif userName not in data:
            if not emailStrength(email):  # ตรวจสอบความถูกต้องของอีเมล
                if mail_entry == '':  # ตรวจสอบว่าอีเมลถูกป้อนหรือไม่
                    messagebox.showerror(0, "กรุณาป้อนอีเมล")
                    signin()
                else:
                    messagebox.showerror(0, "อีเมลไม่ถูกต้อง")
                    signin()
            elif not passwordStrength(password):  # ตรวจสอบความซับซ้อนของรหัสผ่าน
                if password_entry == '':
                    messagebox.showerror(0, "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร")
                    signin()
                else:
                    messagebox.showerror(0, "รหัสผ่านไม่ถูกต้อง")
                    signin()
            elif len(phoneNumber) != 10 or not phoneNumber.isdigit():  # ตรวจสอบความถูกต้องของหมายเลขโทรศัพท์
                messagebox.showerror(0, "โปรดป้อนหมายเลขโทรศัพท์ ให้ครบ 10 ตัว และป้อนเฉพาะตัวเลขเท่านั้น")
                signin()
            else:
                with open(userPath, "r") as file:
                    data = json.load(file)  
                newData = {userName:{"fname":fname,"lname":lname,"nickname":nickname,"email":email,"phoneNumber":phoneNumber,"password":password,"isAdmin":False,"subject":[]}}
                if userName in data:
                    messagebox.showerror(0,"มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว")
                    signin()
                data.update(newData) 
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                messagebox.showinfo(0,"สมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ")
            addstd_desk.destroy()
            
    addstd_desk = Toplevel(root)
    addstd_desk.title("New Student")
    addstd_desk.geometry("1000x500+50+50")

    addstddeskbg = Image.open('Bgadstd.png')  
    root.addstd_bg = ImageTk.PhotoImage(addstddeskbg)
    addstdbg = Label(addstd_desk, image=root.addstd_bg )
    addstdbg.pack()

    fname_entry = Entry(addstd_desk, font=20,borderwidth=0)
    fname_entry.place(x=120, y=113)

    lname_entry = Entry(addstd_desk, font=20,borderwidth=0)
    lname_entry.place(x=560, y=113)

    nickname_entry = Entry(addstd_desk, font=20,borderwidth=0)
    nickname_entry.place(x=120, y=180)

    telNum_entry = Entry(addstd_desk, font=20,borderwidth=0)
    telNum_entry.place(x=560, y=180)

    mail_entry = Entry(addstd_desk, font=20,borderwidth=0)
    mail_entry.place(x=330, y=250)

    userName_entry = Entry(addstd_desk, font=20,borderwidth=0)
    userName_entry.place(x=330, y=303)

    password_entry = Entry(addstd_desk, font=20,borderwidth=0)
    password_entry.place(x=330, y=356)

    homebut = Image.open('Home.png')  
    root.home_but = ImageTk.PhotoImage(homebut)
    homebutton = Button(addstd_desk, image=root.home_but,bg='#5398f6',command=addstd_desk.destroy)
    homebutton.place(x=826,y=22)

    addbut = Image.open('ButtonAdd.png')  
    root.add_but = ImageTk.PhotoImage(addbut)
    addbutton = Button(addstd_desk, image=root.add_but,bg='#66a7ff',command=signupProcess)
    addbutton.place(x=467,y=400)


    backbut = Image.open('Backlow.png')  
    root.back_but = ImageTk.PhotoImage(backbut)
    backbutton = Button(addstd_desk, image=root.back_but,bg='#66a7ff',command=addstd_desk.destroy)
    backbutton.place(x=12,y=435)

def loginmain():
        attemps = 0
        userName = username_loginEntry.get()
        password = password_loginEntry.get()
        login(userName, password)
        if attemps == 3:
            messagebox.showerror(0,"คุณใส่กรอกผิดเกินกว่าที่กำหนด โปรดลองใหม่อีกครั้งในภายหลัง")
            attemps = 0

def login(userName, password):
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == True:
                common(True,setAdmin)
                common(True,setLogin)
                common(userName, setUserName)
                admin()
            if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == False:
                common(True,setLogin)
                common(userName, setUserName)
                userMenu()
            elif userName not in data:
                messagebox.showerror("somthing wrong","ไม่มีชื่อผู้ใช้ในระบบ กรุณาลองใหม่อีกครั้ง")
            elif data[userName]["password"] != password:
                messagebox.showerror("somthing wrong","รหัสผ่านผิด กรุณาลองใหม่อีกครั้ง")
        except Exception as e:
            print(e)
# ฟังก์ชันสำหรับการลงทะเบียน
def register(fname, lname, nickname, email, phoneNumber, userName, password):
    if not common(email, emailStrength):
        messagebox.showerror("อีเมลไม่ถูกต้อง")
    elif not common(password, passwordStrength):
        messagebox.showerror("รหัสผ่านไม่ถูกต้อง")
    elif len(phoneNumber) != 10 or not phoneNumber.isdigit():
        messagebox.showerror("เบอร์โทรศัพท์ไม่ถูกต้อง", "กรุณากรอกตัวเลขให้ครบ 10 ตัว")
    try:
        with open(userPath, "r") as file:
            data = json.load(file)
        newData = {userName: {"fname": fname, "lname": lname, "nickname": nickname, "email": email, "phoneNumber": phoneNumber, "password": password, "isAdmin": False, "subject": []}}
        if userName in data:
            messagebox.showerror("มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว")
        data.update(newData)
        with open(userPath, "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("สมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ")
    except Exception as e:
        messagebox.showerror("เกิดข้อผิดพลาด", str(e))

username_loginEntry = Entry(root,font=20,borderwidth=0)
username_loginEntry.place(x=310,y=170)

password_loginEntry = Entry(root,font=20,borderwidth=0)
password_loginEntry.place(x=310,y=270)

butsignup = Image.open('Signup.png')
signup_but = ImageTk.PhotoImage(butsignup)
signupbutton = Button(root,image=signup_but,bg="#5398F6",command=signin)
signupbutton.place(x=787,y=16)

butlogin = Image.open('Logbut.png')
login_button = ImageTk.PhotoImage(butlogin)
loginbutton = Button(root,image=login_button,bg="#66A7FF",command=loginmain)
loginbutton.place(x=410,y=350)

butAbout = Image.open('About.png')
about_button = ImageTk.PhotoImage(butAbout)
aboutbutton  =Button(root,image=about_button,bg="#66A7FF",command=developper)
aboutbutton.place(x=910,y=420)

root.mainloop()