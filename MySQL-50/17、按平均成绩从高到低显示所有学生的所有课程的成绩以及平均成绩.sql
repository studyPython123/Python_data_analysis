-- 17、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
select
	s.s_id as 学号,s.s_name as 姓名,
	sum(case c_id when 1 then s_score else 0 end) as 语文,
	sum(case c_id when 2 then s_score else 0 end) as 数学,
	sum(case c_id when 3 then s_score else 0 end) as 英语,
	ifnull(round(avg(s_score), 2), 0) as 平均成绩
from student s
left join score sc on s.s_id = sc.s_id
group by s.s_id
order by 平均成绩 desc;

select s.s_id 学号,s.s_name 姓名,
sum(case sc.c_id	 when 1 then sc.s_score else 0 end) as 语文,
sum(case sc.c_id	 when 2 then sc.s_score else 0 end) as 数学,
sum(case sc.c_id	 when 3 then sc.s_score else 0 end) as 英语,
ifnull(round(avg(sc.s_score),2),0) as 平均成绩
from student s left join score sc on s.s_id = sc.s_id
group by s.s_id
order by 平均成绩 desc;


