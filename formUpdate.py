from tkinter import *
from tkinter import messagebox
import sqlite3

# Cấu hình
ws = Tk()
ws.title('Quản lý nhân viên - Python Desktop')
ws.config(bg='#0B5A81')
f = ('Times', 14)
var = StringVar()
var.set('male')

# Kết nối CSDL và tạo bảng
def create_table():
    con = sqlite3.connect('quanlynhanvien3.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            contact TEXT,
            gender TEXT,
            country TEXT,
            password TEXT
        )
    ''')
    con.commit()
    con.close()

create_table()

# Đọc file text và load dữ liệu ra ComboBox
def load_countries():
    countries = []
    with open('countries.txt', 'r') as world:
        for country in world:
            countries.append(country.strip())
    return countries

countries = load_countries()
variable = StringVar()
variable.set(countries[0])

# Tạo giao diện
right_frame = Frame(ws, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)
right_frame.pack(padx=10, pady=10)

# Label và Entry
fields = ['Mã nhân viên:', 'Họ tên:', 'Email:', 'Điện thoại:', 'Chọn giới tính:', 'Chọn quốc gia:', 'Password:', 'Nhập lại Password:']
for i, field in enumerate(fields[1:], start=1):
    Label(right_frame, text=field, bg='#CCCCCC', font=f).grid(row=i, column=0, sticky=W, pady=10)

emp_id_entry = Entry(right_frame, font=f)
register_name = Entry(right_frame, font=f)
register_email = Entry(right_frame, font=f)
register_mobile = Entry(right_frame, font=f)
register_pwd = Entry(right_frame, font=f, show='*')
pwd_again = Entry(right_frame, font=f, show='*')

# RadioButtons cho giới tính
gender_frame = LabelFrame(right_frame, bg='#CCCCCC', padx=10, pady=10)
gender_frame.grid(row=5, column=1, pady=10, padx=20)

male_rb = Radiobutton(gender_frame, text='Nam', bg='#CCCCCC', variable=var, value='male', font=('Times', 10))
female_rb = Radiobutton(gender_frame, text='Nữ', bg='#CCCCCC', variable=var, value='female', font=('Times', 10))
others_rb = Radiobutton(gender_frame, text='Khác', bg='#CCCCCC', variable=var, value='others', font=('Times', 10))
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

# OptionMenu cho quốc gia
register_country = OptionMenu(right_frame, variable, *countries)
register_country.config(width=15, font=('Times', 12))

# Button Load và Modify
def load_employee():
    emp_id = emp_id_entry.get()
    if not emp_id:
        messagebox.showinfo('Thông báo lỗi', 'Nhập mã nhân viên để tìm kiếm!')
        return
    try:
        con = sqlite3.connect('quanlynhanvien3.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM employee WHERE id=?", (emp_id,))
        result = cur.fetchone()
        con.close()
        if result:
            register_name.delete(0, END)
            register_name.insert(0, result[1])
            register_email.delete(0, END)
            register_email.insert(0, result[2])
            register_mobile.delete(0, END)
            register_mobile.insert(0, result[3])
            var.set(result[4])
            variable.set(result[5])
            register_pwd.delete(0, END)
            pwd_again.delete(0, END)
        else:
            messagebox.showinfo('Thông báo lỗi', 'Mã nhân viên không tồn tại!')
    except Exception as e:
        messagebox.showerror('Lỗi', str(e))

def modify_employee():
    emp_id = emp_id_entry.get()
    if not emp_id:
        messagebox.showinfo('Thông báo lỗi', 'Nhập mã nhân viên để cập nhật!')
        return
    if register_pwd.get() != pwd_again.get():
        messagebox.showinfo('Thông báo lỗi', 'Mật khẩu không khớp!')
        return
    try:
        con = sqlite3.connect('quanlynhanvien3.db')
        cur = con.cursor()
        cur.execute('''
            UPDATE employee
            SET name=?, email=?, contact=?, gender=?, country=?, password=?
            WHERE id=?
        ''', (
            register_name.get(),
            register_email.get(),
            register_mobile.get(),
            var.get(),
            variable.get(),
            register_pwd.get(),
            emp_id
        ))
        con.commit()
        con.close()
        messagebox.showinfo('Thông báo', 'Cập nhật thông tin nhân viên thành công!')
    except Exception as e:
        messagebox.showerror('Lỗi', str(e))

load_btn = Button(right_frame, width=15, text='Load', font=f, relief=SOLID, cursor='hand2', command=load_employee)
modify_btn = Button(right_frame, width=15, text='Modify', font=f, relief=SOLID, cursor='hand2', command=modify_employee)

# Hiển thị giao diện
emp_id_entry.grid(row=0, column=1, pady=10, padx=20)
register_name.grid(row=1, column=1, pady=10, padx=20)
register_email.grid(row=2, column=1, pady=10, padx=20)
register_mobile.grid(row=3, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=6, column=1, pady=10, padx=20)
pwd_again.grid(row=7, column=1, pady=10, padx=20)
load_btn.grid(row=8, column=1, pady=10, padx=20)
modify_btn.grid(row=9, column=1, pady=10, padx=20)

# Chạy chương trình
ws.mainloop()
