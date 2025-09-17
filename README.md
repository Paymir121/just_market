Магазин радиофармпрепаратов и медицнских изделей.
## Описание
### Технологии
- **Django**
- **React**
- **Docker**
- **Nginx**

### Авторы
Nikki Nikonor

### Выполнить миграции:
```
        cd backend
        python manage.py makemigrations
        python manage.py migrate
```

### Запустить проект:
```
        cd backend
        python manage.py runserver
```

### Создать суперпользователя:
```
        cd backend
        python manage.py createsuperuser
```

## Запуск докер контейнеров на локальной машине:

### Билдим проект и запускаем:
```
        docker compose up --build
```

### Выполнить миграции:
```
        docker compose exec backend python manage.py migrate
```

### Выполнить создание суперпользователя:
```
        docker compose exec backend python manage.py createsuperuser
```

### Выполнить Собрать статику Django:
```
        docker compose exec backend python manage.py collectstatic
        docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```
