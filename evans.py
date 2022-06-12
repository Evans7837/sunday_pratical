create table singers(id INTEGER, name text, age INTEGER);
insert into singers(id, name, age)
values (1, 'Justin Bieber', 25);
insert into singers (id, name, age)
values (2, 'Wizkid Balogun', 30);
insert into singers(id, name, age)
values (3, 'Olamide Badoo', 35);
insert into singers(id, name, age)
values (4, 'Davido Adeleke', 32);
select * from singers

alter table singers
add column instagram_handle text;
select * from singers

update singers 
set instagram_handle= '@Olamide'
where id = 3;
update singers 
set instagram_handle ='@Wizkidayo'
where id = 2;
update singers 
set instagram_handle = '@Davido'
where id = 4;
update singers 
set instagram_handle = '@Justinbieber'
where id = 1;

select * from singers

alter table singers
add column twitter_handle text;

select * from singers

delete from singers 
where twitter_handle is null;

select * from singers

