-- 43、统计每门课程的学生选修人数（超过5人的课程才统计）
select
	t.c_id,
	course.c_name,
	t.count_sid 
from
	(
	select
		score.c_id c_id,
		count( score.s_id ) count_sid 
	from
		score 
	group by
		score.c_id 
	having
		count( score.s_id ) > 5 
	) t
	join course on t.c_id = course.c_id;