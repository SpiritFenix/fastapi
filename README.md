1. Клонирование репозитория 

```git clone https://github.com/SpiritFenix/fastapi.git```

2. Переход в директорию fastapi

```cd fastapi```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта для демонстрации возможностей fastapi

```uvicorn app.main:app --reload```