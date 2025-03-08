-- 19、按各科成绩进行排序，并显示排名
select student.s_id,student.s_name,course.c_id,course.c_name 课程名称,score.s_score 成绩,
rank() over(partition by course.c_name ORDER BY score.s_score DESC) 排名 
from student 
join score on score.s_id = student.s_id
join course on course.c_id = score.c_id; -- 用了窗口函数

