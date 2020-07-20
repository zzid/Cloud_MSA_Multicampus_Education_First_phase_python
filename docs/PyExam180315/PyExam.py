# 파이썬 예제 모음

###########################################################    
## 2장 ##

# =============== print ===============
print(3 + 4)
4 * 5				# 무시된다.
a = 1
b = 2
print(a + b)

# =============== printsep ===============
s = '서울'
d = '대전'
g = '대구'
b = '부산'
print(s, d, g, b, sep = ' 찍고 ')

# =============== printtwo ===============
a = '강아지'
b = '고양이'
print(a)
print(b)

# =============== printend ===============
a = '강아지'
b = '고양이'
print(a, end = '')
print(b)

# =============== intinput  ===============
price = input('가격을 입력하세요 : ')
num = input('개수를 입력하세요 : ')
sum = int(price) * int(num)
print('총액은', sum, '원입니다')

# ===============  intinput2  ===============
price = int(input('가격을 입력하세요 : '))
num = int(input('개수를 입력하세요 : '))
sum = price * num
print('총액은', sum, '원입니다')

# =============== inputname  ===============
name = input('이름을 입력하세요 : ')
print('안녕하세요', name, '님')

###########################################################    
## 3장 ##

# =============== intradix  ===============
print(hex(26))
print(oct(26))
print(bin(13))

# =============== longstring  ===============
s = """강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네
길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀
구름에 달 가듯이 가는 나그네"""
print(s)

# =============== longstring2  ===============
s = "강나루 건너서 밀밭 길을 구름에 달 가듯이 가는 나그네 \
길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀 \
구름에 달 가듯이 가는 나그네"
print(s)

# =============== linecontinue  ===============
totalsec = 365 * 24 * \
           60 * 60
print(totalsec)

# =============== stringmerge  ===============
s = "korea" "japan" "2002"
print(s)

# =============== multiline  ===============
s = ("korea"
     "japan"
     "2002")
print(s)

# =============== ordchr  ===============
print(ord('a'))
print(chr(98))
for c in range(ord('A'), ord('Z') + 1):
    print(chr(c), end = '')

# =============== listdump  ===============
member = ['손오공', '저팔계', '사오정', '삼장법사']
for m in member:
    print(m, "출동")

# =============== tupledump  ===============
member = ('손오공', '저팔계', '사오정', '삼장법사')
for m in member:
    print(m, "출동")

###########################################################    
## 4장 ##

# =============== round  ===============
print(int(2.54))			# 2
print(round(2.54))		# 3
print(round(2.54, 1))		# 2.5
print(round(123456, -3))		# 123000

###########################################################    
## 5장 ##

# =============== if  ===============
age = int(input("너 몇살이니? "))
if age < 19:
    print("애들은 가라")

# =============== compare  ===============
a = 3
if a == 3:
    print("3이다")
if a > 5:
    print("5보다 크다")
if a < 5:
    print("5보다 작다")

# =============== stringcompare  ===============
country = "Korea"
if country == "Korea":
    print("한국입니다.")
if country == "korea":
    print("대한민국입니다.")

# =============== stringcompare2  ===============
if ("korea" > "japan"):
    print("한국이 더 크다")
if ("korea" < "japan"):
    print("일본이 더 크다")

# =============== intbool  ===============
energy = 1
if energy:
    print("열심히 싸운다")

# =============== andrange  ===============
a = 3
if a > 1 and a < 10:
    print("OK")

# =============== block  ===============
age = 16
if age < 19:
    print("애들은 가라")
    print("공부 열심히 해야지")

# =============== block2  ===============
age = 22
if age < 19:
    print("애들은 가라")
print("공부 열심히 해야지")

# =============== ifelse  ===============
age = 22
if age < 19:
    print("애들은 가라")
else:
    print("어서 옵쇼")

# =============== ifblock  ===============
age = 12
if age < 19:
    print("애들은 가라")
    print("공부 열심히 해야지")
else:
    print("어서 옵쇼")
    print("즐거운 시간 되세요")

# =============== ifelif  ===============
age = 23
if age < 19:
    print("애들은 가라")
elif age < 25:
    print("대학생입니다")
else:
    print("어서 옵쇼")

# =============== elif  ===============
money = 6500
if money >= 20000:
    print("탕수육을 먹는다")
elif money >= 10000:
    print("쟁반 짜장을 먹는다")
elif money >= 6000:
    print("짬뽕을 먹는다")
elif money >= 4000:
    print("짜장면을 먹는다")
else:
    print("단무지를 먹는다")

# =============== ifif  ===============
man = True
age = 22
if man == True:
    if age >= 19:
        print("성인 남자입니다.")

# =============== ifif2  ===============
Man = True
age = 22
if man == True:
    if age >= 19:
        print("성인 남자입니다.")
    else:
        print("소년입니다.")

###########################################################    
## 6장 ##

# =============== while  ===============
student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리한다.")
    student += 1

# =============== sum100  ===============
num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print ("sum =", sum)

# =============== sumodd  ===============
num = 151
sum = 0
while num <= 300:
    sum += num
    num += 2
print ("sum =",sum)

# =============== for  ===============
for student in [1, 2, 3, 4, 5]:
    print(student, "번 학생의 성적을 처리한다.")

# =============== forsum  ===============
sum = 0
for num in range(1, 101):
    sum += num
print ("sum =",sum)

# =============== forsum2  ===============
sum = 0
for num in range(2, 101, 2):
    sum += num
print ("sum =",sum)

# =============== ruler  ===============
for x in range(1, 51):
    if (x % 10 == 0):
        print('+', end= '')
    else:
        print('-', end = '')

# =============== ruler2  ===============
for x in range(1, 5):
    print('-' * 9, end = '')
    print('+', end = '') 

# =============== ruler3  ===============
x = 1
while x <= 50:
    if (x % 10):
        print('-', end= '')
    else:
        print('+', end = '')
    x += 1

# =============== ruler4  ===============
for x in range(1, 51):
    if (x % 5 == 0):
        print('+', end= '')
    else:
        print('-', end = '')

# =============== ruler5  ===============
for x in range(1, 51):
    if (x % 10 == 5):
        print('+', end= '')
    else:
        print('-', end = '')

# =============== break  ===============
score = [ 92, 86, 68, 120, 56]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print("성적 처리 끝")

# =============== continue  ===============
score = [ 92, 86, 68, -1, 56]
for s in score:
    if (s == -1):
        continue
    print(s)
print("성적 처리 끝")

# =============== gugudan  ===============
for dan in range(2, 10):
    print(dan, "단")
    for hang in range(2, 10):
        print(dan, "*", hang, "=", dan * hang)
    print()

# =============== gugudanwhile  ===============
dan = 2
while dan <= 9:
    hang = 2
    print(dan, "단")
    while hang <= 9:
        print(dan, "*", hang, "=", dan * hang)
        hang += 1
    dan += 1
    print()

# =============== triangle  ===============
for y in range(1, 10) :
    for x in range(y) :
        print('*', end = '')
    print()

# =============== infinite  ===============
print("3 + 4 = ?")
while True:
    a = int(input("정답을 입력하시오 : "))
    if (a == 7): break
print("참 잘했어요")

# =============== zerobase  ===============
for ten in range(0, 5) :
    for num in range(ten * 10, ten * 10 + 10) :
        print(num, end = ',')
    print()

###########################################################    
## 7장 ##

# =============== repeat  ===============
sum = 0
for num in range( 5):
    sum += num
print("~ 4 =", sum)

sum = 0
for num in range(11):
    sum += num
print("~ 10 =", sum)

# =============== calcsum  ===============
def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

print("~ 4 =", calcsum(4))
print("~ 10 =", calcsum(10))

# =============== calcrange  ===============
def calcrange(begin, end):
    sum = 0
    for num in range(begin, end + 1):
        sum += num
    return sum

print("3 ~ 7 =", calcrange(3, 7))

# =============== printsum  ===============
def printsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    print("~", n, "=", sum)

printsum(4)
printsum(10)

# =============== vararg  ===============
def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))

# =============== defaultarg  ===============
def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("1 ~ 10 =", calcstep(1, 10, 2))
print("2 ~ 10 =", calcstep(2, 10, 2))

