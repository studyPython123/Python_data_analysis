-- 4、查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩(包括有成绩的和无成绩的)
select s.s_id,s.s_name,ifnull(round(avg_score,2),0) from student s
left join(
  select s_id,avg(s_score) avg_score from score
  group by s_id
) sc on s.s_id = sc.s_id 
where avg_score is null or avg_score < 60;

