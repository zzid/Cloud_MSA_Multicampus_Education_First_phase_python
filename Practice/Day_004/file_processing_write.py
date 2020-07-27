import os
os.chdir('./Practice/Day_4')

my_file = open('count_log.txt', 'w', encoding='utf8')
for i in range(1,11):
    my_file.write(f'{i}\t번째 줄 입니다. \n')
my_file.close()

with open('count_log.txt', 'a', encoding='utf8') as mf:
    for i in range(100,111):
        mf.write(f'{i}\t번째 줄입니다.\n')

