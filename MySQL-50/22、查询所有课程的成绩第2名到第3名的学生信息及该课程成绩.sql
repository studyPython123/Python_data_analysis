-- 22、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩
select * from (select student.*,score.c_id,score.s_score,row_number() over(partition by score.c_id order by score.s_score desc)  as rank1
from student join score on student.s_id = score.s_id) t
where rank1 in (2,3);