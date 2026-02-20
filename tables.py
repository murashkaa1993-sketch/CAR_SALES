#Облік продажу автомобілів в автосалоні. Основне завдання:
# обліковувати процес продажу авто, фіксувати співробітника, який здійснив операцію, рахувати прибуток






from database import Base, engine


from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    phone = Column(String)
    email = Column(String)

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer = Column(String)
    model = Column(String)
    year = Column(Integer)
    cost_price = Column(Float)
    selling_price = Column(Float)
    status = Column(String, default="available")



class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    sale_date = Column(Date)
    sold_price = Column(Float)

    employee = relationship("Employee")
    car = relationship("Car")


# print("CREATING TABLES...")
# Base.metadata.create_all(engine)
# print("DONE")


# from sqlalchemy import inspect

# insp = inspect(engine)
# print("Tables in DB:", insp.get_table_names())






# class Company():
#     def __init__(self):
#         self.employees = []

#     def add_employee(self, name, position, phone, email):
#         new_employee = Employee(name, position, phone, email)
#         self.employees.append(new_employee)

#     def change_info_employee(self):
#         choice_name = input("Enter employyee name: ").lower()
#         found = False

#         for emp in self.employees:
#             if emp.name.lower() == choice_name:
#                 found = True
#                 choice = int(input("What do you want to change: " \
#                 "1. Name - press 1" \
#                 "2. Position - pres 2" \
#                 "3. Phone- press 3" \
#                 "4. Email - press 4"))
#                 if choice == 1:
#                     new_name = input("Update information: ")
#                     emp.name = new_name
#                 elif choice == 2:
#                     new_position = input("Update information: ")
#                     emp.position = new_position
#                 elif choice == 3:
#                     new_phone = input("Update information: ")
#                     emp.phone = new_phone
#                 elif choice == 4:
#                     new_email = input("Update information: ")
#                     emp.email = new_email
#                 else:
#                     print("Input error.")
#                 break
#         if found == False:
#             print("Employee with this name not found")

#     def del_employee(self):
#         name_employee = input("Enter the name of the employee you want to remove: ").lower()
#         found = False
#         for emp in self.employees:
#             if emp.name.lower() == name_employee:
#                 self.employees.remove(emp)
#                 found = True
#                 print("Employee deleted.")
#                 break
#         if found == False:
#             print("Employee with this name not found") 

#     def show_info(self):
#         for emp in self.employees:
#             print(f"""
#             ПІБ: {emp.name} 
#             Посада: {emp.position} 
#             Номер телефону: {emp.phone} 
#             Електронна адреса: {emp.email}
#             """)

#         if not self.employees:
#             print("No employees in company")
#             return




# class ListCar():
#     def __init__(self):
#         self.list_cars = []

#     def add_car(self, manufacturer, year, model, cost_price, selling_price, status):
#         new_car = InfoCar(manufacturer, year, model, cost_price, selling_price, status)
#         self.list_cars.append(new_car)

#     def change_info_cars(self):
#         choice_brand = input("Enter the car brand: ").lower()
#         choice_year = int(input("Enter the car year: "))
#         choice_manufacturer = input("enter the car manufacturer: ").lower()
#         found = False

#         for car in self.list_cars:
#             if car.manufacturer.lower() == choice_manufacturer and car.year == choice_year and car.model.lower() == choice_brand:
#                 found = True
#                 choice = int(input("What do you want to change: \n" \
#                 "1. Manufacturer - press 1\n" \
#                 "2. Year - pres 2\n" \
#                 "3. Model- press 3\n" \
#                 "4. Cost_prise - press 4\n"\
#                 "5. Selling_price - press 5\n"\
#                 "6. Status - press 6\n"))
#                 if choice == 1:
#                     new_manufacturer = input("Update information: ")
#                     car.manufacturer = new_manufacturer
#                 elif choice == 2:
#                     new_year = int(input("Update information: "))
#                     car.year = new_year
#                 elif choice == 3:
#                     new_model = input("Update information: ")
#                     car.model = new_model
#                 elif choice == 4:
#                     new_cost_price = float(input("Update information: "))
#                     car.cost_price = new_cost_price
#                 elif choice == 5:
#                     new_selling_price = float(input("Update information: "))
#                     car.selling_price = new_selling_price
#                 elif choice == 6:
#                     new_status = input("Update information: ")
#                     car.status = new_status
#                 else:
#                     print("Input error.")
#                 break
#         if found == False:
#             print("Car with this data not found")

#     def show_info(self):
#         if not self.list_cars:
#             print("No cars in company")
#             return

#         for car in self.list_cars:
#             print(f"""
#             Manufacturer: {car.manufacturer} 
#             Year: {car.year} 
#             Model: {car.model} 
#             Cost_price: {car.cost_price}
#             Selling_price: {car.selling_price}
#             Status: {car.status}
#             """)
