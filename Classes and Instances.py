class Person:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


p1 = Person('Waseeeq', 'Ahmed', 100000)
p2 = Person('Rohan', 'Bashir', 2000)

print(p1.fullname())
print(p2.fullname())



