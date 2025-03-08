-- 41、查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
select
	* 
from
	score 
where
	s_score in ( select s_score from score group by s_score having count(*) > 1 );