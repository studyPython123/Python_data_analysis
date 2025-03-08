-- 42、查询每门课程成绩最好的前三名
select
	course.c_name,
	t.* 
from
	(
	select
		student.*,
		score.c_id c_id,
		score.s_score s_score,
		row_number() over ( partition by score.c_id order by score.s_score desc ) as 排名 
	from
		student
		join score on student.s_id = score.s_id 
	) t
	join course on t.c_id = course.c_id 
	and t.排名 <= 3;