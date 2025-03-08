use mydataset1;
--  查询年龄最大的员工信息显示工号，员工年龄
select e.eid,e.ename from emp3 e
where e.age in (
  select max(e.age) from emp3 e
);
--  查询研发部和销售部员工的信息
select e.*,d.name from emp3 e
inner join(
  select deptno,name from dept3
  where name in ('研发部','销售部')
) d on d.deptno = e.dept_id;
-- 查询研发部20以下的员工信息，包括员工号，员工姓名，部门名字
-- 方法一
select e.*,d.`name` from emp3 e
inner  join (
  select d.deptno,d.name from dept3 d 
  where d.name = '研发部'
) d on d.deptno = e.dept_id
where e.age < 20;
-- 方法二
select *from emp3
inner  join dept3 on deptno = dept_id and 
(age < 20 and name = '研发部');

