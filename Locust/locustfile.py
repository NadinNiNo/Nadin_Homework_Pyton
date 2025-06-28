from locust import HttpUser, task, between, events
from locust.runners import MasterRunner, WorkerRunner
import random
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчик для инициализации Worker
# @events.init.add_listener
# def on_locust_init(environment, **kwargs):
#     if isinstance(environment.runner, WorkerRunner):
#         logger.info("Initializing worker")
#     elif isinstance(environment.runner, MasterRunner):
#         logger.info("Initializing master")

class TowerEmpireUser(HttpUser):
    host = "https://api.dev.tower-empire.ru/api/base/lobby/"
    # wait_time = between(1, 5)  # Время ожидания между задачами
    
    # def on_start(self):
    #     """Выполняется при старте каждого виртуального пользователя"""
    #     self.login()
    
    # def login(self):
    #     """Пример логина пользователя (замените на реальные данные)"""
    #     response = self.client.post("/api/login", json={
    #         "username": "test_user",
    #         "password": "test_password"
    #     })
    #     if response.status_code == 200:
    #         self.auth_token = response.json().get("token")
    #         logger.info("Login successful")
    #     else:
    #         logger.error(f"Login failed: {response.text}")
    
    @task(1)
    def load_main_page(self):
        """Загрузка главной страницы"""
        with self.client.get("https://api.dev.tower-empire.ru/api/base/lobby/") as response:
            if response.status_code != 200:
                response.failure(f"Failed to load main page: {response.status_code}")
    
    # @task(2)
    # def load_game_data(self):
    #     """Загрузка данных игры"""
    #     headers = {"Authorization": f"Bearer {self.auth_token}"} if hasattr(self, "auth_token") else {}
    #     with self.client.get("/api/game/data", headers=headers, catch_response=True) as response:
    #         if response.status_code != 200:
    #             response.failure(f"Failed to load game data: {response.status_code}")
    
    # @task(1)
    # def perform_game_action(self):
    #     """Выполнение игрового действия"""
    #     if not hasattr(self, "auth_token"):
    #         return
        
    #     action_types = ["build", "upgrade", "attack"]
    #     action_data = {
    #         "action": random.choice(action_types),
    #         "target": f"building_{random.randint(1, 10)}",
    #         "value": random.randint(1, 100)
    #     }
        
    #     headers = {"Authorization": f"Bearer {self.auth_token}"}
    #     with self.client.post("/api/game/action", json=action_data, headers=headers, catch_response=True) as response:
    #         if response.status_code != 200:
    #             response.failure(f"Game action failed: {response.status_code}")