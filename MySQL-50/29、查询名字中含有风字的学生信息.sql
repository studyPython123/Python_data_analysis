-- 29、查询名字中含有"风"字的学生信息
select student.s_id,student.s_name,student.s_birth,student.s_sex from student where student.s_name like '%风%';