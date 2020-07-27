```sql
# 1. descending order by release_date
SELECT *
FROM songs
order by release_date desc;

# 2. release_date after 2020-07-01
select *
from songs
where release_date >'2020-07-01'
order by release_date desc;

# 3. In the result of 2, genre == 'dance'
select *
from songs
where release_date >'2020-07-01' and genre = '댄스'
order by release_date desc;

# 4-1. Unique singer
select DISTINCT singer
from songs;

# 4-2. # of songs each singer
select singer, count(*)
from songs
group by singer
order by count(*) desc;

# 5-1. Unique genre
select distinct genre
from songs;

# 5-2. # of songs each genre
select genre, count(*)
from songs
group by genre
order by count(*) desc;

# 5-3. find count more than 10
select genre, count(*) as cnt
from songs
group by genre
having cnt > 10
order by cnt desc;

# modify 'id' column - not null, auto_increment, primary key
alter table songs
modify id int not null auto_increment primary key;

# Insert
insert into songs(name, singer, album, release_date, genre, lyric)
value('아침이슬', '양희은', '명장6070', '2004-08-14','발라드','블라블라');

select max(id) from songs;

# Update
update songs
set release_date = '2006-07-01', lyric = '아침이슬가사 수정'
where id = 101;

select * from songs where id = 101;

# Delete
delete from songs
where id = 101;

select * from songs where id > 90;

# 'LIKE' keyword
# Find the album name which contain 'OST'
select *
from songs
where album like '%OST %';

# Complement of above one
select *
from songs
where album not like '%OST %';
```

```sql
desc members;

# id col : auto increment, set as pm
alter table members modify id int not null auto_increment primary key

# 생년월일 col : (type) text -> Date
alter table members change 생년월일 생년월일 DATE null;

# id,이름,나이,정당 order by 나이
select id, 이름, 나이, 정당
from members
order by 나이 desc;

# id,이름,나이,정당,취미특기 나이 60~80
select id,이름,나이,정당,취미특기
from members
where 나이 >= 60 and 나이 <= 80
order by 나이;

# id,이름,나이,정당,취미특기 나이 20~40
select id,이름,나이,정당,취미특기
from members
where 나이 >= 20 and 나이 <= 40
order by 나이;

# members with no 취미특기
select id,이름,나이,정당,취미특기
from members
where 취미특기 = 'NULL';

# members with no 취미특기 : change their value to '없음'
update members
set 취미특기 = '없음'
where 취미특기 = 'NULL';

update members
set 홈페이지 = '없음'
where 홈페이지 = 'NULL';

update members
set 이메일 = '없음'
where 이메일 = 'NULL';

update members
set 사무실전화 = '없음'
where 사무실전화 = '';

alter table members change 이름 이름 VARCHAR(10) null;

# find whose family name is '홍'
select 이름
from members
where substr(이름,1,1) = '홍';

# counting by family name
select substr(이름,1,1) as fn,  count(*) as cnt
from members
group by fn
order by cnt desc;

# find who have '보건복지' in 소속위원회
select *
from members
where 소속위원회 like '%보건복지%';

# find who have '보건복지' or '법제사법' in 소속위원회 sort 소속위원회 asc
select id,이름,나이,정당,소속위원회
from members
where 소속위원회 like '%보건복지%' or 소속위원회 like '%법제사법%'
order by 소속위원회 asc;

# find who have 4 비서
select id,이름,나이,정당,비서
from members
where 비서 not like '%,%,%,%,%';

select m.id,m.이름,m.비서,n.value_count
  from members m,
       (SELECT id,(LENGTH(비서) - LENGTH(REPLACE(비서, ',', '')) + 1) as value_count FROM members) n
where m.id = n.id
  and n.value_count = 4;

select id,이름,나이,정당,비서
from members
where char_length(비서) < 16 and char_length(비서) > 12;

# Find 더불어민주당, 초선, 경기 member
select *
from members
where 정당 = '더불어민주당' and 당선횟수 = '초선' and 선거구 = '경기';

# Find 미래통합당, 초선 경기 member
select *
from members
where 정당 = '미래통합당' and 당선횟수 = '초선' and 선거구 = '경기';

# Find for each 정당.초선, 경기 member
select 선거구, 정당, count(*)
from members
where 선거구 = '경기' and 당선횟수 = '초선'
group by 정당;

```