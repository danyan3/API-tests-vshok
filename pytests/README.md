# Тесты REST API для сервиса ВШОКЕ

Работу выполнил Точинов Данил

TG: [@danya639](https://t.me/danya639)

## Стек

- [pytest](https://docs.pytest.org/)
- [faker](https://faker.readthedocs.io/)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)
- [pydantic](https://pydantic-docs.helpmanual.io/)

## Быстрый старт

1. **Создайте виртуальное окружение:**
```console
python -m venv venv
```

2. **Активируйте виртуальное окружение:**

Windows:

```console
venv\Scripts\activate.bat
```
Linux/macOS:

```console
source venv/bin/activate
```

3. **Установите зависимости:**
   
```console
pip install -r requirements.txt
```

4. **Настройте переменные окружения:**

Если нужно указать свой эндпоинт, создайте/отредактируйте файл `.env` в корневой директории репозитория:
```
BASE_URL=http://your-api-endpoint:port
```
По умолчанию используется `http://localhost:3000`.

5. **Запустите тесты:**

В главной директории проекта выполните:
```console
pytest
```

## Структура

- Все тесты и вспомогательные файлы размещены в этой папке.
- Для генерации случайных данных используется Faker.
- Переменные окружения подхватываются с помощью python-dotenv.
- Для моделей и валидации данных используется Pydantic.

## Примечания

- Убедитесь, что тестируемый API доступен по адресу из переменной `BASE_URL`.
- Убедитесь, что файл `.env` НЕ входит в систему контроля версий, если он содержит чувствительные данные.

---
