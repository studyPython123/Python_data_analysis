-- 26、查询每门课程被选修的学生数
select course.c_id,course.c_name,count(score.s_id) 人数 from score join course on score.c_id = course.c_id group by course.c_id;