-- 2、查询"01"课程比"02"课程成绩低的学生的信息及课程分数
select s.*,sc1.s_score coures01,sc2.s_score course02 from student s
join(
  select * from score where c_id = 1
) sc1 on s.s_id = sc1.s_id
join (
  select * from score where c_id = 2
) sc2 on s.s_id = sc2.s_id
where sc1.s_score < sc2.s_score;

-- 利用已有视图查询
select s1.*,s2.c_id,s2.s_score from score_1 s1 join score_2 s2 on s1.s_id = s2.s_id and s1.s_score < s2.s_score;