use mydataset1;
-- 'abc'是否以a开头
select 'abc' regexp '^a';
select * from product where pname regexp '^海';
-- 结尾
select 'abc' regexp 'c$';
select * from product where pname regexp '水$';
-- 
select 'abc' regexp '.b';
-- 
select 'abc' regexp '[xyz]';
select 'abc' regexp '[ayz]';
-- 取反
select 'abc' regexp '[^xyz]';
select 'abc' regexp '[^abc]';
-- *是0次或者多次
select 'stab' regexp '.ta*b';
select ' ' regexp 'a*';
-- +表示至少一次
select 'stab' regexp '.ta+b';
select ' ' regexp 'a+';
-- ？要么0次要么1次
select 'stab' regexp '.ta?b';
select 'aa' regexp 'a？';
-- a1|a2，匹配a1或者a2
select 'a' regexp 'a|b';
select 'b' regexp 'a|b';
select 'a' regexp '^(a|b)';
select 'b' regexp '^(a|b)';
select 'c' regexp '^(a|b)';
-- a{m}表示匹配m个a
select 'auuuuc' regexp 'au{4}c';
-- a{m,}表示匹配m个或者更多a
select 'auuuuuc' regexp 'au{4,}c';
-- a{m,n}表示匹配m个到n个（包括n）a
select 'auuuuuc' regexp 'au{4,8}c';
-- ()作为一个整体
select 'xababy' regexp 'x(ab)*y';