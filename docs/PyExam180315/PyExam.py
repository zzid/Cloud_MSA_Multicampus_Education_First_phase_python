# ���̽� ���� ����

###########################################################    
## 2�� ##

# =============== print ===============
print(3 + 4)
4 * 5				# ���õȴ�.
a = 1
b = 2
print(a + b)

# =============== printsep ===============
s = '����'
d = '����'
g = '�뱸'
b = '�λ�'
print(s, d, g, b, sep = ' ��� ')

# =============== printtwo ===============
a = '������'
b = '�����'
print(a)
print(b)

# =============== printend ===============
a = '������'
b = '�����'
print(a, end = '')
print(b)

# =============== intinput  ===============
price = input('������ �Է��ϼ��� : ')
num = input('������ �Է��ϼ��� : ')
sum = int(price) * int(num)
print('�Ѿ���', sum, '���Դϴ�')

# ===============  intinput2  ===============
price = int(input('������ �Է��ϼ��� : '))
num = int(input('������ �Է��ϼ��� : '))
sum = price * num
print('�Ѿ���', sum, '���Դϴ�')

# =============== inputname  ===============
name = input('�̸��� �Է��ϼ��� : ')
print('�ȳ��ϼ���', name, '��')

###########################################################    
## 3�� ##

# =============== intradix  ===============
print(hex(26))
print(oct(26))
print(bin(13))

# =============== longstring  ===============
s = """������ �ǳʼ� �й� ���� ������ �� ������ ���� ���׳�
���� ���ٱ� ���� ��鸮 �� �ʹ� �������� Ÿ�� �����
������ �� ������ ���� ���׳�"""
print(s)

# =============== longstring2  ===============
s = "������ �ǳʼ� �й� ���� ������ �� ������ ���� ���׳� \
���� ���ٱ� ���� ��鸮 �� �ʹ� �������� Ÿ�� ����� \
������ �� ������ ���� ���׳�"
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
member = ['�տ���', '���Ȱ�', '�����', '�������']
for m in member:
    print(m, "�⵿")

# =============== tupledump  ===============
member = ('�տ���', '���Ȱ�', '�����', '�������')
for m in member:
    print(m, "�⵿")

###########################################################    
## 4�� ##

# =============== round  ===============
print(int(2.54))			# 2
print(round(2.54))		# 3
print(round(2.54, 1))		# 2.5
print(round(123456, -3))		# 123000

###########################################################    
## 5�� ##

# =============== if  ===============
age = int(input("�� ����̴�? "))
if age < 19:
    print("�ֵ��� ����")

# =============== compare  ===============
a = 3
if a == 3:
    print("3�̴�")
if a > 5:
    print("5���� ũ��")
if a < 5:
    print("5���� �۴�")

# =============== stringcompare  ===============
country = "Korea"
if country == "Korea":
    print("�ѱ��Դϴ�.")
if country == "korea":
    print("���ѹα��Դϴ�.")

# =============== stringcompare2  ===============
if ("korea" > "japan"):
    print("�ѱ��� �� ũ��")
if ("korea" < "japan"):
    print("�Ϻ��� �� ũ��")

# =============== intbool  ===============
energy = 1
if energy:
    print("������ �ο��")

# =============== andrange  ===============
a = 3
if a > 1 and a < 10:
    print("OK")

# =============== block  ===============
age = 16
if age < 19:
    print("�ֵ��� ����")
    print("���� ������ �ؾ���")

# =============== block2  ===============
age = 22
if age < 19:
    print("�ֵ��� ����")
print("���� ������ �ؾ���")

# =============== ifelse  ===============
age = 22
if age < 19:
    print("�ֵ��� ����")
else:
    print("� �ɼ�")

# =============== ifblock  ===============
age = 12
if age < 19:
    print("�ֵ��� ����")
    print("���� ������ �ؾ���")
else:
    print("� �ɼ�")
    print("��ſ� �ð� �Ǽ���")

# =============== ifelif  ===============
age = 23
if age < 19:
    print("�ֵ��� ����")
elif age < 25:
    print("���л��Դϴ�")
else:
    print("� �ɼ�")

# =============== elif  ===============
money = 6500
if money >= 20000:
    print("�������� �Դ´�")
elif money >= 10000:
    print("��� ¥���� �Դ´�")
elif money >= 6000:
    print("«���� �Դ´�")
elif money >= 4000:
    print("¥����� �Դ´�")
else:
    print("�ܹ����� �Դ´�")

