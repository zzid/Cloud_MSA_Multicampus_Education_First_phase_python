from datetime import datetime as dt
now = dt.today().year
print('태어난 년도를 입력하세요!')
n = int(input())
age = now - n + 1
if 17 <= age < 20:
    print('고등학생 입니다.')
elif 20 <= age < 27:
    print('대학생 입니다.')
else:
    print('학생이 아닙니다.')