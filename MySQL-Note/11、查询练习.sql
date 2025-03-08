use mydataset1;
show tables;
create table if not exists student(
  id int,
  name varchar(20),
  gender varchar(20),
  chinese int,
  english int,
  math int
);
alter table student change gender gender varchar(20);
insert into student 
values(1,'张明','男',89,78,90),
          (2,'李进','男',67,53,95),
          (3,'王五','女',87,78,77),
          (4,'李一','女',88,98,92),
          (5,'李财','男',82,84,67),
          (6,'张宝','男',55,85,45),
          (7,'黄蓉','女',75,65,30),
          (7,'黄蓉','女',75,65,30);
-- 查询表中所有学生的信息
select * from student;
-- 查询表中所有学生的姓名和对应的英语成绩
select name,english from student;
-- 过滤表中重复数据
select distinct * from student;
-- 统计每个学生的总分
select name,chinese+english+math score from student;
-- 所有学生总分上加10分特长分
select name,chinese+english+math+10 score_10 from student;
-- 使用别名表示学生分数
select name ,chinese chinese_score,english english_score,math math_score 
from student;
-- 查询英语成绩大于90分的同学
select * from student where english>90;
-- 查询总分大于200分的所有同学
select * ,(chinese+english+math) score from student where (chinese+english+math)>200
-- 查询英语成绩在80-90之间的同学
select * from student where english between 80 and 90;
-- 查询英语成绩不在80-90之间的同学
select * from student where english not between 80 and 90;
-- 查询所有姓李的学生英语成绩
select name,english from student where name like '李%';
-- 查询数学80并且语文80的同学
select * from student where math = 80 and chinese = 80;
-- 查询英语80或者总分200的同学
select * from student where english = 80 or (chinese + math + english) = 200;
-- 对数学成绩降序排序输出
select name,math from student order by math desc;
-- 对总分排序后输出，从高到低
select name,(chinese + english + math) score from student
order by score desc;
-- 对姓李的学生成绩排序输出
select name,(chinese + english + math) score from student
where name like '李%'
order by score desc;
-- 查询男生女生有多少人，并且降序输出
select gender,count(*) count from student
group by gender
order by count desc;
use mydataset1;
-- 创建表格
create table if not exists emp(
	empno int, -- 员工编号
	ename varchar(20), -- 员工姓名
	job varchar(20), -- 工作名称
	mgr int, -- 上级领导编号
	hiredate date, -- 入职日期
	sal int, -- 薪资
	comm int, -- 奖金
	deptno int  -- 部门编号
);
-- 插入数据
INSERT INTO emp VALUES(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);
INSERT INTO emp VALUES(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30);
INSERT INTO emp VALUES(7521,'WARD','SALESMAN',7698,'1981-02-22',1250,500,30);
INSERT INTO emp VALUES(7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20);
INSERT INTO emp VALUES(7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30);
INSERT INTO emp VALUES(7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,NULL,30);
INSERT INTO emp VALUES(7782,'CLARK','MANAGER',7839,'1981-06-09',2450,NULL,10);
INSERT INTO emp VALUES(7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20);
INSERT INTO emp VALUES(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);
INSERT INTO emp VALUES(7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30);
INSERT INTO emp VALUES(7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20);
INSERT INTO emp VALUES(7900,'JAMES','CLERK',7698,'1981-12-03',950,NULL,30);
INSERT INTO emp VALUES(7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20);
INSERT INTO emp VALUES(7934,'MILLER','CLERK',7782,'1982-01-23',1300,NULL,10);
select count(*) from emp;-- 检测表格
-- 查询练习
-- 按员工编号升序排列不在10号部门工作的员工信息
select * from emp
where deptno != 10
order by empno asc;
-- 查询名字第二个字不是‘A’且薪水大于1000元的员工信息，按年薪降序排序
select * from emp
where (ename not like '_A%') && sal >1000
order by sal*12+comm desc;
-- 求每个部门的平均薪水
select deptno,avg(sal) from emp
group by deptno; 
-- 求每个部门的最高薪水
select deptno,max(sal) from emp
group by deptno; 
-- 求每个部门每个岗位的最高薪水
select deptno,job,max(sal)from emp
group by deptno,job
order by deptno,max(sal) desc; 
-- 平均薪资大于2000的部门编号
select deptno,avg(sal) from emp group by deptno having avg(sal)>2000;
-- 将部门平均薪水大于1500的部门编号列，安装平均薪水降序排序
select deptno,avg(sal) avg_sal from emp 
group by deptno having avg_sal >1500
order by avg_sal desc;
-- 选择公司有奖金的员工姓名，工资
select ename,sal from emp where comm is not null;
-- 查询员工最高工资和最低工资之间的差距
select max(sal)-min(sal) sal_gap from emp;




