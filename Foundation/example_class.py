#creating a class 
class employee:
    empcount =0
    """docstring for employee"""
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        employee.empcount +=1

    def displaycount(self):
        print "Total Employee %d" %employee.empcount

    def displayemployee(self):
        print "Name:",self.name , "salary:",self.salary
        
#"This would create first object of Employee class"
emp1 =employee("zara",2000)
emp2 = employee("Mani",5000)

# Accessing the object's attributes
emp1.displayemployee()
emp2.displayemployee()
emp2.displaycount()