from sqlalchemy import text


def test_add_student(session):
    """Проверяет добавление студента."""
    session.execute(
        text(
            "INSERT INTO student (user_id, subject_id, level, education_form) "
            "VALUES (:user_id, :subject_id, :level, :education_form)"
        ),
        {
            "user_id": 99999,
            "subject_id": 1,
            "level": "Beginner",
            "education_form": "personal",
        },
    )
    session.commit()

    result = session.execute(
        text("SELECT user_id FROM student WHERE user_id = :user_id"),
        {"user_id": 99999},
    ).fetchone()
    assert result is not None

    # Удаляем за собой
    session.execute(
        text("DELETE FROM student WHERE user_id = :user_id"),
        {"user_id": 99999},
    )
    session.commit()


def test_update_subject(session):
    """Проверяет изменение названия предмета."""
    session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) "
            "VALUES (:id, :title)"
        ),
        {"id": 99999, "title": "Old Title"},
    )
    session.commit()

    session.execute(
        text(
            "UPDATE subject SET subject_title = :title "
            "WHERE subject_id = :id"
        ),
        {"id": 99999, "title": "New Title"},
    )
    session.commit()

    result = session.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": 99999},
    ).fetchone()
    assert result[0] == "New Title"

    session.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": 99999},
    )
    session.commit()


def test_delete_teacher(session):
    """Проверяет удаление учителя."""
    session.execute(
        text(
            "INSERT INTO teacher (teacher_id, email, group_id) "
            "VALUES (:id, :email, :group_id)"
        ),
        {"id": 99999, "email": "test@test.com", "group_id": 1},
    )
    session.commit()

    session.execute(
        text("DELETE FROM teacher WHERE teacher_id = :id"),
        {"id": 99999},
    )
    session.commit()

    result = session.execute(
        text("SELECT teacher_id FROM teacher WHERE teacher_id = :id"),
        {"id": 99999},
    ).fetchone()
    assert result is None