# =============== ifif  ===============
man = True
age = 22
if man == True:
    if age >= 19:
        print("���� �����Դϴ�.")

# =============== ifif2  ===============
Man = True
age = 22
if man == True:
    if age >= 19:
        print("���� �����Դϴ�.")
    else:
        print("�ҳ��Դϴ�.")

###########################################################    
## 6�� ##

# =============== while  ===============
student = 1
while student <= 5:
    print(student, "�� �л��� ������ ó���Ѵ�.")
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
    print(student, "�� �л��� ������ ó���Ѵ�.")

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
print("���� ó�� ��")

# =============== continue  ===============
score = [ 92, 86, 68, -1, 56]
for s in score:
    if (s == -1):
        continue
    print(s)
print("���� ó�� ��")

# =============== gugudan  ===============
for dan in range(2, 10):
    print(dan, "��")
    for hang in range(2, 10):
        print(dan, "*", hang, "=", dan * hang)
    print()

# =============== gugudanwhile  ===============
dan = 2
while dan <= 9:
    hang = 2
    print(dan, "��")
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
    a = int(input("������ �Է��Ͻÿ� : "))
    if (a == 7): break
print("�� ���߾��")

# =============== zerobase  ===============
for ten in range(0, 5) :
    for num in range(ten * 10, ten * 10 + 10) :
        print(num, end = ',')
    print()

###########################################################    
## 7�� ##

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
    print("���� :", sum)
    if (option['avg'] == True ):
        print("��� :", sum / len(score))

calcscore("�����", 88, 99, 77, avg = True)
calcscore("���ѽ�", 99, 98, 95, 89, avg = False)

# =============== local  ===============
def kim():
    temp = "������� �Լ�"
    print(temp)

kim()
print(temp)

# =============== local2  ===============
def kim():
    temp = "������� �Լ�"
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
    print("������ ������ :", salerate)

def lee():
    price = 1000
    print("���� :", price * salerate)

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
    """1 ~ n������ �հ踦 ���� �����Ѵ�."""
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
## 8�� ##

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
print("�Կ� ��¥ : " + file[4:6] + "�� " + file[6:8] + "��")
print("�Կ� �ð� : " + file[9:11] + "�� " + file[11:13] + "��")
print("Ȯ���� : " + file[-3:])

# =============== slice3  ===============
yoil = "��ȭ���������"
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
s = """�����̶� �����Ҽ��� �������Ƿ� �������� ���ƾ� �� ������ �������� 
�������� �ϴ� ������ ���� �����̶�� �����մϴ�."""
print("������ ���� Ƚ�� :", s.count('����'))

# =============== in  ===============
s = "python programming"
print('a' in s)
print('z' in s)
print('pro' in s)
print('x' not in s)

# =============== startswith  ===============
name = "���Ѱ�"
if name.startswith("��"):
    print("�谡�Դϴ�.")
if name.startswith("��"):
    print("�Ѱ��Դϴ�.")

file = "girl.jpg"
if file.endswith(".jpg"):
    print("�׸� �����Դϴ�.")

# =============== isdecimal  ===============
height = input("Ű�� �Է��ϼ��� :")
if height.isdecimal():
    print("Ű =", height)
else:
    print("���ڸ� �Է��ϼ���.")

# =============== lower  ===============
s = "Good morning. my love KIM."
print(s.lower())
print(s.upper())
print(s)

print(s.swapcase())
print(s.capitalize())
print(s.title())

# =============== strlower  ===============
python = input("���̽��� ���� ö�ڸ� �Է��Ͻÿ� : ")
if python.lower() == "python":
    print("������ϴ�.")

# =============== strip  ===============
s = "  angel   "
print(s + "��")
print(s.lstrip() + "��")
print(s.rstrip() + "��")
print(s.strip() + "��")

# =============== split  ===============
s = "¥�� «�� ����"
print(s.split())

s2 = "����->����->�뱸->�λ�"
city = s2.split("->")
print(city)
for c in city:
    print(c, "���", end = ' ')

# =============== splitlines  ===============
traveler = """������ �ǳʼ�\n�й� ����\n\n������ �� ������\n���� ���׳�\n
���� ���ٱ�\n���� ��鸮\n\n�� �ʹ� ��������\nŸ�� �����\n
������ �� ������\n���� ���׳�"""
poet = traveler.splitlines()
for line in poet:
    print(line)

# =============== join  ===============
s = "._."
print(s.join("���ѹα�"))

