import random
n = random.randint(1,100)
# print(n)
flag = False
cnt =0
while not flag:
    guess = int(input('숫자를 입력하세요!\n'))
    cnt += 1
    if guess < n:
        print('숫자가 너무 작습니다.')
    elif guess > n:
        print('숫자가 너무 큽니다.')
    else:
        flag = True
        print('정답입니다. 시도횟수 ( {} 회 )'.format(cnt))
    