-- 11、查询没有学全所有课程的同学的信息
select s.* from student s
where s.s_id not in(
  select sc.s_id from score sc
  group by sc.s_id
  having count(*) =(
     select count(*) from course
  )
);




-- 查找课程的数量
select count(c_id) 课程数 from course;
-- 求未学满课程的学生id(没有统计到为选课的同学)
explain select * from student 
where s_id not in 
(select s_id from score 
group by s_id
having count(*) = (select count(c_id) 课程数 from course));