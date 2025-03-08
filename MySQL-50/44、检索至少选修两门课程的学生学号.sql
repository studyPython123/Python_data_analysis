-- 44、检索至少选修两门课程的学生学号
select
	score.s_id 
from
	score 
group by
	score.s_id 
having
	count( score.c_id ) >= 2;
	
CREATE TABLE teacher1 (
  teacherid BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '教师id',
  tname VARCHAR(200) COMMENT '教师名称',
  age INT COMMENT '年龄'
) COMMENT '教师表';
