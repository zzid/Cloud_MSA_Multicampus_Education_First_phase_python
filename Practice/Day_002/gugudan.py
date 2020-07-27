while 1:
    print('구구단 몇 단을 계산할까요?(1~9) || 0을 입력하면 종료 됩니다.')
    n = int(input())
    if n <0 or n>=10:
        print('1~9 범위의 숫자만 입력하세요')
        continue
    elif n == 0:
        print('Bye!')
        break
    for i in range(1,10):
        print('{} X {} = {}'.format(n, i, n*i))


