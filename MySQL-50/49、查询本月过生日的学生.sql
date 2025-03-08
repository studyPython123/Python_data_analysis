-- 49、查询本月过生日的学生
select *
from student
where month(s_birth) = month(current_date());