# =============== calcstep  ===============
def calcstep(begin, end, step = 1):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("1 ~ 10 =", calcstep(1, 10, 2))
print("1 ~ 100 =", calcstep(1, 100))

# =============== keywordarg  ===============
def calcstep(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

# =============== keywordvararg  ===============
def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("3 ~ 5 =", calcstep(begin = 3, end = 5, step = 1))
print("3 ~ 5 =", calcstep(step = 1, end = 5, begin = 3))

# =============== calcscore  ===============
def calcscore(name, *score, **option):
    print(name)
    sum = 0
    for s in score:
        sum += s
    print("총점 :", sum)
    if (option['avg'] == True ):
        print("평균 :", sum / len(score))

calcscore("김상형", 88, 99, 77, avg = True)
calcscore("김한슬", 99, 98, 95, 89, avg = False)

# =============== local  ===============
def kim():
    temp = "김과장의 함수"
    print(temp)

kim()
print(temp)

# =============== local2  ===============
def kim():
    temp = "김과장의 함수"
    print(temp)

def lee():
    temp = 2 ** 10
    return temp

def park(a):
    temp = a * 2
    print(temp)

kim()
print(lee())
park(6)

# =============== global  ===============
salerate = 0.9

def kim():
    print("오늘의 할인율 :", salerate)

def lee():
    price = 1000
    print("가격 :", price * salerate)

kim()
salerate = 1.1
lee()

# =============== global2  ===============
price = 1000

def sale():
    price = 500

sale()
print(price)

# =============== id  ===============
price = 1000

def sale():
    price = 500
    print("sale", id(price))

sale()
print("global", id(price))

# =============== global3  ===============
price = 1000

def sale():
    global price
    price = 500

sale()
print(price)

# =============== docstring  ===============
def calcsum(n):
    """1 ~ n까지의 합계를 구해 리턴한다."""
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

help(calcsum)

# =============== builtin  ===============
print(abs(-5))
print(max(3, 7))
print(min([8, 9, 1, 6, 2]))

###########################################################    
## 8장 ##

# =============== index  ===============
s = "python"
print(s[2])
print(s[-2])

# =============== stringindex  ===============
s = "python"
for c in s:
    print(c, end = ',')

# =============== slice  ===============
s = "python"
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])

# =============== slice2  ===============
file = "20171224-104830.jpg"
print("촬영 날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영 시간 : " + file[9:11] + "시 " + file[11:13] + "분")
print("확장자 : " + file[-3:])

# =============== slice3  ===============
yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])

# =============== find  ===============
s = "python programming"
print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

# =============== count  ===============
s = """생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 생각하지 
않으려고 하는 생각이 옳은 생각이라고 생각합니다."""
print("생각의 출현 횟수 :", s.count('생각'))

# =============== in  ===============
s = "python programming"
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

# =============== startswith  ===============
name = "김한결"
if name.startswith("김"):
    print("김가입니다.")
if name.startswith("한"):
    print("한가입니다.")

file = "girl.jpg"
if file.endswith(".jpg"):
    print("그림 파일입니다.")

# =============== isdecimal  ===============
height = input("키를 입력하세요 :")
if height.isdecimal():
    print("키 =", height)
else:
    print("숫자만 입력하세요.")

# =============== lower  ===============
s = "Good morning. my love KIM."
print(s.lower())
print(s.upper())
print(s)

print(s.swapcase())
print(s.capitalize())
print(s.title())

# =============== strlower  ===============
python = input("파이썬의 영문 철자를 입력하시오 : ")
if python.lower() == "python":
    print("맞췄습니다.")

# =============== strip  ===============
s = "  angel   "
print(s + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")
print(s.strip() + "님")

# =============== split  ===============
s = "짜장 짬뽕 탕슉"
print(s.split())

s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)
for c in city:
    print(c, "찍고", end = ' ')

# =============== splitlines  ===============
traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.splitlines()
for line in poet:
    print(line)

# =============== join  ===============
s = "._."
print(s.join("대한민국"))

# =============== splitjoin  ===============
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(" 찍고 ".join(city))

# =============== replace  ===============
s = "독도는 일본땅이다. 대마도도 일본땅이다."
print(s)
print(s.replace("일본", "한국"))

# =============== just  ===============
message = "안녕하세요."
print(message.ljust(30))
print(message.rjust(30))
print(message.center(30))

# =============== center  ===============
traveler = """강나루 건너서\n밀밭 길을\n\n구름에 달 가듯이\n가는 나그네\n
길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀\n
구름에 달 가듯이\n가는 나그네"""
poet = traveler.splitlines()
for line in poet:
    print(line.center(30))

# =============== stringcat  ===============
price = 500
print("궁금하면 " + str(price) + "원!")

# =============== format  ===============
price = 500
print("궁금하면 %d원!" % price)

# =============== format2  ===============
month = 8
day = 15
anni = "광복절"
print("%d월 %d일은 %s이다." % (month, day, anni))

# =============== width  ===============
value = 123
print("###%d###" % value)
print("###%5d###" % value)
print("###%10d###" % value)
print("###%1d###" % value)

# =============== align  ===============
price = [30, 13500, 2000]
for p in price:
    print("가격:%d원" % p)
for p in price:
    print("가격:%7d원" % p)

# =============== numalign  ===============
price = [30, 13500, 2000]
for p in price:
    print("가격:%-7d원" % p)

# =============== precision  ===============
pie = 3.14159265
print("%10f" % pie)
print("%10.8f" % pie)
print("%10.5f" % pie)
print("%10.2f" % pie)

# =============== newformat  ===============
name = "한결"
age = 16
height = 162.5
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

# =============== newformat2  ===============
name = "한결"
age = 16
height = 162.5
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name, age, height))

# =============== newformat3  ===============
name = "한결"
age = 16
height = 162.5
print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name, age, height))

# =============== newformat4  ===============
name = "한결"
age = 16
height = 162.5
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name, age, height))

# =============== newformat5  ===============
name = "한결"
age = 16
height = 162.5
print("이름:{0:$^10s}, 나이:{1:>05d}, 키:{2:!<8.2f}".format(name, age, height))

###########################################################    
## 9장 ##

# =============== listscore  ===============
score = [ 88, 95, 70, 100, 99 ]
sum = 0
for s in score:
    sum += s
print("총점 : ", sum)
print("평균 : ", sum / len(score))

# =============== listslice  ===============
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])        # 2~5까지
print(nums[:4])         # 처음부터 4까지
print(nums[6:])         # 6에서 끝까지
print(nums[1:7:2])      # 1~7까지 하나씩 건너뛰며

# =============== listassign  ===============
score = [ 88, 95, 70, 100, 99 ]
print(score[2])     # 70
score[2] = 55       # 값 변경
print(score[2])     # 55

# =============== listreplace  ===============
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5] = [20, 30, 40]
print(nums)
nums[6:8] = [90, 91, 92, 93, 94]
print(nums)

# =============== rangeremove  ===============
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5] = []
del nums[4]
print(nums)

# =============== listcat  ===============
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
listadd = list1 + list2
print(listadd)
listmulti = list2 * 3

# =============== nestlist  ===============
lol = [ [1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])
print(lol[2][1])

for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()

# =============== nestscore  ===============
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
    ]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects = len(student)
    print("총점 %d, 평균 %.2f" % (sum, sum / subjects))
    total += sum
    totalsub += subjects
print("전체평균 %.2f" % (total / totalsub))

# =============== listcomp  ===============
nums = [n * 2 for n in range(1, 11)]
for i in nums:
    print(i, end = ', ')

# =============== listinsert  ===============
nums = [1, 2, 3, 4]
nums.append(5)
nums.insert(2, 99)
print(nums)

# =============== insertrange  ===============
nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92]
print(nums)

nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]
print(nums)

# =============== extend  ===============
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list1.extend(list2)
print(list1)

# =============== listremove  ===============
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)

# =============== pop  ===============
score = [ 88, 95, 70, 100, 99 ]
print(score.pop())
print(score.pop())
print(score.pop(1))
print(score)

# =============== listindex  ===============
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
perfect = score.index(100)
print("만점 받은 학생은 " + str(perfect) + "번입니다.")
pernum = score.count(100)
print("만점자 수는 " + str(pernum) + "명입니다")

