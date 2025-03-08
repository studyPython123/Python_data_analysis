use mydataset1;
-- 
select category_id,count(*) from product group by category_id;
-- 
select category_id,count(*) from product group by category_id having count(*)>1;
select category_id,count(*) from product group by category_id having category_id = 'coo1';
select
  category_id,count(*) 
from 
  product 
group by 
  category_id 
having 
  count(*)>1
order by 
  count(*) 
desc;





