'''
    二维列表写入mysql
'''
import pymysql

class HtmlOutputer(object):
    def output(self, data):
        connect = pymysql.connect(host='localhost',
                                  user='root',
                                  passwd='199571',
                                  db='zhipin',
                                  charset='utf8')
        # 创建游标
        cursor = connect.cursor()
        # 全表删除
        # cursor.execute('TRUNCATE TABLE info')
        for value in data:
            print(value)
            # info 是数据库里表的名字
            cursor.execute("""INSERT INTO info VALUE(%s, %s, %s, %s, %s)""", (value[0], value[1], value[2], value[3], value[4]))
            # cmd = "INSERT INTO activation_code VALUE(id = 0, %(activation_code)s)"
            # cursor.execute(cmd, {'activation_code': key})
            connect.commit()
        # 从数据库输出
        # cursor.execute('SELECT * from info')
        # lists = cursor.fetchall()
        # for list in lists:
        #     print(list)

        connect.close()