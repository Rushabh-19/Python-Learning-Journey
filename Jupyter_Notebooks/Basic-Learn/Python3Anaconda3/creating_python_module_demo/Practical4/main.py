from employee import Employee, create_employee

if __name__ == '__main__':
    
    print ("In Main ********* __name__: " , __name__)
    
    employee_denver = create_employee('Denver' , 'HR' , 67000)
    employee_denver.display_details()
    
    employee_jessica = create_employee('Jessica' , 'Sales' , 69000)
    employee_jessica.display_details()