-- 1、查询“01”课程比“02”课程成绩高的学生的信息及课程分数
-- 方法1
select s.*,sc1.s_score course01,sc2.s_score course02 from student s 
inner join (
  select * from score where c_id = 1
) sc1 on s.s_id = sc1.s_id
inner join(
  select * from score where c_id = 2
) sc2 on s.s_id = sc2.s_id
where sc1.s_score >sc2.s_score;

-- 方法2
select s.*,s1.s_score course1,s2.s_score course2 from student s,score s1,score s2
where s.s_id = s1.s_id and s.s_id = s2.s_id and s1.c_id = 1 and s2.c_id = 2
and s1.s_score > s2.s_score;

-- 
select s.*,sc1.s_score 课程1分数,sc2.s_score 课程2分数 from student s 
inner join(
	select sc.s_score,sc.s_id from score sc 
	where sc.c_id = 1
) sc1 on sc1.s_id = s.s_id
inner join (
 select sc.s_id,sc.s_score from score sc 
 where sc.c_id = 2
)sc2 on sc2.s_id = s.s_id
where sc1.s_score > sc2.s_score;



-- 创建视图查询
-- 1、查询“01”课程比“02”课程成绩高的学生的信息及课程分数
--  1、1 查询课程1的成绩
create or replace 
view score_1
as 
(select s.*,c_id,s_score from student s join score sc on s.s_id = sc.s_id and sc.c_id = 1);
--  1、2 查询课程2的成绩
create or replace 
view score_2
as 
(select s.*,c_id,s_score from student s join score sc on s.s_id = sc.s_id and sc.c_id = 2);
--  1、3查询“01”课程比“02”课程成绩高的学生的信息及课程分数
select s1.*,s2.c_id,s2.s_score from score_1 s1 join score_2 s2 on s1.s_id = s2.s_id and s1.s_score > s2.s_score;






-- 1、查询“01”课程比“02”课程成绩高的学生的信息及课程分数





