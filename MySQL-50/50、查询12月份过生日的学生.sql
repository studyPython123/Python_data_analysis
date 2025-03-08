-- 50、查询12月份过生日的学生
select
	* 
from
	student 
where
	month ( student.s_birth ) = 12;