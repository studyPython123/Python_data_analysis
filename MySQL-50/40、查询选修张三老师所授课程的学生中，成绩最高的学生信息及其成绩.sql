-- 40、查询选修"张三"老师所授课程的学生中，成绩最高的学生信息及其成绩
select
	student.*,
	score.s_score 
from
	student
	join score on student.s_id = score.s_id
	join course on score.c_id = course.c_id
	join teacher on course.t_id = teacher.t_id 
	and teacher.t_name = '张三' 
order by
	score.s_score desc 
	limit 1;