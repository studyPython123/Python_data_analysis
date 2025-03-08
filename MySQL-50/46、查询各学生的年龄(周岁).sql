-- 46、查询各学生的年龄(周岁)
select
	s_id,s_name,s_birth,
	if (
		month(current_date()) < month(s_birth) or (month(current_date()) = month(s_birth) and day(current_date()) < day(s_birth)),
		year(current_date()) - year(s_birth) -1,
		year(current_date()) - year(s_birth)
	)
	as s_age
from student;
