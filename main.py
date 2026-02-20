

from CRUD import *

def main_menu():

    while True:
        print("""
-0--0---0__CAR_SALES__0---0--0-
              
          1. Employee
          2. Cars 
          3. Sales
          4. Reports
          0. EXit
""")    
        choice = int(input("Make yuor choice: "))

        if choice == 1:
            menu_employee()
        if choice == 2:
            menu_cars()
        if choice == 3:
            menu_sale()
        if choice == 4:
            menu_reports()
        if choice == 0:
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
        choice = int(input("Make yuor choice: "))
        if choice == 1:
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            position = input("Enter the position: ")
            phone = input("enter the phone number: ")
            email = input("Enter the email: ")
            add_employee(first_name, last_name, position, phone, email)
                
        if choice == 2:
            print(all_employees())
                
        if choice == 3:
            choice_up = input("What do you want to update(please enter one of the options below\n ): "
            "first_name/ last_name/ position/ phone/ email\n")
            id_empl = int(input("Enter employee id"))
            new_value = input("Enter new value")
            update_employee(id_empl, **{choice_up: new_value})

        if choice == 4:
            id_empl = int(input("Enter employee id"))
            delete_employee(id_empl)
                
        if choice == 0:
            break
        
        
def menu_cars():
    while True:
        print("""
    ======= CARS =======
    1. Add car
    2. Show all
    3. Update
    4. Delete
    5. Sort asc
    6. Sort desc
    0. Back
    """)
        choice = int(input("Make yuor choice: "))
        if choice == 1:
            manufacturer = input("Enter the manufacturer: ")
            model = input("Enter the model: ")
            year = int(input("Enter the year: "))
            cost_price = float(input("Enter the cost_price: "))
            selling_price = float(input("Enter the selling_price: "))
            add_car(manufacturer, model, year, cost_price, selling_price)
                
        if choice == 2:
            all_cars()

        if choice == 3:
            id_car = int(input("Enter ID: "))
            choice_up = input("What do you want to update(please enter one of the options below\n ): "
            "manufacturer/ model/ year/ cost_price/ selling_price\n")
            new_value = input("Enter new value")

            update_car(id_car, **{choice_up : new_value})

        if choice == 4:
            id_car = int(input("Enter ID: "))
            delete_car(id_car)

        if choice == 5:

            colums_sorted = input("Enter your choice: ")
            cars_sorted(colums_sorted)

        if choice == 6:
            colums_sorted = input("Enter your choice: ")
            cars_sorted_desc(colums_sorted)

        if choice == 0:
            break


def menu_sale():
    print("===== NEW SALE =====")
    id_empl = int(input("Enter employee ID: "))
    id_car = int(input("Enter car ID: "))
    soldprice = int(input("Enter sold price: "))

    add_sale(id_empl, id_car, soldprice)

def menu_reports():
    while True:
        print("""
======= REPORTS ======
1. Totat sale for each employee
2. Profit per ymployee
.
.
.
0. Back
""")
        choice = int(input("Make yuor choice: "))
        if choice == 1:
            employee_total_sales()

        if choice == 2:
            id_empl = int(input("Enter employee id"))
            employee_profit(id_empl)

        if choice == 0:
            break






if __name__ == "__main__":
    main_menu()
