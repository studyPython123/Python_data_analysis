-- MySQL实训_06
use hainan_data;
create table if not exists table1(
	id int primary key auto_increment,
	sno varchar(5),
	cno varchar(5),
	score int
);
drop table 表t_1;
insert into table1(sno,cno,score) values(1001,1,89),
																															(1001,1,89),
																															(1002,1,87),
																															(1002,1,90),
																															(1003,1,86);
select * from table1;


-- 1)	查询出sno，cno重复的数据
select * from table1 where (sno,cno) in (select sno,cno from table1 group by sno,cno having count(*)>1);

-- 2)	查询sno，cno，score都重复的数据，且除id最小的一条数据外
select * from table1 where (sno,cno,score) in 
(select sno,cno,score from table1 group by sno,cno,score having count(*)>1)  
and id not in (select min(id) from table1 group by sno,cno,score having count(*)>1);
