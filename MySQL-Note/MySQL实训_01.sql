-- 创建客户表customer
create table
if
	not exists customer (
		c_id char ( 6 ) primary key not null,-- 客户标识
		name varchar ( 30 ) not null,-- 客户姓名
		location varchar ( 30 ),-- 工作地点
		salary decimal ( 8, 2 ) -- 工资
	);

-- 查看是否创建成功
show full columns from customer;

-- 创建银行表bank
create table
if
	not exists bank ( b_id char ( 5 ) not null primary key comment '银行标识', bank_name char ( 30 ) not null comment '银行名次' );

-- 创建存款表desposite
create table
if
	not exists desposite (
		d_id int primary key not null auto_increment comment '存款流水号',
		c_id char ( 6 ) comment '客户标识',
		b_id char ( 5 ) comment '银行标识',
		dep_date date comment '存入日期',
		dep_type char ( 1 ) comment '存款期限',
		amount decimal ( 8, 2 ) comment '存款金额',
		constraint fk_cid foreign key ( c_id ) references customer ( c_id ),
	constraint fk_bid foreign key ( b_id ) references bank ( b_id ));

-- 第三题-插入数据
insert into customer values
(101001,'孙杨','广州',1234),
(101002,'郭海','南京',3526),
(101003,'卢江','苏州',6892),
(101004,'郭惠','济南',3492),
(201042,'吴彦祖','北京',6324);

insert into bank values
('B0001','工商银行'),
('B0002','建设银行'),
('B0003','中国银行'),
('B0004','农业银行');

insert into desposite values
(1,101001,'B0001','2011-04-05',3,42526),
(2,101002,'B0003','2012-07-15',5,66500),
(3,101003,'B0002','2010-11-24',1,42366),
(4,101004,'B0004','2009-03-31',1,62362),
(5,101001,'B0003','2002-02-07',3,56346),
(6,101002,'B0001','2004-09-23',3,353626),
(7,101003,'B0004','2003-12-14',5,36236),
(8,101004,'B0002','2007-04-21',5,435456),
(9,101001,'B0002','2011-02-11',1,435456),
(10,101002,'B0004','2012-05-13',1,234626),
(11,101003,'B0003','2001-01-24',5,26243),
(12,101004,'B0001','2009-08-23',3,45671);

-- 第四题

set SQL_SAFE_UPDATES = 0;#如果MYSQL有权限，不能增删改，加这一句。
update customer 
set salary = salary * 2 
where
	salary < 5000;

-- 5对desposite表进行统计，按银行统计存款总数，显示为b_id,total。
-- 
select
	desposite.b_id,
	sum( desposite.amount ) 存款总数 
from
	desposite 
group by
	desposite.b_id;
--  
select
	b_id,
	sum( amount ) as total 
from
	desposite 
group by
	b_id;
/*
6对desposite、customer、bank进行查询，查询条件为location在广州、苏州、济南的客户，
存款在300000至500000之间的存款记录，
显示客户姓名name、银行名称bank_name、存款金额amount
*/
-- method1
select
	customer.`name`,
	bank.bank_name,
	desposite.amount 
from
	bank
	join desposite on bank.b_id = desposite.b_id 
	and desposite.amount between 300000 
	and 500000
	join customer on desposite.c_id = customer.c_id 
	and customer.location in ( '广州', '苏州', '济南' );
	
-- method2
select
	c.name,
	b.bank_name,
	d.amount 
from
	customer c,
	bank b,
	desposite d 
where
	c.location in ( '广州', '苏州', '济南' ) 
	and d.amount between 300000 
	and 5000000 
	and d.c_id = c.c_id 
	and d.b_id = b.b_id;



