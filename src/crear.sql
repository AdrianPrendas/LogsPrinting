connect system/manager as sysdba;

CREATE USER user1 IDENTIFIED BY user1
DEFAULT TABLESPACE TS1 QUOTA UNLIMITED ON TS1;
GRANT CONNECT TO user1;
GRANT ALL PRIVILEGES TO user1;



CREATE USER user2 IDENTIFIED BY user2
DEFAULT TABLESPACE TS2 QUOTA UNLIMITED ON TS2;
GRANT CONNECT TO user2;
GRANT ALL PRIVILEGES TO user2;



CREATE USER user3 IDENTIFIED BY user3
DEFAULT TABLESPACE TS3 QUOTA UNLIMITED ON TS3;
GRANT CONNECT TO user3;
GRANT ALL PRIVILEGES TO user3;

commit;

connect user1/user1;

CREATE table t1(a int, b int, c varchar(20))tablespace TS1;
insert into t1(a,b,c) values (1,1,'Hola soy u1'); 
insert into t1(a,b,c) values (1,2,'Adios tprueba1');
insert into t1(a,b,c) values (2,1,'Adios tprueba1');
select a,b from t1;
select c,b from t1;
select c,a from tprueba1;
update t1 set a= 32 where b=1;
update t1 set a= 54 where b=2;
commit;
update t1 set a= 32 where a=2;
update t1 set a= 54 where b=1;
commit;
delete from t1 where a=32;
update t1 set a= 32 where b=1;
update t1 set a= 54 where b=2;
commit;

connect user2/user2;

CREATE table t2(a int, b int, c varchar(20))tablespace TS2;
insert into t2(a,b,c) values (2,1,'Hola soy u2');
insert into t2(a,b,c) values (2,2,'Adios t2');
select a,b from t2;
select c,b from t2;
select c,a from t2;
update t2 set a= 32 where b=1;
update t2 set a= 54 where b=2;
commit;
update t2 set a= 32 where a=2;
update t2 set a= 54 where b=1;
commit;
delete from t2 where a=32;
update t2 set a= 32 where b=1;
update t2 set a= 54 where b=2;
commit;


connect user3/user3; 

CREATE table t3(a int, b int, c varchar(20))tablespace TS3;
insert into t3(a,b,c) values (3,1,'Hola soy u3'); 
insert into t3(a,b,c) values (3,2,'Adios t3');
select a,b from t3;
select c,b from t3;
select c,a from t3;
update t3 set a= 3 where b=1;
update t3 set a= 4 where b=2;
commit;
update t3 set a= 323 where a=2;
update t3 set a= 5 where b=1;
commit;
delete from t3 where a=32;
update t3 set a= 33 where b=2;
update t3 set a= 54 where b=2;
commit;

connect user1/user1;
select * from t1;

connect user2/user2;
select * from t2;

connect user3/user3;
select * from t3;