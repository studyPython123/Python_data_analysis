-- 16、检索"01"课程分数小于60，按分数降序排列的学生信息
select s.*,sc.s_score from student s 
inner join (
   select sc.s_id,sc.s_score from score sc
   inner join(
    select c.c_id from course c
    where c.c_id = 1
   ) c on sc.c_id = c.c_id
   where sc.s_score < 60
) sc on sc.s_id = s.s_id
order by sc.s_score desc; 