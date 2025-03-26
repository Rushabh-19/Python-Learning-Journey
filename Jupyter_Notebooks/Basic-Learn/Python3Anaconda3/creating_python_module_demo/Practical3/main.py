import employee

def create_employee(name , department , salary):
    
    emp = employee.Employee (name , department , salary)
    return emp

if __name__ == '__main__':
    
    print ("*********" , __name__)
    employee_denver = create_employee('Denver' , 'HR' , 67000)
    employee_denver.display_details()