# =============== splitjoin  ===============
s2 = "����->����->�뱸->�λ�"
city = s2.split("->")
print(" ��� ".join(city))

# =============== replace  ===============
s = "������ �Ϻ����̴�. �븶���� �Ϻ����̴�."
print(s)
print(s.replace("�Ϻ�", "�ѱ�"))

# =============== just  ===============
message = "�ȳ��ϼ���."
print(message.ljust(30))
print(message.rjust(30))
print(message.center(30))

# =============== center  ===============
traveler = """������ �ǳʼ�\n�й� ����\n\n������ �� ������\n���� ���׳�\n
���� ���ٱ�\n���� ��鸮\n\n�� �ʹ� ��������\nŸ�� �����\n
������ �� ������\n���� ���׳�"""
poet = traveler.splitlines()
for line in poet:
    print(line.center(30))

# =============== stringcat  ===============
price = 500
print("�ñ��ϸ� " + str(price) + "��!")

# =============== format  ===============
price = 500
print("�ñ��ϸ� %d��!" % price)

# =============== format2  ===============
month = 8
day = 15
anni = "������"
print("%d�� %d���� %s�̴�." % (month, day, anni))

# =============== width  ===============
value = 123
print("###%d###" % value)
print("###%5d###" % value)
print("###%10d###" % value)
print("###%1d###" % value)

# =============== align  ===============
price = [30, 13500, 2000]
for p in price:
    print("����:%d��" % p)
for p in price:
    print("����:%7d��" % p)

# =============== numalign  ===============
price = [30, 13500, 2000]
for p in price:
    print("����:%-7d��" % p)

# =============== precision  ===============
pie = 3.14159265
print("%10f" % pie)
print("%10.8f" % pie)
print("%10.5f" % pie)
print("%10.2f" % pie)

# =============== newformat  ===============
name = "�Ѱ�"
age = 16
height = 162.5
print("�̸�:{}, ����:{}, Ű:{}".format(name, age, height))

# =============== newformat2  ===============
name = "�Ѱ�"
age = 16
height = 162.5
print("�̸�:{0:s}, ����:{1:d}, Ű:{2:f}".format(name, age, height))

# =============== newformat3  ===============
name = "�Ѱ�"
age = 16
height = 162.5
print("�̸�:{0:10s}, ����:{1:5d}, Ű:{2:8.2f}".format(name, age, height))

# =============== newformat4  ===============
name = "�Ѱ�"
age = 16
height = 162.5
print("�̸�:{0:^10s}, ����:{1:>5d}, Ű:{2:<8.2f}".format(name, age, height))

# =============== newformat5  ===============
name = "�Ѱ�"
age = 16
height = 162.5
print("�̸�:{0:$^10s}, ����:{1:>05d}, Ű:{2:!<8.2f}".format(name, age, height))

###########################################################    
## 9�� ##

# =============== listscore  ===============
score = [ 88, 95, 70, 100, 99 ]
sum = 0
for s in score:
    sum += s
print("���� : ", sum)
print("��� : ", sum / len(score))

# =============== listslice  ===============
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])        # 2~5����
print(nums[:4])         # ó������ 4����
print(nums[6:])         # 6���� ������
print(nums[1:7:2])      # 1~7���� �ϳ��� �ǳʶٸ�

# =============== listassign  ===============
score = [ 88, 95, 70, 100, 99 ]
print(score[2])     # 70
score[2] = 55       # �� ����
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
    print("���� %d, ��� %.2f" % (sum, sum / subjects))
    total += sum
    totalsub += subjects
print("��ü��� %.2f" % (total / totalsub))

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
print("���� ���� �л��� " + str(perfect) + "���Դϴ�.")
pernum = score.count(100)
print("������ ���� " + str(pernum) + "���Դϴ�")

# =============== listmin  ===============
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
print("�л� ���� %d���Դϴ�." % len(score))
print("�ְ� ������ %d���Դϴ�." % max(score))
print("���� ������ %d���Դϴ�." % min(score))

# =============== listin  ===============
ans = input("���� �Ͻðڽ��ϱ�? ")
if ans in ['yes', 'y', 'ok', '��', '���']:
    print("������ �ּż� �����մϴ�.")
else:
    print("�ȳ��� ������.")

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
print("���� : ", sum)
print("��� : ", sum / len(score))

# =============== onetuple  ===============
tu = 2,
value = 2
print(tu)
print(value)

