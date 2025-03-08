-- 20、查询学生的总成绩并进行排名
select student.s_id,student.s_name,sc.`总分`,rank() over(order by sc.`总分` desc)  from student
join 
(select score.s_id,sum(score.s_score) 总分 from score group by score.s_id) sc
on student.s_id = sc.s_id;

show variables like "%profiling%";
set profiling = 1; #打开
set profiling_history_size = 10;
show profiles;
set profiling=0; #关闭