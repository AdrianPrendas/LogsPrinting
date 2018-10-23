connect system/manager as sysdba;

CREATE USER user1 IDENTIFIED BY user1
DEFAULT TABLESPACE TS1 QUOTA UNLIMITED ON TS1;
GRANT ALL PRIVILEGES TO user1;


CREATE USER user2 IDENTIFIED BY user2
DEFAULT TABLESPACE TS1 QUOTA UNLIMITED ON TS1;
GRANT ALL PRIVILEGES TO user2;


CREATE USER user3 IDENTIFIED BY user3
DEFAULT TABLESPACE TS1 QUOTA UNLIMITED ON TS1;
GRANT ALL PRIVILEGES TO user3;
commit;

connect user1/user1;

CREATE table tprueba1(a int, b int, c varchar(20))tablespace TS1;
insert into tprueba1(a,b,c) values (1,1,'Hola soy u1'); 
insert into tprueba1(a,b,c) values (1,2,'Adios tprueba1');
insert into tprueba1(a,b,c) values (2,1,'Adios tprueba1');
select a,b from tprueba1;
select c,b from tprueba1;
select c,a from tprueba1;
update tprueba1 set a= 32 where b=1;
update tprueba1 set a= 54 where b=2;
	commit;
update tprueba1 set a= 32 where a=2;
update tprueba1 set a= 54 where b=1;
	commit;
delete from tprueba1 where a=32;
update tprueba1 set a= 32 where b=1;
update tprueba1 set a= 54 where b=2;

commit;

connect user2/user2;

CREATE table tprueba2(a int, b int, c varchar(20))tablespace TS1;
insert into tprueba2(a,b,c) values (2,1,'Hola soy u2');
insert into tprueba2(a,b,c) values (2,2,'Adios t2');
select a,b from tprueba2;
select c,b from tprueba2;
select c,a from tprueba2;
update tprueba2 set a= 32 where b=1;
update tprueba2 set a= 54 where b=2;
	commit;
update tprueba2 set a= 32 where a=2;
update tprueba2 set a= 54 where b=1;
	commit;
delete from tprueba2 where a=32;
update tprueba2 set a= 32 where b=1;
update tprueba2 set a= 54 where b=2;

commit;
commit;

connect user3/user3; 

CREATE table tprueba3(a int, b int, c varchar(20))tablespace TS1;
insert into tprueba3(a,b,c) values (3,1,'Hola soy u3'); 
insert into tprueba3(a,b,c) values (3,2,'Adios t3');
	select a,b from tprueba1;
select c,b from tprueba3;
select c,a from tprueba3;
update tprueba3 set a= 3 where b=1;
update tprueba3 set a= 4 where b=2;
	commit;
update tprueba3 set a= 323 where a=2;
update tprueba3 set a= 5 where b=1;
	commit;
delete from tprueba3 where a=32;
update tprueba3 set a= 33 where b=2;
update tprueba3 set a= 54 where b=2;

commit;
commit;

connect user1/user1;
select * from tprueba1;

connect user2/user2;
select * from tprueba2;

connect user3/user3;
select * from tprueba3;