# =============== tupleop  ===============
tu = 1, 2, 3, 4, 5
print(tu[3])         # ����
print(tu[1:4])       # ����
print(tu + (6, 7))    # ����
print(tu * 2)        # ����      
tu[1] = 100          # �Ұ���
del tu[1]            # �Ұ���

# =============== unpacking  ===============
tu = "�̼���", "������", "������"
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
print("������ %d�� %d���Դϴ�" % (result[0], result[1]))

# =============== divmod  ===============
d, m = divmod(7, 3)
print("��", d)
print("������", m)

# =============== convertlist  ===============
score = [ 88, 95, 70, 100, 99 ]
tu = tuple(score)
#tu[0] = 100
print(tu)
li = list(tu)
li[0] = 100
print(li)

###########################################################    
## 10�� ##

# =============== dic  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
print(dic)

# =============== dicread  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
print(dic['boy'])
print(dic['book'])

# =============== dicget  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
print(dic.get('student'))
print(dic.get('student', '������ ���� �ܾ��Դϴ�.'))

# =============== dicin  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
if 'student' in dic:
    print("������ �ִ� �ܾ��Դϴ�.")
else:
    print("�� �ܾ�� ������ �����ϴ�.")

# =============== dicchange  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
dic['boy'] = '���ھ�'
dic['girl'] = '�ҳ�'
del dic['book']
print(dic)

# =============== keys  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
print(dic.keys())
print(dic.values())
print(dic.items())

# =============== keylist  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
keylist = dic.keys()
for key in keylist:
    print(key)

# =============== dicupdate  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
dic2 = { 'student':'�л�', 'teacher':'������', 'book':'����' }
dic.update(dic2)
print(dic)

# =============== listtodic  ===============
li = [ ['boy', '�ҳ�'], ['school', '�б�'], ['book', 'å'] ]
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
print(set(("������", "���ֿ�", "���·�")))
print(set({'boy':'�ҳ�', 'school':'�б�', 'book':'å'}))
print(set())

# =============== setedit  ===============
asia = { 'korea', 'china', 'japan' }
asia.add('vietnam')         # �߰�
asia.add('china')           # �߰� �ȵ�
asia.remove('japan')        # ����
print(asia)

asia.update({'singapore', 'hongkong', 'korea'})
print(asia)

# =============== setop  ===============
twox = { 2, 4, 6, 8, 10, 12 }
threex = { 3, 6, 9, 12, 15 }

print("������", twox & threex)
print("������", twox | threex)
print("������", twox - threex)
print("������", threex - twox)
print("��Ÿ�� ������", twox ^ threex)

# =============== setin  ===============
mammal = { '�ڳ���', '����', '����', '��', '���', '������', '��' }
primate = { '���', '������', '����' }

if '����' in mammal:
    print("���ڴ� �������̴�")
else:
    print("���ڴ� �������� �ƴϴ�.")

print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)

###########################################################    
## 11�� ##

# =============== sequence  ===============
score = [ 88, 95, 70, 100, 99 ]
for s in score:
    print("���� :", s)

# =============== sequence2  ===============
score = [ 88, 95, 70, 100, 99 ]
no = 1
for s in score:
    print(str(no) + "�� �л��� ���� :", s)
    no += 1

# =============== sequence3  ===============
score = [ 88, 95, 70, 100, 99 ]
for no in range(len(score)):
    print(str(no + 1) + "�� �л��� ���� :", score[no])

# =============== enumerate  ===============
score = [ 88, 95, 70, 100, 99 ]
for no, s in enumerate(score, 1):
    print(str(no) + "�� �л��� ���� :", s)

# =============== zip  ===============
yoil = ["��", "ȭ", "��", "��","��", "��", "��"]
food = ["������", "���뱹", "Į����", "����"]
menu = zip(yoil, food)
for y, f in menu:
    print("%s���� �޴� : %s" % (y, f))

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
## 12�� ##

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
print("%d�� %d�� %d��" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))

# =============== datetime  ===============
import datetime

now = datetime.datetime.now()
print("%d�� %d�� %d��" % (now.year, now.month, now.day))
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

print("�ȳ��ϼ���.")
time.sleep(1)
print("�㿡 ���ð��� �� �� ������ �����?")
time.sleep(5)
print("�߰����ð��Դϴ�.")

# =============== sleep2  ===============
import time

for dan in range(2, 10):
    print(dan, "��")
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

yoil = ['��', 'ȭ', '��', '��', '��', '��', '��']
day = calendar.weekday(2020,8,15)
print("��������", yoil[day] + "�����̴�." )

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

