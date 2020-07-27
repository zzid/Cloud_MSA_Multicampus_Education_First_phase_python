import os
os.chdir('.\Practice\Day_4')
# readline()
with open('i_have_a_dream.txt','r') as my_file:
    i =0
    while 1:
        line = my_file.readline()
        if line.strip() != '':
            print(str(i) +' : ' + line.strip())
        if not line:
            break
        i += 1
