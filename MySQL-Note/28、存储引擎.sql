use mydb4;

-- 查询当前数据库支持的存储引擎：
show engines;
 
-- 查看当前的默认存储引擎：
show variables like '%storage_engine%';

-- 查看某个表用了什么引擎(在显示结果里参数engine后面的就表示该表当前用的存储引擎): 
show create table emp; 
 
-- 创建新表时指定存储引擎：
create table(...) engine=MyISAM;
 
-- 修改数据库引擎
alter table emp engine = INNODB;
alter table emp engine = MyISAM;


-- 修改MySQL默认存储引擎方法
-- 1. 关闭mysql服务 
-- 2. 找到mysql安装目录下的my.ini文件： 
-- 3. 找到default-storage-engine=INNODB 改为目标引擎，
--    如：default-storage-engine=MYISAM 
-- 4. 启动mysql服务

