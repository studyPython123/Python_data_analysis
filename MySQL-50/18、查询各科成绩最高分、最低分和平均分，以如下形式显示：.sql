-- 18、查询各科成绩最高分、最低分和平均分，以如下形式显示：
-- 课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
-- – 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
select c.c_id 课程ID,c.c_name 课程名称,max(sc.s_score) 最高分,min(sc.s_score) 最低分,round(avg(sc.s_score),2) 平均成绩,
concat(round(sum(case when (s_score >=60) then 1 else 0 end)/count(*)*100,2),'%') as 及格率,
concat(round(sum(case when (s_score >=70 and s_score <80) then 1 else 0 end)/count(*)*100,2),'%') as 中等率,
concat(round(sum(case when (s_score >=80 and s_score <90) then 1 else 0 end)/count(*)*100,2),'%') as 优良率,
concat(round(sum(case when s_score >= 90 then 1 else 0 end)/count(*)*100,2),'%') as 优秀率
from course c 
inner join score sc on c.c_id = sc.c_id
group by c.c_id;

-- 统计各科及格人数
select s1.c_id c_id,count(*) count from score s1 
where (s1.s_score>=60 and s1.s_score<70) 
group by c_id;

-- 课程评级
select sc.c_id 课程id,
(case 
	when (sc.s_score>=60 and sc.s_score<70) then '及格'
	when (sc.s_score>=70 and sc.s_score<80) then '中等'
	when (sc.s_score>=80 and sc.s_score<90) then '优良'
	when (sc.s_score>=90 and sc.s_score<=100) then '优秀'
	else '不及格'
	end) as 评级,count(*)
from score sc
group by sc.c_id,评级;

-- 标准答案
select
   c.c_id as 课程ID,c.c_name as 课程name,
	max(s_score) as 最高分,
	min(s_score) as 最低分,
	round(avg(s_score), 2) as 平均分,
	concat(round(sum(case when s_score >= 60 then 1 else 0 end) / count(*) * 100, 2), '%') as 及格率,
	concat(round(sum(case when s_score between 70 and 80 then 1 else 0 end) / count(*) * 100, 2), '%') as 中等率,
	concat(round(sum(case when s_score between 80 and 90 then 1 else 0 end) / count(*) * 100, 2), '%') as 优良率,
	concat(round(sum(case when s_score >= 90 then 1 else 0 end) / count(*) * 100, 2), '%') as 优秀率
from course c
inner join score s on c.c_id = s.c_id
group by c.c_id;





-- 18、查询各科成绩最高分、最低分和平均分，以如下形式显示：
-- 课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
-- – 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90

select c.c_id,c.c_name,max(sc.s_score) 最高分,min(sc.s_score) 最低分,round(avg(sc.s_score),2) 平均分 from score sc
inner join course c on c.c_id = sc.c_id
group by sc.c_id;

select * from (
select *,row_number() over(partition by sc.c_id order by sc.s_score)  as rn
from score sc
) scc
where scc.rn <=3;
















