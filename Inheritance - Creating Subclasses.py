class Employee:
    # why this is accessible by the instance variables???
    raise_amount = 1.04
    num_of_persons = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_persons += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        # or you must use this when using multiple inheritance
        # Employee.__init__(self,first, last, pay)
        self.prog_lan = prog_lan


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Waseeeq', 'Ahmed', 100000, 'Python')
dev_2 = Developer('Rohan', 'Bashir', 2000, 'Java')

# print(dev_1.email)
# print(dev_2.email)
# print(help(Developer))

# --------------------------------------------------------------

# now lets say we want different raise amount for the developers
# by just overriding the raise_amount we achieved that without breaking anything
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# --------------------------------------------------------------
# Now we want more information in the Developer class

# print(dev_1.prog_lan)
# print(dev_2.prog_lan)

# --------------------------------------------------------------

# Now we will be working with Mangaer class
# dev_3 = Developer('Ali','Haider',1000,'Js')
# mgr_1 = Manager('Arif','Sir','200000',[dev_1, dev_2])

# mgr_1.print_emps()
# mgr_1.add_emp(dev_3)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emps()


# --------------------------------------------------------------

mgr_1 = Manager('Arif','Sir','200000',[dev_1, dev_2])

print(isinstance(mgr_1,Developer)) #False
print(isinstance(mgr_1,Employee)) #True

print(issubclass(Developer,Employee)) #True
print(issubclass(Manager,Employee)) #True
print(issubclass(Manager,Developer)) #False