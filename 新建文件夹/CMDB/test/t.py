# import paramiko
# import requests
#
#
# ssh=paramiko.SSHClient()
#
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
# ssh.connect(hostname='192.168.14.13',port=22, username='root',password='123456')
#
# stdin,stdout,stderr =ssh.exec_command('df')
# result=stdout.read()
# ssh.close()
# print(result)



import pymysql


conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='密码',db='库名')

# 建立连接

cursor =conn.cursor()
# 邮标
row_affected=cursor.execute("select * from t1")
# # 通过邮标创建操作接口

one=cursor.fetchall()

'''
迭代器
fetchone () 1条
fetchmany() 多条
fetchall ()

# cursor.scroll(1,mode='relative)   1向下  -1向上


cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)   变成字典 结果




'''
conn.commit()
print(one)
cursor.close()
conn.close()



