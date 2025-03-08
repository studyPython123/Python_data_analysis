-- 25、查询各科成绩前三名的记录
select * from (select score.s_id,student.s_name,score.c_id,course.c_name,score.s_score,
rank() over(partition by score.c_id order by score.s_score desc) rank1 from score
join student on score.s_id = student.s_id
join course on course.c_id = score.c_id) t
where t.rank1< 4;