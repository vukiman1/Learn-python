from tkinter import *
from tkinter import messagebox
import MySQLdb

root = Tk()
root.title('Duyet ban ghi')
root.geometry('500x300')

varName = StringVar()
priceName = StringVar()
desName = StringVar()
varGo =  StringVar()

Label(root,text='Ten hai san: ').place(x= 20,y=20)
txtname = Entry(root, width=50,textvariable=varName).place(x=120,y=20)
Label(root, text='Gia hai san: ').place(x = 20, y=60)
txtPrice = Entry(root, width=50,textvariable=priceName).place(x=120,y=60)
Label(root, text='Mo ta: ').place(x = 20, y=100)
txtDescription = Entry(root, width=50,textvariable=priceName).place(x=120,y=100)