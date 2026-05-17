employees = []
def get_non_empty(prompt):
    value = input(prompt).strip()
    while value == "":
        print("This field cannot be empty. Please try again.")
        value = input(prompt).strip()
    return value

def get_positive_salary(prompt):
    while True:
        try:
            salary = float(input(prompt))
            if salary > 0:
                return salary
            else:
                print("Salary must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def is_id_unique(emp_id):
    return not any(emp['id'] == emp_id for emp in employees)


def add_employee():
    print("\n--- Add New Employee ---")
    while True:
        emp_id = get_non_empty("Enter Employee ID: ")
        if is_id_unique(emp_id):
            break
        print("Employee ID already exists. Please use a different ID.")

    name = get_non_empty("Enter Name: ")
    department = get_non_empty("Enter Department: ")
    salary = get_positive_salary("Enter Salary: ")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }
    employees.append(employee)
    print(f"Employee {name} added successfully!\n")


def view_all_employees():
    if not employees:
        print("No employees found.\n")
        return

    print("\n--- All Employees ---")
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Dept: {emp['department']}, Salary: ${emp['salary']:.2f}")
    print()


def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip()
    for emp in employees:
        if emp['id'] == emp_id:
            print(
                f"Found: ID: {emp['id']}, Name: {emp['name']}, Dept: {emp['department']}, Salary: ${emp['salary']:.2f}\n")
            return
    print("Employee not found.\n")


def update_employee():
    emp_id = input("Enter Employee ID to update: ").strip()
    for emp in employees:
        if emp['id'] == emp_id:
            print("Leave blank to keep current value.")
            new_name = input(f"Name ({emp['name']}): ").strip()
            if new_name:
                emp['name'] = new_name
            new_dept = input(f"Department ({emp['department']}): ").strip()
            if new_dept:
                emp['department'] = new_dept
            new_salary = input(f"Salary ({emp['salary']:.2f}): ").strip()
            if new_salary:
                try:
                    salary_val = float(new_salary)
                    if salary_val > 0:
                        emp['salary'] = salary_val
                    else:
                        print("Salary must be positive. Keeping old value.")
                except ValueError:
                    print("Invalid number. Keeping old salary.")
            print("Employee updated successfully.\n")
            return
    print("Employee not found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ").strip()
    for i, emp in enumerate(employees):
        if emp['id'] == emp_id:
            employees.pop(i)
            print(f"Employee with ID {emp_id} deleted successfully.\n")
            return
    print("Employee not found.\n")


def main_menu():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()