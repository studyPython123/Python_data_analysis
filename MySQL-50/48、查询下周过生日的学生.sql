-- 48、查询下周过生日的学生
select *
from student
where
	datediff(concat(year(current_date()), date_format(s_birth, '-%m-%d')), current_date())
	between 7 and 14
or
	datediff(concat(year(current_date()) + 1, date_format(s_birth, '-%m-%d')), current_date())
	between 7 and 14;
