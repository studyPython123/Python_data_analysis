create database mydb_procedure;
-- 创建存储过程
use mydb_procedure;
delimiter $$
create procedure proc01()
begin 
	select empno,ename from emp;
end $$
delimiter ;
-- 调用存储过程
call proc01();

