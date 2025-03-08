-- 23、统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比
#熟练使用case方法
select course.c_id 课程编号,course.c_name 课程名称,
sum(case when score.s_score between 85 and 100 then 1 else 0 end) as '[100-85]',
concat(round(sum(case when score.s_score between 85 and 100 then 1 else 0 end)/count(score.s_id)*100,2),'%')  as '百分比',
sum(case when score.s_score between 70 and 85 then 1 else 0 end) as '[85-70]',
concat(round(sum(case when score.s_score between 70 and 85 then 1 else 0 end)/count(score.s_id)*100,2),'%')  as '百分比',
sum(case when score.s_score between 60 and 70 then 1 else 0 end) as '[70-60]',
concat(round(sum(case when score.s_score between 60 and 70 then 1 else 0 end)/count(score.s_id)*100,2),'%')  as '百分比',
sum(case when score.s_score between 0 and 60 then 1 else 0 end) as '[60-0]',
concat(round(sum(case when score.s_score between 0 and 60 then 1 else 0 end)/count(score.s_id)*100,2),'%')  as '百分比'
from course join score on course.c_id = score.c_id group by course.c_id;