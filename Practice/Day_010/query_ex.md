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