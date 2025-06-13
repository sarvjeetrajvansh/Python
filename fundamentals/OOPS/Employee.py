class Employee:
    # Write your code here
    number_of_employees = 0
    average_age = 0.0
    average_salary =0.0

    def __init__(self, name , age, salary) :
        self.name = name
        self.age = age
        self.salary = salary
       
        total_age = Employee.number_of_employees * Employee.average_age
        total_salary =  Employee.number_of_employees * Employee.average_salary
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.average_age = (total_age + age ) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1

