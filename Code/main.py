from setup import setup_system
from boss import boss_login
from manager import manager_login
from employee import employee_login


def main_menu():
    setup_system()
    while True:
        print(f"{'─'*50}")
        print("*"* 11, "Employee Management System", "*"* 11)
        print(f"{'─'*50}")
        print("─"*50)
        print("─"*14, "Student Information", "─"*14)
        print("─"*50)
        print("Jeevan Karki_(NP071510)")
        print("Anjali Shrestha_(NP071498)")
        print("Esther Khatri_(NP071506)")
        print("Pinki Kumari Yadav_(NP071527)")
        print("─"*50)
        print("\n")
        print("     ", "1. Boss Login")
        print("     ", "2. Manager Login")
        print("     ", "3. Employee Login")
        print("     ", "4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            boss_login()
        elif choice == '2':
            manager_login()
        elif choice == '3':
            employee_login()
        elif choice == '4':
            print("Leaving 🥺🥺... Okay!! Thank You.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main_menu()
