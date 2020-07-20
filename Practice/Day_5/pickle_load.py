import pickle,os
os.chdir('./Practice/Day_5')

name = input('file name ? : ')
f = open(name, 'rb')

inps = pickle.load(f)
for i, item in enumerate(inps):
    print( i, item )

f.close()