food = ["¥���", "«��", "������", "������"]
print(random.choice(food))

# =============== shuffle  ===============
import random

food = ["¥���", "«��", "������", "������"]
print(food)
random.shuffle(food)
print(food)

# =============== sample  ===============
import random

food = ["¥���", "«��", "������", "������"]
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
    print("�����Դϴ�.")
else:
    print("Ʋ�Ƚ��ϴ�.")

# =============== mathquiz2  ===============
import random

correct = 0
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    question = "%d + %d = ?(���� ���� 0) " % (a, b)
    c = int(input(question))

    if c == 0:
        break
    elif c == a + b:
        print("�����Դϴ�.")
        correct = correct + 1
    else:
        print("Ʋ�Ƚ��ϴ�.")

print("%d �� ������ϴ�." % correct)

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

    question = "%d %s %d = ?(���� ���� 0) " % (a, mark, b)
    c = int(input(question))

    if c == 0:
        break
    elif c == ans:
        print("�����Դϴ�.")
        correct = correct + 1
    else:
        print("Ʋ�Ƚ��ϴ�.")

print("%d �� ������ϴ�." % correct)

# =============== randnum  ===============
import random

secret = random.randint(1,100)
while True:
    num = int(input("���ڸ� �Է��ϼ���(���� �� 0) : "))
    if num == 0:
        break
    if num == secret:
        print("������ϴ�")
        break
    elif num > secret:
        print("�Է��� ���ں��� �� �۽��ϴ�.")
    else:
        print("�Է��� ���ں��� �� Ů�ϴ�")

# =============== randnum2  ===============
import random

secret = random.randint(1,100)
count = 0
while True:
    num = int(input("���ڸ� �Է��ϼ���(���� �� 0) : "))
    if num == 0:
        break
    count += 1
    if num == secret:
        print("%d������ ������ϴ�" % count)
        break
    elif num > secret:
        print("�Է��� ���ں��� �� �۽��ϴ�.")
    else:
        print("�Է��� ���ں��� �� Ů�ϴ�")

# =============== sys  ===============
import sys

print("���� :", sys.version)
print("�÷��� :", sys.platform)
if (sys.platform == "win32"):
    print(sys.getwindowsversion())
print("����Ʈ ���� :", sys.byteorder)
print("��� ��� :", sys.path)
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
    print("�μ��� 2�� ���Ͽ��� �մϴ�.")

# =============== datecalc  ===============
import sys
import time

if (len(sys.argv) != 2):
    print("���� ��¥�� yyyymmdd�� �Է��Ͻʽÿ�.")
    sys.exit(0)

birth = sys.argv[1]
if (len(birth) != 8 or birth.isnumeric() == False):
    print("��¥ ������ �߸��Ǿ����ϴ�.")
    sys.exit(0)

tm = (int(birth[:4]), int(birth[4:6]), int(birth[6:8]), 0, 0, 0, 0, 0, 0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)

# =============== ellapsedate2  ===============
import sys
import time

year = int(input("�¾ �⵵�� �Է��ϼ���(4�ڸ�) : "))
month = int(input("�¾ ���� �Է��ϼ��� : "))
day = int(input("�¾ ���� �Է��ϼ��� : "))

tm = (year, month, day, 0, 0, 0, 0, 0, 0)
ellapse = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
print(ellapse)

###########################################################    
## 13�� ##

# =============== exception  ===============
str = "89��"
score = int(str)
print(score)
print("�۾��Ϸ�")

# =============== tryexcept  ===============
str = "89��"
try:
    score = int(str)
    print(score)
except:
    print("���ܰ� �߻��߽��ϴ�.")
print("�۾��Ϸ�")

# =============== whiletry  ===============
while True:
    str = input("������ �Է��ϼ��� : ")
    try:
        score = int(str)
        print("�Է��� ���� :", score)
        break
    except:
        print("���� ������ �߸��Ǿ����ϴ�.")
print("�۾��Ϸ�")

# =============== excepts  ===============
str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("������ ������ �߸��Ǿ����ϴ�.")
except IndexError:
    print("÷�� ������ ������ϴ�.")
print("�۾��Ϸ�")

# =============== exceptas  ===============
str = "89��"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
print("�۾��Ϸ�")

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
    print("�Է°��� �߸��Ǿ����ϴ�.")

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
    print("�Է°��� �߸��Ǿ����ϴ�.")
