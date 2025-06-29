import pytest
from unittest.mock import Mock

# Регистрируем пользовательские метки
pytestmark = [pytest.mark.positive, pytest.mark.negative]

@pytest.mark.positive
class TestPositiveCases:
    def test_create_project(self, yougile_api, mock_requests, test_project_data):
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": "123", **test_project_data}
        mock_requests.post.return_value = mock_response

        response = yougile_api.create_project(test_project_data)
        
        assert response.status_code == 201
        assert response.json()["id"] == "123"
        mock_requests.post.assert_called_once()

    def test_get_project(self, yougile_api, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "123", "name": "Test"}
        mock_requests.get.return_value = mock_response

        response = yougile_api.get_project("123")
        
        assert response.status_code == 200
        assert response.json()["id"] == "123"

@pytest.mark.negative
class TestNegativeCases:
    def test_create_project_failure(self, yougile_api, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_requests.post.return_value = mock_response

        response = yougile_api.create_project({})
        
        assert response.status_code == 400

    def test_get_nonexistent_project(self, yougile_api, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response

        response = yougile_api.get_project("nonexistent")
        
        assert response.status_code == 404