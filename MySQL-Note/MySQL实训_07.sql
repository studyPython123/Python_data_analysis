-- MySQL实训_07
use loan;
create table if not exists table1(cus_id char(1) primary key);
create table if not exists table2(cus_id char(1) primary key);
insert into table1 values(1),
(2),
(3),
(4);
insert into table2 values(2),
(3),
(5),
(6);
-- 第一题(避免主键重复)
select cus_id from table1 join
 (select cus_id as id from table2) t
 on table1.cus_id = t.id;
#B 
select cus_id from table1 union select cus_id from table2;
#C
select
	t.cus_id 
from
	( select cus_id from table1 union select cus_id from table2 ) t 
where
	t.cus_id not in ( select cus_id from table1 join ( select cus_id id from table2 ) ta on table1.cus_id = ta.id );
#D
select table1.cus_id from table1 where table1.cus_id not in (select table1.cus_id from table1 join table2 on table1.cus_id = table2.cus_id);




##############################################################################面试题3######################################################################################

create table invest(
created_at datetime,
user_id char(4),
invest_item varchar(10),
invest_amount decimal(38,10));

create table dim(
user_id char(4),
start_date datetime,
end_date datetime,
agent_id char(5));

insert into invest values
('2017-11-01 01:32:00','A123','CFH','100000'),
('2017-12-05 03:42:00','A123','AX','450000'),
('2017-12-11 17:42:00','A123','CH','700000'),
('2017-12-06 20:06:00','B456','CFH','1500000'),
('2017-12-26 14:36:00','B456','AX','800000'),
('2018-01-06 14:36:00','C789','JUIN','300000');

insert into dim values
('A123','2016-01-01 00:00:00','2017-12-04 23:59:59','10001'),
('A123','2017-12-05 00:00:00','3001-12-31 23:59:59','10002'),
('B456','2015-10-31 00:00:00','2016-12-15 23:59:59','10001'),
('B456','2016-12-16 00:00:00','3001-12-31 23:59:59','10003'),
('C789','2015-01-01 00:00:00','3001-12-31 23:59:59','10002');

#1、	计算2017年每笔投资均大于50万的用户
select
	t.user_id 
from
	(
	select
		i.created_at,
		i.invest_amount,
		i.invest_item,
		i.user_id 
	from
		invest i 
	where
		year ( i.created_at ) = '2017' 
	) t 
group by
	t.user_id 
having
	min( t.invest_amount ) > 500000;

#2、计算2017年仅投资过CFH和AX产品的用户
select
	t.user_id 
from
	(
	select
		i.user_id,
		i.invest_item 
	from
		invest i 
	where
		year ( i.created_at ) = '2017' 
	and i.invest_item in ( 'CFH', 'AX' )) t 
group by
	t.user_id 
having
	count( t.invest_item ) = 2;
	
#3、	计算归属于10002业务员的投资金额
select round(sum(i.invest_amount) ,2)from invest i join dim d on i.user_id = d.user_id and d.agent_id = '10002';


##############################################################################面试题4######################################################################################

create table A(
ID bigint,
OrderNo varchar(20),
Orderdate datetime,
Price int);

insert into A values
(01,01,'2019-6-11',6000),
(01,02,'2019-6-12',8000),
(02,03,'2019-6-11',5000),
(03,04,'2019-6-11',7000),
(04,05,'2019-6-11',3000),
(04,06,'2019-6-12',9000);

create table B(
ID bigint,
Sex varchar(5),
Age int);

insert into B values
(01,'男',20),
(02,'男',50),
(03,'女',20),
(04,'男',42);

#第一问
#请把A表和B表关联，找出订单金额大于5000的客户，年龄区间在0-25,25-45,45岁以上的客户有多少，区间均为前闭后开。
select sum(case when Age between 0 and 25 then 1 else 0 end) as '0-25',
sum(case when Age between 25 and 45 then 1 else 0 end) as  '25-45',
sum(case when Age>=25 then 1 else 0 end) as  '45岁以上'
from A a join B b on a.ID = b.ID and a.Price>5000 group by Sex;

