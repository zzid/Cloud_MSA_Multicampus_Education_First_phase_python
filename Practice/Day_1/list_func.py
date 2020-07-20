# Only things that i didn't know

arr = [1,2,3,4]
del arr[2] # no return, and use index
# arr.remove(3) # >> value, and this will return boolean value
print(arr)
'''
Result >> [1, 2, 4]
'''
# multiple append
arr.extend([5,6,7])
print(arr)
'''
Result >> [1, 2, 4, 5, 6, 7]
'''
arr2 = [1,2,3,4,5,6,7,8]
print(arr2[::2])
'''
Result >> [1, 3, 5, 7]
'''
print(arr2[1::2])
'''
Result >> [2, 4, 6, 8]
'''
print(arr2[::-1])
'''
Result >> [8, 7, 6, 5, 4, 3, 2, 1]
'''