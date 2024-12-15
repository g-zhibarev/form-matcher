# Form Matcher API

API, созданный с использованием FastAPI, который обрабатывает запросы, в которых пользователь предоставляет данные для шаблонов форм. API ищет и возвращает шаблоны, которые соответствуют полям и типам данных, переданным в запросе.

## Установка

1. Клонируйте репозиторий:
   ```bash
   cd your-repository-folder
   git clone https://github.com/g-zhibarev/form-matcher.git
   ```
2. Создайте виртуальное окружение и активируйте его:

- Для Linux/MacOS:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Для Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
3. Установите зависимости из файла requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
4. Создайте базу данных, запустив скрипт create_db.py:
   ```bash
   python create_db.py
   ```
## Запуск API
   
Для запуска API используйте команду:
   ```bash
   python form_matcher_app.py
   ```
Это запустит сервер на http://0.0.0.0:8000, где можно будет обращаться к API.

## Структура проекта
- **form_mathcer_app.py**: основной файл, который содержит код FastAPI для обработки запросов.
- **create_db.py**: скрипт для создания базы данных db.json с шаблонами форм.
- **db.json**: база данных, содержащая шаблоны форм.
- **test.py**: скрипт для тестирования API с примерами запросов и проверкой ответов.
## Тестирование

Для тестирования API используйте файл **test.py**, который отправляет POST-запросы к серверу и выводит ответы.

Запустите тесты с помощью команды:
   ```bash
   python test.py
   ```