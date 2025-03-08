-- 34、查询课程名称为"数学"，且分数低于60的学生姓名和分数
select student.s_name,course.c_name,score.s_score from student join score on student.s_id = score.s_id
join course on score.c_id = course.c_id and course.c_name = '数学' and  score.s_score < 60;

