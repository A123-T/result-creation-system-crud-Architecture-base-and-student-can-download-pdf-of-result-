# It is an GUI Design base Result Creation by teachers and Download by Stuidents and with facility of (pdf)convert
import sqlite3
from tkinter import *
import tkinter.messagebox as msg
from tkinter import StringVar

from reportlab.pdfgen import canvas
from reportlab.lib import colors
root = Tk()
root.title("Result Creation System Based on CRUD Architecture")
root.geometry("600x400")
root.resizable(0, 0)


def home():
    p1 = StringVar()
    f1 = Frame(bg="grey")
    f1.place(x=0, y=0, width=600, height=440)

    h = Label(f1, text="Home for Students", font="Helvetica 33 bold", bg="grey", fg="white")
    h.place(x=65, y=25)

    b1 = Button(f1, text=" Login ", bg="#091e42", fg="white", border=8, font="Helvetica 11 bold", command=login)
    b1.place(x=140, y=120, width=120, height=44)

    b2 = Button(f1, text=" Registration ", bg="#091e42", fg="white", font="Helvetica 11 bold", border=8, command=reg)
    b2.place(x=280, y=120, width=130, height=45)

    def admin():
        l2 = Label(f1, text="Enter your Password: ", font="Halveteica 12 bold", bg="grey", fg="white")
        l2.place(x=140, y=370)
        e1 = Entry(f1, font=(" ", 20), show="*", textvariable=p1)
        e1.place(x=320, y=367, width=150, height=28)

        def ins():
            if p1.get() == "tyagi" or p1.get() == "a":
                insertdata()
            else:
                msg.showinfo('title', "Invalid password")
                lp = Label(text="", bg="grey")
                lp.place(x=140, y=360, width=459, height=40)

        b2 = Button(f1, text=" Submit ", bg="dark green", fg="white", font="Helvetica 9 bold", border=8, command=ins)
        b2.place(x=481, y=360, width=120, height=40)

    h = Button(f1, text="Welcome Teachers", font="Helvetica 33 bold", bg="grey", fg="white", command=admin)
    h.place(x=140, y=270)

    def exit1():
        exit()

    b2 = Button(f1, text=" Log out ", bg="#091e42", fg="white", font="Helvetica 11 bold", border=8, command=exit1)
    b2.place(x=464, y=5, width=130, height=45)

