'''
class member >>
default : public
self.__someting : private

@property  # decorator (getter)
def year():
    return self.__year

@year.setter # decorator (setter)
def year(year):
    self.__year = year
'''
class Product(object):
    def __init__(self, name):
        self.__name = name # private variable
    def __str__(self):
        return '{}'.format(self.__name)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
        
class Inventory(object):
    def __init__(self):
        self.__items = []
    @property # return the hided variable in class
    def items(self):
        return [_.name for _ in self.__items]
    def add_new_item(self, product):
        self.__items.append(product)

temp = Product('tumblr')
print(temp.name)

temp.name = 'starbucks_tumblr' # this can be work because of name.setter
print(temp.name)
# get_name is function but can be called with ()
# because it's a "property"
my_inven = Inventory()
my_inven.add_new_item(temp)
print(my_inven.items)
product1 = Product('iPhone')
my_inven.add_new_item(product1)
print(my_inven.items)