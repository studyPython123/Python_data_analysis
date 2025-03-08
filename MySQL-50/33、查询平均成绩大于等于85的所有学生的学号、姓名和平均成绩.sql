-- 33、查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩
select student.s_id,student.s_name,t.avg_score from student join 
(select student.s_id,round(avg(score.s_score),2) avg_score from student join score on student.s_id = score.s_id group by student.s_id) 
t on student.s_id = t.s_id and t.avg_score >= 85;