else:
    print("~10 =", result)

result = calcsum(-5)
if result == -1:
    print("�Է°��� �߸��Ǿ����ϴ�.")
else:
    print("~10 =", result)

# =============== funcexcept  ===============
dic = { 'boy':'�ҳ�', 'school':'�б�', 'book':'å' }
try:
    print(dic['girl'])
except:
    print("ã�� �ܾ �����ϴ�.")

han = dic.get('girl')
if (han == None):
    print("ã�� �ܾ �����ϴ�.")
else:
    print(han)

# =============== finally  ===============
try:
    print("��Ʈ��ũ ����")
    a = 2 / 0
    print("��Ʈ��ũ ��� ����")
finally:
    print("���� ����")
print("�۾� �Ϸ�")

# =============== assert  ===============
score = 128
assert score <= 100, "������ 100 ���Ͽ��� �մϴ�"
print(score)

###########################################################    
## 14�� ##

# =============== write  ===============
f = open("live.txt", "wt")
f.write("""���� �״븦 ��������
�����ϰų� ������ ����!
����� ������ �ߵ��
������, ����� ���� ������""")
f.close()

# =============== read  ===============
try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("������ �����ϴ�.")
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
f.write("\n\nǪ��Ų ������ �����̾����ϴ�.")
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
## 15�� ##

# =============== capsule  ===============
balance = 8000

def deposit(money):
    global balance
    balance += money

def inquire():
    print("�ܾ��� %d���Դϴ�." % balance)

deposit(1000)
inquire()

# =============== account  ===============
class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def inquire(self):
        print("�ܾ��� %d���Դϴ�." % self.balance)

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
        print(str(self.age) + "�� " + self.name + "�Դϴ�.")

kim = Human(29, "�����")
kim.intro()
lee = Human(45, "�̽¿�")
lee.intro()

# =============== student  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + "�� " + self.name + "�Դϴ�")


class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("�й� : " + str(self.stunum))

    def study(self):
        print("�ϴ�õ ���� ������ ����Ȳ")


kim = Human(29, "�����")
kim.intro()
lee = Student(34, "�̽¿�", 930011)
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

pride = Car("�����̵�")
korando = Car("�ڶ���")
Car.outcount()

# =============== staticmethod  ===============
class Car:
    @staticmethod
    def hello():
        print("���õ� ���� ���� �սô�.")
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

kim = Human(29, "�����")
sang = Human(29, "�����")
moon = Human(44, "������")
print(kim == sang)
print(kim == moon)

# =============== clsstr  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "�̸� %s, ���� %d" % (self.name, self.age)

kim = Human(29, "�����")
print(kim)

# =============== clslen  ===============
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __len__(self):
        return self.age

kim = Human(29, "�����")
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
ar.append(100)                  # �߰�
del ar[0]                       	# ����
print("\nar[1] = ", ar[1])      		# ÷�� ����
print(ar[2:4])                  	# �����̽�

###########################################################    
## 16�� ##

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

print("��ġ =", INCH)
print("�հ� =", calcsum(10))

# =============== util2  ===============
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

if __name__ == "__main__":
    print("��ġ =", INCH)
    print("�հ� =", calcsum(10))

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
frame = wx.Frame(None, 0, "���̽� ����")

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
## 17�� ##

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

solarterm = Seq("��������Ĩ���û�������ϼҸ����������Ҽ��뼭")
for k in solarterm:
    print(k, end = ',')

# =============== generator  ===============
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]

solarterm = seqgen("��������Ĩ���û�������ϼҸ����������Ҽ��뼭")
for k in solarterm:
    print(k, end = ',')

# =============== genexpr  ===============
data = "��������Ĩ���û�������ϼҸ����������Ҽ��뼭"
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
hanhello = makeHello("�ȳ��ϼ���")

enghello("Mr kim")
hanhello("ȫ�浿")

# =============== wrapper  ===============
def inner():
    print("����� ����մϴ�.")

def outer(func):
    print("-" * 20)
    func()
    print("-" * 20)

outer(inner)

# =============== wrapper2  ===============
def inner():
    print("����� ����մϴ�.")

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
    print("����� ����մϴ�.")

inner()

# =============== tagdeco  ===============
def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para
def outname():
    return "�����"

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
    return "�����"

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
    return "�̸�:" + name + "��"

@para
def outage(age):
    return "����:" + str(age)

print(outname("�����"))
print(outage(29))

# =============== decoarg2  ===============
def para(func):
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    return wrapper

