conn sys/manager as sysdba

drop table logminerFiltered;

create table logminerFiltered(
    username varchar2(30),
    operation varchar2(32),
    table_name varchar2(32),
    table_space varchar2(32),
    seg_owner varchar2(32),
    date_ varchar(250),
    time_ varchar(250),
    sql_ varchar2(4000),
    sql_1 varchar2(4000)
);




-----------------------------------------------------------------------------------------------------
EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_10_23\O1_MF_1_8_FWYYGS1J_.ARC', -
       OPTIONS => DBMS_LOGMNR.NEW);

--EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
--   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_10_19\O1_MF_1_37_FWLWY7PN_.ARC');
--
--EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
--   LOGFILENAME => 'C:\GO\FLASHRECOVERYAREA\GO\ARCHIVELOG\2018_10_19\O1_MF_1_38_FWLWY87N_.ARC');
--
--EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
--   LOGFILENAME => 'C:\GO\FLASHRECOVERYAREA\GO\ARCHIVELOG\2018_10_19\O1_MF_1_39_FWN12ZY2_.ARC');
--
-------------------------------------------------------------------------------------------------------



EXECUTE DBMS_LOGMNR.START_LOGMNR( -
OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG + -
              DBMS_LOGMNR.COMMITTED_DATA_ONLY + -
              DBMS_LOGMNR.PRINT_PRETTY_SQL);


ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

EXECUTE DBMS_LOGMNR_D.BUILD( -
       OPTIONS=> DBMS_LOGMNR_D.STORE_IN_REDO_LOGS);

EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG);

CREATE OR REPLACE PROCEDURE filting_logs AS
  CURSOR cur IS SELECT USERNAME, OPERATION, TABLE_NAME, TABLE_SPACE, SEG_OWNER, TIMESTAMP as date_, (XIDUSN || ':' || XIDSLT || ':' || XIDSQN) AS time_, SQL_REDO, sql_undo 
                        FROM V$LOGMNR_CONTENTS WHERE OPERATION IS NOT NULL;
  username varchar2(30);
  operation varchar2(32);
  table_name varchar2(32);
  table_space varchar2(32);
  seg_owner varchar2(32);
  date_ varchar(250);
  time_ varchar(250);
  sql_ varchar2(4000);
  sql_1 varchar2(4000);
BEGIN
    OPEN cur;
    FETCH cur INTO username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1;
    WHILE cur % FOUND LOOP
        insert into logminerFiltered values(username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1);
        FETCH cur INTO username, operation, table_name, table_space, seg_owner, date_, time_, sql_, sql_1;
    END LOOP;
    commit;
    CLOSE cur;
END;
/
show errors;

exec filting_logs

select * from logminerFiltered;