#this is user interface which will provide a pdf and result
def serchuser():    
    f1 = Frame(bg="blue")
    f1.place(x=0, y=0, width=600, height=400)
    se1 = StringVar()
    s3 = Button(f1, text="Log out", bg="grey", font=("", 11), command=home, border=15)
    s3.place(x=495, y=15, width=100, height=50)


    i1 = Label(f1, text="Enter your Roll no : ", font="Halveteica 12 bold", bg="blue", fg="white")
    i1.place(x=120, y=80)
    ei2 = Entry(f1, font=(" ", 15), textvariable=se1)
    ei2.place(x=320, y=80, width=180, height=28)
    print(se1.get())
    def search1():
        global total
        db = sqlite3.connect('dbins1.db')
        cr = db.cursor()
        r = cr.execute("select * from insert3 where Rollno ='" + se1.get() + "' ")
        global r1

        for r1 in r:
            u1 = Label(f1, text="Name", font=("", 11), bg="#091e42", fg="white")
            u1.place(x=0, y=170, width=150, height=30)
            u2 = Label(f1, text=r1[0], font=("", 11), bg="#091e42", fg="white")
            u2.place(x=0, y=200, width=150, height=30)

            u1 = Label(f1, text="Roll no", font=("", 11), bg="purple", fg="white")
            u1.place(x=150, y=170, width=150, height=30)
            u2 = Label(f1, text=r1[1], font=("", 11), bg="purple", fg="white")
            u2.place(x=150, y=200, width=150, height=30)

            u1 = Label(f1, text="Sub 1", font=("", 11), bg="pink", fg="white")
            u1.place(x=300, y=170, width=75, height=30)
            u1 = Label(f1, text=r1[2], font=("", 11), bg="pink", fg="white")
            u1.place(x=300, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 2", font=("", 11), bg="orange", fg="white")
            u1.place(x=376, y=170, width=75, height=30)
            u2 = Label(f1, text=r1[3], font=("", 11), bg="orange", fg="white")
            u2.place(x=376, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 3", font=("", 11), bg="purple", fg="white")
            u1.place(x=451, y=170, width=75, height=30)
            u1 = Label(f1, text=r1[4], font=("", 11), bg="purple", fg="white")
            u1.place(x=451, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 4", font=("", 11), bg="skyblue", fg="white")
            u1.place(x=525, y=170, width=75, height=30)
            u2 = Label(f1, text=r1[5], font=("", 11), bg="skyblue", fg="white")
            u2.place(x=525, y=200, width=75, height=30)

            total = int(r1[2]) + int(r1[3]) + int(r1[4]) + int(r1[5])
            total = int(total)

            if total < 121:
                global t
                t = "FAILED"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="skyblue", fg="white")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 120 and total < 239:
                t = "Average try to Hard work"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="purple")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 239 and total < 300:
                t = "Above Average"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="red")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 299 and total < 341:
                t = "Good score"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="orange")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 340 and total < 401:
                t = "Excellent score"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="black")
                u2.place(x=15, y=270, width=405, height=60)
            break
        else:
            msg.showinfo('Title', 'Invalid Roll No')
            se1.set("")
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=0, y=170, width=150, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=0, y=200, width=150, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=150, y=170, width=150, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=150, y=200, width=150, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=300, y=170, width=75, height=30)
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=300, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=376, y=170, width=75, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=376, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=451, y=170, width=75, height=30)
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=451, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=525, y=170, width=75, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=525, y=200, width=75, height=30)
            u2 = Label(f1, text="", bg="blue")
            u2.place(x=15, y=270, width=405, height=60)
        db.commit()
        db.close()
    def print1():
        db = sqlite3.connect('dbins1.db')
        cr = db.cursor()
        if se1.get() != "":
            r = cr.execute("select * from insert3 where Rollno ='" + se1.get() + "' ")
            from reportlab.platypus import SimpleDocTemplate, Table,Paragraph,TableStyle
            from reportlab.lib.pagesizes import A4
            from reportlab.lib import colors
            from reportlab.lib.styles import getSampleStyleSheet
            DATA = [['          ', '                             ', '        '],
                    ['          ', '                             ', '        '],
                         ["NAME", "REGESTRATION NO", "Sub 1", "Sub 2", 'Sub 3', 'Sub 4'],
                    ]
            DATA1 = [
                      ['        ','           '],
                ]
            # data which we are going to Insert Pdf function  as tables
            l1 = r1[0]
            l2 = r1[2]
            l3 = r1[3]
            l4 = r1[4]
            l5 = r1[5]
            D =[l1,(str(se1.get())),l2,l3,l4,l5]

            DATA.append(D)
            a = [ '          ' ,'                             ','        ']
            DATA.append(a)
            a = ['          ', '                             ', '        ']
            DATA.append(a)
            a = ['          ', '                             ', '        ']
            DATA.append(a)
            DATA1.append(a)
            a = ['          ', '                             ', '        ']
            DATA1.append(a)
            a = ['          ', '                             ', '        ']
            DATA1.append(a)

            # creating a Base Document Template of page size A4
            pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

            # standard stylesheet defined within reportlab itself
            styles = getSampleStyleSheet()

            # fetching the style of Top level heading (Heading1)
            title_style = styles["Heading1"]

            title_style1 = styles["Heading1"]
            title_style2 = styles["Heading1"]
            title_style3 = styles["Heading1"]
            # 0: left, 1: center, 2: right
            title_style.alignment = 1

            title_style1.alignment = 1

            title_style2.alignment = 1

            title_style3.alignment = 1
            # creating the paragraph with
            # the heading text and passing the styles of it
            title = Paragraph('NIT NAGALAND RESULT 2021-23', title_style)
            style = TableStyle(
                [
                    ( "BOX", (0,5),(5,0),1,colors.black),
                    ("BACKGROUND", (0, 5), (5, 0), colors.beige),
                    ("ALIGN",(0,0),(-1,-1),"CENTER"),
                ]
            )
            tp1 = (total / 400) * 100
            tp2 = str(tp1)
            tp2 = "Total Percentage : " + tp2 + " % \n\n"
            t1 = str(t)
            title1 = Paragraph(tp2, title_style1)
            title3 = Paragraph(t, title_style3)
            title2 = Paragraph("| | |---------------THANK YOU----------------| | |", title_style2)
            # creates a table object and passes the style to it
            table = Table(DATA, style = style )
            table1 = Table(DATA1)
            # final step which builds the
            # actual pdf putting together all the elements
            pdf.build([title, table,title1,  title3,table1,title2])
            exit()
        else:
            msg.showinfo('Title', 'Invalid Roll No')

    s3 = Button(f1, text="Print Result", bg="grey", font=("", 11), command=print1, border=15)
    s3.place(x=25, y=15, width=200, height=50)
    b3 = Button(f1, text="Search Result", bg="grey", fg="white", font=("", 10), command=search1)
    b3.place(x=375, y=125, width=100, height=30)

