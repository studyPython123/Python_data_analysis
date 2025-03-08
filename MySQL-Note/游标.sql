/*创建存储过程“get_count_by_limit_total_salary()”
声明IN参数 limit_total_salary，DOUBLE类型；声明OUT参数total_count，INT类型。
函数的功能可以实现累加薪资最高的几个员工的薪资值，直到薪资总和达到limit_total_salary参数的值，返回累加的人数给total_count。*/

DELIMITER //
CREATE PROCEDURE get_count_by_limit_total_salary(IN limit_total_salary DOUBLE,OUT total_count INT)
BEGIN
	DECLARE sum_salary DOUBLE DEFAULT 0;  #记录累加的总工资
	DECLARE cursor_salary DOUBLE DEFAULT 0; #记录某一个工资值
	DECLARE emp_count INT DEFAULT 0; #记录循环个数
	#定义游标
	DECLARE emp_cursor CURSOR FOR SELECT salary FROM employees ORDER BY salary DESC;
	#打开游标
	OPEN emp_cursor;
	REPEAT
		#使用游标（从游标中获取数据）
		FETCH emp_cursor INTO cursor_salary;
		
		SET sum_salary = sum_salary + cursor_salary;
		SET emp_count = emp_count + 1;
		
		UNTIL sum_salary >= limit_total_salary
	END REPEAT;
	SET total_count = emp_count;
	#关闭游标
	CLOSE emp_cursor;

END //
DELIMITER //;


#测试存储过程
create table employees(
	id int primary key auto_increment,
	name varchar(20) default '男',
	salary decimal
)
drop table employees;
insert into employees(salary) values(3000),(8000),(9000),(11000),(20000);
select * from employees;

call get_count_by_limit_total_salary(50000,@total_count);
select @total_count;



# 实例1
-- sys_user 表的创建
CREATE TABLE `sys_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8
 
-- user 表的创建
CREATE TABLE `user` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8

DELIMITER $$
CREATE PROCEDURE user_test()
BEGIN
  -- 定义变量
  DECLARE sys_user_id BIGINT;
  DECLARE sys_user_name VARCHAR(11);
  DECLARE done INT;
  -- 创建游标，并存储数据
  DECLARE cur_test CURSOR FOR 
      SELECT id AS user_id,user_name AS sys_user_name  FROM `sys_user`;
  -- 游标中的内容执行完后将 done 设置为 1 
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
  -- 打开游标
  OPEN cur_test;
  -- 执行循环
  posLoop:LOOP
  -- 判断是否结束循环
        IF done=1 THEN
        LEAVE posLoop;
        END IF;
  -- 取游标中的值
  FETCH cur_test INTO sys_user_id,sys_user_name;
  -- 执行更新操作
    UPDATE `user` SET NAME=sys_user_name WHERE id=sys_user_id;
  END LOOP posLoop;
  -- 释放游标 
  CLOSE cur_test; 
END $$
DELIMITER
 
DROP PROCEDURE user_test;
-- 调用存储过程
CALL user_test;

select * from sys_user;
