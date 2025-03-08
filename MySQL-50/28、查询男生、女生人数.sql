-- 28、查询男生、女生人数
select student.s_sex,count(student.s_id) from student group by student.s_sex;