# =============== listmin  ===============
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
print("학생 수는 %d명입니다." % len(score))
print("최고 점수는 %d점입니다." % max(score))
print("최저 점수는 %d점입니다." % min(score))

# =============== listin  ===============
ans = input("결제 하시겠습니까? ")
if ans in ['yes', 'y', 'ok', '예', '당근']:
    print("구입해 주셔서 감사합니다.")
else:
    print("안녕히 가세요.")

# =============== sort  ===============
score = [ 88, 95, 70, 100, 99 ]
score.sort()
print(score)
score.reverse()
print(score)

# =============== sort2  ===============
country = ["Korea", "japan", "CHINA", "america"]
country.sort()
print(country)
country.sort(key = str.lower)
print(country)

# =============== sorted  ===============
score = [ 88, 95, 70, 100, 99 ]
score2 = sorted(score)
print(score)
print(score2)

# =============== tuplescore  ===============
score = ( 88, 95, 70, 100, 99 )
sum = 0
for s in score:
    sum += s
print("총점 : ", sum)
print("평균 : ", sum / len(score))

# =============== onetuple  ===============
tu = 2,
value = 2
print(tu)
print(value)

# =============== tupleop  ===============
tu = 1, 2, 3, 4, 5
print(tu[3])         # 가능
print(tu[1:4])       # 가능
print(tu + (6, 7))    # 가능
print(tu * 2)        # 가능      
tu[1] = 100          # 불가능
del tu[1]            # 불가능

# =============== unpacking  ===============
tu = "이순신", "김유신", "강감찬"
lee, kim, kang = tu
print(lee)
print(kim)
print(kang)

# =============== swap  ===============
a, b = 12, 34
print(a, b)
a, b = b, a
print(a, b)

# =============== tworeturn  ===============
import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))

# =============== divmod  ===============
d, m = divmod(7, 3)
print("몫", d)
print("나머지", m)

# =============== convertlist  ===============
score = [ 88, 95, 70, 100, 99 ]
tu = tuple(score)
#tu[0] = 100
print(tu)
li = list(tu)
li[0] = 100
print(li)

###########################################################    
## 10장 ##

# =============== dic  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic)

# =============== dicread  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic['boy'])
print(dic['book'])

# =============== dicget  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어입니다.'))

# =============== dicin  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")

# =============== dicchange  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
dic['boy'] = '남자애'
dic['girl'] = '소녀'
del dic['book']
print(dic)

# =============== keys  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic.keys())
print(dic.values())
print(dic.items())

# =============== keylist  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
keylist = dic.keys()
for key in keylist:
    print(key)

# =============== dicupdate  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
dic2 = { 'student':'학생', 'teacher':'선생님', 'book':'서적' }
dic.update(dic2)
print(dic)

# =============== listtodic  ===============
li = [ ['boy', '소년'], ['school', '학교'], ['book', '책'] ]
dic = dict(li)
print(dic)

# =============== alphanum  ===============
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1

print(alphabet)

# =============== alphanum2  ===============
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
        
key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, "=>", num)

# =============== alphanum3  ===============
song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1
        
for code in range(ord('a'), ord('z') + 1):
    c = chr(code)
    num = alphabet.get(c, 0)
    print(c, "=>", num)

# =============== set  ===============
asia = { 'korea', 'china', 'japan', 'korea' }
print(asia)

# =============== set2  ===============
print(set("sanghyung"))
print(set([12, 34, 56, 78]))
print(set(("신지희", "한주완", "김태륜")))
print(set({'boy':'소년', 'school':'학교', 'book':'책'}))
print(set())

# =============== setedit  ===============
asia = { 'korea', 'china', 'japan' }
asia.add('vietnam')         # 추가
asia.add('china')           # 추가 안됨
asia.remove('japan')        # 제거
print(asia)

asia.update({'singapore', 'hongkong', 'korea'})
print(asia)

# =============== setop  ===============
twox = { 2, 4, 6, 8, 10, 12 }
threex = { 3, 6, 9, 12, 15 }

print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox)
print("배타적 차집합", twox ^ threex)

# =============== setin  ===============
mammal = { '코끼리', '고릴라', '사자', '고래', '사람', '원숭이', '개' }
primate = { '사람', '원숭이', '고릴라' }

if '사자' in mammal:
    print("사자는 포유류이다")
else:
    print("사자는 포유류가 아니다.")

print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)

###########################################################    
## 11장 ##

# =============== sequence  ===============
score = [ 88, 95, 70, 100, 99 ]
for s in score:
    print("성적 :", s)

# =============== sequence2  ===============
score = [ 88, 95, 70, 100, 99 ]
no = 1
for s in score:
    print(str(no) + "번 학생의 성적 :", s)
    no += 1

# =============== sequence3  ===============
score = [ 88, 95, 70, 100, 99 ]
for no in range(len(score)):
    print(str(no + 1) + "번 학생의 성적 :", score[no])

# =============== enumerate  ===============
score = [ 88, 95, 70, 100, 99 ]
for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 :", s)

# =============== zip  ===============
yoil = ["월", "화", "수", "목","금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)
for y, f in menu:
    print("%s요일 메뉴 : %s" % (y, f))

# =============== anyall  ===============
adult = [True, False, True, False ]
print(any(adult))
print(all(adult))

# =============== filter  ===============
def flunk(s):
    return s < 60

score = [ 45, 89, 72, 53, 94 ]
for s in filter(flunk, score):
    print(s)

# =============== map  ===============
def half(s):
    return s / 2

score = [ 45, 89, 72, 53, 94 ]
for s in map(half, score):
    print(s, end = ', ')

# =============== map2  ===============
def total(s, b):
    return s + b

score = [ 45, 89, 72, 53, 94 ]
bonus = [ 2, 3, 0, 0, 5 ]
for s in map(total, score, bonus):
    print(s, end=", ")

# =============== lambda  ===============
score = [ 45, 89, 72, 53, 94 ]
for s in filter(lambda x:x < 60, score):
    print(s)

# =============== lambda2  ===============
score = [ 45, 89, 72, 53, 94 ]
for s in map(lambda x:x / 2, score):
    print(s, end=", ")

# =============== varcopy  ===============
a = 3
b = a
print("a = %d, b = %d" % (a, b))

a = 5
print("a = %d, b = %d" % (a, b))

# =============== listcopy  ===============
list1 = [ 1, 2, 3 ]
list2 = list1

list2[1] = 100
print(list1)
print(list2)

# =============== listcopy2  ===============
list1 = [ 1, 2, 3 ]
list2 = list1.copy()

list2[1] = 100
print(list1)
print(list2)

# =============== deepcopy  ===============
list0 = [ 'a', 'b' ]
list1 = [ list0, 1, 2 ]
list2 = list1.copy()

list2[0][1] = 'c'
print(list1)
print(list2)

# =============== deepcopy2  ===============
import copy

list0 = [ "a", "b" ]
list1 = [ list0, 1, 2 ]
list2 = copy.deepcopy(list1)

list2[0][1] = "c"
print(list1)
print(list2)

# =============== is  ===============
list1 = [ 1, 2, 3 ]
list2 = list1
list3 = list1.copy()

print("1 == 2" , list1 is list2)
print("1 == 3" , list1 is list3)
print("2 == 3" , list2 is list3)

# =============== varis  ===============
a = 1
b = a
print("a =", a, " b =", b, ":", a is b)
b = 2
print("a =", a, " b =", b, ":", a is b)

###########################################################    
## 12장 ##

# =============== import  ===============
import math

print(math.sqrt(2))

# =============== fromimport  ===============
from math import sqrt

print(sqrt(2))

# =============== importas  ===============
import math as m

print(m.sqrt(2))

# =============== fromas  ===============
from math import sqrt as sq

print(sq(2))

# =============== sin  ===============
import math

print(math.sin(math.radians(45)))
print(math.sqrt(2))
print(math.factorial(5))

# =============== sincurve  ===============
import math
import turtle as t

t.penup()
t.goto(-720,0)
t.pendown()
for x in range(-720, 720) :
    t.goto(x, math.sin(math.radians(x)) * 100)
t.done()

# =============== statistics  ===============
import statistics

score = [30, 40, 60, 70, 80, 90]
print(statistics.mean(score))
print(statistics.harmonic_mean(score))
print(statistics.median(score))
print(statistics.median_low(score))
print(statistics.median_high(score))

# =============== time  ===============
import time

print(time.time())

# =============== ctime  ===============
import time

t = time.time()
print(time.ctime(t))

# =============== structtime  ===============
import time

t = time.time()
print(time.localtime(t))

# =============== localtime  ===============
import time

now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

# =============== datetime  ===============
import datetime

now = datetime.datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))

