-- 13、查询和"01"号的同学学习的课程完全相同的其他同学的信息
select * from student
where s_id in (
	 select s_id
	 from score s
	 inner join (
		select c_id from score where s_id = 1
	 ) t1
	 on s.c_id = t1.c_id
	 where s_id != 1
	 group by s_id having count(*) = (
		select count(*) from score where s_id = 1
	 )
);
