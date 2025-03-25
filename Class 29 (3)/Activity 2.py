#Python code to demonstrate how parent constructors work
#Parent Class
class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
     
#Child Class   
class Employee (Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self,name,idnumber)
        
a = Employee('Rahul',886001,20000,'Intern')
b = Employee('John',886002,100000,'Chief Manager')
c = Employee('Sunil',100000,750000,'CEO')

inp = input('Which employee do you want to see? (a, b or c) : ')

if inp == 'a':
    a.display()
    print(a.salary)
    print(a.post)
elif inp == 'b':
   b.display()
   print(b.salary)
   print(b.post)
elif inp == 'c':
    c.display()
    print(c.salary)
    print(c.post)