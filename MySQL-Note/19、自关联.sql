use mydataset1;
-- 创建表，建立自关联约束
create table if not exists t_sanguo(
  eid int primary key,
  ename varchar(20),
  manager_id int,
  foreign key (manager_id) references t_sanguo(eid) -- 自关联约束
);
-- 插入数据
insert into t_sanguo values(1,'刘协',NULL);
insert into t_sanguo values(2,'刘备',1);
insert into t_sanguo values(3,'关羽',2);
insert into t_sanguo values(4,'张飞',2);
insert into t_sanguo values(5,'曹操',1);
insert into t_sanguo values(6,'许褚',5);
insert into t_sanguo values(7,'典韦',5);
insert into t_sanguo values(8,'孙权',1);
insert into t_sanguo values(9,'周瑜',8);
insert into t_sanguo values(10,'鲁肃',8);
-- 检查插入情况
select * from t_sanguo;
-- 查询人物信息和上级信息
select a.ename,b.ename from t_sanguo a, t_sanguo b
where a.manager_id = b.eid;
-- 查询所有人物及上级
select a.ename,b.ename from t_sanguo a
left join t_sanguo b on a.manager_id = b.eid;
-- 显示上级的上级
select a.ename,b.ename,c.ename from t_sanguo a
left join t_sanguo b on a.manager_id = b.eid
left join t_sanguo c on b.manager_id = c.eid;




