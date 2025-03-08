-- 38、查询课程编号为01且课程成绩在80分以上的学生的学号和姓名
select
	student.s_id,
	student.s_name 
from
	student
	join score on student.s_id = score.s_id 
	and score.s_score >= 80 
	and score.c_id = '1';