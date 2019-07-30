

import pymysql
from testcase_py.common import conf

"""1,创建连接"""
conn = pymysql.connect(**conf.sql_conn_dict)
"""2,获取游标"""
cur=conn.cursor()
"""3,执行查询，数据库操作"""
sql="select* from myapp_students"
#执行sql语句
cur.execute(sql)
#打印出默认影响的行数
print(cur.execute(sql))
#取一行
print(cur.fetchone())
print('**************************')
#把游标返回第一位，绝对路径
cur.scroll(0,mode='absolute')
print(cur.fetchone())
print(cur.fetchone())
#相对路径，取上一个
cur.scroll(-1,mode='relative')
print(cur.fetchone())
cur.scroll(1,mode='relative')
print("**********************")
cur.fetchmany(3)
print(cur.fetchmany(3))
#当前指针位置，剩下所有的数据
print(cur.fetchall())
#执行影响的行数
print(cur.rowcount)

"""5,带参数的查询语句的写法"""
#写法一
sql="select* from myapp_students where sage=20"
cur.execute(sql)

print(cur.fetchall())

#写法二
sage =20

sql="select* from myapp_students where sage=%s" %sage
cur.execute(sql)
print(cur.fetchall())

#写法三(建议第三种方法比较好)
sage=20

sql="select* from myapp_students where sage=%s"
cur.execute(sql,sage)

print(cur.fetchall())
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#多参数的写法
cur.scroll(0,mode='absolute')
sage=(20,25,30)
sql="select* from myapp_students where sage=%s"
cur.executemany(sql,sage)
#只返回最后的参数
print(cur.fetchall())
#多参数，多个值，注意元祖有一个元素，有一个逗号

sage=((20,1),)
sql="select* from myapp_students where sage=%s and sgender=%s"
cur.executemany(sql,sage)
print(cur.fetchall())
#元祖
sage=((20,1),(25,1))
sql="select* from myapp_students where sage=%s and sgender=%s"
cur.executemany(sql,sage)
print(cur.fetchall())

#列表
sage=[(20,1),(25,1)]
sql="select* from myapp_students where sage=%s and sgender=%s"
cur.executemany(sql,sage)
print(cur.fetchall())
"""6,增删改"""
sql1= "update myapp_students set sname ='小米精神' where sage ='32'"
sql2="update myapp_students set sname ='小米精神十九大一等奖爱神的箭爱神的箭弟弟叫撒阿贾克斯的' where sage ='33'"
try:
    cur.execute(sql1)
    cur.execute(sql2)
    conn.commit()  #一系列数据完成后，再回滚
    print(",","True")
except Exception as e:

    #回滚，事务必须一起完成否则回滚
    conn.rollback()
    print(e,"False")





"""4.关闭游标，关闭数据库"""
cur.close()
conn.close()

