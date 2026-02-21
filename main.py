

from CRUD import *
def get_choice(value, min_val, max_val, count =3):
    while count > 0:
        print(f"You have {count} attempts to enter correct choice")
        choice = get_int(value)
        if min_val <= choice <=max_val:
            return choice
        count -= 1
        print(f"Please enter the number between {min_val}-{max_val}")
            
    print ("Too many wrong attempts. Returning back")
    return None

def get_ID(search_func, name, count = 3):
    while count > 0:
        print(f"You have {count} attempts to enter correct ID")
        id_choice = get_int("Enter  ID or press 0 to return back ")
        if id_choice == 0:
            break

        if search_func(id_choice):
            return id_choice
        
        count-=1
        print(f"{name} with this ID not found")

    print ("Too many wrong attempts. Returning back")        
    return None
def print_info_car():
    print(""""Sort by:
                1.manufacturer - press 1.
                2.model -  press 2.
                3.year - press 3.
                4.cost_price - press 4.
                5.selling_price - press 5.
                6.status - press 6.
                0.return to back - press 0
                """)
def no_empty(value):
    while True:
        new_value = input(value).strip()
        if not new_value:
            print("This field cannot be empty. Please enter the model car.")
        else:
            return new_value
        
def no_empty_str(value):
    while True:
        new_value = input(value).strip()
        if any(i.isdigit() for i in new_value) or len(new_value) == 0:
            print("Enter the correct first_name/ last_name/ position. They should not contain numbers and should not be blank.")
        else:
            return new_value
    
def get_email(mail):
    while True:
        check_mail = input(mail)
        if len(check_mail) != 0 and check_mail.count("@") == 1 and  check_mail[0] != "@"  and check_mail[-1] != "@":
           return check_mail
        else:
            print("Please enter a valid email address. It must contain only one @ character.")

def get_phone(num):
    while True:
        
        phone = input(num)
        if len(phone) == 10 and phone.isdigit():
            return phone 
        else:
            print("Phone number must have 10 digits")

def get_int(value):
    while True:
        
        try:
            return int(input(value))
        except:
            print("Please enter a number.")

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
            last_name = no_empty_str("Enter the last name: ")
            position = no_empty_str("Enter the position: ")
            phone = get_phone("enter the phone number: ")
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
    5. Sort asc
    6. Sort desc
    0. Back
    """)
        choice = get_choice("Make yuor choice: ", 0, 6)
        if choice is None:
            break
        

        if choice == 0:
            break
        elif choice == 1:
            manufacturer = no_empty_str("Enter the manufacturer: ")
            model = no_empty("Enter the model: ")
            year = get_int("Enter the year: ")
            cost_price = get_int("Enter the cost_price: ")
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
        
        elif choice == 5:
            choice_list = ["manufacturer", "model", "year", "cost_price", "selling_price", "status"]
            print_info_car()
            colums_sorted = get_choice("Enter your choice: ",0, 6)
            if colums_sorted is None or colums_sorted == 0:
                break
                
            cars_sorted(choice_list[colums_sorted-1])
                    
        elif choice == 6:
            choice_list = ["manufacturer", "model", "year", "cost_price", "selling_price", "status"]
            print_info_car()
            colums_sorted = get_choice("Enter your choice: ",0, 6)
            if colums_sorted is None or colums_sorted == 0:
                break
                
            cars_sorted_desc(choice_list[colums_sorted-1])


def menu_sale():
    print("===== NEW SALE =====")
    while True:
        id_empl = get_ID(search_employee_ID, "Employee")
        id_car = get_ID(search_car_ID, "Car")
        soldprice = get_int("Enter sold price: ")

        if id_empl and id_car:

            add_sale(id_empl, id_car, soldprice)
            print("Sale successfully")
        
        choise = get_choice("""Would you like to make another sale?
                         1. Yes - press 1.
                         2. No  - press 2.""",1 ,2)
        if choise is None or choise == 2:
            break
        elif choise == 1:
            continue


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
        choice = get_int("Make yuor choice: ")
        if choice == 1:
            employee_total_sales()

        elif choice == 2:
            id_empl = get_int("Enter employee id")
            employee_profit(id_empl)

        elif choice == 0:
            break






if __name__ == "__main__":
    main_menu()
