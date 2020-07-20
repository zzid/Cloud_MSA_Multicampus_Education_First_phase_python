dicts = []
categories = ['id', 'name', 'email', 'hp_num']
one = ['1', 'hong kildong', 'hong@mail.com', '010-2343-9870']
two = ['2', 'lee soonsin', 'lee@mail.com', '010-3333-5555']
three = ['3', 'jang youngsil', 'jang@mail.com', '010-7777-1234']
four = ['4', 'king sejong', 'king@mail.com', '010-4567-0987']

for a,b,c,d,e in zip(categories, one, two, three,four):
    temp1, temp2, temp3, temp4 = {},{},{},{}
    temp1[a] = b
    temp2[a] = c
    temp3[a] = d
    temp4[a] = e
    dicts.extend([temp1,temp2,temp3,temp4])
