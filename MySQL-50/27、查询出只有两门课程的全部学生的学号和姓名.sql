-- 27、查询出只有两门课程的全部学生的学号和姓名
-- 方法一
select student.s_id,student.s_name from student join (select score.s_id from score group by score.s_id having count(score.c_id) = 2) t on student.s_id = t.s_id;
-- 方法二
select student.s_id,student.s_name from student where student.s_id in (select score.s_id from score group by score.s_id having count(score.c_id) = 2);