-- 创建学生表 student
create table student (
	s_id int primary key,
	s_name varchar(8),
	s_birth date,
	s_sex varchar(4)
);
-- 插入学生数据
insert into student values
(1,'赵雷','1990-01-01','男'),
(2,'钱电','1990-12-21','男'),
(3,'孙风','1990-05-20','男'),
(4,'李云','1990-08-06','男'),
(5,'周梅','1991-12-01','女'),
(6,'吴兰','1992-03-01','女'),
(7,'郑竹','1989-07-01','女'),
(8,'王菊','1990-01-20','女');
-- 创建课程表 course
create table course (
	c_id int primary key,
	c_name varchar(8),
	t_id int
);
-- 插入课程数据
insert into course values
(1,'语文',2),
(2,'数学',1),
(3,'英语',3);
-- 创建教师表 teacher
create table teacher (
	t_id int primary key,
	t_name varchar(8)
);
-- 插入教师数据
insert into teacher values
(1,'张三'),
(2,'李四'),
(3,'王五');
-- 创建成绩表 score
create table score (
	s_id int,
	c_id int,
	s_score int
);
-- 插入成绩数据
insert into score values
(1,1,80),
(1,2,90),
(1,3,99),
(2,1,70),
(2,2,60),
(2,3,65),
(3,1,80),
(3,2,80),
(3,3,80),
(4,1,50),
(4,2,30),
(4,3,40),
(5,1,76),
(5,2,87),
(6,1,31),
(6,3,34),
(7,2,89),
(7,3,98);







