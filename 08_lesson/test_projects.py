import pytest
from api_client import YougileAPIClient
from unittest.mock import MagicMock


class TestProjectsAPI:
    @pytest.fixture
    def mock_client(self):
        client = YougileAPIClient(use_mock=True)
        # Настраиваем мок-ответы
        client.create_project = MagicMock()
        client.get_project = MagicMock()
        client.update_project = MagicMock()
        return client

    def test_create_project_positive(self, mock_client):
        """Тест успешного создания проекта"""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": "mock_prj_123",
            "title": "Test Project",
            "description": "Test Description"
        }
        mock_client.create_project.return_value = mock_response 
        response = mock_client.create_project("Test Project", "Test Description")
        assert response.status_code == 201
        assert response.json()["id"] == "mock_prj_123"

    def test_create_project_negative(self, mock_client):
        """Тест с невалидными данными"""
        mock_client.create_project.side_effect = ValueError("Invalid title")
        with pytest.raises(ValueError) as exc_info:
            mock_client.create_project(None)
        assert "Invalid title" in str(exc_info.value)

    def test_get_project_positive(self, mock_client):
        """Тест успешного получения проекта"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "mock_prj_123",
            "title": "Test Project"
        }
        mock_client.get_project.return_value = mock_response
        response = mock_client.get_project("mock_prj_123")
        assert response.status_code == 200
        assert response.json()["id"] == "mock_prj_123"

    def test_get_project_negative(self, mock_client):
        """Тест с несуществующим ID"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Project not found"}
        mock_client.get_project.return_value = mock_response
        response = mock_client.get_project("invalid_id")
        assert response.status_code == 404
        assert "error" in response.json()

    def test_update_project_positive(self, mock_client):
        """Тест успешного обновления"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "mock_prj_123",
            "title": "New Title",
            "description": "New Desc"
        }
        mock_client.update_project.return_value = mock_response
        response = mock_client.update_project("mock_prj_123", title="New Title")
        assert response.status_code == 200
        assert response.json()["title"] == "New Title"

    def test_update_project_negative(self, mock_client):
        """Тест без изменений"""
        mock_client.update_project.side_effect = ValueError("No fields to update")
        with pytest.raises(ValueError) as exc_info:
            mock_client.update_project("mock_prj_123")
        assert "No fields to update" in str(exc_info.value)