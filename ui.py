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

        # Поля ввода
        self.full_name_input = QLineEdit(self)
        self.full_name_input.setPlaceholderText("ФИО")
        layout.addWidget(self.full_name_input)

        self.record_book_input = QLineEdit(self)
        self.record_book_input.setPlaceholderText("Номер зачетки")
        layout.addWidget(self.record_book_input)

        self.subject_input = QLineEdit(self)
        self.subject_input.setPlaceholderText("Предмет")
        layout.addWidget(self.subject_input)

        self.grade_input = QLineEdit(self)
        self.grade_input.setPlaceholderText("Оценка")
        layout.addWidget(self.grade_input)

        # Кнопка добавления
        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.clicked.connect(self.addStudent)
        layout.addWidget(self.submit_button)

        # Кнопка удаления
        self.delete_button = QPushButton("Удалить", self)
        self.delete_button.clicked.connect(self.deleteStudent)
        layout.addWidget(self.delete_button)

        # Таблица для отображения студентов
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ФИО", "Номер зачетки", "Предмет", "Оценка"])
        layout.addWidget(self.table_widget)

        # Установка основного макета
        self.setLayout(layout)
        self.setWindowTitle("Студенческая база данных")
        self.resize(600, 400)

    def loadStudents(self):
        students = self.db.get_students()

        # Очистка таблицы перед загрузкой данных
        self.table_widget.setRowCount(0)

        for student in students:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            for column in range(4):
                item = QTableWidgetItem(str(student[column]))
                self.table_widget.setItem(row_position, column, item)

    def addStudent(self):
        full_name = self.full_name_input.text()
        record_book_number = self.record_book_input.text()
        subject = self.subject_input.text()

        try:
            grade = int(self.grade_input.text())
            if not full_name or not record_book_number or not subject:
                raise ValueError("Все поля должны быть заполнены.")

            # Добавление студента в базу данных
            self.db.add_student(full_name, record_book_number, subject, grade)
            QMessageBox.information(self, "Успех", "Данные успешно добавлены.")
            self.clearInputs()
            self.loadStudents()  # Обновляем таблицу

        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))

    def deleteStudent(self):
        selected_row = self.table_widget.currentRow()  # Получаем выбранную строку

        if selected_row < 0:  # Если строка не выбрана
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите студента для удаления.")
            return

        full_name = self.table_widget.item(selected_row, 0).text()

        reply = QMessageBox.question(
            self,
            'Подтверждение удаления',
            f'Вы уверены, что хотите удалить студента "{full_name}"?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            student_id = selected_row + 1  # ID соответствует порядку в таблице (начиная с 1)

            # Удаление студента из базы данных
            try:
                self.db.delete_student(student_id)
                QMessageBox.information(self, "Успех", f"Студент \"{full_name}\" успешно удален.")
                self.loadStudents()  # Обновляем таблицу после удаления
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")

    def clearInputs(self):
        """Очищает поля ввода."""
        self.full_name_input.clear()
        self.record_book_input.clear()
        self.subject_input.clear()
        self.grade_input.clear()
