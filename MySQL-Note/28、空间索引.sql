use mydb4;

create table shop_info (
  id  int  primary key auto_increment comment  'id',
  shop_name varchar(64) not null comment '门店名称',
  geom_point geometry not null comment '经纬度',
  spatial key geom_index(geom_point) -- 空间索引
);

show index from shop_info;
show engines;