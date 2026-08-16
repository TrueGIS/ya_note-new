# YaNote: начальное состояние

Список пользователя показывает не больше десяти заметок на странице. Новые
заметки расположены первыми.

## Запуск проекта

Для проекта нужен Python 3.14.

```bash
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Тесты запускаются из директории с файлом `manage.py`:

```bash
pytest
```

До создания первых тестов pytest завершится с сообщением, что проверки не
найдены. Это ожидаемое состояние.