# =============== ellapse  ===============
import time

start = time.time()
for a in range(1000):
    print(a)
end = time.time()
print(end - start)

# =============== sleep  ===============
import time

print("안녕하세요.")
time.sleep(1)
print("밤에 성시경이 두 명 있으면 뭘까요?")
time.sleep(5)
print("야간투시경입니다.")

# =============== sleep2  ===============
import time

for dan in range(2, 10):
    print(dan, "단")
    for hang in range(2, 10):
        print(dan, "*", hang, "=", dan*hang)
        time.sleep(0.2)
    print()
    time.sleep(1)

# =============== calendar  ===============
import calendar

print(calendar.calendar(2018))
print(calendar.month(2019, 1))
#calendar.prcal(2018)
#calendar.prmonth(2019, 1)

# =============== weekday  ===============
import calendar

yoil = ['월', '화', '수', '목', '금', '토', '일']
day = calendar.weekday(2020,8,15)
print("광복절은", yoil[day] + "요일이다." )

# =============== random  ===============
import random

for i in range(5):
    print(random.random())

# =============== randint  ===============
import random

for i in range(5):
    print(random.randint(1,10))

# =============== uniform  ===============
import random

for i in range(5):
    print(random.uniform(1,100))

# =============== choice  ===============
import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

# =============== shuffle  ===============
import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(food)
random.shuffle(food)
print(food)

# =============== sample  ===============
import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.sample(food, 2))

# =============== lotto  ===============
import random

nums = random.sample(range(1, 46), 6)
nums.sort()
print(nums)

# =============== mathquiz  ===============
import random

a = random.randint(1, 9)
b = random.randint(1, 9)
question = "%d + %d = ? " % (a, b)
c = int(input(question))

if c == a + b:
    print("정답입니다.")
else:
    print("틀렸습니다.")

# =============== mathquiz2  ===============
import random

correct = 0
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    question = "%d + %d = ?(끝낼 때는 0) " % (a, b)
    c = int(input(question))

    if c == 0:
        break
    elif c == a + b:
        print("정답입니다.")
        correct = correct + 1
    else:
        print("틀렸습니다.")

print("%d 개 맞췄습니다." % correct)

# =============== mathquiz3  ===============
import random

correct = 0
while True:
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    op = random.randint(1, 3)

    if op == 1:
        ans = a + b
        mark = "+"
    elif op == 2:
        if (a < b):
            a, b = b, a
        ans = a - b
        mark = "-"
    else:
        ans = a * b
        mark = "*"

    question = "%d %s %d = ?(끝낼 때는 0) " % (a, mark, b)
    c = int(input(question))

    if c == 0:
        break
    elif c == ans:
        print("정답입니다.")
        correct = correct + 1
    else:
        print("틀렸습니다.")

print("%d 개 맞췄습니다." % correct)

# =============== randnum  ===============
import random

secret = random.randint(1,100)
while True:
    num = int(input("숫자를 입력하세요(끝낼 때 0) : "))
    if num == 0:
        break
    if num == secret:
        print("맞췄습니다")
        break
    elif num > secret:
        print("입력한 숫자보다 더 작습니다.")
    else:
        print("입력한 숫자보다 더 큽니다")

# =============== randnum2  ===============
import random

secret = random.randint(1,100)
count = 0
while True:
    num = int(input("숫자를 입력하세요(끝낼 때 0) : "))
    if num == 0:
        break
    count += 1
    if num == secret:
        print("%d번만에 맞췄습니다" % count)
        break
    elif num > secret:
        print("입력한 숫자보다 더 작습니다.")
    else:
        print("입력한 숫자보다 더 큽니다")

# =============== sys  ===============
import sys

print("버전 :", sys.version)
print("플랫폼 :", sys.platform)
if (sys.platform == "win32"):
    print(sys.getwindowsversion())
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)
sys.exit(0)

# =============== sysarg  ===============
import sys

print(sys.argv)

# =============== argcal  ===============
import calendar
import time
import sys

if (len(sys.argv) == 1):
    t = time.time()
    tm = time.localtime(t)
    calendar.prmonth(tm.tm_year, tm.tm_mon)
elif (len(sys.argv) == 2):
    print(calendar.calendar(int(sys.argv[1])))
elif (len(sys.argv) == 3):
    calendar.prmonth(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("인수는 2개 이하여야 합니다.")

# =============== datecalc  ===============
import sys
import time

if (len(sys.argv) != 2):
    print("시작 날짜를 yyyymmdd로 입력하십시오.")
    sys.exit(0)

birth = sys.argv[1]
if (len(birth) != 8 or birth.isnumeric() == False):
    print("날짜 형식이 잘못되었습니다.")
    sys.exit(0)

tm = (int(birth[:4]), int(birth[4:6]), int(birth[6:8]), 0, 0, 0, 0, 0, 0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)

# =============== ellapsedate2  ===============
import sys
import time

year = int(input("태어난 년도를 입력하세요(4자리) : "))
month = int(input("태어난 월을 입력하세요 : "))
day = int(input("태어난 일을 입력하세요 : "))

tm = (year, month, day, 0, 0, 0, 0, 0, 0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)

###########################################################    
## 13장 ##

# =============== exception  ===============
str = "89점"
score = int(str)
print(score)
print("작업완료")

# =============== tryexcept  ===============
str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다.")
print("작업완료")

# =============== whiletry  ===============
while True:
    str = input("점수를 입력하세요 : ")
    try:
        score = int(str)
        print("입력한 점수 :", score)
        break
    except:
        print("점수 형식이 잘못되었습니다.")
print("작업완료")

# =============== excepts  ===============
str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")
print("작업완료")

# =============== exceptas  ===============
str = "89점"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
print("작업완료")

# =============== raise  ===============
def calcsum(n):
    if (n < 0):
        raise ValueError
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

try:
    print("~10 =", calcsum(10))
    print("~-5 =", calcsum(-5))
except ValueError:
    print("입력값이 잘못되었습니다.")

# =============== errorret  ===============
def calcsum(n):
    if (n < 0):
        return -1
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

result = calcsum(10)
if result == -1:
    print("입력값이 잘못되었습니다.")
else:
    print("~10 =", result)

result = calcsum(-5)
if result == -1:
    print("입력값이 잘못되었습니다.")
else:
    print("~10 =", result)

# =============== funcexcept  ===============
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
try:
    print(dic['girl'])
except:
    print("찾는 단어가 없습니다.")

han = dic.get('girl')
if (han == None):
    print("찾는 단어가 없습니다.")
else:
    print(han)

# =============== finally  ===============
try:
    print("네트워크 접속")
    a = 2 / 0
    print("네트워크 통신 수행")
finally:
    print("접속 해제")
print("작업 완료")

# =============== assert  ===============
score = 128
assert score <= 100, "점수는 100 이하여야 합니다"
print(score)

###########################################################    
## 14장 ##

# =============== write  ===============
f = open("live.txt", "wt")
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close()

# =============== read  ===============
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

# =============== read2  ===============
f = open("live.txt", "rt")
while True:
    text = f.read(10)
    if len(text) == 0: break
    print(text, end = '')
f.close()

# =============== readline  ===============
f = open("live.txt", "rt")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)

# =============== readlines  ===============
f = open("live.txt", "rt")
rows = f.readlines()
for row in rows:
    print(row, end = '')
f.close()

# =============== readfile  ===============
f = open("live.txt", "rt")
for line in f:
    print(line, end = '')
f.close()

# =============== seek  ===============
f = open("live.txt", "rt")
f.seek(12,0)
text = f.read()
f.close()
print(text)

# =============== append  ===============
f = open("live.txt", "at")
f.write("\n\n푸쉬킨 형님의 말씀이었습니다.")
f.close()

