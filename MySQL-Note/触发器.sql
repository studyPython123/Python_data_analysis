CREATE DATABASE trigger_set;
USE trigger_set;
drop table students;
-- 创建学生表
CREATE TABLE students(
  id TINYINT PRIMARY KEY auto_increment,
	stu_name VARCHAR(10) NOT NULL,
	sex CHAR(4) DEFAULT('男'),
	age TINYINT NOT NULL
)
-- 创建日志表
CREATE TABLE log(
	id TINYINT PRIMARY KEY auto_increment,
	time TIMESTAMP,
	operation VARCHAR(10),
	detail VARCHAR(50)
)
-- 插入学生信息
insert into students(stu_name,sex,age) value ('张三','男',17),
('李四','男',25),
('王妞','女',18),
('王麻子','男',28);
select * from students;

-- 创建插入触发器
CREATE TRIGGER trigger_insert
	AFTER insert on students for each ROW
	insert into log(time,operation,detail) VALUES (now(),'insert',CONCAT('新记录：',new.id,new.stu_name,new.sex,new.age));
	
-- 测试触发器
insert into students(stu_name,sex,age) values ('大壮','男',14);
select * from log;

TRUNCATE log;
drop TRIGGER trigger_insert;

-- 创建更新触发器
CREATE TRIGGER trigger_update
	AFTER UPDATE on students for each ROW
	insert into log(time,operation,detail) VALUES (now(),'update',CONCAT('(',old.id,old.stu_name,old.sex,old.age,')','-->','(',new.id,new.stu_name,new.sex,new.age,')'));
	
UPDATE  students set stu_name = '狗蛋',sex = '男', age = 12 WHERE id = 2;
SELECT * from log;

-- 创建删除触发器
CREATE TRIGGER trigger_delete
	AFTER DELETE on students for each ROW
	insert into log(time,operation,detail) VALUES (now(),'delete',CONCAT('旧记录：',old.id,old.stu_name,old.sex,old.age));
	
delete from students where stu_name = '大壮'
-- 删除触发器
DROP TRIGGER trigger_insert;
DROP TRIGGER trigger_update;
DROP TRIGGER trigger_delete;