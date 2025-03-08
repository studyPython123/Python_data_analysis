-- 12、查询至少有一门课与学号为"01"的同学所学相同的同学的信息
explain select * from student
where s_id in (
	select distinct s_id
	from score s
	inner join (
		select c_id from score where s_id = 1
	) t1
	on s.c_id = t1.c_id
);


explain select distinct
	student.* 
from
	student
	join score on student.s_id = score.s_id 
	and score.c_id in (
	select
		sc.c_id 
	from
		student st
	join score sc on st.s_id = sc.s_id 
	and st.s_id = '01')