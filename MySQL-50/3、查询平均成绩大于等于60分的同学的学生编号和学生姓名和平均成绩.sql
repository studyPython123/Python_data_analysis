-- 3、查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
-- 方法一
select s.s_id,s.s_name,round(sc.avg_score,2) avg_score from student s 
join(
  select s_id,avg(s_score) avg_score from score
  group by s_id
  having avg_score>=60
) sc on s.s_id =  sc.s_id;
-- 方法二
select s.s_id,s.s_name,avg(sc.s_score) avg_score from student s, score sc
where s.s_id = sc.s_id
group by s.s_id
having avg_score >=60;
-- 附加题：总分超过200分的同学
select s.*,round(sum(sc.s_score),2) sum_score from student s 
join score sc on s.s_id = sc.s_id
group by s.s_id
having sum_score > 200;

-- 创建视图my_view1
create or replace 
view my_view1
as 
select s_id,avg(s_score) avg_score from score
group by s_id
having avg_score> = 60;

select s.s_id,s.s_name,round(mv.avg_score,2) as avg_score from student s 
join my_view1 mv on s.s_id =  mv.s_id;


explain select st.s_id 学生编号,st.s_name 学生姓名,AVG(sc.s_score) avg_score from student st,score sc where st.s_id = sc.s_id GROUP BY sc.s_id HAVING avg_score >=60
explain select st.s_id 学生编号,st.s_name 学生姓名,AVG(sc.s_score) avg_score from student st inner join score sc on st.s_id = sc.s_id GROUP BY sc.s_id HAVING avg_score >=60
