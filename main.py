

from CRUD import *
from reports import *
from additional_functions import *
def main_menu():

    while True:
        print("""
-0--0---0__CAR_SALES__0---0--0-
              
          1. Employee
          2. Cars 
          3. Sales
          4. Reports
          0. Exit
""")    
        choice = get_choice("Make yuor choice:", 0, 4)
        if choice is None:
            break

        if choice == 1:
            menu_employee()
        elif choice == 2:
            menu_cars()
        elif choice == 3:
            menu_sale()
        elif choice == 4:
            menu_reports()
        elif choice == 0:
            break

def menu_employee():
    
    while True:
        print("""
    ====== EMPLOYEE =====

    1. Add employee
    2. Show all
    3. Update
    4. Delete
    0. Back

    """)
        choice = get_choice("Make yuor choice:", 0, 4)
        if choice is None:
            break
        
        if choice == 1:
            first_name = no_empty_str("Enter the first name: ")
            if first_name:
                last_name = no_empty_str("Enter the last name: ")
                if last_name:
                    position = no_empty_str("Enter the position: ")
                    if position:    
                        phone = get_phone("enter the phone number: ")
                        if phone:
                            email = get_email("Enter the email: ")
                            add_employee(first_name, last_name, position, phone, email)
                        
        elif choice == 2:
            all_employees()
                        
        elif choice == 3:
                id_empl = get_ID(search_employee_ID, "Employee")
                
                if id_empl:

                    choice_list = ["first_name", "last_name", "position", "phone", "email"]
                    choice_up = get_choice("""What do you want to update(please enter one of the options below
                        1.first_name - press 1.
                        2.last_name - press 2.
                        3.position - press 3.
                        4.phone - press 4.
                        5.email - press 5.
                        6. To return back - pres 6.
                        """, 1, 6)
                    if choice_up is None:
                        break
                    if choice_up == 6:
                        break
                    elif 0 < choice_up < 6:
                        if choice_up == 4:
                            new_value = get_phone("Enter new value")
                        elif choice_up == 5:
                            new_value = get_email("Enter new value")
                        else: 
                            new_value = no_empty_str("Enter new value")

                        update_employee(id_empl, **{choice_list[choice_up-1]: new_value})
                        print("Updated successfully")
                        break

        elif choice == 4:
            id_empl = get_ID(search_employee_ID, "Employee")
            if id_empl:
                delete_employee(id_empl)
                print("Employee deleted successfully") 
        elif choice == 0:
            break
               
def menu_cars():
    while True:
        print("""
    ======= CARS =======
    1. Add car
    2. Show all
    3. Update
    4. Delete
    0. Back
    """)
        choice = get_choice("Make yuor choice: ", 0, 4)
        if choice is None:
            break
        

        if choice == 0:
            break
        elif choice == 1:
            manufacturer = no_empty_str("Enter the manufacturer: ")
            if manufacturer: 
                model = no_empty("Enter the model: ")
                if model:    
                    year = get_int("Enter the year: ")
                    if year:
                        cost_price = get_int("Enter the cost_price: ")
                        if cost_price:
                            selling_price = get_int("Enter the selling_price: ")
                            add_car(manufacturer, model, year, cost_price, selling_price)
                
        elif choice == 2:
            all_cars()
        elif choice == 3:
                id_car = get_ID(search_car_ID, "Car")
                if id_car:
                    choice_list = ["manufacturer", "model", "year", "cost_price", "selling_price"]
                    choice_up = get_choice("""What do you want to update(please enter one of the options below
                        1.manufacturer - press 1.
                        2.model -  press 2.
                        3.year - press 3.
                        4.cost_price - press 4.
                        5.selling_price - press 5.
                        6. To return back - pres 6.
                        """, 1, 6)
                    if choice_up is None or choice_up == 6:
                        break
                    if choice_up == 1:
                        new_value = no_empty_str("Enter new value")
                    elif choice_up == 2:
                        new_value = no_empty("Enter new value")
                    elif choice_up in (3,4,5):
                        new_value = get_int("Enter new value")

                    update_car(id_car, **{choice_list[choice_up-1] : new_value})
                    print("Updated successfully")
                        
        elif choice == 4:
            id_car = get_ID(search_car_ID, "Car")
            if id_car:
                delete_car(id_car)
                print("Car deleted successfully") 

