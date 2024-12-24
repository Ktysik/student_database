import sqlite3

class Database:
    def __init__(self, db_name='students.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                record_book_number TEXT NOT NULL,
                subject TEXT NOT NULL,
                grade INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def add_student(self, full_name, record_book_number, subject, grade):
        self.cursor.execute('''
            INSERT INTO students (full_name, record_book_number, subject, grade)
            VALUES (?, ?, ?, ?)
        ''', (full_name, record_book_number, subject, grade))
        self.connection.commit()

    def get_students(self):
        self.cursor.execute('SELECT full_name, record_book_number, subject, grade FROM students')
        return self.cursor.fetchall()

    def update_student(self, student_id, full_name, record_book_number, subject, grade):
        self.cursor.execute('''
            UPDATE students SET full_name=?, record_book_number=?, subject=?, grade=?
            WHERE id=?
        ''', (full_name, record_book_number, subject, grade, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
