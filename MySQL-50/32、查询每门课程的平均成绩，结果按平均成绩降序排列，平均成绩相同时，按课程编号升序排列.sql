-- 32、查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select course.c_id,course.c_name,t.avg_score from score join course on score.c_id = course.c_id
join
(select score.c_id,avg(score.s_score) avg_score from score group by score.c_id) t on t.c_id = score.c_id
group by course.c_id
order by t.avg_score desc,t.c_id asc;