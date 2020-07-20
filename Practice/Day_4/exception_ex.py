# try ~ except ~ else
# try ~ except ~ finally 

for i in range(-2,5):
    try:
        result = 10 // i
    except ZeroDivisionError as err:
        print(err, end= ' || ')
    else:
        print(result, end= ' || ')
    finally:
        print('no matter it\'s error or not ')


while True:
    value = input("변환할 정수값을 입력해주세요")
    if not value.isdecimal():
        raise ValueError("숫자값을 입력하지 않으셨습니다")
    print("정수값으로 변환된 숫자 -", bin(int(value)))
    # for digit in value:
        # if digit not in "0123456789":