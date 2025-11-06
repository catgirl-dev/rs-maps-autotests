# Rahul Shetty Maps API Autotests

Автоматизированные тесты для проверки функционала **[Rahul Shetty Maps API](https://rahulshettyacademy.com)**.
Тесты написаны с использованием **Python**, **Pytest**, **Requests**, **Allure** и **Loguru**.
## ⚙️ Установка зависимостей
```bash
pip install -r requirements.txt
```
## 🧪 Запуск тестов
С генерацией Allure отчёта:
```bash
pytest --alluredir=allure-results tests/test_rs_maps_api.py
```
Без генерации Allure отчёта:
```bash
pytest tests/test_rs_maps_api.py
```
Просмотр Allure отчёта:
```bash
allure serve allure-results
```
## 📖 Внешний вид Allure отчёта
* Overview
<img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/025ca39d-8892-48a8-a4d2-51b23a392ede" />


* Categories
<img width="600" height="270" alt="image" src="https://github.com/user-attachments/assets/60f4c60b-4476-4301-94ad-69b1eb102600" />


* Suites
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/ae09052c-0aa9-466c-a357-4713e0716bbb" />


* Graphs
<img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/22e94144-a67b-4e68-96b8-d043b9fc953b" />


* Behaviors
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/db21f931-fa8d-4ed7-9519-b48133211b02" />


## 📝 Настройки логгирования и фикстур
* Логи можно отключить или настроить через `logger_config.py`
* Фикстуры можно настроить через `conftest.py`
---
