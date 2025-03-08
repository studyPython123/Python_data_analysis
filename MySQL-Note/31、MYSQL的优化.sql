use mydb4;
-- 下面的命令显示了当前 session 中所有统计参数的值
show session status like 'Com_______';  -- 查看当前会话统计结果
show global  status  like 'Com_______';  -- 查看自数据库上次启动至今统计结果
show status like 'Innodb_rows_%';       -- 查看针对Innodb引擎的统计结果

-- 查看慢日志配置信息 
show variables like '%slow_query_log%'; 
-- 开启慢日志查询 
set global slow_query_log=1; 
-- 查看慢日志记录SQL的最低阈值时间 
show variables like 'long_query_time%';
-- 修改慢日志记录SQL的最低阈值时间 
set global long_query_time=4;

-- 定位低效率执行SQL-show processlist  
show processlist; 
-- 1） id列，用户登录mysql时，系统分配的"connection_id"，可以使用函数connection_id()查看
-- 2） user列，显示当前用户。如果不是root，这个命令就只显示用户权限范围的sql语句
-- 3） host列，显示这个语句是从哪个ip的哪个端口上发的，可以用来跟踪出现问题语句的用户
-- 4） db列，显示这个进程目前连接的是哪个数据库
-- 5） command列，显示当前连接的执行的命令，一般取值为休眠（sleep），查询（query），连接（connect）等
-- 6） time列，显示这个状态持续的时间，单位是秒
-- 7） state列，显示使用当前连接的sql语句的状态，很重要的列。state描述的是语句执行中的某一个状态。一个sql语句，以查询为例，可能需要经过copying to tmp table、sorting result、sending data等状态才可以完成
-- 8） info列，显示这个sql语句，是判断问题语句的一个重要依据
