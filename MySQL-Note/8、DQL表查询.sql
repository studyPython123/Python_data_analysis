use mydataset1;
-- 创建表
create table if not exists product(
  pid int primary key auto_increment, -- 商品编号
  pname varchar(20) not null, -- 商品名称
  price double, -- 商品价格
  category_id varchar(10) -- 商品所属分类
);
truncate product; -- 清空数据表
-- 插入商品信息
insert into product values(null,'海尔洗衣机',5000,'coo1'),
(null,'美的冰箱',3000,'coo1'),
(null,'格力空调',5000,'coo1'),
(null,'九阳电饭煲',5000,'coo1'),

(null,'啄木鸟衬衣服',300,'coo2'),
(null,'恒源祥西裤',800,'coo2'),
(null,'花花公子夹克',440,'coo2'),
(null,'劲霸休闲裤',266,'coo2'),
(null,'海澜之家卫衣',180,'coo2'),
(null,'杰克琼斯运动裤',430,'coo2'),

(null,'兰蔻面霜',300,'coo3'),
(null,'雅诗兰黛精华水',200,'coo3'),
(null,'SK-II神仙水',350,'coo3'),
(null,'香奈儿香水',350,'coo3'),
(null,'资生堂粉底液',180,'coo3'),

(null,'老北京方便面',56,'coo4'),
(null,'良品铺子海带丝',17,'coo4'),
(null,'三只松鼠坚果',88,null);

-- 1、查询所有商品
select * from product;
-- 2、查询商品名称和价格
select pname,price from product;
-- 3、别名查询，使用关键词as（as可省略）
-- 3.1、表别名
select * from product as p;
select * from product p;
-- 3.2、列别名
select pname as '商品名称' ,price as '商品价格' from product;
-- 4、去掉重复值(多列时要全部重复才去重)
select distinct category_id,price from product;
-- 5、查询结果表达式(不修改原表)
select pname,price+10 as new_price from product;
-- 6、运算符
select pname, price*1.1 as new_price from product;
select * from product where pname = '海尔洗衣机';
select * from product where price = 800;
-- 价格不为800的所有商品信息
select * from product where price != 800;
select * from product where price <> 800;
select * from product where not(price = 800);
-- 价格大于60的所有商品信息
select * from product where price > 60;
-- 价格在200到1000之间的所有商品信息
select * from product where price between 200 and 1000;
select * from product where price <=1000 && price >=200;
-- 使用least求最小值
select least(10,20,30) small_number; -- 10
select least(10,null,30); -- null
-- 使用greatest求最大值
select greatest(10,20,30); -- 30
select greatest(10,null,30); -- null
-- 
select * from product where pname = '海尔洗衣机';
-- 
select * from product where price = 800;
-- 
select * from product where price = 200 || price = 800;
-- 
select * from product where pname like '%裤%';
-- 
select * from product where pname like '海%';
-- 
select * from product where pname like '_蔻%';
-- 
select * from product where category_id is null;
-- 
select * from product where category_id is not null;
-- 
select * from product order by price asc;
select * from product where category_id = 'coo1' order by price desc;
select * from product order by price desc,category_id desc;
select distinct price from product order by price asc;

































