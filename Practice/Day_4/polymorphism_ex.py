class Animal:
    def __init__(self, name):
        self.name = name
        # print(f'{self.name}')
    def talk(self): #Abstract method!! interface? right? 
        # forced overriding 
        raise NotImplementedError("Subclass must implement abstact method")


#####################################
### __init__() gonna be inherited ###
#####################################
class Cat(Animal):
    def talk(self):
        return 'Meow!'
class Dog(Animal):
    def talk(self):
        return 'Bark!'
# class Fox(Animal):
#     def no_talk(self):
#         return '..'

animals= [Dog('Jinju'), Cat('Anfisa')]

for i in animals:
    print(i.talk())