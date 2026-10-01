import requests


class ProjectPage:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users):
        """Создает новый проект."""
        payload = {"title": title, "users": users}
        return requests.post(
            self.base_url, json=payload, headers=self.headers
        )

    def get_project(self, project_id):
        """Получает проект по ID."""
        url = f"{self.base_url}/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, title):
        """Обновляет проект по ID."""
        url = f"{self.base_url}/{project_id}"
        payload = {"title": title}
        return requests.put(url, json=payload, headers=self.headers)
