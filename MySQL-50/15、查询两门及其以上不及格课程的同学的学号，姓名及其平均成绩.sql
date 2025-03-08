-- 15、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select s.s_id,s.s_name,round(avg(sc1.s_score),2) from student s
inner join(
  select sc.s_id from score sc 
  where sc.s_score < 60
  group by sc.s_id 
  having count(*) >=2
) sc on sc.s_id = s.s_id
inner join score sc1 on sc1.s_id = s.s_id
group by s.s_id;