-- 查看当前数据库所有的表
use mydataset1;
-- 查看表
show tables;
-- 查看表的创建语句
show create table student;
-- 查看表结构
desc student;
-- 删除表
drop table student;
-- 添加新的列
alter table student add dept varchar(20);
-- 修改列名和类型
alter table student change dept department varchar(30);
-- 删除列
alter table student drop department;
-- 修改表名
rename table student to stu;
