use mydataset1;
-- 创建表
create table if not exists dept(
	deptid varchar(20) primary key,
	deptname varchar(20)
);
create table if not exists empp(
	empid varchar(20) primary key,
	empname varchar(20),
	empage int,
	dept_id varchar(20),
	constraint emp_fk foreign key(dept_id) references dept(deptid)
);
-- 添加约束的另一种方式
alter table empp constraint emp_fk foreign key(dept_id) 
references dept(deptid);
-- 插入数据
insert into dept values('1001','研发部'),
				('1002','销售部'),
				('1003','财政部'),
				('1004','人事部');
insert into empp values('1','乔峰',20,'1001'),
('2','段誉',21,'1001'),
('3','虚竹',23,'1001'),
('4','阿紫',18,'1002'),
('5','扫地僧',35,'1002'),
('6','李秋水',33,'1003'),
('7','鸠摩智',50,'1003');
('8','天山童姥',60,'1005'); -- 不可以
-- 外键约束主要限制数据的增删改
-- 删除外键约束
alter table empp drop foreign key emp_fk;
-- 1、创建学生表
create table if not exists student(
	sid int primary key auto_increment,
	name varchar(20),
	age int,	
	gender varchar(20)
);
-- 2、创建课程表
create table course(
cid int primary key auto_increment,
cidname varchar(20)
);
-- 3、创建中间表student_course/score(从表)
create table score(
sid int,
cid int,
score double
);
-- 添加外键约束
alter table score add
constraint score_sid foreign key(sid) 
references student(sid);
alter table score add
constraint score_cid foreign key(cid) 
references course(cid);
-- 学生表插入数据
insert into student values(1,'小龙女',18,'女'),(2,'阿紫',19,'女'),(3,'周芷若',20,'男');
-- 课程表插入数据
insert into course values(1,'语文'),(2,'数学'),(3,'英语');
-- 中间表插入数据
insert into score values(1,1,78),(1,2,75),(2,1,88),(2,3,90),(3,2,80),(3,3,65);
-- 
select * from student,course;


