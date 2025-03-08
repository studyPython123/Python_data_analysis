-- 14、查询没学过"张三"老师讲授的任一门课程的学生姓名
select s.s_name from student s
where s.s_id not in(
  select sc.s_id from score sc
  inner join(
    select c.c_id,c.t_id from course c
    inner join teacher t on t.t_id = c.t_id
    where t.t_name = '张三'
  ) c on sc.c_id = c.c_id
);
