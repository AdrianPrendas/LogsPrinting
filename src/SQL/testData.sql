conn system/manager 

@"C:\oraclexe\app\oracle\product\11.2.0\server\sqlplus\admin\pupbld.sql"

connect system/manager as sysdba;

CREATE USER user1 IDENTIFIED BY user1 DEFAULT TABLESPACE TS1 QUOTA UNLIMITED ON TS1;
GRANT CONNECT TO user1;
GRANT ALL PRIVILEGES TO user1;

CREATE USER user2 IDENTIFIED BY user2 DEFAULT TABLESPACE TS2 QUOTA UNLIMITED ON TS2;
GRANT CONNECT TO user2;
GRANT ALL PRIVILEGES TO user2;

CREATE USER user3 IDENTIFIED BY user3 DEFAULT TABLESPACE TS3 QUOTA UNLIMITED ON TS3;
GRANT CONNECT TO user3;
GRANT ALL PRIVILEGES TO user3;

CREATE USER user4 IDENTIFIED BY user4 DEFAULT TABLESPACE TS4 QUOTA UNLIMITED ON TS4;
GRANT CONNECT TO user4;
GRANT ALL PRIVILEGES TO user4;

CREATE USER user5 IDENTIFIED BY user5 DEFAULT TABLESPACE TS5 QUOTA UNLIMITED ON TS5;
GRANT CONNECT TO user5;
GRANT ALL PRIVILEGES TO user5;

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
insert into t3(a,b,c) values (2,1,'Hola soy u3');
insert into t3(a,b,c) values (2,1,'Hola soy u3');
insert into t3(a,b,c) values (2,1,'Hola soy u3');
insert into t3(a,b,c) values (2,2,'Adios t3');
insert into t3(a,b,c) values (2,2,'Adios t3');
insert into t3(a,b,c) values (2,2,'Adios t3');
insert into t3(a,b,c) values (2,2,'Adios t3');
select a,b from t3;
select c,b from t3;
select c,a from t3;
select * from t3;
update t3 set a= 32 where b=1;
update t3 set a= 54 where b=2;
commit;
update t3 set a= 32 where a=2;
update t3 set a= 54 where b=1;
commit;
delete from t3 where a=32;
update t3 set a= 32 where b=1;
update t3 set a= 54 where b=2;
delete from t3 where a=54;
commit;

connect user4/user4;

CREATE table t4(a int, b int, c varchar(20))tablespace TS4;
insert into t4(a,b,c) values (2,1,'Hola soy u3');
insert into t4(a,b,c) values (2,1,'Hola soy u3');
insert into t4(a,b,c) values (2,2,'Adios t4');
insert into t4(a,b,c) values (2,2,'Adios t4');
select a,b from t4;
select c,a from t4;
select * from t4;
update t4 set a= 32 where b=1;
commit;
update t4 set a= 32 where a=2;
update t4 set a= 54 where b=1;
commit;
delete from t4 where a=32;
update t4 set a= 54 where b=2;
delete from t4 where a=54;
commit;

connect user5/user5;

CREATE table t5(a int, b int, c varchar(20))tablespace TS5;
insert into t5(a,b,c) values (2,1,'Hola soy u2');
insert into t5(a,b,c) values (2,2,'Adios t5');
select a,b from t5;
select c,b from t5;
select c,a from t5;
update t5 set a= 32 where b=1;
update t5 set a= 54 where b=2;
commit;
update t5 set a= 32 where a=2;
update t5 set a= 54 where b=1;
commit;
delete from t5 where a=32;
update t5 set a= 32 where b=1;
update t5 set a= 54 where b=2;
commit;
insert into t5(a,b,c) values (2,3,'Hola soy u3');
insert into t5(a,b,c) values (2,3,'Hola soy u3');
insert into t5(a,b,c) values (2,3,'Hola soy u3');
insert into t5(a,b,c) values (2,3,'Adios t5');
insert into t5(a,b,c) values (2,4,'Adios t5');
insert into t5(a,b,c) values (2,4,'Adios t5');
insert into t5(a,b,c) values (2,4,'Adios t5');
select a,b from t5;
select c,b from t5;
select c,a from t5;
select * from t5;
update t5 set a= 32 where b=3;
update t5 set a= 54 where b=3;
commit;
update t5 set a= 32 where a=2;
update t5 set a= 54 where b=4;
commit;
delete from t5 where b=4;
update t5 set a= 32 where b=4;
update t5 set a= 54 where b=4;
delete from t5 where a=54;
commit;


connect user1/user1;
select * from t1;

connect user2/user2;
select * from t2;

connect user3/user3;
select * from t3;

connect user4/user4;
select * from t4;

connect user5/user5;
select * from t5;
