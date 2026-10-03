import os
import datetime
from setup import employee_path, enquiry_path, suggestion_path


def employee_login():
    attempts = 0
    while attempts < 3:
        print("\n───── Employee Login ─────")
        email    = input("Email    : ").strip()
        password = input("Password : ").strip()
        if os.path.exists(employee_path):
            with open(employee_path, "r") as file:
                for line in file:
                    data = [x.strip() for x in line.strip().split("|")]
                    if len(data) < 8:
                        continue
                    # Fields: id|name|designation|age|address|salary|email|password
                    if email == data[6] and password == data[7]:
                        print(f"\nWelcome, {data[1]}!")
                        employee_menu(data)
                        return
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Invalid details. {remaining} attempt(s) remaining.")
        else:
            print("Too many failed attempts. System is now terminating.")
            exit()


def employee_menu(emp):
    while True:
        print("─"*35)
        print(" "*6, "─"*5, "Employee Menu", "─"*5)
        print("─"*35)
        print("1. My Profile")
        print("2. Reset Password")
        print("3. Submit Enquiry")
        print("4. Give Suggestion")
        print("5. Logout")
        print("─"*35)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            employee_profile(emp)
        elif choice == "2":
            reset_employee_password(emp)
        elif choice == "3":
            submit_enquiry(emp)
        elif choice == "4":
            give_suggestion(emp)
        elif choice == "5":
            print("Logging out...")
            return
        else:
            print("  Invalid choice. Please choose from 1-5.")


def employee_profile(emp):
    while True:
        with open(employee_path, "r") as file:
            for line in file:
                data = [x.strip() for x in line.strip().split("|")]
                if len(data) >= 8 and data[0] == emp[0]:
                    emp = data
                    break
        print("\n───── My Profile ─────")
        print(f"ID          : {emp[0]}")
        print(f"Name        : {emp[1]}")
        print(f"Designation : {emp[2]}")
        print(f"Age         : {emp[3]}")
        print(f"Address     : {emp[4]}")
        print(f"Salary      : {emp[5]}")
        print(f"Email       : {emp[6]}")
        print("Password    : ********")
        print("\n1. Edit Profile")
        print("2. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            emp = edit_employee_profile(emp)
        elif choice == "2":
            break
        else:
            print("Invalid choice.")


def edit_employee_profile(emp):
    print("\n───── Edit Profile ─────")
    print("  (Press Enter to keep current value)")
    while True:
        new_name = input(f"Name [{emp[1]}]: ").strip()
        if new_name == "" or validate_name(new_name):
            break
    while True:
        new_age = input(f"Age [{emp[3]}]: ").strip()
        if new_age == "" or validate_age(new_age):
            break
    while True:
        new_address = input(f"Address [{emp[4]}]: ").strip()
        if new_address == "" or validate_address(new_address):
            break
    while True:
        new_email = input(f"Email [{emp[6]}]: ").strip()
        if new_email == "" or (validate_email(new_email) and validate_email_unique(new_email, emp[0])):
            break
    if new_name:    emp[1] = new_name
    if new_age:     emp[3] = new_age
    if new_address: emp[4] = new_address
    if new_email:   emp[6] = new_email
    update_employee_record(emp)
    print("  Profile updated successfully!")
    return emp


def update_employee_record(emp):
    with open(employee_path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    with open(employee_path, "w") as file:
        for i, line in enumerate(lines):
            data = [x.strip() for x in line.split("|")]
            if data[0] == emp[0]:
                file.write("|".join(emp))
            else:
                file.write(line)
            if i < len(lines) - 1:
                file.write("\n")


def reset_employee_password(emp):
    print("\n───── Reset Password ─────")
    old_pw = input("Current password  : ").strip()
    if old_pw != emp[7]:
        print("Incorrect current password.")
        return
    while True:
        new_pw = input("New password      : ").strip()
        if validate_password(new_pw):
            break
    confirm = input("Confirm password  : ").strip()
    if new_pw != confirm:
        print("Passwords do not match.")
        return
    emp[7] = new_pw
    update_employee_record(emp)
    print("Password reset successfully!")


def submit_enquiry(emp):
    print("\n───── Submit Enquiry ─────")
    message = input("Enter your enquiry : ").strip()
    if message == "":
        print("Enquiry cannot be empty.")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    record = f"{timestamp}|{emp[0]}|{emp[1]}|{message}"
    with open(enquiry_path, "a") as file:
        if os.path.exists(enquiry_path) and os.path.getsize(enquiry_path) > 0:
            file.write("\n" + record)
        else:
            file.write(record)
    print("Enquiry submitted successfully!")


def give_suggestion(emp):
    print("\n───── Give Suggestion ─────")
    message = input("Enter your suggestion : ").strip()
    if message == "":
        print("Suggestion cannot be empty.")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    record = f"{timestamp}|{emp[0]}|{emp[1]}|{message}"
    with open(suggestion_path, "a") as file:
        if os.path.exists(suggestion_path) and os.path.getsize(suggestion_path) > 0:
            file.write("\n" + record)
        else:
            file.write(record)
    print("Suggestion submitted successfully!")


def generate_id(path, prefix):
    if not os.path.exists(path):
        return prefix + "1"
    with open(path, "r") as file:
        lines = [l for l in file.readlines() if l.strip()]
    if not lines:
        return prefix + "1"
    last_line = lines[-1].strip().split("|")
    last_id   = last_line[0]
    try:
        number = int(last_id[len(prefix):]) + 1
    except ValueError:
        number = 1
    return prefix + str(number)


def validate_name(name):
    if name == "":
        print("Name cannot be empty.")
        return False
    if not name.replace(" ", "").isalpha():
        print("Name must contain letters only.")
        return False
    return True


def validate_age(age):
    if age == "":
        print("Age cannot be empty.")
        return False
    if not age.isdigit():
        print("Age must be a number.")
        return False
    if int(age) < 18 or int(age) > 65:
        print("Age must be between 18 and 65.")
        return False
    return True


def validate_address(address):
    if address == "":
        print("Address cannot be empty.")
        return False
    return True


def validate_email(email):
    if email == "":
        print("Email cannot be empty.")
        return False
    if "@" not in email:
        print("Invalid email. Must contain @.")
        return False
    if "." not in email.split("@")[-1]:
        print("Invalid email. Must contain domain like .com")
        return False
    return True


def validate_email_unique(email, current_id):
    if not os.path.exists(employee_path):
        return True
    with open(employee_path, "r") as file:
        for line in file:
            data = [x.strip() for x in line.strip().split("|")]
            if len(data) >= 7 and data[0] != current_id and data[6].lower() == email.lower():
                print("Email already registered.")
                return False
    return True


def validate_password(password):
    if password == "":
        print("Password cannot be empty.")
        return False
    if len(password) < 4:
        print("Password must be at least 4 characters.")
        return False
    return True
