use mydb4;

show variables like 'log_error%';
-- 查看MySQL是否开启了binlog日志
show variables like 'log_bin';
 
 
-- 查看binlog日志的格式
show variables like 'binlog_format';
 
-- 查看所有日志
show binlog events;
 
-- 查看最新的日志
show master status;
 
-- 查询指定的binlog日志
show binlog events in 'binlog.000010';
select * from mydb1.emp2;
select count(*) from mydb1.emp2;
update mydb1.emp2 set salary = 8000;

-- 从指定的位置开始,查看指定的Binlog日志
show binlog events in 'binlog.000010' from 156;

-- 从指定的位置开始,查看指定的Binlog日志,限制查询的条数
show binlog events in 'binlog.000010' from 156 limit 2;
--从指定的位置开始，带有偏移，查看指定的Binlog日志,限制查询的条数
show binlog events in 'binlog.000010' from 666 limit 1, 2;
 
-- 清空所有的 binlog 日志文件
reset master

-- 查看MySQL是否开启了查询日志
show variables like 'general_log';
 
-- 开启查询日志
set global  general_log=1;
select * from emp;
-- 查看慢查询日志是否开启（用于优化）
show variables like 'slow_query_log%';
# 该参数用来控制慢查询日志是否开启， 可取值： 1 和 0 ， 1 代表开启， 0 代表关闭
slow_query_log=1
 # 该参数用来指定慢查询日志的文件名
slow_query_log_file=slow_query.log
/* 该选项用来配置查询的时间限制， 超过这个时间将认为值慢查询， 
将需要进行日志记录， 默认10s
*/
long_query_time=10

