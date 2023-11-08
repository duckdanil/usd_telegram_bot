import os

from dotenv import load_dotenv

load_dotenv()


DB_CONNECTION = "local"
SCHEDULER_INTERVAL_SECONDS = 10

BOT_TOKEN = os.getenv("BOT_TOKEN")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")
