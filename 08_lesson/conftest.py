import pytest


@pytest.fixture(scope="session")
def mock_api_token():
    return "yg_mock_token_for_testing_12345"