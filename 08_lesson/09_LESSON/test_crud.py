from models import Student


def test_create_student(db_session):
    """Тест создания студента"""
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(name="Иван Иванов").first()
    assert student is not None
    assert student.email == "ivan@example.com"

    # Очистка
    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    """Тест обновления студента"""
    # Создаем студента для теста
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()

    # Обновляем email
    student.email = "new_petr@example.com"
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(name="Петр Петров").first()
    assert updated_student.email == "new_petr@example.com"

    # Очистка
    db_session.delete(updated_student)
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления студента"""
    # Создаем студента для теста
    student = Student(name="Сергей Сергеев", email="sergey@example.com")
    db_session.add(student)
    db_session.commit()

    # Удаляем студента
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(name="Сергей Сергеев").first()
    assert deleted_student is None
