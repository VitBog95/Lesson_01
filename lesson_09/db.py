from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql+psycopg2://postgres:7284.Vitales.@localhost:5432/QA"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def get_session():
    """Возвращает новую сессию для работы с БД."""
    return Session()
