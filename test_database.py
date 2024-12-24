import pytest
import os
from database import Database


@pytest.fixture(scope="module")
def db():
    # Создаем временную базу данных для тестов
    test_db_name = 'test_students.db'
    if os.path.exists(test_db_name):
        os.remove(test_db_name)  # Удаляем старую базу данных, если она существует

    db_instance = Database(db_name=test_db_name)
    yield db_instance  # Возвращаем экземпляр базы данных для использования в тестах

    db_instance.close()  # Закрываем соединение после завершения всех тестов
    os.remove(test_db_name)  # Удаляем временную базу данных


def test_create_table(db):
    """Проверяем создание таблицы студентов."""
    result = db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';").fetchone()
    assert result is not None, "Таблица 'students' не была создана."


def test_add_student(db):
    """Проверяем добавление студента в базу данных."""
    db.add_student("Иванов Иван", "123456", "Математика", 5)

    students = db.get_students()
    assert len(students) == 1, "Студент не был добавлен."
    assert students[0] == ("Иванов Иван", "123456", "Математика", 5), "Данные студента не совпадают."


def test_update_student(db):
    """Проверяем обновление данных студента."""
    db.add_student("Петров Петр", "654321", "Физика", 4)

    # Обновляем данные студента
    student_id = 2  # ID второго студента (Петров Петр)
    db.update_student(student_id, "Петров Петр", "654321", "Химия", 5)

    students = db.get_students()
    assert students[1] == ("Петров Петр", "654321", "Химия", 5), "Данные студента не были обновлены."


def test_delete_student(db):
    """Проверяем удаление студента из базы данных."""
    student_id = 1  # ID первого студента (Иванов Иван)

    db.delete_student(student_id)

    students = db.get_students()
    assert len(students) == 1, "Студент не был удален."
    assert students[0] == ("Петров Петр", "654321", "Химия", 5), "Неверные данные оставшегося студента."
