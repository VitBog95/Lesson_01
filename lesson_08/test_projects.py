import time
import pytest
from project_page import ProjectPage


BASE_URL = "https://ru.yougile.com/api-v2/projects"
TOKEN = ""
USER_ID = ""


@pytest.fixture
def project_page():
    return ProjectPage(BASE_URL, TOKEN)


# === POST: Создание проекта ===
def test_create_project_positive(project_page):
    title = f"Тестовый проект {int(time.time())}"
    response = project_page.create_project(title, {USER_ID: "admin"})
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative(project_page):
    response = project_page.create_project("", {USER_ID: "admin"})
    assert response.status_code == 400


# === GET: Получение проекта ===
def test_get_project_positive(project_page):
    title = f"Проект для GET {int(time.time())}"
    create_response = project_page.create_project(title, {USER_ID: "admin"})
    project_id = create_response.json()["id"]

    response = project_page.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == title


def test_get_project_negative(project_page):
    response = project_page.get_project("non-existent-id")
    assert response.status_code in [400, 404]


# === PUT: Обновление проекта ===
def test_update_project_positive(project_page):
    old_title = f"Старое название {int(time.time())}"
    new_title = f"Новое название {int(time.time())}"

    create_response = project_page.create_project(
        old_title, {USER_ID: "admin"}
    )
    project_id = create_response.json()["id"]

    response = project_page.update_project(project_id, new_title)
    assert response.status_code == 200

    get_response = project_page.get_project(project_id)
    assert get_response.json()["title"] == new_title


def test_update_project_negative(project_page):
    response = project_page.update_project("non-existent-id", "Новое имя")
    assert response.status_code in [400, 404]
