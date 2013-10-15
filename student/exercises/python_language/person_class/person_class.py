
"""
Person Class
------------

1. Write a class that represents a person with first and last name that
can be initialized like so::

    p = Person('eric', 'jones')

Write a method that returns the person's full name.

Write a __repr__ method that prints out an official representation
of the person that would produce an identical object if evaluated::

    Person('eric', 'jones')

Bonus:
~~~~~~
2. Extend this class in such as way that the code about Homer in the slides
on OOP works: for that create the methods eat, take_nap, speak.

See :ref:`person-class-solution`.
"""


class Person(object):
    
    def __init__(self,firstname,surname):
        self.first = firstname
        self.last = surname
    
    def full_name(self):
        return self.first + ' ' + self.last
    
    def __repr__(self):
        return "Person('{first}','{last}')".format(first=self.first,last=self.last)
