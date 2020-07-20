from datetime import datetime
from random import random
import os,sys
os.chdir('./Practice/Day_4')

if not os.path.isdir('log'):
    os.mkdir('log')

file = open('./log/count_log.txt', 'a', encoding='utf8')

for i in range(1,11):
    file.write(f'{str(datetime.now())} - random number : {random() * 100000}\n')