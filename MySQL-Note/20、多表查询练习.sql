use mydataset1;
-- 创建表格
create table if not exists dept(
	deptno int primary key,
	dname varchar(20),
	loc varchar(20)
);
-- 插入数据
insert into dept values(10,'accounting','new york');
insert into dept values(20,'research','dallas');
insert into dept values(30,'sales','chicago');
insert into dept values (40,'operations','boston');

-- 创建员工表
create table emp(
	empno int primary key,
	ename varchar(20),
	job varchar(20),
	mar int,
	hiredate date,
	sal double,
	comm double,
	deptnp int
);
alter table emp change deptnp deptno int;
-- 添加主外键关系
alter table emp add 
constraint foreign key emp(deptno) 
references dept(deptno);
-- 插入数据
insert into emp  values(7369,'smith','emp',7902,'1980-12-17',800,null,20);
insert into emp values(7499,'allen','salesman',7698,'1981-02-20',1600,300,30);
insert into emp values(7521,'ward','salesman',7698,'1981-02-22',1250,500,30);
insert into emp values(7566,'jones','manager',7839,'1981-04-02',2975,null,20);
insert into emp values(7654,'martin','salesman',7698,'1981-09-28',1250,1400,30);
insert into emp values(7698,'blake','manager',7839,'1981-05-01',2850,null,30);
insert into emp values(7782,'clark','manager',7839,'1981-06-09',2450,null,10);
insert into emp values(7788,'scott','analyst',7566,'1987-07-03',3000,null,20);
insert into emp values(7839,'king','president',null,'1981-11-17',5000,null,10);
insert into emp values(7844,'turner','salesman',7698,'1981-09-08',1500,0,30);
insert into emp values(7876,'adams','clerk',7788,'1987-07-13',1100,null,20);
insert into emp values(7900,'james','clerk',7698,'1981-12-03',3000,null,20);
insert into emp values(7902,'ford','analyst',7566,'1981-12-03',950,null,30);
insert into emp values(7934,'miller','clerk',7782,'1981-01-23',1300,null,10);

-- 创建工资等级表
create table salgrade(
	grade int,
	losal double,
	hisal double
);
-- 插入数据
insert into salgrade values (1,700,1200);
insert into salgrade values (2,1201,1400);
insert into salgrade values (3,1401,2000);
insert into salgrade values (4,2001,3000);
insert into salgrade values (5,3001,9999);

-- 1、返回所有员工的部门名和部门号
select e.ename,e.deptno,d.dname from emp e 
join dept d on e.deptno = d.deptno;
-- 2、工资多于smith的员工信息
select e.* from emp e where e.sal  >  (
	select e.sal from emp e 
	where e.ename = 'smith');
-- 	3、返回员工和所属经理的姓名
select a.ename 下级,b.ename 上级 from emp a,emp b where a.mar = b.empno;
-- 4、返回雇员的雇佣日早于期经理雇佣日期的员工表
select a.* from emp a
join emp b on a.mar = b.empno and a.hiredate < b.hiredate; 
-- 5、返回员工姓名及其所在部门名称
select e.ename,d.dname from emp e 
join dept d on e.deptno = d.deptno;
-- 6、返回从事clerk工作的员工姓名和所在部门名称
select e.ename,d.dname from emp e 
join dept d on e.deptno = d.deptno
where e.job = 'clerk';
-- 7、返回部门号及其本部门最低工作
select deptno,min(sal) from emp group by deptno;
-- 8、返回销售部门所有员工的姓名
select ename from emp a
where a.deptno in (
	select d.deptno from dept d
	where d.dname = 'sales'
);
-- 9、返回与scott从事相同工作的员工
select * from emp e where e.job = 
(select b.job from emp b where b.ename = 'scott') 
and e.ename != 'scott';
-- 10、返回工资多余平均工资的员工
select e.* from emp e where e.sal > (
	select avg(sal) from emp 
);
-- 11、返回工资高于30部门所有员工工资水平的员工信息
select e.* from emp e 
where e.sal > (
	select max(e.sal) from emp e 
	where e.deptno = 30
);
select e.* from emp e 
where e.sal > all(
	select e.sal from emp e 
	where e.deptno = 30
);
-- 12、返回员工工作及其从事工作的最低工资
select e.job,min(e.sal) as min_sal from emp e group by e.job;
-- 13、计算员工的年薪，并且按照年薪排序
update emp set comm = 0 where ename not in (
	'allen','turner','martin','ward'
);
update emp set comm = 0 where comm is null;

select ename,12*sal+comm as year_sal from emp 
order by  year_sal desc;
-- ifnull函数
select ename,12*sal+ifnull(comm,0) as year_sal from emp 
order by  year_sal desc;
-- 14、返回工资处于第四级别的员工的姓名
-- 方法一
select ename from emp where sal 
between (select s.losal from salgrade s where s.grade = 4) 
and (select s.hisal from salgrade s where s.grade = 4) ;
-- 方法二
select ename from emp 
join salgrade s on s.grade = 4
where sal between s.losal and s.hisal;

-- 15、返回工资为第二级别的职员姓名和部门所在地
-- 方法一
select e.ename,d.loc from emp e join dept d on e.deptno = d.deptno
where e.sal 
between (select s.losal from salgrade s where s.grade = 2) 
and (select s.hisal from salgrade s where s.grade = 2); 
-- 方法二
select e.ename,d.loc from emp e 
join dept d on e.deptno = d.deptno
join salgrade s on s.grade = 2 and e.sal between s.losal and s.hisal;















