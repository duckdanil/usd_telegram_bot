from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DB_CONNECTION, db_user, db_password, db_host, db_port, db_name

if DB_CONNECTION == "container":
    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
elif DB_CONNECTION == "local":
    engine = create_engine('sqlite:///usd_history.db')
else:
    raise ValueError("Invalid DB_CONNECTION value. Supported values are 'container' and 'local'")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class CurrencyHistory(Base):
    __tablename__ = 'currency_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(DateTime)
    currency_rate = Column(Float)

    def __init__(self, user_id, date, currency_rate):
        self.user_id = user_id
        self.date = date
        self.currency_rate = currency_rate


class Subscriber(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Base.metadata.create_all(engine)
