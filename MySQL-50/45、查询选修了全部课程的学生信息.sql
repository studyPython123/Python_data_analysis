-- 45、查询选修了全部课程的学生信息
select
	* 
from
	student 
where
	student.s_id in (
	select
		score.s_id 
	from
		score 
	group by
		score.s_id 
having
	count( score.c_id ) = ( select count(*) from course ));