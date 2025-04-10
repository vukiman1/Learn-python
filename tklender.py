from tkinter import *
from tkcalendar import *

ws = Tk()
ws.title("Chọn ngày tháng")
ws.geometry("500x400")
ws.config(bg="#cd950c")


hour_string = StringVar()
min_string = StringVar()
last_value_sec = ""
last_value = ""
f = ('Times', 20)



fone =Frame(ws)
ftwo = Frame(ws)

fone.pack(pady=10)
ftwo.pack(pady=10)

cal = Calendar(
    fone,
    selectmode = "day",
    year = 2024,
    month = 8,
    day = 17
)

cal.pack()


min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
)

sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    width=2,
    font=f,
    justify=CENTER
)

sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
)


def display_msg():
    date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    s = sec.get()
    t = f"Bạn đã đặt phòng vào ngày {date} vào lúc {m}:{h}:{s}."
    msg_display.config(text=t)

if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value = min_string.get()

if last_value_sec == "59" and sec_hour.get() == "0":
    min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)

if last_value == "59":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)






min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill= X, expand=True)
sec.pack(side=LEFT, fill= X, expand=True)

msg = Label(
    ws,
    text="Giờ phút giây",
    font=("Time", 12),
    bg="#cd950c"
)

msg.pack(side=TOP)

actionBtn = Button(
    ws,
    text = "Đặt phòng",
    padx=10,
    pady=10,
    command=display_msg
)

actionBtn.pack(pady=10)

msg_display = Label(
    ws,
    text="",
    bg= "#cd950c"
)

msg_display.pack(pady=10)

ws.mainloop()