-- 39、求每门课程的学生人数
select
	course.c_id,
	course.c_name,
	t.count_sid 
from
	course
	join ( select score.c_id, count( score.s_id ) count_sid from score group by score.c_id ) t on course.c_id = t.c_id;
	
	select score.c_id 课程编号, count(*) 学生人数 from score group by score.c_id