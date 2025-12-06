class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    @classmethod
    def from_string(cls, employee_str):
        name, employee_id, salary = employee_str.split(',')

        return cls(name, employee_id, salary)
    
    def display_employee_info(self):
        print("=" * 50)
        print("Employee INFO: ")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}$")
    


first_employee = Employee("Andrew", "1", "4,000,000,000")
first_employee.display_employee_info()

employee_from_string = "John Doe,E123,50000"
second_employee = Employee.from_string(employee_from_string)
second_employee.display_employee_info()