#第二问
#请把A表和B表关联，限制男性客户，取每个男性客户的第一次订单时间，及对应的订单金额。
select
	t.Orderdate,
	t.price 
from
	(
	select
		a.Orderdate,
		a.Price,
		row_number() over ( partition by a.ID order by a.Price ) rank1 
	from
		A a 
	where
		a.ID in (
		select
			a.ID 
		from
			A a
			join B b on a.ID = b.ID 
			and b.Sex = '男' 
		group by
			a.ID 
		) 
	order by
		a.Orderdate 
	) t 
where
	t.rank1 = 1;
	
	#第三问
#请把A表和B表关联，用分组求和，取不同性别中，累计订单金额TOP2的客户。
select
	* 
from
	(
	select
		t.Sex,
		t.ID,
		row_number() over ( partition by t.Sex order by t.aum_price desc ) rank1 
	from
		(
		select
			b.Sex,
			a.ID,
			sum( a.Price ) aum_price 
		from
			A a
			join B b on a.ID = b.ID 
		group by
			b.Sex,
			a.ID 
		) t 
	) t1 
where
	t1.rank1 <= 2;
	
	
	#第三题
create table invest(
created_at datetime,
user_id char(4),
invest_item varchar(10),
invest_amount decimal(38,10));

create table dim(
user_id char(4),
start_date datetime,
end_date datetime,
agent_id char(5));

insert into invest values
('2017-11-01 01:32:00','A123','CFH','100000'),
('2017-12-05 03:42:00','A123','AX','450000'),
('2017-12-11 17:42:00','A123','CH','700000'),
('2017-12-06 20:06:00','B456','CFH','1500000'),
('2017-12-26 14:36:00','B456','AX','800000'),
('2018-01-06 14:36:00','C789','JUIN','300000');

insert into dim values
('A123','2016-01-01 00:00:00','2017-12-04 23:59:59','10001'),
('A123','2017-12-05 00:00:00','3001-12-31 23:59:59','10002'),
('B456','2015-10-31 00:00:00','2016-12-15 23:59:59','10001'),
('B456','2016-12-16 00:00:00','3001-12-31 23:59:59','10003'),
('C789','2015-01-01 00:00:00','3001-12-31 23:59:59','10002');

#1、计算2017年每笔投资均大于50万的用户
select
	t.user_id 
from
	(
	select
		i.created_at,
		i.invest_amount,
		i.invest_item,
		i.user_id 
	from
		invest i 
	where
		year ( i.created_at ) = '2017' 
	) t 
group by
	t.user_id 
having
	min( t.invest_amount ) > 500000;
	
select user_id from invest where year(created_at)='2017' group by user_id having min(invest_amount)>500000;
#2、计算2017年仅投资过CFH和AX产品的用户
select a.user_id from (select user_id from invest group by user_id having count(user_id)=2)a
inner join  
(select a.user_id from 
(select user_id from invest where year(created_at)='2017' and invest_item='CFH')a inner join
(select user_id from invest where year(created_at)='2017' and invest_item='AX')b
on a.user_id=b.user_id)b
on a.user_id=b.user_id;

#严谨
select t.user_id from (select i.user_id from invest i where year(i.created_at) = '2017' group by i.user_id having count(i.invest_item) = 2) t join 
(select i.user_id from invest i where i.invest_item = 'CFH') t1 on t.user_id = t1.user_id join 
(select i.user_id from invest i where i.invest_item = 'AX') t2 on t1.user_id = t2.user_id

#3、计算归属于10002业务员的投资金额
select
	round( sum( i.invest_amount ), 2 ) 总投资金额 
from
	invest i
	join dim d on i.user_id = d.user_id 
	and d.agent_id = '10002' 
	and ( i.created_at between d.start_date and d.end_date );
	
	
	
select agent_id,sum(invest_amount) as sums from dim a left join 
invest b on a.user_id=b.user_id and created_at between start_date and end_date
where agent_id=10002
group by agent_id;
