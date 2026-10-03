import os
from setup import manager_path, employee_path, enquiry_path, suggestion_path


def manager_login():
    attempts = 0
    while attempts < 3:
        print("\n───── Manager Login ─────")
        email    = input("  Email    : ").strip()
        password = input("  Password : ").strip()
        if os.path.exists(manager_path):
            with open(manager_path, "r") as file:
                for line in file:
                    data = [x.strip() for x in line.strip().split("|")]
                    if len(data) < 7:
                        continue
                    if email == data[5] and password == data[6]:
                        print(f"\n  Welcome, {data[1]}!")
                        manager_menu(data)
                        return
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"  Invalid details. {remaining} attempt(s) remaining.")
        else:
            print("  Too many failed attempts. System is now terminating.")
            exit()


def manager_menu(mgr):
    while True:
        print("\n" + "─"*30)
        print("─"*7, "Manager Menu", "─"*7)
        print("─"*30)
        print("1. My Profile")
        print("2. Add Employee")
        print("3. View Employees")
        print("4. Search Employee")
        print("5. Delete Employee")
        print("6. View Enquiries & Suggestions")
        print("7. Logout")
        print("─"*30)
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            manager_profile(mgr)
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_file(employee_path)
        elif choice == "4":
            search_file(employee_path)
        elif choice == "5":
            delete_record(employee_path)
        elif choice == "6":
            view_enquiries_suggestions()
        elif choice == "7":
            print("  Logging out...")
            return
        else:
            print("  Invalid choice. Please choose from 1-7.")


