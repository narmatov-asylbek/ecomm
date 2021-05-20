# Basic E-commerce web application
## English
The techstack is following: Python, Django REST Framework, Django, Redis, django-environ, HTML, CSS. Celery for some tasks.

### Features:
- Adding to cart
- Creating products
- Creating orders
- Coupon system
- Categories
- Session based cart system
- Basic recommendation system using Redis
- API using DRF

TODO: Implement Pagination and user aut.

#### To run project on your local machine, follow these steps:
- [ ] Clone this repo to your machine
- [ ] Optional: Create a virtualenv
- [ ] Instal requirements: pip install -r requirements.txt
- [ ] Migrate: python3 manage.py migrate

## На Русском
##### Использованные технологии: Python, Django REST Framework, Django, Redis, django-environ, Html, Css, Немного Сelery
### Возможности
- Добавление в карзину
- Создание товаров
- Добавление категории товаров
- Купоны
- API
- Базовая система рекомендаций
- Отпавка email об успешном заказн

TODO: Добавить пагинацию, аутентификацию и авторизацию

#### Чтобы запустить и протестировать проект:
- Сделать клон данного репозитория
- Создать вирутальную среду: python3 -m venv <название>
- Установить зависимости: pip install -r requirements.txt
- Проверить на наличие миграций: python3 manage.py makemigrations
- Создать миграции: python3 manage.py migrate
