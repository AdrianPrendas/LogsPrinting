
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

--   select * from logminerFiltered 
--            where username <> 'UNKNOWN' 
--            and username <> 'SYS' 
--            and table_space <> 'None' 
--            and table_space <> 'UNKNOW' 
--            and table_name <> 'None';