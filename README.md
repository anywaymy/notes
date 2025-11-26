<h1 align="center">NOTES ПРИЛОЖЕНИЕ (django/vue.js)</h1>



## 🚀 Запуск BACKEND части локально

Следуйте этим шагам, чтобы запустить проект у себя на компьютере.

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/anywaymy/notes.git
cd backend
```

### 2. Создайте виртуальное окружение для бэкенда

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Примите миграции

```bash
python manage.py migrate
```

### 5. Создайте супер пользователя

```bash
python manage.py createsuperuser
```

### 6. Запустите проект

```bash
python manage.py runserver
```

После запуска проекта результат можно увидеть по данной ссылке - http://127.0.0.1:8000/api/v1/notes/

Проверить работу API можно как через браузер, так и через приложение postman.

Также можно ограничить доступ через браузер. В settings.py раскомментируйте строку ниже

```python
'DEFAULT_RENDERER_CLASSES': [
  'rest_framework.renderers.JSONRenderer',  # Рендеринг в JSON
],
```

## ВАЖНО

Не стоит хранить .env файлик в публичных репозиториях, так как он может хранить секретные данные. Только если в учебных целях

## 🚀 Запуск FRONTEND части локально

### 1. Установите зависимости

```bash
cd vue-notes
npm install
```

### 3. Запуск vue приложения

```bash
cd vue-notes
npm run dev
```

После всех этих манипуляций, результат можно увидеть по этому адресу - http://localhost:5173/













