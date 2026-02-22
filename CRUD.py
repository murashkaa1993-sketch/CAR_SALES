

from datetime import date
from database import Session
from tables import Employee, Car, Sale


def add_employee(first_name, last_name, position, phone, email):
    session = Session() 
    new_employee = Employee(
        first_name=first_name,
        last_name=last_name,
        position=position,
        phone=phone,
        email=email
    )
    session.add(new_employee) 
    session.commit()
    session.close()
    print("Employee added successfully!")

def all_employees():
    session = Session()
    employees = session.query(Employee).all()
    if not employees:
        print("Employees not found")
        session.close()
        return

    for emp in employees:
            print(f"""
            ID: {emp.id}      
            First_name: {emp.first_name}
            Last_name: {emp.last_name} 
            Position: {emp.position} 
            Phone: {emp.phone} 
            Email: {emp.email}
            """)
    session.close()

def update_employee(emp_id, **kwargs):
    session = Session()
    emp = session.query(Employee).get(emp_id)
    if not emp:
        print("Employee not found")
        session.close()
        return

    for key, value in kwargs.items():
        setattr(emp, key, value)
        
    session.commit()
    print("Information updated")
    session.close()

def delete_employee(emp_id):
    session = Session()
    emp = session.query(Employee).get(emp_id)
    if emp:
        session.delete(emp)
        session.commit()
        print("Employee deleted")
    else:
        print("Employee not found")
    session.close()

def search_employee_ID(emp_ID):
    session = Session()
    search = session.query(Employee).filter(Employee.id == emp_ID).first() is not None
    session.close()
    return search


def add_car(manufacturer, model, year, cost_price, selling_price):
    session = Session() 
    new_car = Car(
        manufacturer=manufacturer,
        model = model,
        year = year,
        cost_price = cost_price,
        selling_price = selling_price
    )
    session.add(new_car)  
    session.commit() 
    session.close()
    print("Car added successfully!")

def all_cars():
    session = Session()
    cars = session.query(Car).all()
    if not cars:
        print("Cars not found")
        session.close()
        return

    for car in cars:
            print(f"""
            ID: {car.id}
            Manufacturer: {car.manufacturer} 
            Year: {car.year} 
            Model: {car.model} 
            Cost_price: {car.cost_price}
            Selling_price: {car.selling_price}
            Status: {car.status}
            """)
    session.close()

def update_car(car_id, **kwargs):
    session = Session()
    car = session.query(Car).get(car_id)
    if not car:
        print("Employee not found")
        session.close()
        return

    for key, value in kwargs.items():
        setattr(car, key, value)
        
    session.commit()
    print("Information updated")
    session.close() 

def delete_car(car_id):
    session = Session()
    car = session.query(Car).get(car_id)
    if car:
        session.delete(car)
        session.commit()
        print("Car Deleted")
    else:
        print("Car not found")
    session.close()

def search_car_ID(car_ID):
    session = Session()
    search = session.query(Car).filter(Car.id == car_ID).first() is not None
    session.close()
    return search

def add_sale(employee_id, car_id, sold_price):
    session = Session()
    employee = session.query(Employee).get(employee_id)
    if not employee:
        print("Employee not found")
        session.close()
        return
    car = session.query(Car).get(car_id)
    if not car:
        print("Car not found")
        session.close()
        return
    
    if car.status != "available":
        print("Car is already sold")
        session.close()
        return
    
    new_sale = Sale(
        employee_id = employee_id,
        car_id = car_id,
        sale_date = date.today(),
        sold_price = sold_price
    )
    session.add(new_sale)

    car.status = "sold"

    session.commit()
    print(f"Sale recorded. Profit: {sold_price - car.cost_price}")
    session.close()

