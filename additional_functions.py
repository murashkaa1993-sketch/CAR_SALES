from datetime import datetime
import json
from pathlib import Path


def input_date(prompt, count = 3):
    while count > 0:
        print(f"You have {count} attempts to enter correct choice")
        date_str = input(prompt)
        try:
            valid_date = datetime.strptime(date_str, "%d-%m-%Y").date()
            return valid_date
        except ValueError:
            count-=1
            print("Invalid date format. Please enter in dd-mm-yyyy format.")

def save_yes_or_no(name_file, resault):
    save = get_choice("""\n Do you want to save the data to a file? \n" \
                "1. Yes - press 1\n" \
                "2. No - press 2 """, 1, 2)
    if save == 1:
        write_report(name_file, resault)
        print(f"Report saved to {name_file}")
        return True
    elif save == 2:
        print("Report not saved.")

def write_report(value, result):
    # Шлях до папки з проектом
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / value

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4,ensure_ascii=False)

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
        id_choice = get_int(f"Enter  ID {name} or press 0 to return back ")
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
def no_empty(value, count = 3):
    while count > 0:
        new_value = input(value).strip()
        if not new_value:
            count -= 1
            print("This field cannot be empty. Please enter the model car.")
        else:
            return new_value
    print ("Too many wrong attempts. Returning back")
        
def no_empty_str(value, count = 3):
    while count > 0:
        print(f"You have {count} attempts to enter correct information")
        new_value = input(value).strip()
        if any(i.isdigit() for i in new_value) or len(new_value) == 0:
            count -=1
            print("Enter the correct first_name/ last_name/ position. They should not contain numbers and should not be blank.")
        else:
            return new_value
    print ("Too many wrong attempts. Returning back") 
    
def get_email(mail, count = 3):
    while count > 0:
        print(f"You have {count} attempts to enter correct information")
        check_mail = input(mail)
        if len(check_mail) != 0 and check_mail.count("@") == 1 and  check_mail[0] != "@"  and check_mail[-1] != "@":
           return check_mail
        else:
            count -= 1
            print("Please enter a valid email address. It must contain only one @ character.")
    print ("Too many wrong attempts. Returning back") 

def get_phone(num, count = 3):
    while count > 0:
        print(f"You have {count} attempts to enter correct information")
        phone = input(num)
        if len(phone) == 10 and phone.isdigit():
            return phone 
        else:
            count -= 1
            print("Phone number must have 10 digits")
    print ("Too many wrong attempts. Returning back") 

def get_int(value, count = 3):

    while count > 0:
        try:
            return int(input(value))
        except:
            count -= 1
            print("Please enter a number.")
