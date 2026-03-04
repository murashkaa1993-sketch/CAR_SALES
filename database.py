



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError
import os

#Шлях до бази даних
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("Please check your .env file: missing BD connection parameters!")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# створення обєкту який відповідає за зєднання з БД
engine = create_engine(DATABASE_URL)

# Створення сесій до БД(через неї ми робимо зміни в БД)
Session = sessionmaker(bind=engine)

# Базовий клас для створення таблиць
Base = declarative_base()

#Перевірка підключення до БД
def check_connection():
    try:
        conn = engine.connect()
        conn.close()
        print("Database connected successfully!")
    except OperationalError as e:
        print(f"Cannot connect to database: {e}")
        print("Make sure the database exists and your .env file is correct.")
        exit(3)

def create_tables():
    from tables import Employee, Car, Sale
    Base.metadata.create_all(bind=engine)
    print(" Database tables are ready!")
