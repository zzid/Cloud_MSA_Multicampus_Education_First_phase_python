###########################################################
import pickle # pickle is binary                        ###
#pickle can store class, object, and value, everything  ###
###########################################################
import os
os.chdir('./Practice/Day_5')
name = input('file name ? : ')
f= open(name, 'wb')
n = int(input('How many things you want to store? : '))
inp = []
for i in range(n):
    inp.append(f' Entered data {i+1} : {input()}')
pickle.dump(inp, f)

f.close()
