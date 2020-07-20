# https://www.youtube.com/watch?v=_O23jIXsshs

# https://python-guide-kr.readthedocs.io/ko/latest/

# join
colors = ['red', 'yellow', 'blue']
temp = ' '.join(colors)
print(temp)

one_string = "hello world!"
temp_list = one_string.split(' ')
print(temp_list)

my_list = [val for val in range(10) if val % 2 == 0]
print(my_list)


my_list2 = [val if val % 2 ==0 else -1 for val in range(10)]
print(my_list2)

# pythonic code
words = "Yesterday, all my troubles seemed so far away".split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

# asterisk
a, *rest = [1,2,3,4]
print(a, rest)


# zip
a, b, c = zip((1,2,3), (10,20,30), (100,200,300))
print(a,b,c)

for i in zip((1,2,3),(10,20,30), (100,200,300)):
    print(i)

sum_list = [sum(i) for i in zip((1,2,3),(10,20,30), (100,200,300))]
print(sum_list)

# enum & zip
a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for i, (a,b) in enumerate(zip(a_list,b_list)): 
    print(i,a,b)