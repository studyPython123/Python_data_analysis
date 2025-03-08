-- 创建表
-- 选择数据库
USE mydataset1;
-- 创建表
create table if not exists student(
  sid int,
  name varchar(20),
  gender varchar(20),
  age int,
  brith date,
  address varchar(20)
);