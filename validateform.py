from tkinter import *
from tkinter import *


ws = Tk()
ws.title("Validate form")
ws.config(bg="#0B5A81")


f = ("Time", 14)
var = StringVar()
var.set('male')

courses = []
variable =StringVar()


world = open('course.txt', 'r')
for course in world:
    course = course.rstrip('\n')
    courses.append(course)



right_frame = Frame(
    ws,
    bd=2,
    bg="#CCCCCC",
    relief=SOLID,
    padx=40,
    pady=40
)

Label(
    right_frame,
    text="Course Register",
    bg="#377dff",
    font=f,
).grid(row=0, columnspan=2, sticky=EW, pady=10,)

Label(
    right_frame,
    text="Full Name",
    bg="#CCCCC1",
    font=f,
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Email",
    bg="#CCCCC1",
    font=f,
).grid(row=2, column=0, sticky=W, pady=10)
Label(
    right_frame,
    text="DOB",
    bg="#CCCCC1",
    font=f,
).grid(row=3, column=0, sticky=W, pady=10)
Label(
    right_frame,
    text="Gender",
    bg="#CCCCC1",
    font=f,
).grid(row=4, column=0, sticky=W, pady=10)
Label(
    right_frame,
    text="Contact no.",
    bg="#CCCCC1",
    font=f,
).grid(row=5, column=0, sticky=W, pady=10)
Label(
    right_frame,
    text="Select cource",
    bg="#CCCCC1",
    font=f,
).grid(row=6, column=0, sticky=W, pady=10)




gender_frame = LabelFrame(
    right_frame,
    bg="#CCCCCC",
    padx=10,
    pady=10
)


daysSelect = ['2/5/2024','22/08/2024']


gender_frame.grid(row=4, column=1, pady=10, padx=20, sticky='w')

txtName = Entry(right_frame, font=f).grid(row=1, column=1, pady=10, padx=20)
txtEmail = Entry(right_frame, font=f).grid(row=2, column=1, pady=10, padx=20)
registerDOB = Menubutton(
    right_frame,
    text="22/08/2024",
    relief=RAISED
)
registerDOB.grid(row=3, column=1, pady=10, padx=20, sticky='w')

registerDOB.menu = Menu(registerDOB, tearoff=0)
registerDOB["menu"] = registerDOB.menu

mayoVar = IntVar()
ketchVar = IntVar()

registerDOB.menu.add_checkbutton(label="mayo", variable=mayoVar)
registerDOB.menu.add_checkbutton(label="ketchup", variable=ketchVar)
 

male_rb = Radiobutton(gender_frame, 
    text='Nam', bg='#CCCCCC',
    variable=var, value='male', font=('Times', 10),)
female_rb = Radiobutton(gender_frame, 
    text='Nu', bg='#CCCCCC',
    variable=var, value='male', font=('Times', 10),)

male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)

txtContact = Entry(right_frame, font=f).grid(row=5, column=1, pady=10, padx=20)

register_course = OptionMenu(
    right_frame, variable,courses[0], *courses
).grid(row=6, column=1, pady=10, ipadx=60, padx=20, sticky='w')
right_frame.pack()


register_btn = Button(
   right_frame, width=15, bg="#00d082",text='Submit', fg="#ffffff", font=f, relief=SOLID, cursor='hand2', 
).grid(row=7, column=0, pady=10, padx=20)
register_btn = Button(
   right_frame, width=15, text='Cancel', bg="#cf2e2e", fg="#ffffff", font=f, relief=SOLID, cursor='hand2', 
).grid(row=7, column=1, pady=10, padx=20)

ws.mainloop()