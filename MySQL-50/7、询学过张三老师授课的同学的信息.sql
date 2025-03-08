-- 7、询学过"张三"老师授课的同学的信息
-- 方法一
select * from student s
where s.s_id in (
  select distinct sc.s_id from score as sc
  inner join (
    select c.c_id from course as c
    inner join teacher t on t.t_id = c.t_id
    where t.t_name = '张三'
  ) t on sc.c_id = t.c_id
) ;
-- 方法二
select s.* from student s,teacher t,course c,score sc
where s.s_id = sc.s_id
and sc.c_id = c.c_id
and c.t_id = t.t_id
and t.t_name = '张三';

-- 7、询学过"张三"老师授课的同学的信息
-- 7、1查询张三老师的id
select t_id from teacher where t_name = '张三';
-- 7、2在课程表上面找到老师id对应的课程id
select c_id from course where t_id = (select t_id from teacher where t_name = '张三');
-- 7、3在成绩表上面找到对应课程id的学生id
select s_id from score where c_id = (select c_id from course where t_id = (select t_id from teacher where t_name = '张三'));
-- 7、4在学生表上面找到对应学生id的信息
select * from student where s_id in (select s_id from score where c_id = (select c_id from course where t_id = (select t_id from teacher where t_name = '张三'))); -- 常规思路

-- 创建学过张三老师课程的学生id视图
create or replace
view zhangsan_s_id
as
(select s_id from score where c_id = (select c_id from course where t_id = (select t_id from teacher where t_name = '张三')));



select st.* from student st join score sc on st.s_id = sc.s_id join course c on sc.c_id = c.c_id join teacher t on c.t_id = t.t_id where t.t_name = '张三'

