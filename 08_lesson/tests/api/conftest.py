import pytest
from unittest.mock import Mock
from ..yougile_api import YougileAPI  # <-- Исправленный импорт

@pytest.fixture
def mock_requests():
    return Mock()

@pytest.fixture
def yougile_api(mock_requests):
    api = YougileAPI("https://yougile.com/api-v2", "test-token")
    api.session = mock_requests
    return api

@pytest.fixture
def test_project_data():
    import uuid
    return {
        "name": f"Test Project {uuid.uuid4().hex[:8]}",
        "description": "Test project for API testing"
    }
