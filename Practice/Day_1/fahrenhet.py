n = float(input())
print('섭씨 온도 : ', n)
print('화씨 온도 : {:.2f}'.format((float(9/5) * n) + 32)) # 1 (use format function)
# print('화씨 온도 : ' ,round((float(9/5) * n) + 32,2)) # 2