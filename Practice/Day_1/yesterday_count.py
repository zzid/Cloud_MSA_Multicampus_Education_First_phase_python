# Current directory :: Claas_1_(First project)
file = open("./Practice/Day_1/yesterday.txt",'r')
# mode : r(read), w(write), a(append), rb, wb (binary file)
yesterday_lyrics =''
while 1:
    line = file.readline()
    if not line:
        break
    yesterday_lyrics += line
print('# of a word YESTERDAY', yesterday_lyrics.upper().count("YESTERDAY"))
print('# of a word yesterday', yesterday_lyrics.count("yesterday"))
print('# of a word Yesterday', yesterday_lyrics.count("Yesterday"))

file.close()