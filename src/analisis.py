#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import sys
sys.path.append("C:\\Users\\Addiel\\Desktop\\LogsPrinting\\src")
import matplotlib as matplot
from db_oracle import DB
db = DB()

def loadTable():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    data.head(20000)
    return data

def userGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['USERNAME'])['USERNAME'].count().plot(kind="bar", x="USERNAME")

def tableGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TABLE_NAME'])['TABLE_NAME'].count().plot(kind="bar", x="OPERATION")

def tablespaceGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TABLE_SPACE'])['TABLE_SPACE'].count().plot(kind="bar", x="SEG_OWNER")    

def operationGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return  data.groupby(['OPERATION'])['OPERATION'].count().plot(kind="bar", x="OPERATION")

def dateGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['DATE_'])['DATE_'].count().plot(kind="bar", x="DATE")

def timeGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TIME_'])['TIME_'].count().plot(kind="bar", x="TIME_")





