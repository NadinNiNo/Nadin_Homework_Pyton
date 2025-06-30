# test_debug.py
import os
from dotenv import load_dotenv

def test_env_loading():
    """Проверка загрузки .env"""
    load_dotenv()
    token = os.getenv("YOUGILE_API_TOKEN")
    assert token is not None, "Токен не загружен из .env"
    assert token.startswith("yg_"), "Токен должен начинаться с yg_"
    print(f"Токен успешно загружен: {token[:10]}...")