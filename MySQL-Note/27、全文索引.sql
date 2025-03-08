use mydb4;
-- 创建表格
create table t_article (
     id int primary key auto_increment ,
     title varchar(255) ,
     content varchar(1000) ,
     writing_date date -- , 
     -- fulltext (content) -- 创建全文检索
);
-- 插入数据
insert into t_article values(null,"Yesterday Once More","When I was young I listen to the radio",'2021-10-01');
insert into t_article values(null,"Right Here Waiting","Oceans apart, day after day,and I slowly go insane",'2021-10-02'); 
insert into t_article values(null,"My Heart Will Go On","every night in my dreams,i see you, i feel you",'2021-10-03');
insert into t_article values(null,"Everything I Do","eLook into my eyes,You will see what you mean to me",'2021-10-04');
insert into t_article values(null,"Called To Say I Love You","say love you no new year's day, to celebrate",'2021-10-05');
insert into t_article values(null,"Nothing's Gonna Change My Love For You","if i had to live my life without you near me",'2021-10-06');
insert into t_article values(null,"Everybody","We're gonna bring the flavor show U how.",'2021-10-07');

-- 创建全文索引的两种
alter table t_article add fulltext index_content(content)
-- 直接添加全文索引
create fulltext index index_content on t_article(content);

-- 使用全文索引
select * from t_article where match(content) against('yo'); -- 没有结果 单词数需要大于等于3 
select * from t_article where match(content) against('you'); -- 有结果






