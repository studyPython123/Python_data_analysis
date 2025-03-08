-- 26、存储过程传参
use mydb_procedure;
-- 封装有参数的存储过程
delimiter $$
create procedure proc05(in param_enpno int)
begin 
	select * from emp e where e.empno = param_enpno;
end $$
delimiter ;

call proc05(7788);

-- 多个参数
delimiter $$
create procedure proc06(in dname varchar(20),in sal int)
begin 
	select * from emp e,dept d 
	where e.deptno = d.deptno and d.dname = dname and e.sal > sal;
end $$
delimiter ;

call proc06('accounting',2000);

--  out将结果传出去
delimiter $$
create procedure proc07(in empno int,out empname varchar(20))
begin 
	select ename into empname from emp where emp.empno = empno;
end $$
delimiter;
call proc07(7698,@out_name);
select @out_name;

-- 传入员工编号，返回姓名和薪资
delimiter $$
create procedure proc08(in empno int,out empname varchar(20),out salary double)
begin 
	select emp.ename,emp.sal into empname,salary from emp where emp.empno = empno;
end $$
delimiter;
call proc08(7698,@out_name,@out_salary);
select @out_name 姓名,@out_salary 工资;

-- inout
delimiter $$
create procedure proc09(inout num int)
begin 
	set num = num*10;
end $$
delimiter;

set @result = 10;
call proc09(@result);
select @result;

-- 传入员工姓名，拼接部门号，传入薪水，求出年薪
delimiter $$
create procedure proc10(inout name_deptno varchar(20),inout year_salary double)
begin 
	select concat(emp.ename,'-',emp.deptno) into name_deptno from emp 
	where emp.ename = name_deptno;
	select (12*year_salary+ifnull(emp.comm,0)) into year_salary from emp 
	where emp.sal = year_salary;
end $$
delimiter ;
set @name_deptno = 'allen';
set @year_salary = 1600;
call proc10(@name_deptno,@year_salary);
select @name_deptno,@year_salary;