# =============== withas  ===============
with open("live.txt", "rt") as f:
   text = f.read()
print(text)

# =============== filecopy  ===============
import shutil

shutil.copy("live.txt", "live2.txt")

# =============== listdir  ===============
import os

files = os.listdir("c:\\Test")
for f in files:
    print(f)

# =============== listdir2  ===============
import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)

dumpdir("c:\\MP3")

# =============== changename  ===============
import os

path = "c:\\Test"
files = os.listdir(path)
for f in files:
    if (f.find("-") and f.endswith(".mp3")):
        name = f[0:-4]
        ext = f[-4:]
        part = name.split("-")
        newname = part[1].strip() + "-" + part[0].strip() + ext
        print(newname)
        os.rename(path + "\\" + f, path + "\\" + newname)

###########################################################    
## 15장 ##

# =============== capsule  ===============
balance = 8000

def deposit(money):
    global balance
    balance += money

def inquire():
    print("잔액은 %d원입니다." % balance)

deposit(1000)
inquire()

# =============== account  ===============
class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def inquire(self):
        print("잔액은 %d원입니다." % self.balance)

sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()

# =============== human  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

kim = Human(29, "김상형")
kim.intro()
lee = Human(45, "이승우")
lee.intro()

# =============== student  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다")


class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번 : " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을현 누를황")


kim = Human(29, "김상형")
kim.intro()
lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()

# =============== getset  ===============
class Date:
    def __init__(self, month):
        self.month = month
    def getmonth(self):
        return self.month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.month = month

today = Date(8)
today.setmonth(15)
print(today.getmonth())

# =============== property  ===============
class Date:
    def __init__(self, month):
        self.inner_month = month
    def getmonth(self):
        return self.inner_month
    def setmonth(self, month):
        if 1<= month <= 12:
            self.inner_month = month
    month = property(getmonth, setmonth)

today = Date(8)
today.month = 15
print(today.month)

# =============== property2  ===============
class Date:
    def __init__(self, month):
        self.inner_month = month
    @property
    def month(self):
        return self.inner_month
    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15
print(today.month)

# =============== hidden  ===============
class Date:
    def __init__(self, month):
        self.__month = month
    def getmonth(self):
        return self.__month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month
    month = property(getmonth, setmonth)

today = Date(8)
today.__month = 15
print(today.month)

# =============== classmethod  ===============
class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()

# =============== staticmethod  ===============
class Car:
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)

Car.hello()

# =============== eqop  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

kim = Human(29, "김상형")
sang = Human(29, "김상형")
moon = Human(44, "문종민")
print(kim == sang)
print(kim == moon)

# =============== clsstr  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)

kim = Human(29, "김상형")
print(kim)

# =============== clslen  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __len__(self):
        return self.age

kim = Human(29, "김상형")
print(len(kim))

# =============== floaterror  ===============
f = 0.1
sum = 0
for i in range(100):
    sum += f
print(sum)

# =============== decimal  ===============
from decimal import Decimal

f = Decimal('0.1')
sum = 0
for i in range(100):
    sum += f
print(sum)

# =============== context  ===============
from decimal import *

a = Decimal('1111111111')
b = Decimal('1111111111')

setcontext(BasicContext)
c = a * b
print(c)

setcontext(DefaultContext)
c = a * b
print(c)

# =============== fraction  ===============
from fractions import *

a = Fraction(1,3)
print(a)
b = Fraction(8, 14)
print(b)

# =============== fraction2  ===============
from fractions import *

a = Fraction(2, 3)
b = Fraction(3, 5)
c = a + b
print(c)

d = c + 0.1
print(d)

# =============== array  ===============
import array

ar = array.array('i', [33, 44, 67, 89, 56])
for a in ar:
    print(a, end = ',')
ar.append(100)                  # 추가
del ar[0]                       	# 삭제
print("\nar[1] = ", ar[1])      		# 첨자 참조
print(ar[2:4])                  	# 슬라이스

###########################################################    
## 16장 ##

# =============== util  ===============
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

# =============== utiltest  ===============
import util

print("1inch =", util.INCH)
print("~10 =", util.calcsum(10))

# =============== util  ===============
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

print("인치 =", INCH)
print("합계 =", calcsum(10))

# =============== util2  ===============
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

if __name__ == "__main__":
    print("인치 =", INCH)
    print("합계 =", calcsum(10))

# =============== utiltest2  ===============
import util2

print("1inch =", util2.INCH)
print("~10 =", util2.calcsum(10))

# =============== path  ===============
import sys
sys.path.append("C:\\Temp")
import util2
print("1inch =", util2.INCH)
print("~10 =", util2.calcsum(10))

# =============== usepackage  ===============
import sys
sys.path.append("C:/PyStudy")

import mypack.calc.add
mypack.calc.add.outadd(1,2)

import mypack.report.table
mypack.report.table.outreport()

# =============== importall  ===============
import sys
sys.path.append("C:/PyStudy")

from mypack.calc import *
add.outadd(1,2)
multi.outmulti(1,2)

# =============== __init__  ===============
__all__ = ["add", "multi"]

print("add module imported")

# =============== wxtest  ===============
import wx

app = wx.App()
frame = wx.Frame(None, 0, "파이썬 만세")

frame.Show(True)
app.MainLoop()

# =============== bstest  ===============
from urllib import request
import bs4

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs4.BeautifulSoup(target, "html.parser")

for city in soup.select("location"):
    name = city.select_one("city").string
    wf = city.select_one("wf").string
    tmn = city.select_one("tmn").string
    tmx = city.select_one("tmx").string
    print("%s : %s(%s ~ %s)" % (name, wf, tmn, tmx))

###########################################################    
## 17장 ##

# =============== foriter  ===============
nums = [11, 22, 33]
it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)

# =============== classiter  ===============
class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index:self.index + 2]

solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ',')

# =============== generator  ===============
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ',')

# =============== genexpr  ===============
data = "입춘우수경칩춘분청명곡우입하소만망종하지소서대서"
for k in (data[index:index+2] for index in range(0, len(data), 2)):
    print(k, end = ',')

# =============== rangegen  ===============
for n in [i for i in range(100)]:
    print(n, end=",")
print("")
for n in (i for i in range(100)):
    print(n, end = ',')

# =============== funcvalue  ===============
def add(a, b):
    print(a + b)

plus = add
plus(1, 2)

# =============== funcpara  ===============
def calc(op,a,b):
    op(a,b)

def add(a, b):
    print(a+b)

def multi(a,b):
    print(a*b)

calc(add,1,2)
calc(multi,3,4)

# =============== localfunc  ===============
def calcsum(n):
    def add(a, b):
        return a+b
    
    sum = 0
    for i in range(n+1):
        sum = add(sum, i)
    return sum

print("~10 =", calcsum(10))

# =============== factoryfunc  ===============
def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Morning")
hanhello = makeHello("안녕하세요")

enghello("Mr kim")
hanhello("홍길동")

# =============== wrapper  ===============
def inner():
    print("결과를 출력합니다.")

def outer(func):
    print("-" * 20)
    func()
    print("-" * 20)

outer(inner)

# =============== wrapper2  ===============
def inner():
    print("결과를 출력합니다.")

def outer(func):
    def wrapper():
        print("-" * 20)
        func()
        print("-" * 20)
    return wrapper

inner = outer(inner)
inner()

# =============== decorator  ===============
def outer(func):
    def wrapper():
        print("-" * 20)
        func()
        print("-" * 20)
    return wrapper

@outer
def inner():
    print("결과를 출력합니다.")

inner()

# =============== tagdeco  ===============
def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname():
    return "김상형"

@para
def outage():
    return "29"

print(outname())
print(outage())

# =============== deconest  ===============
def div(func):
    def wrapper():
        return "<div>" + str(func()) + "</div>"
    return wrapper

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@div
@para
def outname():
    return "김상형"

@para
@div
def outage():
    return "29"

print(outname())
print(outage())

# =============== decoarg  ===============
def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname(name):
    return "이름:" + name + "님"

@para
def outage(age):
    return "나이:" + str(age)

print(outname("김상형"))
print(outage(29))

# =============== decoarg2  ===============
def para(func):
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    return wrapper

@para
def outname(name):
    return "이름:" + name + "님"

