Логика проекта
Проект представляет собой приложение для управления базой данных студентов с использованием библиотеки PyQt5 для создания графического интерфейса и SQLite3 для хранения данных. Основная функциональность приложения включает добавление, редактирование и удаление записей о студентах, а также отображение этих данных в таблице.
Структура проекта
Проект организован в виде модулей, что позволяет разделить логику приложения на отдельные части, улучшая читаемость и поддерживаемость кода. Ниже представлена структура проекта и описание основных модулей:
text
student_database/
│
├── main.py          # Точка входа в приложение
├── database.py      # Модуль для работы с базой данных
├── ui.py            # Модуль для интерфейса пользователя
└── requirements.txt  # Файл с зависимостями
Описание основных модулей
1. main.py
Функция: Этот файл является точкой входа в приложение. Он инициирует выполнение программы, создает экземпляр класса интерфейса пользователя и запускает главный цикл приложения.
Основные действия:
Импортирует необходимые библиотеки и модули.
Создает экземпляр приложения QApplication.
Создает и отображает окно приложения (StudentApp).
Запускает главный цикл обработки событий.
python
import sys
from PyQt5.QtWidgets import QApplication
from ui import StudentApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec_())
2. database.py
Функция: Этот модуль управляет всеми операциями с базой данных SQLite. Он отвечает за создание таблицы, добавление, обновление, удаление и получение записей о студентах.
Основные действия:
Устанавливает соединение с базой данных.
Создает таблицу students, если она не существует.
Реализует методы для добавления (add_student), получения (get_students), обновления (update_student) и удаления (delete_student) записей.
python
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

    # Методы для работы с базой данных...
3. ui.py
Функция: Этот модуль отвечает за создание графического интерфейса пользователя (GUI). Он определяет, как будет выглядеть приложение и как пользователь будет взаимодействовать с ним.
Основные действия:
Создает интерфейс с полями ввода для информации о студенте (ФИО, номер зачетки, предмет, оценка).
Реализует кнопки для добавления и удаления студентов.
Отображает данные студентов в таблице QTableWidget.
Обрабатывает события, такие как нажатие кнопок и двойной клик по строкам таблицы для редактирования.
python
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QMessageBox, QTableWidget,
    QTableWidgetItem
)
from database import Database

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.initUI()
        self.loadStudents()

    def initUI(self):
        layout = QVBoxLayout()
        # Создание полей ввода и кнопок...
        
    def loadStudents(self):
        students = self.db.get_students()
        # Загрузка студентов в таблицу...
        
    def addStudent(self):
        # Логика добавления студента...
        
    def deleteStudent(self):
        # Логика удаления студента...
Взаимодействие между модулями
main.py:
Инициализирует приложение и создает экземпляр класса StudentApp из модуля ui.py.
ui.py:
Импортирует класс Database из модуля database.py для выполнения операций с базой данных.
При вызове методов (например, addStudent, deleteStudent) взаимодействует с объектом базы данных для выполнения соответствующих операций.
database.py:
Обрабатывает все запросы к базе данных и возвращает результаты обратно в ui.py, где они отображаются в интерфейс
