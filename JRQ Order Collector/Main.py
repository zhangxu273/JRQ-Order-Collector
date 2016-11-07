#! /usr/bin/env python
#coding=utf-8
import time
import sqlite3
import Mushi
import MailManager
import DbManager


#打算监听的牛人id
UserList = ['4591548','5196432','5040593','5200551','3083419','3742979','4801721','5030369','5066299','5055710']
#UserList = ['5055710']
#全局邮件服务器
MailManager.Login();
#全局数据库连接
conn = sqlite3.connect('data.db')
conn.row_factory = sqlite3.Row
print ("Opened database successfully");
conn.execute(DbManager.GetCreateSQL())
print ("Table created successfully");
	

  
def task():  
	for uid in UserList:
		Mushi.Start(uid,conn)
  
def timer(n):  
    while True:  
        print(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
        task()  
        time.sleep(n)  
  
if __name__ == '__main__':  
    timer(300)  
