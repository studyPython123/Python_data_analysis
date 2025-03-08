-- 35、查询所有学生的课程及分数情况
select student.s_id,student.s_name,
sum(case score.c_id when 1 then score.s_score else 0 end) as 语文,
sum(case score.c_id when 2 then score.s_score else 0 end) as 数学,
sum(case score.c_id when 3 then score.s_score else 0 end) as 英语
from student join score on student.s_id = score.s_id
group by student.s_id;