@para
def outname(name):
    return "�̸�:" + name + "��"

@para
def outage(age):
    return "����:" + str(age)

print(outname("�����"))
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
    return "�̸�:" + name + "��"

@para
def outage(age):
    return "����:" + str(age)

print(outname("�����"))
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
    print("����� ����մϴ�.")

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
    print("����� ����մϴ�.")

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
        expr = input("������ �Է��ϼ���(���� �� 0) : ")
        if expr == '0':
            break
        print(eval(expr))
    except:
        print("������ �߸��Ǿ����ϴ�.")

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
        return "�̸� %s, ���� %d" % (self.name, self.age)
    def __repr__(self):
        return "Human(" + str(self.age) + ",'" + self.name + "')"

kim = Human(29, "�����")
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
## 18�� ##

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
    if tkinter.messagebox.askyesno("����", "����� �̼������Դϱ�?"):
        tkinter.messagebox.showwarning("���", "�ֵ��� ����")
    else:
        tkinter.messagebox.showinfo("ȯ��", "�������. ����")
btn = Button(main, text="����", foreground="Blue", command = btnclick)
btn.pack()

main.mainloop()

# =============== askstring  ===============
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

main = Tk()

def btnclick():
    name = tkinter.simpledialog.askstring("����", "�̸��� �Է��Ͻÿ�")
    age = tkinter.simpledialog.askinteger("����", "���̸� �Է��Ͻÿ�")
    if name and age:
        tkinter.messagebox.showwarning("ȯ��", str(age) + "�� " + name + "�� �ݰ����ϴ�.")

btn = Button(main, text="Ŭ��", foreground="Blue", command = btnclick)
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
menubar.add_cascade(label = "����", menu = popup)

def about():
    tkinter.messagebox.showinfo("�Ұ�", "�޴� ��� �����Դϴ�.")

popup.add_command(label = "�Ұ�", command = about)
popup.add_command(label = "����", command = quit)

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
## �η� ##

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
## �¶��� ���� ##

# =============== readgreen  ===============
color = 0xaa80ff
green = (color & 0x00ff00) >> 8
print("�ʷϻ� ���� =", green)

# =============== forelse  ===============
score = [ 92, 86, 68, 77, 56]
for s in score:
    print(s)
else:
    print("�� ����߽��ϴ�.")

# =============== breakelse  ===============
score = [ 92, 86, 68, 120, 56]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
else:
    print("�� ����߽��ϴ�.")

