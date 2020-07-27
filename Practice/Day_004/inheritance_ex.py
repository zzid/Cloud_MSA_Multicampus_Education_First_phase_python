'''
Inheritance >>
## 'is a' realtion

'''

class Person(object): # parent
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'My name is {self.name}, i\'m {self.age} ')



class Employee(Person): # child
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name,age, gender)
        self.salary = salary
        self.hire_date = hire_date
    def do_work(self):
        print('I\'m working now')
    def introduce(self):
        super().introduce()
        print(f'My salary is ${self.salary}, i has been entered this company on {self.hire_date}')

person1 = Person('Nadia', 22, 'Famale')
person1.introduce()
employee1 = Employee('David', 29, 'Male', 8000, '23th, December, 2010')
employee1.introduce()