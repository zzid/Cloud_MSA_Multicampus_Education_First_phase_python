# filter
arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = list(filter(lambda  x : x % 2 == 0, arr))
print(arr2)

for i in filter(lambda x: x >2, arr):
    print(i)
