-- 4.	MySQL实训_04
##################################################################################################
#4.	MySQL实训_04
##################################################################################################
#第一题
create database BToy;
use BToy;

create table boys(
Boy_id int,
Boy varchar(20),
Toy_id int);

insert into boys values
(1,'Tony',3),
(2,'Andy',2),
(3,'Frank',1),
(4,'Only',2),
(4,'Only',3),
(5,'Terrance',4),
(5,'Terrance',6);

create table toys (
toy_id int,
toy varchar(20)
);

insert into toys values
(1,'ToyA'),
(2,'ToyB'),
(3,'ToyC'),
(4,'ToyD'),
(5,'ToyE');

-- 1.	请用left join写出查询代码，找出每个男孩买了哪个玩具，并写出输出结果集。
select boys.Boy,toys.toy from boys left join toys on boys.Toy_id = toys.toy_id;
-- 2.	找出既买过“ToyB”也买过”ToyC”的男孩
select Boy from boys join toys on boys.Toy_id = toys.toy_id and toys.toy in ('ToyB','ToyC')
group by boys.Boy
having  count(*) >= 2;

create table drink(
 name varchar(10) comment '饮料名称',
 price decimal(10,1) comment '价格',
 carbohydrate decimal(10,1) comment'碳水化合物',
 color varchar(10)comment '颜色' ,
 ice varchar(10) comment '加冰' ,
 calorie decimal(10,1) comment'卡路里'
);
insert into drink values
('A',1,8.4,'Yellow','N',33),
('B',2.5,3.2,'Blue','N',12),
('C',3.5,8.8,'Orange','Y',35),
('D',2.5,5.4,'Green','Y',24),
('E',5.5,42.5,'Purple','Y',171);
-- 1.	列出不加冰，且颜色为yellow，且卡路里大于30的饮料名称和价格
select name,price from drink where drink.ice = 'N' and drink.color = 'Yellow' and drink.calorie > 30;
-- 2.	列出碳水化合物小于4，或者加冰的饮料名称和颜色
select name,color from drink where drink.carbohydrate<4 or drink.ice = 'Y';
-- 3.	我想买所有卡路里小于100的饮料各一杯，需要多少钱
select sum(drink.price) 总费用 from drink where drink.calorie<100;