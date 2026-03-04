
# Описуємл таблиці Employee, Car, Sale

from database import Base
# Імпорт необхідних компонентів для роботи з таблицями
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
# імпортуємо relationship для того щоб таблиці могли взаємодіяти між собою
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    phone = Column(String)
    email = Column(String)

class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer = Column(String)
    model = Column(String)
    year = Column(Integer)
    cost_price = Column(Float)
    selling_price = Column(Float)
    # Вказуємо значення за замовчуванням available
    status = Column(String, default="available")



class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    car_id = Column(Integer, ForeignKey("car.id"))
    sale_date = Column(Date)
    sold_price = Column(Float)

    # Підключаємо таблиці (Car and Employee) для взаємодії між ними
    employee = relationship("Employee")
    car = relationship("Car")
