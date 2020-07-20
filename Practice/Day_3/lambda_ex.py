# lambda function
print((lambda x:x+1)(5))

nums = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
f = lambda x: x **2
print(list(map(f,nums)))

# print((lambda x,y: x*y)(nums, nums2))
# >> error, () is only work in case of has only one parameter
print(list(map(lambda x,y: y+x, nums, nums2)))
print(list(map(lambda x,y: int(y/x), nums, nums2)))

temp = map(f,nums)
for i in range(len(nums)):
    print(next(temp))

