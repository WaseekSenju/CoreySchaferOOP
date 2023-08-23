class Employee:
    raise_amount = 1.04
    num_of_persons = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Deleted Nanme!')
        self.first = None
        self.last = None



dev_1 = Employee('Waseeeq', 'Ahmed')
# Now you have used the email as an attribute
# print(dev_1.first)
# print(dev_1.email)
# print(dev_1.fullname)

# Now what if we have to change the name?
dev_1.fullname = 'Dark Knight'
print(dev_1.first)
print(dev_1.email)
print(dev_1.fullname)

# Now you can make deleter in the same way
del dev_1.fullname
print(dev_1.fullname)