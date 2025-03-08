create database shaoshichang;
use shaoshichang;
#创建表1：
create table employee(
empid int(8) not null primary key auto_increment,
name varchar(20) not null,
gender varchar(6) not null,
title varchar(20),
birthday date,
depid int(3)
);

#创建表2：
create table department(
depid int(5) not null primary key,
depname varchar(20)
);

#创建表3：
create table salary(
empid int(8) not null primary key,
base_salary decimal(10,2),
title_salary decimal(10,2),
deduction decimal(10,2)
);

-- 修改表结构，在部门表中添加一个”部门简介”字段。
alter table department add deptjj varchar(30);
#第四题
insert employee values
(1000,'张三','男','高级工程师','1975-1-1',111),
(1002,'李四','女','助工','1985-1-1',111),
(1003,'王五','男','工程师','1978-11-11',222),
(1004,'赵六','男','工程师','1979-1-1',222);

insert department values
(111,'生产部',Null),
(222,'销售部',Null),
(333,'人事部',Null);

insert salary values
(1001,2200,1100,200),
(1002,1200,200,100),
(1003,1900,700,200),
(1004,1950,700,150);

-- 5.将李四的职称改为“工程师”，并将她的基本工资改为5700元，职务工资为600。
update employee set employee.title = '工程师' where name='李四';
update salary set base_salary = 5700,title_salary = 600 where  empid in (select empid from employee where employee.`name` = '李四');
select * from employee join salary on employee.empid = salary.empid and name='李四';

-- 6. 查询出每个雇员的雇员编号，姓名，职称，所在部门，实发工资和应发工资。
select employee.empid, employee.`name`, employee.title, depname,( base_salary + title_salary ) 应发工资,
( base_salary + title_salary - deduction ) 实发工资 
from
	employee
	join department on employee.depid = department.depid
	join salary on employee.empid = salary.empid;
	
-- 7. 查询姓“张”且年龄小于45岁的员工的记录
select * from employee where (now()-birthday) <45 and name like '张%';
select* from employee where name like '张%' and (now()-birthday)<45;

-- 8. 查询销售部所有雇员的雇员编号，姓名，职称，部门名称，实发工资。
select e.empid, e.`name`, e.title, d.depname,( base_salary + title_salary - deduction ) 实发工资 
from
	employee e
	join department d on e.depid = d.depid 
	and d.depname = '销售部'
	join salary s on e.empid = s.empid;
	
-- 9. 统计各类职称的人数。
select e.title,count(e.empid) from employee e group by e.title ;

-- 10. 统计各部门的部门名称，实发工资总和，平均工资。
select
	d.depname,
	sum( s.base_salary + s.title_salary - deduction ) 实发工资总和,
	avg( s.base_salary + s.title_salary ) 平均工资 
from
	department d
	left join employee e on d.depid = e.depid
	left join salary s on e.empid = s.empid 
group by
	d.depname

-- 11. 查询实际月收入比销售部门所有员工基本工资都高的雇员姓名。（选做）
select
	employee.`name`,(
		salary.base_salary + salary.title_salary - salary.deduction 
	) 实际月收入 
from
	employee
	join salary on employee.empid = salary.empid 
	and ( salary.base_salary + salary.title_salary - salary.deduction ) > all (
	select
		s.base_salary 
	from
		employee e
		join department d on e.depid = d.depid
		join salary s on e.empid = s.empid 
		and d.depname = '销售部' 
	);
