n = float(input('변환하고 싶은 섭씨 온도를 입력해 주세요\n'))
print('섭씨 온도 : ',n)
print('화씨 온도 : {:.2f}'.format((float(9/5) * n) + 32))