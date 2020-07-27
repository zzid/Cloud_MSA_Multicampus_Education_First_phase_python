import os
os.chdir('.\Practice\Day_4')
# file open with 'with'
with open('i_have_a_dream.txt','r') as my_file:
    contents = my_file.read()
    word_list = contents.split(' ')
    line_list = contents.split('\n')

print('Total # of characters : {}'.format(len(contents)))
print('Total # of words : {}'.format(len(word_list)))
print('Total # of lines : {}'.format(len(line_list)))
