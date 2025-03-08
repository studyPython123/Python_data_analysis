-- 创建表
use mydataset1;
create table if not exists employee(
  id int unsigned,
  name varchar(20),
  gender char(1),
  salary int
);
alter table employee change gender gender char(1);
-- 插入数据
insert into employee values(1,'张三','男',2000),
                                            (2,'李四','男',1000),
                                            (3,'王五','女',4000);
desc employee;
update employee set salary = 5000; 
update employee set salary = 3000 where name = '张三';
update employee set salary = 4000 ,gender = '女' where name = '李四';
update employee set salary = salary + 1000 where name = '王五';
