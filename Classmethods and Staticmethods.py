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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True


p1 = Person('Waseeeq', 'Ahmed', 100000)
p2 = Person('Rohan', 'Bashir', 2000)

Person.set_raise_amt(1.09)
# print(Person.raise_amount)
# print(p1.raise_amount)
# print(p2.raise_amount)

# class methods as alternative constructors

# person_str_1 = 'Salman-Javaid-90000'
# person_str_2 = 'Alama-Iqbal-150000'
# person_str_3 = 'Santiago-Bhatii-2000'

# By using slow method
# first, last, pay = person_str_1.split('-')
# new_person_1 = Person(first,last,pay)

# By using the class method or alternative constructor
#new_person_1 = Person.from_string(person_str_1)

# print(new_person_1.email)
# print(new_person_1.pay)

# Now lets talk about static functions they don't take self or cls

import datetime
my_date = datetime.date(2023,8,23)
print(Person.is_workday(my_date))
