import sqlite3

# Kết nối cơ sở dữ liệu
con = sqlite3.connect('quanlynhanvien3.db')
cur = con.cursor()

# Tạo bảng nếu chưa tồn tại
cur.execute('''
    CREATE TABLE IF NOT EXISTS employee(
        id TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        contact INTEGER,
        gender TEXT,
        country TEXT,
        password TEXT
    )
''')

# Thêm một bản ghi vào bảng employee
cur.execute('''
    INSERT INTO employee (id, name, email, contact, gender, country, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    "1231312",
    "Kim An",
    "kiman@gmail.com",
    12345,
    "Nam",
    "Ha Noi",
    "123456"
))

# Commit và đóng kết nối
con.commit()
con.close()
