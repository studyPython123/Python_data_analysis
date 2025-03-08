-- 21、查询不同老师所教不同课程平均分从高到低显示
#标准答案
select t.t_id,t.t_name,c.c_id,c.c_name,round(avg(s_score), 2) as avg_score
from score sc
inner join course c on sc.c_id = c.c_id
inner join teacher t on t.t_id = c.t_id
group by t.t_id,c.c_id
order by t.t_id,avg_score desc;
#答案二
select teacher.t_id,teacher.t_name,course.c_name,sc.`平均成绩`,rank() over(order by 平均成绩 desc) 平均分排名 from teacher 
join course on teacher.t_id = course.t_id
join (select course.t_id,avg(score.s_score) 平均成绩 from score join course on score.c_id = course.c_id group by course.t_id) 
sc on course.t_id = sc.t_id;
