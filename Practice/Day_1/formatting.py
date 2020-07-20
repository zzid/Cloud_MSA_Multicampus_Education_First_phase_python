temperature = 36
print('온도 값 : %d' %(temperature))
print('온도 값 : {}'.format(temperature))
print(f'온도 값 : {temperature}')

#padding
print('Product {0:10s}, Price per unit {1:10.3f}'.format("Apple", 5243))
print('Product {0:>10s}, Price per unit {1:10.3f}'.format("Apple", 5243))
print('Product {name:10s}, Price per unit {price:10.3f}'.format(name = "Apple", price = 5243))

# printing " ' "
print('Hello i\'m Yun')

#str functions 
word = 'how are you?'
print(word.upper()) # upper() is just temporary!
print(word)

print(word.split(' ')) # split() is just temporary!
print(word)

#list -> str : unpacking
word_list = word.split(' ')
print(word_list)
str1, str2, str3 = word_list
print(str1)
print(str2)
print(str3)

print(word.title())
print(word.capitalize())