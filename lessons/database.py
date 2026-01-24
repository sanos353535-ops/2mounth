import sqlite3


def create_tables(connection):
    connection.execute('''DROP TABLE IF EXISTS users''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_name TEXT,
        age INTEGER,
        city TEXT 
    )
    ''')


def delete_student(connection, student_id):
    connection.execute(
        'DELETE FROM students WHERE student_id = ?',
        (student_id,)
    )
    connection.commit()


def delete_student_by_name(connection, student_name):
    connection.execute(
        "DELETE FROM students WHERE student_name = ?",
        (student_name,)
    )
    connection.commit()

def get_all_students(connection):
    ...

def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age, city) VALUES 
    (?, ?, ?)
    ''', (student_name, age, city))
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_tables(conn)

    add_student(conn, "Данил", 18, "Бишкек")
    add_student(conn, "Игорь", 18, "Каракол")
    delete_student(conn, 1)