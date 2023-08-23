class Person:
    # why this is accessible by the instance variables???
    raise_amount = 1.04
    num_of_persons = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Person.num_of_persons += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


p1 = Person('Waseeeq', 'Ahmed', 100000)
p2 = Person('Rohan', 'Bashir', 2000)

#  we have to change this for all instances in the good

print(p1.pay)
p1.apply_raise()
print(p1.pay)

# First it checks the instance for the variable if isn't present it checks in the clas itself
# print(Person.raise_amount)
# print(p1.raise_amount)
# print(p2.raise_amount)
#
# # no raised amount here
# print(p1.__dict__)
#
# # but here it is present
# print(Person.__dict__)

Person.raise_amount = 1.05
p1.raise_amount = 1.07

print(Person.raise_amount)
print(p1.raise_amount)
print(p2.raise_amount)

print(Person.num_of_persons)
