-- 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
explain select s.* from student s
where s.s_id in (
 select sc.s_id from score as sc
 where  sc.c_id in (1,2)
 group by sc.s_id
 having count(*) = 2
);


-- 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
-- 9、1找到学过编号1的同学id
select s_id from score where c_id = 1;
-- 9、2找到学过编号2的同学id
select s_id from score where c_id = 2;
-- 9、3学过编号为"01"并且也学过编号为"02"的课程的同学id、创建视图
create or replace 
view student12
as
select s_id from student where s_id in (select s_id from score where c_id = 1) and s_id in (select s_id from score where c_id = 2);
-- 9、4查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
select * from student where s_id in (select * from student12);


-- 查询01和02都没学的学生
select * from student st join score sc on st.s_id = sc.s_id where sc.c_id not in ('1','2')

-- 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
explain select st.* from student st join (select sc.s_id s_id from score sc where sc.c_id = 1) a on st.s_id = a.s_id join
(select s.s_id s_id from score s where s.c_id = 2) b on a.s_id = b.s_id
