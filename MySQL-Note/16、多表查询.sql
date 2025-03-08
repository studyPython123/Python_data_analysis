use mydataset1;
-- 创建部门表
create table if not exists dept3(
deptno varchar(20)primary key,-- 部门号
name varchar(20) -- 部门名字
);
-- 创建员工表
create table if not exists emp4(
eid varchar(20) primary key comment  '员工编号',-- 员工编号
ename varchar(20), -- 员工名字
age int,-- 员工年龄
dept_id varchar(20) -- 员工所属部门
);
show create table emp4;
describe emp4;
show tables;
show full columns from emp4;
insert into dept3 values('1001','研发部'),
				('1002','销售部'),
				('1003','财政部'),
				('1004','人事部');
insert into emp3 values('1','乔峰',20,'1001'),
('2','段誉',21,'1001'),
('3','虚竹',23,'1001'),
('4','阿紫',18,'1001'),
('5','扫地僧',35,'1002'),
('6','李秋水',33,'1002'),
('7','鸠摩智',50,'1002'),
('8','天山童姥',60,'1003'),
('9','慕容博',58,'1003');
-- 交叉连接查询
select * from dept3,emp3;
-- 内连接查询
select * from dept3,emp3 where dept3.deptno = emp3.dept_id;
select * from dept3 inner join emp3 on dept3.deptno = emp3.dept_id;
-- 查询研发部和销售部的所属员工
select *from dept3,emp3 where dept3.deptno =emp3.dept_id
and name in ('研发部','销售部');
select *from dept3 join emp3 on dept3.deptno =emp3.dept_id
and name in ('研发部','销售部');
-- 查询每个部门的员工数，并升序排序
select deptno,name,count(*) as total_cnt 
from dept3,emp3 where dept3.deptno = emp3.dept_id 
group by deptno 
order by total_cnt;
select deptno,name,count(*) as totil_count 
from dept3 join emp3 on dept3.deptno = emp3.dept_id 
group by deptno
order by totil_count asc;
-- 查询研发部门所属员工
select * from emp3 join dept3 on dept3.deptno = emp3.dept_id 
and dept3.name = '研发部';
-- 查询研发部和销售部的所属员工 
select * from emp3 a join dept3 b on a.dept_id = b.deptno
and b.name in  ('研发部','销售部');
-- 查询人数大于大于3的部门，并按照人数降序排序
select dept3.deptno,dept3.name,count(*) totil_count 
from dept3,emp3 where dept3.deptno = emp3.dept_id
group by dept3.deptno having totil_count  >= 3
order by totil_count desc; 
-- 左外链接
-- 查询哪些部门没有员工，哪些部门没有员工
explain select * from dept3 left outer join emp3 on dept3.deptno = emp3.dept_id;
explain select * from dept3 where dept3.deptno in (select emp3.dept_id from emp3);
create index index_emp3_name on emp3(ename);
explain select emp3.age from emp3 where emp3.ename = '阿紫';
drop index index_emp3_name on emp3;
-- 查询员工对应部门
select * from dept3 right outer 
join emp3 on dept3.deptno = emp3.dept_id;
select * from emp3 left outer 
join dept3 on dept3.deptno = emp3.dept_id;
-- 左外链接和右外链接的并集
explain
select * from dept3 left outer join emp3 on dept3.deptno = emp3.dept_id
union
select * from emp3 left outer join dept3 on dept3.deptno = emp3.dept_id
SELECT INSERT('我喜欢3',2,3,'超级') -- INSERT(str,pos,len,newstr) 从str的pos位置开始替换为长度为len字符串为newstr





CREATE TABLE sales (
  id INT PRIMARY KEY,
  product VARCHAR(50),
  category VARCHAR(50),
  sale_date DATE,
  quantity INT,
  revenue DECIMAL(10, 2)
);

INSERT INTO sales (id, product, category, sale_date, quantity, revenue)
VALUES
  (1, 'Product A', 'Category 1', '2022-01-01', 10, 100.00),
  (2, 'Product B', 'Category 1', '2022-01-01', 5, 50.00),
  (3, 'Product A', 'Category 2', '2022-01-02', 8, 80.00),
  (4, 'Product B', 'Category 2', '2022-01-02', 3, 30.00),
  (5, 'Product A', 'Category 1', '2022-01-03', 12, 120.00),
  (6, 'Product B', 'Category 1', '2022-01-03', 7, 70.00),
  (7, 'Product A', 'Category 2', '2022-01-04', 6, 60.00),
  (8, 'Product B', 'Category 2', '2022-01-04', 4, 40.00);


  SELECT 
	t1.*, 
	t2.avg_revenue FROM sales t1 
  LEFT JOIN (
		SELECT category, AVG(revenue) AS avg_revenue 
		FROM sales  
		GROUP BY category
  ) t2 ON t1.category = t2.category ORDER BY t1.category

SELECT
  sales.*,
  AVG( revenue ) OVER ( PARTITION BY category ) AS avg_revenue 
FROM
	sales

SELECT 
	*,
	RANK() OVER(PARTITION BY category ORDER BY quantity DESC) AS `quantity_rank`,
	DENSE_RANK() OVER(PARTITION BY category ORDER BY product DESC) AS `product_dense_rank`,
	ROW_NUMBER() OVER(PARTITION BY category ORDER BY product DESC) AS `product_row_number`,
	PERCENT_RANK() OVER(PARTITION BY category ORDER BY quantity DESC) AS `quantity_percent_rank`,
	CUME_DIST() OVER(PARTITION BY category ORDER BY quantity DESC) AS `quantity_cume_dist`
FROM sales

