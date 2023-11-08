# Телеграм Бот

**Используемые технологии**: aiogram, sqlalchemy, postgres

## Описание

Этот телеграм-бот разработан на Python и предоставляет возможность получать курс доллара. Бот имеет следующие команды:

- /start - запускает бота.
- /send_usd_rate - запрашивает текущий курс доллара.
- /subscribe - подписаться на получение курса доллара.
- /unsubscribe - отписаться от получения курса доллара.
- /history - просмотр истории запросов курса доллара.

**Примечание**: При подписке на получение курса доллара, бот будет присылать уведомление каждые 10 секунд (это значение можно настроить в файле config.py, переменная SCHEDULER_INTERVAL_SECONDS).

## Переменные окружения

Для обоих способов запуска (локального и через Docker Compose), создайте файл .env в корневой папке проекта и заполните его следующими переменными окружения:

BOT_TOKEN=ВАШ_ТОКЕН_БОТА
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres

## Запустить проект

**Локальный запуск**:

git clone https://github.com/your-repository.git
pip install -r requirements.txt
python main.py

**Запуск с использованием Docker Compose**:

docker build -t mytelegrambot .
docker-compose up -d
