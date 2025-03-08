-- 1、主键约束（唯一非空且不能重复）
use mydataset1;
create table if not exists 主键约束表(
  id int unsigned primary key,-- 主键
  name varchar(20),
  deptid int,
  salary double
);
-- 另一种方式
create table if not exists 约束表(
  id int unsigned,-- 主键
  name varchar(20),
  deptid int,
  salary double,
  constraint pk1 primary key(id)
);
-- 主键的作用（约束的列非空且唯一）
insert into 主键约束表(id, name,deptid,salary) values(1001,'张三',10,5000);
insert into 主键约束表(id, name,deptid,salary) values(1002,'李四',9,6000);
rename table 约束表 to 主键约束表;

-- 2、联合主键
create table if not exists 联合主键约束表(
  id int unsigned,
  name varchar(20),
  deptid int,
  salary double,
  constraint pk2 primary key(id,name) -- id和name联合成一个主键
);-- 主键任何一个都不能为空

-- 3、添加主键
alter table 主键约束表 add primary key(id);
alter table 联合主键约束表 add primary key(id,name);

-- 4、删除主键（删除时不分是否是联合主键）
alter table 主键约束表 drop primary key;

-- 5、自增长约束(与主键捆绑在一起)
 create table if not exists table1(
  id int unsigned primary key auto_increment,-- 有增长上限
  name varchar(20),
  dept varchar(20),
  tel char(11)
 );
insert into table1 values(null,'张三','销售部','15170108745');
insert into table1 values(null,'李四','研发部','16723569452');

-- 方式一：指定自增长初始值
 create table if not exists table1(
  id int unsigned primary key auto_increment,-- 有增长上限
  name varchar(20),
  dept varchar(20),
  tel char(11)
 )auto_increment = 100;
--  方式二： 创建表格之后再设置
 alter table table1 auto_increment = 100;
-- delete删除数据后从断点开始
-- truncate清理数据后从默认值开始 

-- 6、非空约束
create table if not exists table2(
  id int,
  name varchar(10) not null,
  address varchar(20) not null
);
-- 添加非空约束
alter table table2 modify name varchar(20)  not null ;
alter table table2 modify address varchar(20) not null ;
-- 删除非空约束
alter table table2 modify name varchar(20);
alter table table2 modify address varchar(20);

-- 7、唯一约束(可以有多个,不同于主键)
create table if not exists table2(
  id int,
  name varchar(10),
  address varchar(20),
  tel char(11) unique
);-- null和任何值都不相同 null != null
-- 添加约束方法二
alter table table2 add constraint unique1 unique(tel)
-- 删除约束
alter table table2 drop index unique1;

-- 8、默认约束
create table if not exists table3(
  id int,
  name varchar(10),
  address varchar(20) default '北京', -- 指定默认约束
  tel char(11) 
);
-- 添加默认值
alter table table3 modify address varchar(20) default '深圳';

-- 9、0填充约束
create table if not exists table4(
  id int(10) zerofill,-- 设置要填充的位数
  name varchar(10),
  address varchar(20),
  tel char(11) 
);
-- 添加约束
-- 删除约束
alter table table4 modify id int;

