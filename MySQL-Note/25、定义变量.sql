use mydb_procedure;

-- 局部变量
delimiter $$
create procedure proc02()
begin 
	declare var_name01 varchar(20) default 'aaa'; -- 声明变量
	set var_name01 = 'zhanguan'; -- 变量赋值
	select var_name01; -- 输出变量的值
end $$
delimiter ;

call proc02();
-- 
delimiter $$
create procedure proc03()
begin 
	declare var_name02 varchar(20); -- 声明变量
	select ename into var_name02  from emp where empno = 7566; -- 变量赋值
	select var_name02; -- 输出变量的值
end $$
delimiter ;

call proc03();

-- 用户变量
delimiter $$ -- 设置结束字符
create procedure  proc04()
begin
	set @var_name01 = 'zs';
	select @var_name01;
end $$
delimiter ;
call proc04() ;
select @var_name01;

-- 系统变量-全局变量
show global variables; -- 查看全局变量

-- 系统变量-会话变量
show session variables;







