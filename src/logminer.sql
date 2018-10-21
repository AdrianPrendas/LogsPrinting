-- Este fichero activa al log-miner
-- Es necesario configurar manualmente la ruta de los archive logs, y la ruta de salida
-- SELECT user, date, time, sql, sql-1 FROM V$LOGMNR_CONTENTS > salida.txt
-- la salida va a dar a otro fichero
conn sys/manager as sysdba

-- se setea la salida del spool, no se pudo como .csv, asi que adecua para luego convertilo en .csv
set recsepchar  "%"
set linesize 1024
set trimspool on
set feedback off
set pagesize 0
set verify off
set echo off
set term off

--rutas de los archive
EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_10_19\O1_MF_1_36_FWLWTHFS_.ARC', -
       OPTIONS => DBMS_LOGMNR.NEW);

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FlashRecoveryArea\GO\ARCHIVELOG\2018_10_19\O1_MF_1_37_FWLWY7PN_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FLASHRECOVERYAREA\GO\ARCHIVELOG\2018_10_19\O1_MF_1_38_FWLWY87N_.ARC');

EXECUTE DBMS_LOGMNR.ADD_LOGFILE(-
   LOGFILENAME => 'C:\GO\FLASHRECOVERYAREA\GO\ARCHIVELOG\2018_10_19\O1_MF_1_39_FWN12ZY2_.ARC');
--

EXECUTE DBMS_LOGMNR.START_LOGMNR( -
OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG + -
              DBMS_LOGMNR.COMMITTED_DATA_ONLY + -
              DBMS_LOGMNR.PRINT_PRETTY_SQL);


ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;
--SELECT SUPPLEMENTAL_LOG_DATA_MIN FROM V$DATABASE;
EXECUTE DBMS_LOGMNR_D.BUILD( -
       OPTIONS=> DBMS_LOGMNR_D.STORE_IN_REDO_LOGS);

EXECUTE DBMS_LOGMNR.START_LOGMNR(OPTIONS => DBMS_LOGMNR.DICT_FROM_ONLINE_CATALOG);

--SELECT USERNAME AS usr,(XIDUSN || '.' || XIDSLT || '.' || XIDSQN) as XID, 
--  SQL_REDO FROM V$LOGMNR_CONTENTS 
--   WHERE SEG_OWNER IS NULL OR SEG_OWNER NOT IN ('SYS', 'SYSTEM');

--fichero de salida
spool 'G:\\Carrera\Ciclo II 2018\\Administracion de Base de datos\\Proyecto\\Trazabilidad de transacciones\\data\\unstructured.txt'

SELECT SEG_OWNER, TIMESTAMP as date_, (XIDUSN || '.' || XIDSLT || '.' || XIDSQN) AS time_, SQL_REDO, sql_undo  FROM V$LOGMNR_CONTENTS WHERE SEG_OWNER = 'USER1';

spool off

quit

--EOF
--exit

--SELECT table_name, column_name, data_type, data_length
--FROM USER_TAB_COLUMNS
--WHERE table_name = 'T1'

