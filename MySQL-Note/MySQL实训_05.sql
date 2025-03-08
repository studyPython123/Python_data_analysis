#MySQL实训_05
create database hainan_data;
use hainan_data;

create table if not exists customer(
id int primary key,
name char,
company char,
sales int);

alter table customer add address varchar(100);

drop table customer;

select  name from customer;
#没有数据，后面的习题代码运行起来没意义

#MySQL实训_06
create database test2;
use test2;

create table t_1(
id int,
sno int,
cno int,
score int);

insert into t_1
values
(1,1001,1,89),
(2,1001,1,89),
(3,1002,1,87),
(4,1002,1,90),
(5,1003,1,86);

select * from t_1 
where (sno,cno) in 
(select sno,cno from t_1 group by sno,cno having count(*)>1);

select * from t_1 where (sno,cno,score) in 
(select sno,cno,score from t_1 group by sno,cno,score having count(*)>1)  
and id not in (select min(id)from t_1 group by sno,cno,score having count(*)>1);
