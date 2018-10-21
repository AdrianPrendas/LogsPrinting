
import cx_Oracle

CONN_INFO = {
    'host': '127.0.0.1',
    'port': 1521,
    'user': 'sys',
    'pass': 'manager',
    'service':'GO'
}

CONN_STR = '{user}/{pass}@{host}:{port}/{service}'.format(**CONN_INFO)

class DB:
    def __init__(self):
        self.conn = cx_Oracle.connect(CONN_STR, mode = cx_Oracle.SYSDBA)

    def exec_dml(self, query, params={}):
        cursor = self.conn.cursor()
        rows = cursor.execute(query, params).fetchall()
        cols = tuple([d[0] for d in cursor.description])
        result = []
        for row in rows:
            dic = dict(zip(cols, row))
            result.append(dic)
        cursor.close()
        return result

    def exec_ddl(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            print("everything ok")
        except cx_Oracle.Error as err:
            print(err)
            return -1
        return 0

    def callfunction(self, hof): #higher order function
        cursor = self.conn.cursor()
        try:
            return cursor.callfunc(hof,cx_Oracle.CURSOR)
        except cx_Oracle.Error as err:
            print(err)
            return -1
        return 0

    def callproc(self, hof): #higher order function
        cursor = self.conn.cursor()
        try:
            return cursor.callproc(hof,cx_Oracle.CURSOR)
        except cx_Oracle.Error as err:
            print(err)
            return -1
        return 0

