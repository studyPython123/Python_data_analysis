use mydb4;
-- 查看隔离级别
show variables like '%isolation%';
-- 设置隔离级别
/*
set session transaction isolation level 级别字符串
级别字符串：read uncommitted、read committed、repeatable read、serializable
*/
-- 设置read uncommitted
set session transaction isolation level read uncommitted;
-- 设置read committed
set session transaction isolation level read committed;
-- 设置repeatable read
set session transaction isolation level repeatable read;
-- 设置serializable
set session transaction isolation level serializable;
