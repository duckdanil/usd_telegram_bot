# Телеграм Бот

**Используемые технологии**: aiogram, sqlalchemy, postgres

## Описание

Этот телеграм-бот разработан на Python и предоставляет возможность получать курс доллара. Бот имеет следующие команды:

- /start - запускает бота.
- /send_usd_rate - запрашивает текущий курс доллара.
- /subscribe - подписаться на получение курса доллара.
- /unsubscribe - отписаться от получения курса доллара.
- /history - просмотр истории запросов курса доллара.

## Переменные окружения

Для обоих способов запуска (локального и через Docker Compose), создайте файл .env в корневой папке проекта и заполните его следующими переменными окружения (по аналогии с файлом env-example):

BOT_TOKEN=ВАШ_ТОКЕН_БОТА<br>
POSTGRES_USER=postgres<br>
POSTGRES_PASSWORD=postgres<br>
POSTGRES_HOST=db<br>
POSTGRES_PORT=5432<br>
POSTGRES_DB=postgres


## Запуск локально

1. git clone https://github.com/duckdanil/usd_telegram_bot.git
2. pip install -r requirements.txt
3. Укажите DB_CONNECTION=local в файле «config.py» перед запуском бота локально.
4. python main.py
5. Бот будет запущен с использованием базы данных SQLite.

## Запуск с использованием Docker Compose

1. В файлах «config.py» установите DB_CONNECTION=container перед запуском бота в контейнере.
2. Создайте образ, используя Dockerfile, командой docker build -t mytelegrambot .
3. Запустите контейнеры с помощью Docker Compose командой docker-compose up -d.
4. Бот будет запущен в контейнере Docker, связанным с контейнером базы данных PostgreSQL.

В обоих случаях следите за настройками переменных окружения (например, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST и т. д.), чтобы они соответствовали вашей конфигурации базы данных.

Вы можете вносить свой вклад в проект и настраивать его под свои потребности!
