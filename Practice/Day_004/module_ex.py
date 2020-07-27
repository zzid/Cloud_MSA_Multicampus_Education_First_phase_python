## 1. import the module name ##
# import new_module
# usage : new_module.fah_converter()

## 2. import and make it as alias ##
# import new_module as md
# usage : md.fah_converter()

## 3. import specific function in the module ##
from new_module import fah_converter
# usage : fah_converter()

## 4. import whole function in the module ##
# from new_module import *
# usage : fah_converter()

celcius = float(input('Type the celcius degree you want to convert : '))
fah = fah_converter(celcius)

print(f'Temperature - C : {celcius}, F : {fah:.2f}')