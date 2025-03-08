-- 24、查询学生平均成绩及其名次
# 我的答案
select student.s_id,student.s_name,sc.`平均成绩`,row_number() over(order by 平均成绩 desc) 平均成绩名次 
from student join 
(select score.s_id,round(avg(score.s_score),2) 平均成绩 from score group by score.s_id)
sc on student.s_id = sc.s_id;

#网上答案
select (@i := @i + 1) as rank,t2.*
from (select  @i := 0) var
cross join (
	select s.s_id,s.s_name,avg_score
	from student s
	inner join (
		select s_id,round(avg(s_score), 2) as avg_score
		from score
		group by s_id
	) t1
	on s.s_id = t1.s_id
	order by avg_score desc
) t2;
