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
<img width="508" height="353" alt="image" src="https://github.com/user-attachments/assets/f4c71467-9a65-43be-b481-416575038842" />

## 📝 Настройки логгирования и фикстур
* Логи можно отключить или настроить через logger_config.py
* Фикстуры можно настроить через conftest.py
---
