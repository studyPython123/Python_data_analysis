-- 10、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息
select s.* from student s
where s.s_id in(
  select sc.s_id from score as sc 
  where sc.c_id = 1
  and sc.s_id not in(
    select sc.s_id from score sc
    where sc.c_id = 2
  )
);


-- 9、1找到学过编号1的同学id
select s_id from score where c_id = 1;
-- 9、2找到学过编号2的同学id
select s_id from score where c_id = 2;

select * from student where s_id in (select s_id from score where c_id = 1) and s_id not in (select s_id from score where c_id = 2);