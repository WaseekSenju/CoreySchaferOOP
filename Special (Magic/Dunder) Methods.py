class Employee:
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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self, other):
        return self.pay + other.pay

dev_1 = Employee('Waseeeq', 'Ahmed', 100000)
dev_2 = Employee('Rohan', 'Bashir', 2000)


print(dev_1)
print(repr(dev_1))
print(str(dev_1))

# Now lets talk about arithmetic operators
print(dev_1+dev_2)