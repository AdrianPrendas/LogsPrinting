conn sys/manager as sysdba

--drop table logminerFiltered;

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
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_04\O1_MF_1_8_FXYNT7NJ_.ARC', -
       OPTIONS => DBMS_LOGMNR.NEW);

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_7_FXWO5VB8_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_8_FXWO7HZ2_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_9_FXWO7JFL_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_10_FXWOHZ6V_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_11_FXWOJ25N_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_12_FXWOJC5T_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_11_03\O1_MF_1_13_FXWOJK88_.ARC');
-------------------------------------------------------------------------------------------------------



EXECUTE DBMS_LOGMNR.START_LOGMNR( -
OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG);

 + -
              DBMS_LOGMNR.COMMITTED_DATA_ONLY + -
              DBMS_LOGMNR.PRINT_PRETTY_SQL + -
              DBMS_LOGMNR.CONTINUOUS_MINE);

SELECT SUPPLEMENTAL_LOG_DATA_MIN FROM V$DATABASE;
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

EXECUTE DBMS_LOGMNR_D.BUILD( -
       OPTIONS=> DBMS_LOGMNR_D.STORE_IN_REDO_LOGS);--este procedure genera un checkpoint y un switch

EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG);

CREATE OR REPLACE PROCEDURE filting_logs 
IS
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

--SELECT USERNAME,TABLE_SPACE,TABLE_NAME,SQL_REDO FROM V$LOGMNR_CONTENTS where username ='USER1';
--select * from logminerFiltered;
select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None';