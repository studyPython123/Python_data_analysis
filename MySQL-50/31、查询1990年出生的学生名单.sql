-- 31、查询1990年出生的学生名单
select student.* from student where year(student.s_birth) = '1990';