#Here total login  verification if you previously regester then only youn open
def login():
    l = Frame(bg="#091e30")
    l.place(x=0, y=0, width=600, height=400)
    g1 = StringVar()
    g2 = StringVar()
    lb = Label(text="Login", font="Halveteica 35 bold", bg="#091e30", fg="white")
    lb.place(x=200, y=25)

    l1 = Label(l, text="Enter your Full name : ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l1.place(x=140, y=120)
    e1 = Entry(l, font=(" ", 12), textvariable=g1)
    e1.place(x=320, y=120, width=180, height=28)

    l2 = Label(l, text="Enter your Password : ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l2.place(x=140, y=170)
    e1 = Entry(l, font=(" ", 20), show="*", textvariable=g2)
    e1.place(x=320, y=170, width=160, height=28)
  #verification function
    def login1():
        if g1.get() == "" and g2.get() == "":
            msg.showinfo('Title', 'Invalid Username or Password')
        else:
            db = sqlite3.connect("db1.db")
            cr = db.cursor()
            r = cr.execute("select * from reg where UNAME='" + g1.get() + "'AND UPASS='" + g2.get() + "'")
            for r1 in r:
                msg.showinfo('Title', 'Welcome')
                serchuser()
                break
            else:
                msg.showinfo('Title', 'Invalid Username or Password')
            db.commit()
            db.close()
        g1.set("")
        g2.set("")

    s = Button(l, text="login", font="Halveteica 14 bold", bg="pink", border="8", command=login1)
    s.place(x=324, y=219, width=150, height=45)

    s = Button(l, text="Registeration", font="Halveteica 14 bold", bg="grey", border="8", command=reg)
    s.place(x=364, y=330, width=200, height=45)

    s = Button(l, text=" Home ", font="Halveteica 15 bold", bg="grey", border="8", command=home)
    s.place(x=80, y=330, width=160, height=45)

#It is only for techers to insert Data only it will calculate percentage and sve Data to Sqlite 3
def insertdata():
    f1 = Frame(bg="pink")
    f1.place(x=0, y=0, width=600, height=400)

    b2 = Button(f1, fg="black", text="Insert Data", bg="skyblue", command=insertdata)
    b2.place(x=0, y=0, width=100, height=20)

    b3 = Button(f1, fg="black", text="Show Result", command=showdata)
    b3.place(x=100, y=0, width=100, height=20)

    s = Button(f1, text=" Serch result ", bg="grey", command=serch)
    s.place(x=200, y=0, width=100, height=20)

    b2 = Button(f1, fg="black", text="Delete result", bg="skyblue", command=Delete)
    b2.place(x=300, y=0, width=100, height=20)

    b3 = Button(f1, fg="black", text="Update", command=Update)
    b3.place(x=400, y=0, width=100, height=20)

    s = Button(f1, text="Log out", bg="grey", command=home)
    s.place(x=500, y=0, width=100, height=20)
    ri1 = StringVar()
    ri2 = StringVar()
    ri3 = StringVar()
    ri4 = StringVar()
    ri5 = StringVar()
    ri6 = StringVar()
    i = Label(f1, text="Enter your Name : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i.place(x=120, y=40)
    ei1 = Entry(f1, font=(" ", 15), textvariable=ri1)
    ei1.place(x=320, y=40, width=180, height=28)

    i1 = Label(f1, text="Enter your Roll no : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i1.place(x=120, y=80)
    ei2 = Entry(f1, font=(" ", 15), textvariable=ri2)
    ei2.place(x=320, y=80, width=180, height=28)

    i2 = Label(f1, text="Enter your sub 1 marks : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i2.place(x=120, y=120)
    ei3 = Entry(f1, font=(" ", 15), textvariable=ri3)
    ei3.place(x=320, y=120, width=180, height=28)

    i3 = Label(f1, text="Enter your sub 2 marks : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i3.place(x=120, y=160)
    ei4 = Entry(f1, font=(" ", 15), textvariable=ri4)
    ei4.place(x=320, y=160, width=180, height=28)

    i4 = Label(f1, text="Enter your sub 3 marks : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i4.place(x=120, y=200)
    ei5 = Entry(f1, font=(" ", 15), textvariable=ri5)
    ei5.place(x=320, y=200, width=180, height=28)

    i5 = Label(f1, text="Enter your sub 4 marks : ", font="Halveteica 12 bold", bg="pink", fg="white")
    i5.place(x=120, y=240)
    ei6 = Entry(f1, font=(" ", 15), textvariable=ri6)
    ei6.place(x=320, y=240, width=180, height=28)

    def total():
        a1 = ri3.get()
        a2 = ri4.get()
        a3 = ri5.get()
        a4 = ri6.get()
        total = int(a1) + int(a2) + int(a3) + int(a4)
        tp1 = (total / 400) * 100
        tp2 = str(tp1)
        tp2 = tp2 + " % "
        if total > 400:
            bi2 = Label(text="You Enter out of limit", font="Halveteica 20 bold", bg="black", fg="white")
            bi2.place(x=0, y=0, width=600, height=40)
            bt = Button(text="BACK", bg="grey", font="Halevetica 18 bold", fg="red", command=insertdata, border=10)
            bt.place(x=0, y=300, width=600, height=105)
        else:
            bi2 = Label(text=total, font="Halveteica 20 bold", bg="black", fg="white")
            bi2.place(x=330, y=300)
            bi21 = Label(text=tp2, font="Halveteica 20 bold", bg="black", fg="white")
            bi21.place(x=100, y=350)

    bt = Button(text="Total marks : -> ", bg="pink", font="Halevetica 18 bold", fg="black", command=total)
    bt.place(x=100, y=300, width=200, height=45)

    def subins():
        db = sqlite3.connect("dbins1.db")
        cr = db.cursor()
        if ri1.get() != "" and ri2.get() != "" and ri3.get() and ri4.get() != "":
            cr.execute(
                "insert into insert3 values('" + ri1.get() + "','" + ri2.get() + "','" + ri3.get() + "','" + ri4.get() + "','" + ri5.get() + "','" + ri6.get() + "')")
            db.commit()
            db.close()
            t = msg.showinfo('Title', 'User Marks  Sucessfully Submit  See Result session!!!')
            ri1.set("")
            ri2.set("")
            ri3.set("")
            ri4.set("")
            ri5.set("")
            ri6.set("")
        else:
            msg.showinfo('Title', 'Please Enter Full Data')
            ri1.set("")
            ri2.set("")
            ri3.set("")
            ri4.set("")
            ri5.set("")
            ri6.set("")

    b = Button(f1, text="  Submit ", bg="grey", fg="white", font="Halevetica 20 bold", border=6, command=subins)
    b.place(x=380, y=327, width=200, height=40)

#Show data function to show all the data only registered teacher only not show students
def showdata():
    f1 = Frame(bg="yellow")
    f1.place(x=0, y=0, width=600, height=400)

    b2 = Button(f1, fg="black", text="Insert Data", bg="skyblue", command=insertdata)
    b2.place(x=0, y=0, width=100, height=20)

    b3 = Button(f1, fg="black", text="Show Result", command=showdata)
    b3.place(x=100, y=0, width=100, height=20)

    s = Button(f1, text=" Serch result ", bg="grey", command=serch)
    s.place(x=300, y=0, width=100, height=20)

    b2 = Button(f1, fg="black", text="Delete result", bg="skyblue", command=Delete)
    b2.place(x=200, y=0, width=100, height=20)

    b3 = Button(f1, fg="black", text="Update marks", command=Update)
    b3.place(x=400, y=0, width=100, height=20)

    s = Button(f1, text="Log out", bg="grey", command=home)
    s.place(x=500, y=0, width=100, height=20)

    u1 = Label(f1, text="Name", font=("", 11), bg="#091e42", fg="white")
    u1.place(x=0, y=20, width=170, height=30)

    u1 = Label(f1, text="Registration no", font=("", 11), bg="orange", fg="white")
    u1.place(x=170, y=20, width=120, height=30)

    u1 = Label(f1, text="sub 1", font=("", 11), bg="pink", fg="white")
    u1.place(x=280, y=20, width=100, height=30)

    u1 = Label(f1, text="sub 2", font=("", 11), bg="purple", fg="white")
    u1.place(x=380, y=20, width=80, height=30)

    u1 = Label(f1, text="sub 3", font=("", 9), bg="skyblue", fg="white")
    u1.place(x=460, y=20, width=100, height=30)

    u1 = Label(f1, text="sub 4", font=("", 9), bg="green", fg="white")
    u1.place(x=540, y=20, width=75, height=30)

    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=150, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="#091e42", fg="white")
    for r1 in r:
        listbox.insert(END, str(r1[0]))
    listbox.place(x=0, y=50, width=150, height=167)
    s.config(command=listbox.yview)
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=275, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="orange")
    for r1 in r:
        listbox.insert(END, str(r1[1]))
    listbox.place(x=170, y=50, width=100, height=167)
    s.config(command=listbox.yview)
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=360, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="pink")
    for r1 in r:
        listbox.insert(END, str(r1[2]))
    listbox.place(x=300, y=50, width=65, height=167)
    s.config(command=listbox.yview)
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=455, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="purple", fg="white")
    for r1 in r:
        listbox.insert(END, str(r1[3]))
    listbox.place(x=385, y=50, width=65, height=167)
    s.config(command=listbox.yview)
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=515, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="skyblue")
    for r1 in r:
        listbox.insert(END, str(r1[4]))
    listbox.place(x=475, y=50, width=40, height=167)
    s.config(command=listbox.yview)
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=585, y=50, height=167)
    listbox = Listbox(root, yscrollcommand=s.set, bg="green")
    for r1 in r:
        listbox.insert(END, str(r1[5]))
    listbox.place(x=540, y=50, width=40, height=167)
    s.config(command=listbox.yview)
    db.commit()
    db.close()
    db = sqlite3.connect('dbins1.db')
    cr = db.cursor()
    r = cr.execute("select * from insert3")
    s = Scrollbar(root)
    s.place(x=575, y=220, height=170)
    listbox = Listbox(root, yscrollcommand=s.set, bg="#00ffff", fg="#091e42", font=("", 15))
    for r1 in r:
        listbox.insert(END, str(r1[0]) + "        " + str(r1[1]) + "        " + str(r1[2]) + "        " + str(
            r1[3]) + "        " + str(r1[4]) + "        " + str(r1[5]))
    listbox.place(x=0, y=220, width=570, height=170)
    s.config(command=listbox.yview)

# it is Data delete function  which you insert
def Delete():
    f1 = Frame(bg="purple")
    f1.place(x=0, y=0, width=600, height=400)
    d1 = StringVar()
    b1 = Button(f1, fg="black", text="Insert Data", bg="skyblue", command=insertdata)
    b1.place(x=0, y=0, width=100, height=20)
    b2 = Button(f1, text=" Serch result ", bg="grey", command=serch)
    b2.place(x=300, y=0, width=100, height=20)
    b3 = Button(f1, fg="black", text="Show Result", command=showdata)
    b3.place(x=100, y=0, width=100, height=20)
    b4 = Button(f1, text=" Delete result ", bg="grey", command=Delete)
    b4.place(x=200, y=0, width=100, height=20)
    b5 = Button(f1, fg="black", text="Update", command=Update)
    b5.place(x=400, y=0, width=100, height=20)
    b6 = Button(f1, text="Log out", bg="grey", command=home)
    b6.place(x=500, y=0, width=100, height=20)
    i1 = Label(f1, text="Enter your Roll no : ", font="Halveteica 12 bold", bg="purple", fg="white")
    i1.place(x=120, y=40)
    ei2 = Entry(f1, font=(" ", 15), textvariable=d1)
    ei2.place(x=280, y=40, width=177, height=30)

    def delete2():
        db = sqlite3.connect("dbins1.db")
        cr = db.cursor()
        if d1.get() == "":
            msg.showinfo('Title', 'Invalid input')
        else:
            cr.execute("delete from insert3 where Rollno='" + d1.get() + "'")
            db.commit()
            db.close()
            msg.showinfo('Title', 'Data sucessfully Deleted')
            d1.set("")

    b1 = Button(f1, text="Delete", font=("", 11), bg="grey", fg="white", command=delete2)
    b1.place(x=460, y=40, width=100, height=30)


def Update():
    f1 = Frame(bg="orange")
    f1.place(x=0, y=0, width=600, height=400)
    se1 = StringVar()
    b1 = Button(f1, fg="black", text="Insert Data", bg="skyblue", command=insertdata)
    b1.place(x=0, y=0, width=100, height=20)
    b2 = Button(f1, text=" Serch result ", bg="grey", command=serch)
    b2.place(x=300, y=0, width=100, height=20)
    b3 = Button(f1, fg="black", text="Show Result", command=showdata)
    b3.place(x=100, y=0, width=100, height=20)
    b4 = Button(f1, text=" Delete result ", bg="grey", command=Delete)
    b4.place(x=200, y=0, width=100, height=20)
    b5 = Button(f1, fg="black", text="Update", command=Update)
    b5.place(x=400, y=0, width=100, height=20)
    b6 = Button(f1, text="Log out", bg="grey", command=home)
    b6.place(x=500, y=0, width=100, height=20)
    i1 = Label(f1, text="Enter your Roll no : ", font="Halveteica 12 bold", bg="orange", fg="white")
    i1.place(x=120, y=40)
    ei2 = Entry(f1, font=(" ", 15), textvariable=se1)
    ei2.place(x=280, y=40, width=150, height=28)

    def update1():
        db = sqlite3.connect('dbins1.db')
        cr = db.cursor()
        r = cr.execute("select * from insert3 where Rollno ='" + se1.get() + "' ")
        for r1 in r:
            su1 = StringVar()
            su2 = StringVar()
            su3 = StringVar()
            su4 = StringVar()
            su5 = StringVar()
            u1 = Label(f1, text="Name", font=("", 18), bg="#091e42", fg="white")
            u1.place(x=40, y=80, width=150, height=60)
            u2 = Entry(f1, font=("", 11), bg="white", fg="black", textvariable=su1)
            u2.insert(0, r1[0])
            u2.place(x=210, y=80, heigh=60)
            u3 = Label(f1, text="Sub 1", font=("", 11), bg="pink", fg="white")
            u3.place(x=40, y=170, width=150, height=30)
            u1 = Entry(f1, font=("", 11), bg="white", fg="black", textvariable=su2)
            u1.insert(0, r1[2])
            u1.place(x=210, y=170, width=150, height=30)
            u1 = Label(f1, text="Sub 2", font=("", 11), bg="skyblue", fg="white")
            u1.place(x=40, y=210, width=150, height=30)
            u4 = Entry(f1, font=("", 11), bg="white", fg="black", textvariable=su3)
            u4.insert(0, r1[3])
            u4.place(x=210, y=210, width=150, height=30)
            u1 = Label(f1, text="Sub 3", font=("", 11), bg="purple", fg="white")
            u1.place(x=40, y=250, width=150, height=30)
            u5 = Entry(f1, font=("", 11), bg="white", fg="black", textvariable=su4)
            u5.insert(0, r1[4])
            u5.place(x=210, y=250, width=150, height=30)
            u1 = Label(f1, text="Sub 4", font=("", 11), bg="pink", fg="black")
            u1.place(x=40, y=290, width=150, height=30)
            u6 = Entry(f1, font=("", 11), bg="white", fg="black", textvariable=su5)
            u6.insert(0, r1[5])
            u6.place(x=210, y=290, width=150, height=30)

            def update2():
                db = sqlite3.connect("dbins1.db")
                cr = db.cursor()
                cr.execute(
                    "update insert3 set UNAME='" + su1.get() + "',sub1='" + su2.get() + "',sub2='" + su3.get() + "',sub3='" + su4.get() + "',sub4='" + su5.get() + "'where Rollno= '" + se1.get() + "' ")
                db.commit()
                db.close()
                msg.showinfo('Title', 'Data sucessfully Updated')

            bu = Button(f1, text="Update", font=("", 15), border=5, command=update2)
            bu.place(x=160, y=350, width=140, height=40)
            break
        else:
            msg.showinfo('Title', 'Invalid Roll No')
            se1.set("")
            u1 = Label(f1, text="", font=("", 11), bg="orange")
            u1.place(x=40, y=80, width=480, height=400)

    b3 = Button(f1, text="Search Result", bg="grey", fg="white", font=("", 10), border=5, command=update1)
    b3.place(x=431, y=40, width=100, height=30)

#Serch functio Start for teachers
def serch():
    f1 = Frame(bg="blue")
    f1.place(x=0, y=0, width=600, height=400)
    se1 = StringVar()
    b2 = Button(f1, fg="black", text="Insert Data", bg="skyblue", command=insertdata)
    b2.place(x=0, y=0, width=100, height=20)
    b3 = Button(f1, fg="black", text="Show Result", command=showdata)
    b3.place(x=100, y=0, width=100, height=20)
    s1 = Button(f1, text=" Delete result ", bg="grey", command=Delete)
    s1.place(x=200, y=0, width=100, height=20)
    s2 = Button(f1, text=" Serch result ", bg="grey", command=serch)
    s2.place(x=300, y=0, width=100, height=20)
    b3 = Button(f1, fg="black", text="Update", command=Update)
    b3.place(x=400, y=0, width=100, height=20)
    s3 = Button(f1, text="Log out", bg="grey", command=home)
    s3.place(x=500, y=0, width=100, height=20)
    i1 = Label(f1, text="Enter your Roll no : ", font="Halveteica 12 bold", bg="blue", fg="white")
    i1.place(x=120, y=80)
    ei2 = Entry(f1, font=(" ", 15), textvariable=se1)
    ei2.place(x=320, y=80, width=180, height=28)

    def search1():
        db = sqlite3.connect('dbins1.db')
        cr = db.cursor()
        r = cr.execute("select * from insert3 where Rollno ='" + se1.get() + "' ")
        for r1 in r:
            u1 = Label(f1, text="Name", font=("", 11), bg="#091e42", fg="white")
            u1.place(x=0, y=170, width=150, height=30)
            u2 = Label(f1, text=r1[0], font=("", 11), bg="#091e42", fg="white")
            u2.place(x=0, y=200, width=150, height=30)

            u1 = Label(f1, text="Roll no", font=("", 11), bg="purple", fg="white")
            u1.place(x=150, y=170, width=150, height=30)
            u2 = Label(f1, text=r1[1], font=("", 11), bg="purple", fg="white")
            u2.place(x=150, y=200, width=150, height=30)

            u1 = Label(f1, text="Sub 1", font=("", 11), bg="pink", fg="white")
            u1.place(x=300, y=170, width=75, height=30)
            u1 = Label(f1, text=r1[2], font=("", 11), bg="pink", fg="white")
            u1.place(x=300, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 2", font=("", 11), bg="orange", fg="white")
            u1.place(x=376, y=170, width=75, height=30)
            u2 = Label(f1, text=r1[3], font=("", 11), bg="orange", fg="white")
            u2.place(x=376, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 3", font=("", 11), bg="purple", fg="white")
            u1.place(x=451, y=170, width=75, height=30)
            u1 = Label(f1, text=r1[4], font=("", 11), bg="purple", fg="white")
            u1.place(x=451, y=200, width=75, height=30)

            u1 = Label(f1, text="Sub 4", font=("", 11), bg="skyblue", fg="white")
            u1.place(x=525, y=170, width=75, height=30)
            u2 = Label(f1, text=r1[5], font=("", 11), bg="skyblue", fg="white")
            u2.place(x=525, y=200, width=75, height=30)

            total = int(r1[2]) + int(r1[3]) + int(r1[4]) + int(r1[5])
            total = int(total)
            if total < 121:
                t = "FAILED"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="skyblue", fg="white")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 120 and total < 239:
                t = "Average try to Hard work"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="purple")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 239 and total < 300:
                t = "Above Average"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="red")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 299 and total < 341:
                t = "Good score"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="orange")
                u2.place(x=15, y=270, width=405, height=60)
            elif total > 340 and total < 401:
                t = "Excellent score"
                u2 = Label(f1, text=t, font="Halevetica 18 bold", bg="#00ffff", fg="black")
                u2.place(x=15, y=270, width=405, height=60)
            break
        else:
            msg.showinfo('Title', 'Invalid Roll No')
            se1.set("")
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=0, y=170, width=150, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=0, y=200, width=150, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=150, y=170, width=150, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=150, y=200, width=150, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=300, y=170, width=75, height=30)
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=300, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=376, y=170, width=75, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=376, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=451, y=170, width=75, height=30)
            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=451, y=200, width=75, height=30)

            u1 = Label(f1, text="", font=("", 11), bg="blue")
            u1.place(x=525, y=170, width=75, height=30)
            u2 = Label(f1, text="", font=("", 11), bg="blue")
            u2.place(x=525, y=200, width=75, height=30)
            u2 = Label(f1, text="", bg="blue")
            u2.place(x=15, y=270, width=405, height=60)
        db.commit()
        db.close()

    b3 = Button(f1, text="Search Result", bg="grey", fg="white", font=("", 10), command=search1)
    b3.place(x=375, y=125, width=100, height=30)

