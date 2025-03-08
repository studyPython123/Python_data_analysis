-- 36、查询任何一门课程成绩在70分以上的学生姓名、课程名称和分数
select student.s_id,course.c_name,score.s_score from student join score on student.s_id = score.s_id join course on score.c_id = course.c_id and student.s_id
join (select score.s_id from score group by score.s_id having max(score.s_score)>70) t on t.s_id = student.s_id and score.s_score > 70;

select
	student.s_name 学生姓名,
	course.c_name 课程名称,
	score.s_score 课程分数 
from
	student
	join score on student.s_id = score.s_id
	join course on score.c_id = course.c_id 
	and score.s_id in (
	select
		sc.s_id 
	from
		score sc 
	group by
		sc.s_id 
having
	min( sc.s_score )> 70)