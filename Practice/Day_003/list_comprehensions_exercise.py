books = list()

books.append({
    '제목' : '개발자의 코드', 
    '출판연도' : '2013.02.28',
    '출판사' : 'A출판',
    '쪽수' : 200,
    '추천유무' : False})
books.append({
    '제목' : '클린 코드', 
    '출판연도' : '2013.03.04',
    '출판사' : 'B출판',
    '쪽수' : 584,
    '추천유무' : True})
books.append({
    '제목' : '빅데이터 마케팅', 
    '출판연도' : '2014.07.02',
    '출판사' : 'A출판',
    '쪽수' : 296,
    '추천유무' : True})
books.append({
    '제목' : '구글드', 
    '출판연도' : '2010.02.10',
    '출판사' : 'B출판',
    '쪽수' : 526,
    '추천유무' : False})
books.append({
    '제목' : '강의력', 
    '출판연도' : '2013.12.12',
    '출판사' : 'C출판',
    '쪽수' : 248,
    '추천유무' : True})

#1
over250 = [_['제목'] for _ in books if _['쪽수'] > 250]
print(over250)

#2
has_recommanded = [_['제목'] for _ in books if _['추천유무']]
print(has_recommanded)

#3
publishers = list(set([_['출판사'] for _ in books]))
print(publishers)