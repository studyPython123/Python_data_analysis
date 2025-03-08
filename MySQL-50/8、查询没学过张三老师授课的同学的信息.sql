-- 8、查询没学过"张三"老师授课的同学的信息
-- 方法一
select
	* 
from
	student s 
where
	s.s_id not in (
	select distinct
		sc.s_id 
	from
		score as sc
		inner join ( select c.c_id from course as c inner join teacher t on t.t_id = c.t_id where t.t_name = '张三' ) t on sc.c_id = t.c_id 
	);-- 利用视图查询
select
	* 
from
	student 
where
	s_id not in ( select * from zhangsan_s_id );
	

select 
  *
from
	student 
where
	student.s_id not in (
	select
		st.s_id 
	from
		student st
		join score sc on st.s_id = sc.s_id
		join course c on sc.c_id = c.c_id
		join teacher t on c.t_id = t.t_id 
where
	t.t_name = '张三')
	
	
	