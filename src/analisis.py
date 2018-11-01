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
    data.head(50000)
    return data

def userGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    #explode =  [0.1, 0.1, 0.1, 0.1]    # explode 1st slice
    return data.groupby(['USERNAME'])['USERNAME'].count().plot(kind="pie", x="USERNAME",autopct='%1.1f%%',shadow=False)
    

def tableGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TABLE_NAME'])['TABLE_NAME'].count().plot(kind="bar", x="OPERATION")
    

def tablespaceGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TABLE_SPACE'])['TABLE_SPACE'].count().plot(kind="pie", x="SEG_OWNER",autopct='%1.1f%%',shadow=False)

def segOwnerGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    #explode = [0.1, 0.1, 0.1, 0.1]   # explode 1st slice
    return data.groupby(['SEG_OWNER'])['SEG_OWNER'].count().plot(kind="bar", x="SEG_OWNER")        

def operationGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    #explode =  [0.1, 0.1, 0.1, 0.1]   # explode 1st slice
    return data.groupby(['OPERATION'])['OPERATION'].count().plot(kind="pie", x="OPERATION",autopct='%1.1f%%',shadow=False)


def dateGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['DATE_'])['DATE_'].count().plot(kind="barh", x="DATE")
    

def timeGraphic():
    data = pd.DataFrame.from_dict(db.exec_dml('''select * from logminerFiltered where username <> 'UNKNOWN' and
    username <> 'SYS' and table_space <> 'None' and table_space <> 'UNKNOW' and table_name <> 'None' '''))
    return data.groupby(['TIME_'])['TIME_'].count().plot(kind="barh", x="TIME_")

def isFlag():
    return True