def manager_profile(mgr):
    while True:
        with open(manager_path, "r") as file:
            for line in file:
                data = [x.strip() for x in line.strip().split("|")]
                if len(data) >= 7 and data[0] == mgr[0]:
                    mgr = data
                    break
        print("\n───── My Profile ─────")
        print(f"ID          : {mgr[0]}")
        print(f"Name        : {mgr[1]}")
        print(f"Designation : {mgr[2]}")
        print(f"Address     : {mgr[3]}")
        print(f"Salary      : {mgr[4]}")
        print(f"Email       : {mgr[5]}")
        print("Password    : ********")
        print("\n1. Edit Profile")
        print("2. Reset Password")
        print("3. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            mgr = edit_manager_profile(mgr)
        elif choice == "2":
            reset_manager_password(mgr)
        elif choice == "3":
            break
        else:
            print("  Invalid choice.")


def edit_manager_profile(mgr):
    print("\n───── Edit Profile ─────")
    print("(Press Enter to keep current value)")
    while True:
        new_name = input(f"Name [{mgr[1]}]: ").strip()
        if new_name == "" or validate_name(new_name): break
    while True:
        new_address = input(f"Address [{mgr[3]}]: ").strip()
        if new_address == "" or validate_address(new_address): break
    while True:
        new_salary = input(f"Salary [{mgr[4]}]: ").strip()
        if new_salary == "" or validate_salary(new_salary): break
    while True:
        new_email = input(f"Email [{mgr[5]}]: ").strip()
        if new_email == "" or validate_email(new_email): break
    if new_name:    mgr[1] = new_name
    if new_address: mgr[3] = new_address
    if new_salary:  mgr[4] = new_salary
    if new_email:   mgr[5] = new_email
    update_manager_record(mgr)
    print("  Profile updated successfully!")
    return mgr


def reset_manager_password(mgr):
    print("\n───── Reset Password ─────")
    old_pw = input("Current password: ").strip()
    if old_pw != mgr[6]:
        print("Incorrect current password.")
        return
    while True:
        new_pw = input("New password: ").strip()
        if validate_password(new_pw): break
    confirm = input("Confirm password: ").strip()
    if new_pw != confirm:
        print("Passwords do not match.")
        return
    mgr[6] = new_pw
    update_manager_record(mgr)
    print("Password reset successfully!")


def update_manager_record(mgr):
    with open(manager_path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    with open(manager_path, "w") as file:
        for i, line in enumerate(lines):
            data = [x.strip() for x in line.split("|")]
            if data[0] == mgr[0]:
                file.write("|".join(mgr))
            else:
                file.write(line)
            if i < len(lines) - 1:
                file.write("\n")


def add_employee():
    print("\n───── Add Employee ─────")
    emp_id = generate_id(employee_path, "E")
    while True:
        name = input("Name: ").strip()
        if validate_name(name): break
    while True:
        designation = input("Designation: ").strip()
        if validate_designation(designation): break
    while True:
        age = input("Age: ").strip()
        if validate_age(age): break
    while True:
        address = input("Address: ").strip()
        if validate_address(address): break
    while True:
        salary = input("Salary: ").strip()
        if validate_salary(salary): break
    while True:
        email = input("Email: ").strip()
        if validate_email(email) and validate_email_unique(employee_path, email): break
    while True:
        password = input("Password: ").strip()
        if validate_password(password): break
    data = f"{emp_id}|{name}|{designation}|{age}|{address}|{salary}|{email}|{password}"
    with open(employee_path, "a") as file:
        if os.path.exists(employee_path) and os.path.getsize(employee_path) > 0:
            file.write("\n" + data)
        else:
            file.write(data)
    print(f"\n  Employee added successfully! ID: {emp_id}")


def view_enquiries_suggestions():
    while True:
        print("\n───── Enquiries & Suggestions ─────")
        print("1. View Enquiries")
        print("2. View Suggestions")
        print("3. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            view_messages(enquiry_path, "Enquiries")
        elif choice == "2":
            view_messages(suggestion_path, "Suggestions")
        elif choice == "3":
            break
        else:
            print("  Invalid choice.")


def view_messages(path, label):
    print(f"\n───── {label} ─────")
    if not os.path.exists(path):
        print(f"No {label.lower()} found.")
        input("Press Enter to continue...")
        return
    with open(path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    if not lines:
        print(f"No {label.lower()} found.")
        input("Press Enter to continue...")
        return
    print(f"\nTotal {label}: {len(lines)}")
    print(f"  {'─'*40}")
    for i, line in enumerate(lines, 1):
        data = [x.strip() for x in line.split("|")]
        if len(data) >= 4:
            print(f"\n{label[:-1]} #{i}")
            print(f"{'─'*40}")
            print(f"Date & Time  : {data[0]}")
            print(f"Employee ID  : {data[1]}")
            print(f"Employee     : {data[2]}")
            print(f"Message      : {data[3]}")
            print(f"{'─'*40}")
    input("\n  Press Enter to continue...")


def view_file(path):
    if not os.path.exists(path):
        print("\nNo records found.")
        return
    with open(path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    if not lines:
        print("\nNo records found.")
        return
    print(f"\n{'─'*40}")
    print(f"Total Records: {len(lines)}")
    print(f"{'─'*40}")
    for i, line in enumerate(lines, 1):
        data = [x.strip() for x in line.split("|")]
        print(f"\n  Record #{i}")
        print(f"{'─'*40}")
        print(f"ID          : {data[0]}")
        print(f"Name        : {data[1]}")
        print(f"Designation : {data[2]}")
        print(f"Age         : {data[3]}")
        print(f"Address     : {data[4]}")
        print(f"Salary      : {data[5]}")
        print(f"Email       : {data[6]}")
        print("Password    : ********")
        print(f"{'─'*40}")
    input("\n  Press Enter to continue...")


def search_file(path):
    key = input("Enter Name / ID / Email to search: ").strip().lower()
    if not os.path.exists(path):
        print("No records found.")
        return
    with open(path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    results = [line for line in lines if key in line.lower()]
    if not results:
        print("\n  No matching record found.")
        return
    print(f"\n{len(results)} record(s) found.")
    for i, line in enumerate(results, 1):
        data = [x.strip() for x in line.split("|")]
        print(f"\nResult #{i}")
        print(f"{'─'*40}")
        print(f"ID          : {data[0]}")
        print(f"Name        : {data[1]}")
        print(f"Designation : {data[2]}")
        print(f"Age         : {data[3]}")
        print(f"Address     : {data[4]}")
        print(f"Salary      : {data[5]}")
        print(f"Email       : {data[6]}")
        print(f"{'─'*40}")
    input("\n  Press Enter to continue...")


def delete_record(path):
    key = input("Enter Name / ID / Email to delete: ").strip()
    if not os.path.exists(path):
        print("No records found.")
        return
    with open(path, "r") as file:
        lines = [l for l in file.readlines() if l.strip()]
    matched = [line for line in lines if key.lower() in line.lower()]
    remaining = [line for line in lines if key.lower() not in line.lower()]
    if not matched:
        print("No record found.")
        return
    confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return
    with open(path, "w") as file:
        for i, line in enumerate(remaining):
            if i == 0:
                file.write(line.strip())
            else:
                file.write("\n" + line.strip())
    print("  Record deleted successfully.")


def generate_id(path, prefix):
    if not os.path.exists(path):
        return prefix + "1"
    with open(path, "r") as file:
        lines = [l for l in file.readlines() if l.strip()]
    if not lines:
        return prefix + "1"
    last_line = lines[-1].strip().split("|")
    last_id = last_line[0]
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


def validate_designation(designation):
    if designation == "":
        print("Designation cannot be empty.")
        return False
    return True


def validate_age(age):
    if age == "":
        print("Age cannot be empty.")
        return False
    if not age.isdigit():
        print("Age must be a number.")
        return False
    return True


def validate_address(address):
    if address == "":
        print("Address cannot be empty.")
        return False
    return True


def validate_salary(salary):
    if salary == "":
        print("Salary cannot be empty.")
        return False
    if not salary.isdigit():
        print("Salary must be a number only.")
        return False
    if int(salary) <= 0:
        print("Salary must be greater than 0.")
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


def validate_email_unique(path, email):
    if not os.path.exists(path):
        return True
    with open(path, "r") as file:
        for line in file:
            data = [x.strip() for x in line.strip().split("|")]
            if len(data) >= 7 and data[6].lower() == email.lower():
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
