use mydb4;
create table `tb_seller` (
    `sellerid` varchar (100),
    `name` varchar (100),
    `nickname` varchar (50),
    `password` varchar (60),
    `status` varchar (1),
    `address` varchar (100),
    `createtime` datetime,
    primary key(`sellerid`)
); 
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('alibaba','阿里巴巴','阿里小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('baidu','百度科技有限公司','百度小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('huawei','华为科技有限公司','华为小店','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('itcast','传智播客教育科技有限公司','传智播客','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('itheima','黑马程序员','黑马程序员','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('luoji','罗技科技有限公司','罗技小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('oppo','OPPO科技有限公司','OPPO官方旗舰店','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('ourpalm','掌趣科技股份有限公司','掌趣小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('qiandu','千度科技','千度小店','e10adc3949ba59abbe56e057f20f883e','2','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('sina','新浪科技有限公司','新浪官方旗舰店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('xiaomi','小米科技','小米官方旗舰店','e10adc3949ba59abbe56e057f20f883e','1','西安市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('yijia','宜家家居','宜家家居旗舰店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
-- 创建组合索引 
create index idx_seller_name_sta_addr on tb_seller(name,status,address);
explain select * from tb_seller where name='小米科技' and status='1' and address='北京市'; -- 813
-- 最左前缀法则
 -- 如果索引了多列，要遵守最左前缀法则。指的是查询从索引的最左前列开始，并且不跳过索引中的列。
explain select * from tb_seller where name='小米科技'; -- 403
 
explain select * from tb_seller where name='小米科技' and status='1'; -- 410
explain select * from tb_seller where  status='1' and name='小米科技'; -- 410
-- 违法最左前缀法则 ， 索引失效：
explain select * from tb_seller where status='1'; -- nulll
-- 如果符合最左法则，但是出现跳跃某一列，只有最左列索引生效：
explain select * from tb_seller where name='小米科技'  and address='北京市'; -- 403

select @@have_profiling; 
set profiling=1; -- 开启profiling 开关； 
show profiles;

-- 范围查询右边的列，不能使用索引 。 
explain select * from tb_seller where name = '小米科技' and status >'1' and address='北京市'; 

-- 不要在索引列上进行运算操作， 索引将失效。 
explain select * from tb_seller where substring(name,3,2) = '科技';

-- 字符串不加单引号，造成索引失效。 
explain select * from tb_seller where name = '小米科技' and status = 1 ; -- 403
explain select * from tb_seller where name = '小米科技' and status = '1' ; -- 410

-- 1、范围查询右边的列，不能使用索引 。
-- 根据前面的两个字段name ， status 查询是走索引的， 但是最后一个条件address 没有用到索引。
explain select * from tb_seller where name='小米科技' and status >'1' and address='北京市';
 
-- 2、不要在索引列上进行运算操作， 索引将失效。
explain select * from tb_seller where substring(name,3,2)='科技'
 
-- 3、字符串不加单引号，造成索引失效。 
explain select * from tb_seller where name='小米科技' and status = 1 ;
 
-- 4、尽量使用覆盖索引，避免select *
-- 需要从原表及磁盘上读取数据
explain select * from tb_seller where name='小米科技'  and address='北京市';  -- 效率低
 
-- 从索引树中就可以查询到所有数据
explain select name from tb_seller where name='小米科技'  and address='北京市';  -- 效率高
explain select name,status,address from tb_seller where name='小米科技'  and address='北京市';  -- 效率高
-- 如果查询列，超出索引列，也会降低性能。
explain select name,status,address,password from tb_seller where name='小米科技'  and address='北京市';  -- 效率低
-- 尽量使用覆盖索引，避免select *
-- 需要从原表及磁盘上读取数据
explain select * from tb_seller where name='小米科技'  and address='北京市';  -- 效率低
 
-- 从索引树中就可以查询到所有数据
explain select name from tb_seller where name='小米科技'  and address='北京市';  -- 效率高
explain select name,status,address from tb_seller where name='小米科技'  and address='北京市';  -- 效率高
-- 如果查询列，超出索引列，也会降低性能。
explain select name,status,address,password from tb_seller where name='小米科技'  and address='北京市';  -- 效率低

-- 用or分割开的条件， 那么涉及的索引都不会被用到。
explain select * from tb_seller where name='黑马程序员' or createtime = '2088-01-01 12:00:00'; 
explain select * from tb_seller where name='黑马程序员' or address = '西安市';  
explain select * from tb_seller where name='黑马程序员' or status = '1';   
 
-- 以%开头的Like模糊查询，索引失效。
explain select * from tb_seller where name like '科技%'; -- 用索引
explain select * from tb_seller where name like '%科技'; -- 不用索引
explain select * from tb_seller where name like '%科技%';-- 不用索引
-- 弥补不足,不用*，使用索引列
explain select name from tb_seller where name like '%科技%';

--  1、如果MySQL评估使用索引比全表更慢，则不使用索引。
  -- 这种情况是由数据本身的特点来决定的
create index index_address on tb_seller(address);
 
explain select * from tb_seller where address = '北京市'; -- 没有使用索引
explain select * from tb_seller where address = '西安市'; -- 没有使用索引
 
 
--  2、is  NULL ， is NOT NULL  有时有效，有时索引失效。
create index index_address on tb_seller(nickname);
explain select * from tb_seller where nickname is NULL;  -- 索引有效
explain select * from tb_seller where nickname is not NULL; -- 无效

