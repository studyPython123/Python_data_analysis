-- 6、查询"李"姓老师的数量
select count(*) from teacher as t
where t.t_name like '李%';