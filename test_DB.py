import pytest
import requests
from bs4 import BeautifulSoup
import pymysql


class Test_DB:
    sql_case_one = '''select stu.dept_id,stu.stu_id,stu.stu_name,A.sum_score from
    stu inner join (select stu_id ,sum(score) as sum_score from sc group by stu_id)A 
    on A.stu_id=stu.stu_id inner join dept on dept.dept_id=stu.dept_id group by stu.dept_id,stu_id;
    '''

    sql_case_two = '''
    select * from sc where sc.stu_id in 
    (select sc.stu_id,min(score) as min_sc from sc group by sc.stu_id having min(score)>60 );
    
    '''

    sql_case_three = '''
    select Websites.name ,Websites.url,TEMP.sum_count from
    Websites inner join
    (select site_id ,sum(count) as sum_count from access_log  group by site_id having sum(count)>200) TEMP
    on Websites.id=TEMP.site_id ;
    
    '''

    def test_DB_query(self, localhost='', testdb='', sql=sql_case_one):
        # sql = self.sql_case_one

        # 打开数据库连接
        db = pymysql.connect(localhost, "testuser", "test123", testdb, charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句

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


if __name__ == '__main__':
    pytest.main(['-s', "test_DB.py"])
