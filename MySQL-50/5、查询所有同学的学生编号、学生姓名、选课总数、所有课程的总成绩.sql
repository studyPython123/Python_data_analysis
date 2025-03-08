-- 5、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
select s.s_id,s.s_name,ifnull(cnt_course, 0) as cnt_course,ifnull(sum_score, 0) as sum_score
from student s
left join (
	select s_id,count(*) as cnt_course,sum(s_score) as sum_score
	from score
	group by s_id
) t1
on s.s_id = t1.s_id;

-- 创建视图
create or replace 
view sc_count
as 
select s_id,count(*) as cnt_course,sum(s_score) as sum_score from score group by s_id;
-- 用视图查询
select s.s_id,s.s_name,ifnull(cnt_course, 0) as cnt_course,ifnull(sum_score, 0) as sum_score
from student s
left join sc_count
on s.s_id = sc_count.s_id;


