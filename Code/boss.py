import os
from setup import boss_path, manager_path, employee_path


def boss_login():
    attempts = 0
    while attempts < 3:
        print("\n───── Boss Login ─────")
        email = input("Email    : ").strip()
        password = input("Password : ").strip()
        if os.path.exists(boss_path):
            with open(boss_path, "r") as file:
                data = file.read().strip().split("|")
                if email == data[5] and password == data[6]:
                    print("\nHey Boss! Welcome...")
                    boss_menu()
                    return
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Invalid details. {remaining} attempt(s) remaining.")
        else:
            print("Too many failed attempts. System is now terminating.")
            exit()


def boss_menu():
    while True:
        print("─"*30)
        print(" "*6, "─"*5, "Boss", "─"*5)
        print("─"*30)
        print("1. My Profile")
        print("2. Manager Actions")
        print("3. Employee Actions")
        print("4. Logout")
        choose = input("Choose an option (1-4): ").strip()
        if choose == "1":
            boss_profile()
        elif choose == "2":
            manager_actions()
        elif choose == "3":
            employee_actions()
        elif choose == "4":
            print("Logging out...")
            return
        else:
            print("Unrecognized Command. Please choose from above options.")


def boss_profile():
    while True:
        with open(boss_path, "r") as file:
            data = file.read().strip().split("|")
        print("\n───── Boss Profile ─────")
        print("ID         :", data[0])
        print("Name       :", data[1])
        print("Designation:", data[2])
        print("Address    :", data[3])
        print("Salary     :", data[4])
        print("Email      :", data[5])
        print("Password   : ********")
        print("\n1. Edit Profile")
        print("2. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            print("  (Press Enter to keep current value)")
            while True:
                new_name = input(f"  Name [{data[1]}]: ").strip()
                if new_name == "" or validate_name(new_name):
                    break
            while True:
                new_address = input(f"  Address [{data[3]}]: ").strip()
                if new_address == "" or validate_address(new_address):
                    break
            while True:
                new_salary = input(f"  Salary [{data[4]}]: ").strip()
                if new_salary == "" or validate_salary(new_salary):
                    break
            while True:
                new_email = input(f"  Email [{data[5]}]: ").strip()
                if new_email == "" or validate_email(new_email):
                    break
            while True:
                new_password = input("  Password (leave blank to keep): ").strip()
                if new_password == "" or validate_password(new_password):
                    break
            if new_name:
                data[1] = new_name
            if new_address:
                data[3] = new_address
            if new_salary:
                data[4] = new_salary
            if new_email:
                data[5] = new_email
            if new_password:
                data[6] = new_password
            with open(boss_path, "w") as file:
                file.write("|".join(data))
            print("  Profile updated successfully!")
        elif choice == "2":
            break
        else:
            print("  Invalid choice.")


def manager_actions():
    while True:
        print("\n───── Manager Actions ─────")
        print("1. Add Manager")
        print("2. View Managers")
        print("3. Search Manager")
        print("4. Delete Manager")
        print("5. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_manager(manager_path)
        elif choice == "2":
            view_manager_file(manager_path)
        elif choice == "3":
            search_file(manager_path)
        elif choice == "4":
            delete_record(manager_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def add_manager(manager_path):
    print("\n───── Add Manager ─────")
    manager_id = generate_id(manager_path, "M")
    while True:
        name = input("  Name        : ").strip()
        if validate_name(name):
            break
    while True:
        designation = input("  Designation : ").strip()
        if validate_designation(designation):
            break
    while True:
        address = input("  Address     : ").strip()
        if validate_address(address):
            break
    while True:
        salary = input("  Salary      : ").strip()
        if validate_salary(salary):
            break
    while True:
        email = input("  Email       : ").strip()
        if validate_email(email) and validate_email_unique(manager_path, email):
            break
    while True:
        password = input("  Password    : ").strip()
        if validate_password(password):
            break
    data = f"{manager_id}|{name}|{designation}|{address}|{salary}|{email}|{password}"
    if not os.path.exists(manager_path):
        with open(manager_path, "w") as file:
            file.write(data)
    else:
        with open(manager_path, "a") as file:
            file.write("\n" + data)
    print(f"\n  Manager added successfully! ID: {manager_id}")


def employee_actions():
    while True:
        print("\n───── Employee Actions ─────")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Back")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee_file(employee_path)
        elif choice == "3":
            search_file(employee_path)
        elif choice == "4":
            delete_record(employee_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def add_employee():
    print("\n───── Add Employee ─────")
    emp_id = generate_id(employee_path, "E")
    while True:
        name = input("  Name        : ").strip()
        if validate_name(name):
            break
    while True:
        designation = input("  Designation : ").strip()
        if validate_designation(designation):
            break
    while True:
        age = input("  Age         : ").strip()
        if validate_age(age):
            break
    while True:
        address = input("  Address     : ").strip()
        if validate_address(address):
            break
    while True:
        salary = input("  Salary      : ").strip()
        if validate_salary(salary):
            break
    while True:
        email = input("  Email       : ").strip()
        if validate_email(email) and validate_email_unique(employee_path, email):
            break
    while True:
        password = input("  Password    : ").strip()
        if validate_password(password):
            break
    data = f"{emp_id}|{name}|{designation}|{age}|{address}|{salary}|{email}|{password}"
    if not os.path.exists(employee_path):
        with open(employee_path, "w") as file:
            file.write(data)
    else:
        with open(employee_path, "a") as file:
            file.write("\n" + data)
    print(f"\n  Employee added successfully! ID: {emp_id}")


def view_manager_file(path):
    if not os.path.exists(path):
        print("\nNo records found.")
        return
    with open(path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    if not lines:
        print("\n  No records found.")
        return
    print(f"\n  {'─'*40}")
    print(f"  Total Records: {len(lines)}")
    print(f"  {'─'*40}")
    for i, line in enumerate(lines, 1):
        data = [x.strip() for x in line.split("|")]
        print(f"\n  Record #{i}")
        print(f"  {'─'*40}")
        print(f"  ID          : {data[0]}")
        print(f"  Name        : {data[1]}")
        print(f"  Designation : {data[2]}")
        print(f"  Address     : {data[3]}")
        print(f"  Salary      : {data[4]}")
        print(f"  Email       : {data[5]}")
        print("  Password    : ********")
        print(f"  {'─'*40}")
    input("\n  Press Enter to continue...")


def view_employee_file(path):
    if not os.path.exists(path):
        print("\nNo records found.")
        return
    with open(path, "r") as file:
        lines = [l.strip() for l in file if l.strip()]
    if not lines:
        print("\n  No records found.")
        return
    print(f"\n  {'─'*40}")
    print(f"  Total Records: {len(lines)}")
    print(f"  {'─'*40}")
    for i, line in enumerate(lines, 1):
        data = [x.strip() for x in line.split("|")]
        print(f"\n  Record #{i}")
        print(f"  {'─'*40}")
        print(f"  ID          : {data[0]}")
        print(f"  Name        : {data[1]}")
        print(f"  Designation : {data[2]}")
        print(f"  Age         : {data[3]}")
        print(f"  Address     : {data[4]}")
        print(f"  Salary      : {data[5]}")
        print(f"  Email       : {data[6]}")
        print("  Password    : ********")
        print(f"  {'─'*40}")
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
        print("\nNo matching record found.")
        return
    print(f"\n{len(results)} record(s) found.")
    for i, line in enumerate(results, 1):
        data = [x.strip() for x in line.split("|")]
        print(f"\n  Result #{i}")
        print(f"  {'─'*40}")
        if len(data) == 7:
            print(f"  ID          : {data[0]}")
            print(f"  Name        : {data[1]}")
            print(f"  Designation : {data[2]}")
            print(f"  Address     : {data[3]}")
            print(f"  Salary      : {data[4]}")
            print(f"  Email       : {data[5]}")
            print("  Password    : ********")
        elif len(data) == 8:
            print(f"  ID          : {data[0]}")
            print(f"  Name        : {data[1]}")
            print(f"  Designation : {data[2]}")
            print(f"  Age         : {data[3]}")
            print(f"  Address     : {data[4]}")
            print(f"  Salary      : {data[5]}")
            print(f"  Email       : {data[6]}")
            print("  Password    : ********")
        print(f"  {'─'*40}")
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
    print("Record deleted successfully.")


def generate_id(path, prefix):
    if not os.path.exists(path):
        return prefix + "1"
    with open(path, "r") as file:
        lines = [l for l in file.readlines() if l.strip()]
    if len(lines) == 0:
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
        print("  Name cannot be empty.")
        return False
    if not name.replace(" ", "").isalpha():
        print("  Name must contain letters only.")
        return False
    return True


def validate_designation(designation):
    if designation == "":
        print("  Designation cannot be empty.")
        return False
    return True


def validate_age(age):
    if age == "" or not age.isdigit():
        print("  Age cannot be empty.")
        return False
    return True


def validate_address(address):
    if address == "":
        print("  Address cannot be empty.")
        return False
    return True


def validate_salary(salary):
    if salary == "":
        print("  Salary cannot be empty.")
        return False
    if not salary.isdigit():
        print("  Salary must be a number only.")
        return False
    if int(salary) <= 0:
        print("  Salary must be greater than 0.")
        return False
    return True


def validate_email(email):
    if email == "":
        print("  Email cannot be empty.")
        return False
    if "@" not in email:
        print("  Invalid email. Must contain @.")
        return False
    if "." not in email.split("@")[-1]:
        print("  Invalid email. Must contain domain like .com")
        return False
    return True


def validate_email_unique(path, email):
    if not os.path.exists(path):
        return True
    with open(path, "r") as file:
        for line in file:
            data = [x.strip() for x in line.strip().split("|")]
            email_index = 5 if len(data) == 7 else 6 if len(data) >= 8 else None
            if email_index is not None and data[email_index].lower() == email.lower():
                print("  Email already registered.")
                return False
    return True


def validate_password(password):
    if password == "":
        print("  Password cannot be empty.")
        return False
    if len(password) < 4:
        print("  Password must be at least 4 characters.")
        return False
    return True