# =============== makedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""CREATE TABLE tblAddr
    (name CHAR(16) PRIMARY KEY, phone CHAR(16), addr TEXT)""")

cursor.execute("INSERT INTO tblAddr VALUES ('�����', '123-4567', '����')")
cursor.execute("INSERT INTO tblAddr VALUES ('�Ѱ���', '555-1004', '����')")
cursor.execute("INSERT INTO tblAddr VALUES ('���ֿ�', '444-1092', '����')")

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
    print("�̸� : %s, ��ȭ : %s, �ּ� : %s" % record)

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
    print("�̸� : %s, ��ȭ : %s, �ּ� : %s" % record)

cursor.close()
con.close()

# =============== drderby  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr ORDER BY addr")
table = cursor.fetchall()
for record in table:
    print("�̸� : %s, ��ȭ : %s, �ּ� : %s" % record)

cursor.close()
con.close()

# =============== orderbydesc  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT addr FROM tblAddr WHERE name = '�����'")
record = cursor.fetchone()
print("������� %s�� ��� �ֽ��ϴ�." % record)

cursor.close()
con.close()

# =============== updatedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("UPDATE tblAddr SET addr = '���ֵ�' WHERE name = '�����'")
con.commit()

cursor.close()
con.close()

# =============== deletedb  ===============
import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("DELETE FROM tblAddr WHERE name = '�����'")
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
frame.SetTitle("���̽����� ���� ������")
frame.SetWindowStyle(wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)

frame.Show(True)
app.MainLoop()

# =============== KeyEvent  ===============
import wx

app = wx.App()
frame = wx.Frame(None)

def OnLeftDown(event):
    # x, y = event.GetPosition()
    message = "(%d, %d) �� Ŭ���߽��ϴ�." % (event.x, event.y)
    wx.MessageBox(message, "�˸�", wx.OK)
frame.Bind(wx.EVT_LEFT_DOWN, OnLeftDown)

def OnKeyDown(event):
    message = "%d Ű�� �������ϴ�." % event.KeyCode
    wx.MessageBox(message, "�˸�", wx.OK)
frame.Bind(wx.EVT_KEY_DOWN, OnKeyDown)

frame.Show(True)
app.MainLoop()

# =============== Button  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn = wx.Button(frame, label="Click")
def OnClick(event):
    wx.MessageBox("��ư�� Ŭ���Ͽ����ϴ�.", "�˸�", wx.OK)
btn.Bind(wx.EVT_BUTTON, OnClick)

frame.Show(True)
app.MainLoop()

# =============== ButtonStatic  ===============
import wx

app = wx.App()
frame = wx.Frame(None, title = "wxPython")

btn = wx.Button(frame, label="Click")
def OnClick(event):
    wx.MessageBox("��ư�� Ŭ���Ͽ����ϴ�.", "�˸�", wx.OK)
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

radio1 = wx.RadioButton(frame, label="����", style = wx.RB_GROUP)
radio2 = wx.RadioButton(frame, label="�����佺")
radio3 = wx.RadioButton(frame, label="�׶�")

box = wx.StaticBoxSizer(wx.HORIZONTAL, frame, "����")
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
    wx.MessageBox(str, "�Է³���", wx.OK)
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

chkvisible = wx.CheckBox(frame, label = "����")
chkvisible.SetValue(wx.CHK_CHECKED)
def onvisible(event):
    if chkvisible.GetValue() == wx.CHK_CHECKED:
        btn.Show(True)
    else:
        btn.Show(False)
chkvisible.Bind(wx.EVT_CHECKBOX, onvisible)

chkenable = wx.CheckBox(frame, label = "��밡��")
chkenable .SetValue(wx.CHK_CHECKED)
def onenable(event):
    if chkenable.GetValue() == wx.CHK_CHECKED:
        btn.Enable(True)
    else:
        btn.Enable(False)
chkenable.Bind(wx.EVT_CHECKBOX, onenable)

btn = wx.Button(frame, label="Click")
def onClick(event):
    wx.MessageBox("Ŭ���߽��ϴ�.", "�˸�", wx.OK)
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

red = wx.RadioButton(frame, label = "����", style = wx.RB_GROUP)
def onred(event):
    frame.SetBackgroundColour(wx.Colour(255, 0, 0, 0))
    frame.Refresh()
red.Bind(wx.EVT_RADIOBUTTON, onred)

green = wx.RadioButton(frame, label = "�ʷ�",)
def ongreen(event):
    frame.SetBackgroundColour(wx.Colour(0, 255, 0, 0))
    frame.Refresh()
green.Bind(wx.EVT_RADIOBUTTON, ongreen)

blue = wx.RadioButton(frame, label = "�Ķ�",)
def onblue(event):
    frame.SetBackgroundColour(wx.Colour(0, 0, 255, 0))
    frame.Refresh()
blue.Bind(wx.EVT_RADIOBUTTON, onblue)

yellow = wx.RadioButton(frame, label = "���",)
def onyellow(event):
    frame.SetBackgroundColour(wx.Colour(255, 255, 0, 0))
    frame.Refresh()
yellow.Bind(wx.EVT_RADIOBUTTON, onyellow)
yellow.SetValue(True)

box = wx.StaticBoxSizer(wx.VERTICAL, frame, "����")
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
colorname = ["����", "�ʷ�", "�Ķ�", "���", "�Ͼ�", "����"]
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

desc = wx.StaticText(frame, label = "�԰� ���� ���ڸ� ���ÿ�.")
snack = ["��¡�� ����", "������", "������", "��������"]
combo = wx.ComboBox(frame, choices = snack)
result = wx.StaticText(frame, label = "")

def onitemchange(event):
    idx = combo.GetCurrentSelection()
    result.SetLabelText(snack[idx] + " ���ְ� �弼��.")
combo.Bind(wx.EVT_COMBOBOX, onitemchange)
def oniteminput(event):
    result.SetLabelText(combo.GetValue() + " ���ְ� �弼��.")
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
menubar.Append(file, "����")
about = wx.MenuItem(id = wx.ID_ANY, text="�Ұ�")
file.Append(about)
file.AppendSeparator()
exit = wx.MenuItem(id = wx.ID_ANY, text="����")
file.Append(exit)
frame.SetMenuBar(menubar)

def onAbout(event):
    wx.MessageBox("�޴��� ����ϴ� ���α׷��Դϴ�.", "�˸�", wx.OK)
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




