use mydataset1;
-- ALL 
-- 查询年龄大于1003部门年龄的员工信息
select * from emp3
where age >  all(
  select age from emp3
  where dept_id = '1001'
);
-- 查询 不属于任何一个部门的员工信息
select * from emp3
syswhere dept_id not in (
  select deptno from dept3
);
-- 拓展，不在销售部和研发部的人员信息
select * from emp3
where dept_id not in (
  select deptno from dept3
  where name in ('研发部','销售部')
);
-- ANY
-- 查询年龄大于1003部门任意一个员工年龄的员工信息
-- 方法一
select * from emp3
where age > any (
	select age from emp3
	where dept_id = '1001'
);
select * from emp3;
-- 方法二
select * from emp3
where age > (
	select min(age) from emp3
	where dept_id = 1001
);
-- IN
-- 查询研发部和销售部的员工信息
-- 方法一
select e.* from emp3 e
where e.dept_id in (
 select d.deptno from dept3 d 
 where d.name in ('研发部','销售部')
);
-- 方法二
select e.*,d.`name` from emp3 e 
inner join(
	select d.deptno,d.name from dept3 d 
	where d.name in ('研发部','销售部')
) d on d.deptno = e.dept_id;
-- EXISTS
-- 查询公司是否有大于60岁的员工
select * from emp3 a where exists(
	select * from emp3 b where a.age >50
);
-- 查询有所属部门的员工信息
select * from emp3 a where exists(select * from dept3 b where a.dept_id = b.deptno);