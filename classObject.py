class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name: ', name, '\n' 'Age: ', age)
        print('--------')

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name: ', company_name, '\n' 'location: ', location)
        print('---------')

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary: ', salary, '\n' 'Skill: ', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Mumbai')
emp.Employee_info(12000, 'Machine Learning')