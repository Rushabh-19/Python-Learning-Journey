class Employee:
    
    __organization = 'Skillsoft'
    
    def __init__(self , name , department , salary):
        self.__name = name
        self.__department = department
        self.__salary= salary
        
    def display_details(self):
        print (f'Name: {self.__name}')
        print (f'Department: {self.__department}')
        print (f'Salary: {self.__salary}')
        print (f'Organization: {self.__organization}')
   
def create_employee(name , department , salary):
    
    employee = Employee(name , department , salary)
    return employee

if __name__ == '__main__':
    #The special variable name is set by default by Python. And Python is going to use its judgment while setting the value of this variable. If we happen to be inside a module, which is the current entry point for our code, then the value of the special name variable is going to be equal to main.
    
    print ('********', __name__)
    employee_denver = create_employee("Denver" , "HR" , 67000)
    employee_denver.display_details()