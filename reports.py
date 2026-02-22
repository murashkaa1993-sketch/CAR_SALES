from CRUD import *

def report_all_employee():
    session = Session()
    try:
        employees = session.query(Employee).all()

        result = []
        for emp in employees:
            result.append({
                "id": emp.id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "position": emp.position,
                "phone": emp.phone,
                "email": emp.email
            })
        return result
    
    except Exception as e:
        print(f"Error querying employees: {e}")
    finally:
        session.close()


def report_all_car():
    
    session = Session()
    try:
        cars = session.query(Car).all()

        result = []
        for car in cars:
            result.append({
                "id": car.id,
                "manufacturer": car.manufacturer,
                "model": car.model,
                "year": car.year,
                "cost_price": car.cost_price,
                "selling_price": car.selling_price,
                "status": car.status
            })
        return result

    except Exception as e:
        print(f"Error querying cars: {e}")
    finally:
        session.close()

def report_all_sales():
    session = Session()
    try:
        sales = session.query(Sale).all()

        result = []
        for sale in sales:
            result.append({
                "id": sale.id,
                "employee_id": sale.employee_id,
                "car_id": sale.car_id,
                "sale_date": sale.sale_date,
                "sold_price": sale.sold_price
            })
        return result

    except Exception as e:
        print(f"Error querying sales: {e}")
    finally:
        session.close()



def report_suma_all_sales():
    session = Session()
    try:
        sales = session.query(Sale).all()
        suma = sum(s.sold_price for s in sales)
        if suma == 0:
            print("No sales")
        else:
            return suma
    except Exception as e:
        print(f"Error calculating total sales: {e}")

    finally:
        session.close()


def report_suma_all_sales_for_data(target_data: date):
    session = Session()
    try:
        sales = session.query(Sale).all()
        suma = sum(s.sold_price for s in sales if target_data == s.sale_date)
        if suma == 0:
            print("No sales for this date")
        else:
            return suma
    except Exception as e:
        print(f"Error calculating total sales: {e}")

    finally:
        session.close()


def report_suma_all_sales_for_period(start_date: date, end_date: date):
    session = Session()
    try:
        sales = session.query(Sale).all()
        suma = sum(s.sold_price for s in sales if start_date <= s.sale_date <= end_date)
        if suma == 0:
            print("No sales for this date")
        else:
            return suma
    except Exception as e:
        print(f"Error calculating total sales: {e}")

    finally:
        session.close()

def report_suma_sale_for_each_emp():
    session = Session()
    try:
        sales = session.query(Sale).all()
        sales_each_emp = {}
        
        for sale in sales:
            emp_id = sale.employee_id
            if emp_id not in sales_each_emp:
                sales_each_emp[emp_id] = sale.sold_price
            else:
                sales_each_emp[emp_id] += sale.sold_price


        if not sales_each_emp:
            print("No sales")
        else:
            return sales_each_emp
    except Exception as e:
        print(f"Error calculating total sales: {e}")
    finally:
        session.close()

def report_suma_sale_one_employee(id_employee):
    session = Session()
    try:
        sales = session.query(Sale).all()
        total_sales = 0

        
        for sale in sales:
            emp_id = sale.employee_id
            if emp_id == id_employee:
                total_sales += sale.sold_price

        if total_sales == 0:
            print("No sales")
        else:
            return total_sales
    except Exception as e:
        print(f"Error calculating total sales: {e}")
    finally:
        session.close()


def report_better_auto_sale(start_date: date, end_date: date):
    session = Session()
    try:
        sales = session.query(Sale).all()
        if not sales:
            print("No sales!")
            return
        
        count_sale_each_auto = {}

        for sale in sales:
            if start_date <= sale.sale_date <= end_date:
                model = sale.car.model

                if model not in count_sale_each_auto:
                    count_sale_each_auto[model] = 1
                else:
                    count_sale_each_auto[model] += 1

        best_model = max(count_sale_each_auto, key=count_sale_each_auto.get)
        best_count = count_sale_each_auto[best_model]

        return best_model, best_count
    except Exception as e:
        print(f"Error calculating total sales: {e}")
    finally:
        session.close()



def report_best_employee(start_date: date, end_date: date):
    session = Session()
    try:
        sales = session.query(Sale).all()
        if not sales:
            print("No sales")
            return
        sales_each_emp = {}
        
        for sale in sales:
            if start_date <= sale.sale_date <= end_date:
                emp_id = f"{sale.employee.first_name} {sale.employee.last_name}"
                if emp_id not in sales_each_emp:
                    sales_each_emp[emp_id] = sale.sold_price
                else:
                    sales_each_emp[emp_id] += sale.sold_price

        best_employee = max(sales_each_emp, key=sales_each_emp.get)
        best_sale = sales_each_emp[best_employee]
        return best_employee, best_sale
    except Exception as e:
        print(f"Error calculating total sales: {e}")
    finally:
        session.close()


def report_total_profit():
    session = Session()
    try:
        sales = session.query(Sale).all()
        suma_sp = sum(s.sold_price for s in sales)
        if suma_sp == 0:
            print("No sales")
            return
        total_profit = 0

        for sale in sales:
            cost_price = sale.car.cost_price
            sold_price = sale.sold_price
            total_profit += (sold_price - cost_price)
        return total_profit
    except Exception as e:
        print(f"Error calculating total sales: {e}")

    finally:
        session.close()