from tkinter import *
from tkinter import messagebox
import sqlite3

ws = Tk()
ws.title('Dang ky tai khoan - Python Desktop')
ws.config(bg='#0B5A81')
f = ('Times',14)
var = StringVar()
var.set('male')

con = sqlite3.connect('quanlynhanvien.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS employee(
                id text,
                name text,
                email text,
                contact number,
                gender text,
                country text,
                password text
                )'''
            )
con.commit()

countries = []
variable = StringVar() 
world = open('countries.txt','r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)

print(countries)
variable.set(countries[1])

right_frame = Frame( 
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text='Ho ten: ',
    bg='#CCCCCC',
    font=f
).grid(row=0,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Email: ',
    bg='#CCCCCC',
    font=f
).grid(row=1,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Dien thoai: ',
    bg='#CCCCCC',
    font=f
).grid(row=2,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Chon gioi tinh: ',
    bg='#CCCCCC',
    font=f
).grid(row=3,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Chon quoc gia: ',
    bg='#CCCCCC',
    font=f
).grid(row=4,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Password: ',
    bg='#CCCCCC',
    font=f
).grid(row=5,column=0,sticky=W,pady=10)

Label(
    right_frame,
    text='Re-enter Password: ',
    bg='#CCCCCC',
    font=f
).grid(row=6,column=0,sticky=W,pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx= 10,
    pady= 10
)

register_name = Entry(
    right_frame,
    font= f
)

register_email = Entry(
    right_frame,
    font= f
)

register_mobile = Entry(
    right_frame,
    font= f
)

male_rb = Radiobutton(
    gender_frame,
    text='Nam',
    bg='#CCCCCC',
    variable= var,
    value='male',
    font=('Times',10)
)

female_rb = Radiobutton(
    gender_frame,
    text='Nu',
    bg='#CCCCCC',
    variable= var,
    value='female',
    font=('Times',10)
)

others_rb = Radiobutton(
    gender_frame,
    text='Khac',
    bg='#CCCCCC',
    variable= var,
    value='others',
    font=('Times',10)
)

register_country = OptionMenu(
    right_frame,
    variable,
    *countries
)

register_country.config(
    width=15,
    font=('Times',12)
)

register_pwd = Entry(
    right_frame,
    font=f,
    show= '*'
)

pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

def saverecord():
    try:
        con = sqlite3.connect('quanlynhanvien.db')
        cur = con.cursor()
        cur.execute("INSERT INTO employee VALUES(:id,:name,:email,:contact,:gender,:country,:password)",{
            'id': "1231312",
            'name': register_name.get(),
            'email': register_email.get(),
            'contact':register_mobile.get(),
            'gender': var.get(),
            'country': variable.get(),
            'password': register_pwd.get()
        })
        con.commit()
        messagebox.showinfo('Thong bao!','Da them nhan vien thanh cong!')
    except Exception as ep:
        messagebox.showerror('',ep)

def validateform():
    check_counter = 0
    warn = ""

    if register_name.get() == "":
        warn = "Ban can nhap ho ten!"
        messagebox.showinfo('Thong bao loi', warn)
    else:
        check_counter += 1
    check_counter = 0

    if register_email.get() == "":
        warn = "Email cant be empty"
    else:
        check_counter += 1
    
    if register_mobile.get() == "":
        warn ="Contact cant be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select gender"
    else:
        check_counter += 1
    
    if variable.get() == "":
        warn = "Select country"
    else:
        check_counter += 1
    
    if register_pwd.get() == "":
        warn = "Password cant be empty"
    else:
        check_counter += 1
    
    if pwd_again.get() == "":
        warn = "Re-enter Password cant be empty"
    else:
        check_counter += 1

    print(warn)
    saverecord()

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=validateform
)

register_name.grid(row=0,column=1,pady=10,padx=20)
register_email.grid(row=1,column=1,pady=10,padx=20)
register_mobile.grid(row=2,column=1,pady=10,padx=20)
register_country.grid(row=4,column=1,pady=10,padx=20)
register_pwd.grid(row=5,column=1,pady=10,padx=20)
pwd_again.grid(row=6,column=1,pady=10,padx=20)
register_btn.grid(row=7,column=1,pady=10,padx=20)
right_frame.pack()
gender_frame.grid(row=3,column=1,pady=10,padx=20)
male_rb.pack(expand=True, side= LEFT)
female_rb.pack(expand=True, side= LEFT)
others_rb.pack(expand=True, side= LEFT)

ws.mainloop()


