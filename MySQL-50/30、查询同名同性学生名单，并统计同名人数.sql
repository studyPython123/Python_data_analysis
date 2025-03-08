-- 30、查询同名同性学生名单，并统计同名人数
select student.s_name,student.s_sex,count(student.s_id) as cont from student group by student.s_name,student.s_sex having cont >1;