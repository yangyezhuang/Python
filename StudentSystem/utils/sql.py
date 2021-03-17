import pymysql


class SQLHelper(object):

    @staticmethod
    def open():
        conn = pymysql.connect(host='localhost', user='root', passwd='mysql', port=3306, db='students', charset='utf8')
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cur

    @staticmethod
    def close(conn, cur):
        cur.close()
        conn.close()

    @staticmethod
    def fetch_one(sql, args):
        conn, cur = SQLHelper.open()
        cur.execute(sql, args)
        obj = cur.fetchone()
        SQLHelper.close(conn, cur)
        return obj

    @staticmethod
    def fetch_all(sql, args):
        conn, cur = SQLHelper.open()
        cur.execute(sql, args)
        obj = cur.fetchall()
        SQLHelper.close(conn, cur)
        return obj
