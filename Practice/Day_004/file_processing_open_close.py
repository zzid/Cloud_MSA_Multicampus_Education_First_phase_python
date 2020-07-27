import os
os.chdir('.\Practice\Day_4')
# default mode is 'r'
myfile = open('i_have_a_dream.txt') #########
contents = myfile.read()
print(contents)
myfile.close() ########