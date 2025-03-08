create database mydb4;
use mydb4;
create table emp(
	empid int primary key auto_increment comment '编号',
	emp_name char(20) not null default ' ' comment '姓名',
	salary decimal(10,2) not null default 0 comment '工资',
	department char(20) not null default ' ' comment '部门'
);
insert into emp(emp_name,salary,department)
values ('张晶晶',5000,'财务部'),
('王飞飞',5800,'财务部'),
('赵刚',6200,'财务部'),
('刘小贝',5700,'人事部'),
('王大鹏',6700,'人事部'),
('张小斐',5200,'人事部'),
('刘云云',7500,'销售部'),
('刘云鹏',7800,'销售部');
-- 所有员工名合成一行
select group_concat(emp_name separator';') from emp;
-- 指定排序方式和分隔符
select department,group_concat(emp_name separator';') from emp
group by department;
--  排序合并姓名
select department,group_concat(emp_name order by salary desc separator';')
from emp group by department;