@para
def outage(age):
    return "나이:" + str(age)

print(outname("김상형"))
print(outage(29))
print(outname.__name__)

# =============== decoarg3  ===============
from functools import wraps

def para(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    return wrapper

@para
def outname(name):
    return "이름:" + name + "님"

@para
def outage(age):
    return "나이:" + str(age)

print(outname("김상형"))
print(outage(29))
print(outname.__name__)

# =============== classwrapper  ===============
class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("-" * 20)
        self.func()
        print("-" * 20)

def inner():
    print("결과를 출력합니다.")

inner = Outer(inner)
inner()

# =============== classdeco  ===============
class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("-" * 20)
        self.func()
        print("-" * 20)

@Outer
def inner():
    print("결과를 출력합니다.")

inner()

# =============== eval  ===============
result = eval("2 + 3 * 4")
print(result)

a = 2
print(eval("a + 3"))

city = eval("['seoul', 'osan', 'suwon']")
for c in city:
    print(c, end = ', ')

# =============== simplecalc  ===============
import math

while True:
    try:
        expr = input("수식을 입력하세요(끝낼 때 0) : ")
        if expr == '0':
            break
        print(eval(expr))
    except:
        print("수식이 잘못되었습니다.")

# =============== strrepr  ===============
print(str(1234), end = ', ')
print(str(3.14), end = ', ')
print(str(['seoul', 'osan', 'suwon']), end = ', ')
print(str('korea'))

print(repr(1234), end = ', ')
print(repr(3.14), end = ', ')
print(repr(['seoul', 'osan', 'suwon']), end = ', ')
print(repr('korea'))

# =============== repreval  ===============
intexp = repr(1234)
intvalue = eval(intexp)
print(intvalue)

strexp = repr('korea')
strvalue = eval(strexp)
print(strvalue)

# =============== classrepr  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)
    def __repr__(self):
        return "Human(" + str(self.age) + ",'" + self.name + "')"

kim = Human(29, "김상형")
print(kim)
kimexp = repr(kim)
kimcopy = eval(kimexp)
print(kimcopy)

# =============== exec  ===============
exec("value = 3")
print(value)
exec("for i in range(5):print(i, end = ', ')")

# =============== exec2  ===============
for n in range(10):
    exec("""
for i in range(5):
    print(i, end = ', ')
print()
    """)

# =============== compile  ===============
code = compile("""
for i in range(5):
    print(i, end = ', ')
print()
    """, '"<string>', 'exec')

for n in range(10):
    exec(code)

###########################################################    
## 18장 ##

# =============== tkwindow  ===============
from tkinter import *
main = Tk()

main.mainloop()

# =============== widget  ===============
from tkinter import *
main = Tk()
main.title("Tk Test")
main.geometry("300x200")

lbl = Label(main, text="Label", font="Arial 20")
lbl.pack()
apple = Button(main, text="Apple", foreground="Red")
apple.pack()
orange = Button(main, text="Orange", foreground="Green")
orange.pack()

main.mainloop()

# =============== event  ===============
from tkinter import *
main = Tk()
main.title("Tk Test")
main.geometry("300x200")

lbl = Label(main, text="Label", font="Arial 20")
lbl.pack()

def appleclick():
    lbl["text"] = "Apple"
apple = Button(main, text="Apple", foreground="Red", command=appleclick)
apple.pack()

def orangeclick():
    lbl["text"] = "Orange"
orange = Button(main, text="Orange", foreground="Green", command=orangeclick)
orange.pack()

main.mainloop()

# =============== messagebox  ===============
from tkinter import *
import tkinter.messagebox

main = Tk()

def btnclick():
    if tkinter.messagebox.askyesno("질문", "당신은 미성년자입니까?"):
        tkinter.messagebox.showwarning("경고", "애들은 가라")
    else:
        tkinter.messagebox.showinfo("환영", "어서오세요. 고객님")
btn = Button(main, text="입장", foreground="Blue", command = btnclick)
btn.pack()

main.mainloop()

# =============== askstring  ===============
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()

def btnclick():
    name = tkinter.simpledialog.askstring("질문", "이름을 입력하시오")
    age = tkinter.simpledialog.askinteger("질문", "나이를 입력하시오")
    if name and age:
        tkinter.messagebox.showwarning("환영", str(age) + "세 " + name + "님 반갑습니다.")

btn = Button(main, text="클릭", foreground="Blue", command = btnclick)
btn.pack()

main.mainloop()

# =============== tkmenu  ===============
from tkinter import *
import tkinter.messagebox

main = Tk()
main.title("Tk Test")
main.geometry("300x200")

menubar = Menu(main)
main.config(menu = menubar)

popup = Menu(menubar)
menubar.add_cascade(label = "파일", menu = popup)

def about():
    tkinter.messagebox.showinfo("소개", "메뉴 사용 예제입니다.")

popup.add_command(label = "소개", command = about)
popup.add_command(label = "종료", command = quit)

main.mainloop()

# =============== canvas  ===============
from tkinter import *
main = Tk()
c = Canvas(main, width=400, height=200)
c.pack()

c.create_line(10, 10, 100, 100)
c.create_line(10, 100, 100, 10, fill="blue")
c.create_rectangle(110, 10, 200, 100, outline="red", width=5)
c.create_oval(210, 10, 300, 100, width=3, fill="yellow")

main.mainloop()

# =============== canvasimage  ===============
from tkinter import *
main = Tk()
c = Canvas(main, width = 500, height = 400)
c.pack()

img = PhotoImage(file = "child.gif")
c.create_image(10, 10, image = img, anchor = NW)

main.mainloop()

# =============== turtle  ===============
import turtle as t
t.shape("turtle")

t.forward(100)
t.right(90)
t.forward(100)
t.done()

# =============== turtletriangle  ===============
import turtle as t
t.shape("turtle")

t.right(60)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.done()

# =============== updown  ===============
import turtle as t
t.shape("turtle")

t.speed(1)
t.forward(100)
t.up()
t.forward(100)
t.down()
t.forward(100)
t.done()

# =============== drawcircle  ===============
import turtle as t
t.shape("turtle")

t.pensize(3)
t.color("blue")
t.bgcolor("green")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.done()

# =============== drawstar  ===============
import turtle as t
t.shape("turtle")

for a in range(5):
    t.forward(150)
    t.right(144)
t.done()

# =============== freeline  ===============
import turtle as t

def draw(head,dist):
    t.setheading(head)
    t.forward(dist)

def toleft():
    draw(180, 15)

def toright():
    draw(0, 15)

def toup():
    draw(90, 15)

def todown():
    draw(270, 15)

def move(x,y):
    t.up()
    t.setpos(x,y)
    t.down()
        
t.shape("turtle")
t.speed(0)
t.onkeypress(toleft, "Left")
t.onkeypress(toright, "Right")
t.onkeypress(toup, "Up")
t.onkeypress(todown, "Down")
t.onscreenclick(move)
t.listen()
t.done()

# =============== freeline2  ===============
import turtle as t

def draw(x, y):
    t.setpos(x, y)

def move(x, y):
    t.up()
    t.setpos(x, y)
    t.down()


t.shape("turtle")
t.speed(0)
t.pensize(3)
t.onscreenclick(draw)
t.onscreenclick(move, 3)
t.onkeypress(lambda :t.color("red"), "r")
t.onkeypress(lambda :t.color("green"), "g")
t.onkeypress(lambda :t.color("blue"), "b")
t.onkeypress(lambda :t.color("black"), "k")
t.onkeypress(lambda :t.pensize(1), "1")
t.onkeypress(lambda :t.pensize(3), "3")
t.onkeypress(lambda :t.pensize(5), "5")
t.listen()
t.done()

###########################################################    
## 부록 ##

# =============== print("Triangle")  ===============
for y in range(1, 10) :
    for x in range(y) :
        print('*', end = '')
    print()

# =============== CharmUtil  ===============
def add(a, b):
    return a + b

print(add(2, 3))

###########################################################    
## 온라인 강좌 ##

# =============== readgreen  ===============
color = 0xaa80ff
green = (color & 0x00ff00) >> 8
print("초록색 강도 =", green)

# =============== forelse  ===============
score = [ 92, 86, 68, 77, 56]
for s in score:
    print(s)
else:
    print("다 출력했습니다.")

# =============== breakelse  ===============
score = [ 92, 86, 68, 120, 56]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
else:
    print("다 출력했습니다.")

# =============== makedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""CREATE TABLE tblAddr
    (name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)""")

cursor.execute("INSERT INTO tblAddr VALUES ('김상형', '123-4567', '오산')")
cursor.execute("INSERT INTO tblAddr VALUES ('한경은', '555-1004', '수원')")
cursor.execute("INSERT INTO tblAddr VALUES ('한주완', '444-1092', '대전')")

con.commit()

cursor.close()
con.close()

# =============== selectdb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")
table = cursor.fetchall()
for record in table:
    print("이름 : %s, 전화 : %s, 주소 : %s" % record)

cursor.close()
con.close()

# =============== selectdb2  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")
while True:
    record = cursor.fetchone()
    if record == None:
        break
    print("이름 : %s, 전화 : %s, 주소 : %s" % record)

cursor.close()
con.close()

# =============== drderby  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr ORDER BY addr")
table = cursor.fetchall()
for record in table:
    print("이름 : %s, 전화 : %s, 주소 : %s" % record)

cursor.close()
con.close()

# =============== orderbydesc  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT addr FROM tblAddr WHERE name = '김상형'")
record = cursor.fetchone()
print("김상형은 %s에 살고 있습니다." % record)

cursor.close()
con.close()

# =============== updatedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'")
con.commit()

cursor.close()
con.close()

# =============== deletedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DELETE FROM tblAddr WHERE name = '김상형'")
con.commit()

cursor.close()
con.close()

# =============== wxApp  ===============
import wx

app = wx.App()
frame = wx.Frame(None)

frame.Show(True)
app.MainLoop()

# =============== wxApp2  ===============
import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()

# =============== wxApp3  ===============
import wx

app = wx.App()
frame = wx.Frame(None)

size = wx.Size(600, 400)
frame.SetSize(size)
pos = wx.Point(100, 100)
frame.SetPosition(pos)
color = wx.Colour(0, 0, 255, 0)
frame.SetBackgroundColour(color)
frame.SetTitle("파이썬으로 만든 윈도우")
frame.SetWindowStyle(wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)

frame.Show(True)
app.MainLoop()

# =============== KeyEvent  ===============
import wx

app = wx.App()
frame = wx.Frame(None)

def OnLeftDown(event):
    # x, y = event.GetPosition()
    message = "(%d, %d) 를 클릭했습니다." % (event.x, event.y)
    wx.MessageBox(message, "알림", wx.OK)
frame.Bind(wx.EVT_LEFT_DOWN, OnLeftDown)

def OnKeyDown(event):
    message = "%d 키를 눌렀습니다." % event.KeyCode
    wx.MessageBox(message, "알림", wx.OK)
frame.Bind(wx.EVT_KEY_DOWN, OnKeyDown)

frame.Show(True)
app.MainLoop()

# =============== Button  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn = wx.Button(frame, label="Click")
def OnClick(event):
    wx.MessageBox("버튼을 클릭하였습니다.", "알림", wx.OK)
btn.Bind(wx.EVT_BUTTON, OnClick)

frame.Show(True)
app.MainLoop()

# =============== ButtonStatic  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn = wx.Button(frame, label="Click")
def OnClick(event):
    wx.MessageBox("버튼을 클릭하였습니다.", "알림", wx.OK)
btn.Bind(wx.EVT_BUTTON, OnClick)
lbl = wx.StaticText(frame, label="Text")

btn.SetPosition(wx.Point(150, 100))
lbl.SetPosition(wx.Point(180, 60))

frame.Show(True)
app.MainLoop()

# =============== BoxSizer  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(btn1)
box.Add(btn2)
box.Add(btn3)

frame.Show(True)
app.MainLoop()

# =============== BoxSizer2  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(btn1, proportion = 0)
box.Add(btn2, proportion = 1)
box.Add(btn3, proportion = 2)

frame.Show(True)
app.MainLoop()

# =============== BoxSizer3  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(btn1, border = 10)
box.Add(btn2, border = 10, flag = wx.ALL)
box.Add(btn3, border = 10)

frame.Show(True)
app.MainLoop()

# =============== BoxSizer4  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(btn1)
box.Add(btn2, flag = wx.ALIGN_CENTER)
box.Add(btn3, flag = wx.ALIGN_BOTTOM)

frame.Show(True)
app.MainLoop()

# =============== StaticBoxSizer  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

radio1 = wx.RadioButton(frame, label="저그", style = wx.RB_GROUP)
radio2 = wx.RadioButton(frame, label="프로토스")
radio3 = wx.RadioButton(frame, label="테란")

box = wx.StaticBoxSizer(wx.HORIZONTAL, frame, "종족")
frame.SetSizer(box)
box.Add(radio1)
box.Add(radio2)
box.Add(radio3)

frame.Show(True)
app.MainLoop()

# =============== GridSizer  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")
btn4 = wx.Button(frame, label="Button4")
btn5 = wx.Button(frame, label="Button5")
btn6 = wx.Button(frame, label="Button6")

grid = wx.GridSizer(2, 3, 15, 15)
frame.SetSizer(grid)
grid.Add(btn1, 0, wx.EXPAND)
grid.Add(btn2, 0, wx.EXPAND)
grid.Add(btn3, 0, wx.EXPAND)
grid.Add(btn4, 0, wx.EXPAND)
grid.Add(btn5, 0, wx.EXPAND)
grid.Add(btn6, 0, wx.EXPAND)

frame.Show(True)
app.MainLoop()

# =============== FlexGridSizer  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn1 = wx.Button(frame, label="Button1")
btn2 = wx.Button(frame, label="Button2")
btn3 = wx.Button(frame, label="Button3")
btn4 = wx.Button(frame, label="Button4")
btn5 = wx.Button(frame, label="Button5")
btn6 = wx.Button(frame, label="Button6")

grid = wx.FlexGridSizer(2, 3, 15, 15)
frame.SetSizer(grid)
grid.Add(btn1, 0, wx.EXPAND)
grid.Add(btn2, 0, wx.EXPAND)
grid.Add(btn3, 0, wx.EXPAND)
grid.Add(btn4, 0, wx.EXPAND)
grid.Add(btn5, 0, wx.EXPAND)
grid.Add(btn6, 0, wx.EXPAND)

grid.AddGrowableCol(2)
grid.AddGrowableRow(1)

frame.Show(True)
app.MainLoop()

# =============== Panel  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

panelhorz = wx.Panel(frame)
btn1 = wx.Button(panelhorz, label="Button1")
btn2 = wx.Button(panelhorz, label="Button2")
btn3 = wx.Button(panelhorz, label="Button3")
sizerhorz = wx.BoxSizer(wx.HORIZONTAL)
sizerhorz.Add(btn1)
sizerhorz.Add(btn2)
sizerhorz.Add(btn3)
panelhorz.SetSizer(sizerhorz)

panelvert = wx.Panel(frame)
static1 = wx.StaticText(panelvert, label="StaticText1")
static2 = wx.StaticText(panelvert, label="StaticText2")
static3 = wx.StaticText(panelvert, label="StaticText3")
sizervert = wx.BoxSizer(wx.VERTICAL)
sizervert.Add(static1)
sizervert.Add(static2)
sizervert.Add(static3)
panelvert.SetSizer(sizervert)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(panelhorz, border = 10, flag = wx.DOWN)
box.Add(panelvert, border = 10, flag = wx.UP)

frame.Show(True)
app.MainLoop()

# =============== Panel2  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

static = wx.StaticText(frame, label="Fruit")

panelhorz = wx.Panel(frame)
btnApple = wx.Button(panelhorz, label="Apple")
def onApple(event):
    static.SetLabelText("Apple")
btnApple.Bind(wx.EVT_BUTTON, onApple)
btnOrange = wx.Button(panelhorz, label="Orange")
def onOrange(event):
    static.SetLabelText("Orange")
btnOrange.Bind(wx.EVT_BUTTON, onOrange)
sizerhorz = wx.BoxSizer(wx.HORIZONTAL)
sizerhorz.Add(btnApple)
sizerhorz.Add(btnOrange)
panelhorz.SetSizer(sizerhorz)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(static, border = 20, flag = wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)
box.Add(panelhorz, flag = wx.ALIGN_CENTER_HORIZONTAL)

frame.Show(True)
app.MainLoop()

# =============== Text  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

text = wx.TextCtrl(frame)
btn = wx.Button(frame, label="Click")
def onClick(event):
    str = text.GetValue()
    wx.MessageBox(str, "입력내용", wx.OK)
btn.Bind(wx.EVT_BUTTON, onClick)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(text)
box.Add(btn)

frame.Show(True)
app.MainLoop()

# =============== EvtText  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

text = wx.TextCtrl(frame)
def onTextChange(event):
    str = text.GetValue()
    frame.SetTitle(str)
text.Bind(wx.EVT_TEXT, onTextChange)

frame.Show(True)
app.MainLoop()

# =============== CheckBox  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

chkvisible = wx.CheckBox(frame, label = "보임")
chkvisible.SetValue(wx.CHK_CHECKED)
def onvisible(event):
    if chkvisible.GetValue() == wx.CHK_CHECKED:
        btn.Show(True)
    else:
        btn.Show(False)
chkvisible.Bind(wx.EVT_CHECKBOX, onvisible)

chkenable = wx.CheckBox(frame, label = "사용가능")
chkenable .SetValue(wx.CHK_CHECKED)
def onenable(event):
    if chkenable.GetValue() == wx.CHK_CHECKED:
        btn.Enable(True)
    else:
        btn.Enable(False)
chkenable.Bind(wx.EVT_CHECKBOX, onenable)

btn = wx.Button(frame, label="Click")
def onClick(event):
    wx.MessageBox("클릭했습니다.", "알림", wx.OK)
btn.Bind(wx.EVT_BUTTON, onClick)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(chkvisible)
box.Add(chkenable)
box.Add(btn)

frame.Show(True)
app.MainLoop()

# =============== RadioButton  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

red = wx.RadioButton(frame, label = "빨강", style = wx.RB_GROUP)
def onred(event):
    frame.SetBackgroundColour(wx.Colour(255, 0, 0, 0))
    frame.Refresh()
red.Bind(wx.EVT_RADIOBUTTON, onred)

green = wx.RadioButton(frame, label = "초록",)
def ongreen(event):
    frame.SetBackgroundColour(wx.Colour(0, 255, 0, 0))
    frame.Refresh()
green.Bind(wx.EVT_RADIOBUTTON, ongreen)

blue = wx.RadioButton(frame, label = "파랑",)
def onblue(event):
    frame.SetBackgroundColour(wx.Colour(0, 0, 255, 0))
    frame.Refresh()
blue.Bind(wx.EVT_RADIOBUTTON, onblue)

yellow = wx.RadioButton(frame, label = "노랑",)
def onyellow(event):
    frame.SetBackgroundColour(wx.Colour(255, 255, 0, 0))
    frame.Refresh()
yellow.Bind(wx.EVT_RADIOBUTTON, onyellow)
yellow.SetValue(True)

box = wx.StaticBoxSizer(wx.VERTICAL, frame, "배경색")
frame.SetSizer(box)
box.Add(red)
box.Add(green)
box.Add(blue)
box.Add(yellow)

frame.SetBackgroundColour(wx.Colour(255, 255, 0, 0))
frame.Show(True)
app.MainLoop()

# =============== ListBox  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

panel = wx.Panel(frame)
colorname = ["빨강", "초록", "파랑", "노랑", "하양", "검정"]
colorvalue = [wx.Colour(255, 0, 0, 0), wx.Colour(0, 255, 0, 0), wx.Colour(0, 0, 255, 0),
              wx.Colour(255, 255, 0, 0), wx.Colour(255, 255, 255, 0), wx.Colour(0, 0, 0, 0)]

colorlist = wx.ListBox(panel, choices = colorname)
colorlist.SetSize(wx.Size(100, 150))
colorlist.SetPosition(wx.Point(100, 20))
def onitemchange(event):
    name = colorlist.GetSelection()
    color = colorvalue[name]
    frame.SetBackgroundColour(color)
    frame.Refresh()
colorlist.Bind(wx.EVT_LISTBOX, onitemchange)

frame.Show(True)
app.MainLoop()

# =============== ComboBox  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

desc = wx.StaticText(frame, label = "먹고 싶은 과자를 고르시오.")
snack = ["오징어 땅콩", "꼬깔콘", "맛동산", "초코파이"]
combo = wx.ComboBox(frame, choices = snack)
result = wx.StaticText(frame, label = "")

def onitemchange(event):
    idx = combo.GetCurrentSelection()
    result.SetLabelText(snack[idx] + " 맛있게 드세요.")
combo.Bind(wx.EVT_COMBOBOX, onitemchange)
def oniteminput(event):
    result.SetLabelText(combo.GetValue() + " 맛있게 드세요.")
combo.Bind(wx.EVT_TEXT_ENTER, oniteminput)

box = wx.BoxSizer(wx.VERTICAL)
frame.SetSizer(box)
box.Add(desc)
box.Add(combo)
box.Add(result)

frame.Show(True)
app.MainLoop()

# =============== MenuBar  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

menubar = wx.MenuBar()
file = wx.Menu()
menubar.Append(file, "파일")
about = wx.MenuItem(id = wx.ID_ANY, text="소개")
file.Append(about)
file.AppendSeparator()
exit = wx.MenuItem(id = wx.ID_ANY, text="종료")
file.Append(exit)
frame.SetMenuBar(menubar)

def onAbout(event):
    wx.MessageBox("메뉴를 사용하는 프로그램입니다.", "알림", wx.OK)
frame.Bind(wx.EVT_MENU, onAbout, about)

def onExit(event):
    frame.Close()
frame.Bind(wx.EVT_MENU, onExit, exit)

frame.Show(True)
app.MainLoop()

# =============== PaintDC  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

def OnPaint(event):
    dc = wx.PaintDC(frame)
    dc.DrawLine(10, 10, 110, 110)
    dc.SetPen(wx.Pen(wx.Colour(255,0,0,0), 6))
    dc.SetBrush(wx.Brush(wx.Colour(255,255,0,0)))
    dc.DrawCircle(150,60,50)
    dc.SetPen(wx.Pen(wx.Colour(0,0,255,0), 3))
    dc.SetBrush(wx.Brush(wx.Colour(0,255,0,0)))
    dc.DrawRectangle(210, 10, 100, 100)
frame.Bind(wx.EVT_PAINT, OnPaint)

frame.Show(True)
app.MainLoop()

# =============== gameloop  ===============
import pygame
import random

pygame.init()
surface = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()
color = pygame.color.Color(128, 128, 128)
running = True
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            color.r = random.randint(0, 255)
            color.g = random.randint(0, 255)
            color.b = random.randint(0, 255)
        elif event.type == pygame.QUIT:
            running = False

    surface.fill(color)
    pygame.display.flip()
    count += 1
    pygame.display.set_caption(str(count))
    clock.tick(30)
pygame.quit()

# =============== gameloop2  ===============
import pygame

pygame.init()
surface = pygame.display.set_mode((300, 200))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill(0xffffff)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

# =============== gamedraw  ===============
import pygame

pygame.init()
surface = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill(0xffffff)
    pygame.draw.line(surface, 0xff0000, (10, 10), (110,110), 3)
    pygame.draw.circle(surface,0x0000ff, (150, 60), 50, 3)
    pygame.draw.rect(surface, 0x000000, [(210, 10), (100, 100)], 3)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

# =============== gameimage  ===============
import pygame

pygame.init()
surface = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
running = True

img = pygame.image.load("flower.jpg")
rect = img.get_rect()
rect.y = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill(0xffffff)
    surface.blit(img, rect)
    rect.x += 1
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

# =============== gamesound  ===============
import pygame

pygame.init()
surface = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
running = True

gun = pygame.mixer.Sound("GUN_SHOT.WAV")
blast = pygame.mixer.Sound("BLAST.WAV")
arial = pygame.font.SysFont("Arial", 30)
usage = arial.render("Press A or B key", True, (0, 0, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                gun.play()
            elif event.key == pygame.K_b:
                blast.play()

    surface.fill(0xffffff)
    surface.blit(usage, (100, 100))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()




