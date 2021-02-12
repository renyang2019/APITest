import pytest
import requests
from bs4 import BeautifulSoup
import pymysql


class Test_DB:
    def test_DB_query(self):

        # 打开数据库连接
        db = pymysql.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM EMPLOYEE \
               WHERE INCOME > %s" % (1000)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print
                "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                (fname, lname, age, sex, income)
        except:
            print
            "Error: unable to fecth data"

        # 关闭数据库连接
        db.close()
