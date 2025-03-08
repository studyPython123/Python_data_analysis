-- 增删改
use mydataset1;
show tables;
desc stu;
desc student;
alter table student drop familyname;
-- 插入值
insert into student values(456,'张三','15167842341','wsdawd@123','营销部',1),
  (789,'王五','09876543211','sddrer@1234','销售部',0);-- 位置插入
insert into student(id,name,tel,email,department,gender) values(); -- 控制添加的变量，关键词插入
-- 数据修改
update student set 
name = '王五' where id = 123;-- 修改满足条件的值
update student set tel = '18770107022' , 
  name = 'SSC' where id = 123; -- 修改多列
-- 数据删除
delete from student where id = 123; -- 一次删除一行
-- 清空数据表
truncate table student;-- 类似删除表格后再创建一个空表
truncate student;-- 可以省略table