#This is Regestration  function Start
def reg():
    l = Frame(bg="#091e30")
    l.place(x=0, y=0, width=600, height=400)
    r1 = StringVar()
    r2 = StringVar()
    r3 = StringVar()
    r4 = StringVar()

    lb = Label(text="Registration", font="Halveteica 35 bold", bg="#091e30", fg="white")
    lb.place(x=200, y=25)

    l1 = Label(l, text="Enter your Full name : ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l1.place(x=140, y=120)
    e1 = Entry(l, font=(" ", 15), textvariable=r1)
    e1.place(x=320, y=120, width=180, height=28)

    l2 = Label(l, text="Enter your Password : ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l2.place(x=140, y=155)
    e1 = Entry(l, font=(" ", 20), show="*", textvariable=r2)
    e1.place(x=320, y=155, width=180, height=28)

    l2 = Label(l, text="Enter your Contact Number: ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l2.place(x=80, y=193)
    e1 = Entry(l, font=(" ", 20), textvariable=r3)
    e1.place(x=320, y=193, width=180, height=28)

    l1 = Label(l, text="Enter your Branch : ", font="Halveteica 12 bold", bg="#091e30", fg="white")
    l1.place(x=140, y=230)
    e1 = Entry(l, font=(" ", 17), textvariable=r4)
    e1.place(x=320, y=230, width=180, height=28)

    def reg1():
        db = sqlite3.connect("db1.db")
        cr = db.cursor()
        if r1.get() != "" and r2.get() != "" and r3.get() and r4.get() != "":
            cr.execute(
                "insert into reg values('" + r1.get() + "','" + r2.get() + "','" + r3.get() + "','" + r4.get() + "')")
            db.commit()
            db.close()
            t = msg.showinfo('Title', 'User Registered Sucessfully!!!')
            r1.set("")
            r2.set("")
            r3.set("")
            r4.set("")
            if t == t:
                login()
        else:
            msg.showinfo('Title', 'Please Enter Full Data')
            r1.set("")
            r2.set("")
            r3.set("")
            r4.set("")

    s = Button(l, text="Submit", font="Halveteica 14 bold", bg="grey", border="8", command=reg1)
    s.place(x=284, y=285, width=220, height=45)
    s = Button(l, text=" Home ", font="Halveteica 15 bold", bg="grey", border="8", command=home)
    s.place(x=40, y=350, width=100, height=45)
#Here User delete function in side regestration form
    def delete():
        f1 = Frame(bg="orange")
        f1.place(x=0, y=0, width=600, height=400)
        d1 = StringVar()
        i1 = Label(f1, text="Enter your  User Name : ", font="Halveteica 12 bold", bg="orange", fg="white")
        i1.place(x=80, y=40)
        ei2 = Entry(f1, font=(" ", 15), textvariable=d1)
        ei2.place(x=280, y=40, width=177, height=30)

        def delete2():
            db = sqlite3.connect("db1.db")
            cr = db.cursor()
            if d1.get() == "":
                msg.showinfo('Title', 'Invalid input')
            else:
                cr.execute("delete from reg where UNAME='" + d1.get() + "'")
                db.commit()
                db.close()
                msg.showinfo('Title', 'Data sucessfully Deleted')
                d1.set("")

        b0 = Button(f1, text="Delete", font=("", 11), bg="grey", fg="white", command=delete2)
        b0.place(x=460, y=40, width=100, height=30)
        s = Button(f1, text=" Home ", font="Halveteica 15 bold", bg="grey", border="8", command=home)
        s.place(x=150, y=100, width=230, height=45)

        def pass1():
            e1 = Entry(f1, font=(" ", 20), show="*", textvariable=r2)
            e1.place(x=240, y=225, width=200, height=28)

            def scroll():
                if r2.get() == "":
                    msg.showinfo('Title', 'Invalid Username or Password')
                    r2.set("")
                    L = Label(text="", bg="orange")
                    L.place(x=0, y=180, width="200", height=170)
                else:
                    db = sqlite3.connect("db1.db")
                    cr = db.cursor()
                    r = cr.execute("select * from reg where UPASS='" + r2.get() + "'")
                    for r1 in r:
                        msg.showinfo('Title', 'Welcome')
                        db = sqlite3.connect('db1.db')
                        cr = db.cursor()
                        r = cr.execute("select * from reg")
                        s = Scrollbar(root)
                        s.place(x=170, y=180, height=167)
                        listbox = Listbox(root, yscrollcommand=s.set, bg="#00ffff", font=("", 14))
                        u1 = Label(f1, text="Name", font=("", 11), bg="#091e42", fg="white")
                        u1.place(x=0, y=150, width=195, height=30)
                        for r1 in r:
                            listbox.insert(END, str(r1[0]))
                        listbox.place(x=0, y=180, width=170, height=167)
                        s.config(command=listbox.yview)
                        db.commit()
                        db.close()
                        break
                    else:
                        msg.showinfo('Title', 'Invalid Username or Password')
                        r2.set("")
                        L = Label(text="", bg="orange")
                        L.place(x=0, y=180, width="200", height=170)

            l2 = Button(f1, text="Submit", font="Halveteica 12 bold", bg="grey", fg="white", command=scroll)
            l2.place(x=260, y=280)

        l2 = Button(f1, text="Press and Enter your Password If you want to See Users ", font="Halveteica 10 bold",
                    bg="#091e30", fg="white", command=pass1)
        l2.place(x=200, y=180)

    s = Button(l, text=" Delete user ", font="Halveteica 15 bold", bg="grey", border="8", command=delete)
    s.place(x=385, y=350, width=200, height=45)

#Here the program starting
home()
#here End
root.mainloop()