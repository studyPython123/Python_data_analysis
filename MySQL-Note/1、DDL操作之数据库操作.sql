-- 1、DDL操作之数据库操作(不区分大小写)
-- 查看所以数据库
SHOW DATABASES;
-- 创建数据库
CREATE DATABASE IF NOT EXISTS mydataset1;
-- 选择使用哪一个数据库
USE mydataset1;
-- 删除数据库
DROP DATABASE IF EXISTS mydataset1;
-- 修改数据库编码通常是utf8
ALTER DATABASE mydataset1 CHARACTER SET utf8;
