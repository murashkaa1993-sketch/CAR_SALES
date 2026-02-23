



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Шлях до бази даних
DATABASE_URL = "postgresql+psycopg2://postgres:20011993@localhost:5432/CarSalesAccounting"

# створення обєкту який відповідає за зєднання з БД
engine = create_engine(DATABASE_URL)
# Створення сесій до БД(через неї ми робимо зміни в БД)
Session = sessionmaker(bind=engine)

# Базовий клас для створення таблиць
Base = declarative_base()