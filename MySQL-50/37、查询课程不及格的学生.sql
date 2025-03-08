-- 37、查询课程不及格的学生
select
	student.s_id,
	student.s_name,
	course.c_name,
	score.s_score 
from
	student
	join score on student.s_id = score.s_id 
	and score.s_score < 60
	join course on score.c_id = course.c_id;
	
select distinct student.s_name from student join score on student.s_id = score.s_id and score.s_score<60