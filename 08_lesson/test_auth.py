import requests
import os
from dotenv import load_dotenv
import pytest

load_dotenv()


def test_get_token():
    # Правильный формат данных для аутентификации
    auth_data = {
        "username": os.getenv("YOUGILE_LOGIN"),  # Используйте email
        "password": os.getenv("YOUGILE_PASSWORD")  # Пароль
    }
    
    # Попробуйте оба варианта endpoint (один из них должен сработать)
    endpoints = [
        "https://yougile.com/api-v2/auth/api",
        "https://yougile.com/api-v2/auth/token"
    ]
    
    for endpoint in endpoints:
        response = requests.post(endpoint, json=auth_data)
        if response.status_code == 200:
            assert "token" in response.json() or "access_token" in response.json()
            token = response.json().get("token") or response.json().get("access_token")
            print(f"Успешная аутентификация. Токен: {token[:10]}...")
            return
    
    # Если ни один endpoint не сработал
    pytest.fail(f"Не удалось получить токен. Ответы: {[requests.post(e, json=auth_data).status_code for e in endpoints]}")