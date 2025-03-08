use mydataset1;
-- 
select count(pid) from product;
-- 
select * from product 
where price = (select max(price) from product);
-- 
select count(pid) from product where price >= 200;
-- 
select max(price) max_price,min(price) min_price from product;
-- 
select avg(price) avg_price from product;
-- null不处理
create database mysql_exercise;






