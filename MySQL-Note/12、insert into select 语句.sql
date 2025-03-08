use mydataset1;
-- 从table1查询结果插入到table2
insert into table2 select * from table1;
-- 
insert into table2(field1,field2,field3)
select value1,value2,value3 from table1;  