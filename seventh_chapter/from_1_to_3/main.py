import sqlite3

DB_PATH = "./from_1_to_3/school.db"
def basic_sqllite_CRUD(data):

    cursor.execute("""CREATE TABLE IF NOT EXISTS Students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,grade REAL)""")
    connection.commit()
    
    cursor.executemany("INSERT INTO Students(name, grade) VALUES(?, ?)", data)
    connection.commit()


def parameterized_quieres():
    student_name = input("Please enter your name: ").strip()
    grade = float(input("Please enter your grade: ").strip())
    cursor.execute("INSERT INTO Students (name, grade) VALUES (?, ?)", (student_name, grade))
    connection.commit()


def transactions():
    cursor.execute("INSERT INTO Students (name, grade) VALUES(?, ?)", ("Test", 55))
    try:
        result = 123/0
        connection.commit()
    except ZeroDivisionError:
        print("An error occurred! Rolling back")
        connection.rollback()


def show_table():
    cursor.execute(f"SELECT * FROM Students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def DELETE_DATA():
    cursor.execute(f"DELETE FROM Students")
#================================================
data = [
    ["Ali", 85.5],
    ["Sara", 92.0],
    ["Mohammed", 78.3]
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# 1: basic_sqllite_CRUD]
print("=" * 50)
print("Basic SQLite CRUD: ")
DELETE_DATA()
basic_sqllite_CRUD(data)
show_table()

#2: parameterized_quieres
print("=" * 50)
print("Parameterized quieres:")
parameterized_quieres()
show_table()

#3: Transactions:
print("=" * 50)
print("Transactions:")
transactions()
show_table()

connection.close()