def menu_sale():
    print("===== NEW SALE =====")
    while True:
        id_empl = get_ID(search_employee_ID, "Employee")
        if id_empl:
            id_car = get_ID(search_car_ID, "Car")
            if id_car:
                soldprice = get_int("Enter sold price: ")
                add_sale(id_empl, id_car, soldprice)
                print("Sale successfully")
        
                choise = get_choice("""Would you like to make another sale?
                                1. Yes - press 1.
                                2. No  - press 2.""",1 ,2)
                if choise is None or choise == 2:
                    break
                elif choise == 1:
                    continue
        break

def menu_reports():
    while True:
        print("""
======= REPORTS ======
1. All Employee
2. All Car
3. All Sales
4. Amount all sales
5. Amount all sales for day
6. Amount all sales for period
7. Amount sales for each employees
8. Amount sales one employee
9. Best auto sale for period
10. Best Employee for period
11. Amount total profit
0. Back
""")
        choice = get_choice("Make yuor choice: ", 0, 11)
        if choice is None or choice == 0:
            break

        if choice == 1:
            result = report_all_employee()
            if result:
                for i in result:
                    print(i)
                save_yes_or_no("info_employee.json", result)

        elif choice == 2:
            result = report_all_car()
            if result:
                for i in result:
                    print(i)
                save_yes_or_no("info_cars.json", result)

        elif choice == 3:
            result = report_all_sales()
            if result:
                for i in result:
                    print(i)
        
                save_yes_or_no("info_sales.json", result)

        elif choice == 4:
            result = report_suma_all_sales()
            if result:
                print(f"Amound Sales = {result}")
            
                save_yes_or_no("All_suma_sales.json", {"Amound sales" : result})

        elif choice == 5:
            target_date = input_date("Enter the date: day-month-year " )
            result = report_suma_all_sales_for_data(target_date)
            if result:
                print(f"Total sale for {target_date} = {result}")
        
                save_yes_or_no("Suma_sales_for_day.json", {"Total" :result})

        elif choice == 6:
            start_date = input_date("Enter the start date (dd-mm-yyyy): ")
            end_date = input_date("Enter the end date (dd-mm-yyyy): ")
            result = report_suma_all_sales_for_period(start_date, end_date)
            
            if result:
                print(f"Total sales for periof {start_date} - {end_date} = {result}")
        
                save_yes_or_no("Suma_sales_for_period.json", {"Total" :result})

        elif choice == 7:
            result = report_suma_sale_for_each_emp()
            if result:
                for i in result:
                    print(i)
        
                save_yes_or_no("sale_each_employee.json", result)

        elif choice == 8:
            emp_ID = int(input("Enter employee ID: "))
            result = report_suma_sale_one_employee(emp_ID)

            if result:
                print(f"Total sale employee ID:{emp_ID} = {result}")
        
                save_yes_or_no("sale_one_employee.json", {emp_ID :result})

        elif choice == 9:
            start_date = input_date("Enter the start date (dd-mm-yyyy): ")
            end_date = input_date("Enter the end date (dd-mm-yyyy): ")
            result = report_better_auto_sale(start_date, end_date)

            if result:
                print(f"Best selling model: {result[0]}")
                print(f"Total sales: {result[1]}")
        
                save_yes_or_no("best_car_sale.json",{
                "Model" : result[0],
                "Total sale" : result[1]})

        elif choice == 10:
            start_date = input_date("Enter the start date (dd-mm-yyyy): ")
            end_date = input_date("Enter the end date (dd-mm-yyyy): ")
            result = report_best_employee(start_date, end_date)

            if result:
                print(f"Best selling model: {result[0]}")
                print(f"Total sales: {result[1]}")
        
                save_yes_or_no("best_employee_sale.json",{
                "Employee" : result[0],
                "Total sale" : result[1]})
        elif choice == 11:
            result = report_total_profit()
            if result:
                print(f"Total profit: {result}")
        
                save_yes_or_no("Total_profit.json",{
                "Total profit" : result})








if __name__ == "__main__":
    main_menu()
