class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
#developer class will inherit settings from employee class
    #pass
    #using 'pass' when u dont have any other function and just pass as-is

    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_language):
        super().__init__(first,last,pay)
        #this one will make the same code as in employee init method and also maintainable
        #Employee.__init__(self,first,last,pay)
        self.prog_language = prog_language

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print ('--->',emp.full_name())



dev1 = Developer ('Corey','Schafer',50000, 'python')
dev2 = Developer ('Test', 'Developer', 60000, 'java')
dev3 = Developer ('Cheryl','Le',70000,'Python')
mgr1 = Manager  ('Sue','Smith', 90000, [dev1])


print(isinstance(mgr1,Manager)) # it will print to see if mgr1 is instance of Manager class
print(isinstance(mgr1,Employee)) # it will point back to where it inherits from
print(isinstance(mgr1,Developer))

print(issubclass(Manager,Employee)) # it will print to see if class Manager is a subclass of Employee
print(issubclass(Developer,Employee))
print(issubclass(Manager,Developer))

# print(dev1.email)
# print(dev1.prog_language)



# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)