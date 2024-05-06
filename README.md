# Проект ThinkLand Products

Cервис **ThinkLand Products**, для работы с продуктами и их категориями и поиском по продуктам.


---

### Использованные технологии:

- ***Django** 5.0.4*
- ***Django REST Framework** 3.15.1*
- *WSGI сервер **gunicorn** 22.0.0*
- *База Данных **PostgreSQL** 15.5*
- *Поисковый движок **Elasticsearch** (интеграция - elasticsearch-dsl 8.12.0)*
- *Контейнеризация **Docker***

*Приложение написано на **Python** 3.10*

---

### Как начать работу с проектом:

Клонировать репозиторий:
```bash
git clone git@github.com:VtlBz/thinkland_products_crud.git
```

Перейти в папку ***infra/***, находящуюся внутри папки с проектом.

В указанной папке в файле ***.env*** указать переменные окружения, соответствующие проекту.
Пример заполнения:

```bash
SECRET_KEY=<указать-тут-ключ-проекта>
ALLOWED_HOSTS=<перечислить разрешенные хосты через пробел>

DEBUG_STATE=False # Статус режима DEBUG, по умолчанию False

COMPOSE_PROJECT_NAME=tl # Имя проекта проекта в Docker Compose

DB_ENGINE=django.db.backends.postgresql # Тип используемой БД. В проекте используется PostgreSQL
DB_NAME=postgres # Имя базы
POSTGRES_USER=postgres # Имя пользователя БД
POSTGRES_PASSWORD=postgres # Пароль пользователя БД
DB_HOST=tl # название сервиса (контейнера), по умолчанию - localhost
DB_PORT=5432 # Порт для подключения к сервису, стандартный по умолчанию

ES_HOST=tl-es # название сервиса (контейнера) или localhost
ES_PORT=9200 # порт для подключения к сервису

```

Запустить сборку контейнеров командой:

```bash
sudo docker compose up -d
```

- *В зависимости от настроек системы возможно тут и далее потребуется использовать команду **docker compose** c дефисом вместо пробела: **docker-compose***

При первом запуске создать и применить миграции:

```bash
sudo docker exec -it tl-srv python manage.py makemigrations
sudo docker exec -it tl-srv python manage.py migrate
```

Создать индексы Elasticsearch:

```bash
sudo docker exec -it tl-srv python manage.py search_index --rebuild -f
```

При необходимости создать суперпользователя:

```bash
sudo docker exec -it tl-srv python manage.py createsuperuser
```

В браузере перейти на страницу [localhost/api/v1](localhost/api/v1)  

В сервисе доступны следующие эндпоинты:

- 
    ```
    localhost/api/v1/categories/
    ```

    Позволяет создать категорию (```POST``` запрос) или получить список существующих категорий (```GET``` запрос),
    а так же получить информацию о конкретной категории - ```api/v1/categories/<ID>``` (```GET``` запрос)

- 
    ```
    localhost/api/v1/products/
    ```

    Позволяет создать продукт (```POST``` запрос) или получить список существующих продуктов (```GET``` запрос),
    а так же получить информацию о конкретном продукте - ```api/v1/products/<ID>``` (```GET``` запрос).

- 
    ```
    localhost/api/v1/products-search
    ```

    Позволяет искать продукт по совпадению слова в поле ```title``` или ```description``` - параметр запроса - ```?search=<text>```,
    или фильтровать по категориям - параметр запроса - ```?category=<ID категории>```.

- 
    ```
    localhost/api/v1/products-search/suggest
    ```

    Позволяет искать продукт по совпадению начала текста в поле ```title``` - параметр запроса - ```?title__completion=<text>```.

При необходимости указать вместо ***localhost*** нужное имя хоста.

---
