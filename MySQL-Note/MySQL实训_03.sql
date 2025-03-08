##################################################################################################
#3.	MySQL实训_03
##################################################################################################
#第一步
CREATE DATABASE Loan;
USE Loan;

#第二步：建表。
 create table a1(LOAN_NO INT,
                ID_NO INT,
                ACTV_DT DATE);

create table a2(LOAN_NO INT,
                OD_DAYS INT);

create table a3(ID_NO INT,
                LIM INT,
                OUTSTANDING INT);

#第四步：插入数据。
insert into a1 values(1000114260,1,'2011-06-07'),
					  (1000143723,2,'2011-09-21'),
                      (1000162024,3,'2011-12-09'),
                      (1000174934,4,'2012-03-23'),
                      (1000182256,5,'2012-05-15');

Insert into a2 values(1000114260,90),
                      (1000174934,18),
                      (1000182256,0),
					  (1000143723,45),
                      (1000162024,3);

Insert into a3 values( 5,30000,25110),
                     (2,40000,40000),
                     (2,60000,56000),
                     (2,45000,45000),
                     (1,15000,6378),
                     (1,80000,60395),
                     (3,60000,57773),
                     (4,30000,28656),
                     (4,30000,10000);
										 
-- 创建表4
use loan;
/*表4中TYPE字段的要求：根据贷款逾期天数定义贷款类型（如果贷款逾期天数等于0则贷款类型为CURRENT；
如果贷款逾期天数大于0且小于等于89则贷款类型为MIDDLE；如果贷款逾期天数大于等于90则贷款类型为CHRGO）*/
create  table a4 select
a1.LOAN_NO,a1.ID_NO,a1.ACTV_DT,a2.OD_DAYS,
case when a2.OD_DAYS = 0 then 'CURRENT'
				when a2.OD_DAYS between 0 and 89 then 'MIDDLE'
				else 'CHRGO'
end as TYPE, a3.LIM,a3.OUTSTANDING
from a1 join a2 on a1.LOAN_NO = a2.LOAN_NO join a3 on a1.ID_NO = a3.ID_NO;

select * from a4;