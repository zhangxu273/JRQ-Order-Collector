#coding=utf-8
import time
import sqlite3
import Mushi
import MailManager
import DbManager
import Logger
import sys

#全局数据库连接
conn = sqlite3.connect('data.db')
conn.row_factory = sqlite3.Row
Logger.Info("Opened database successfully");
conn.execute(DbManager.GetCreateSQL())
Logger.Info ("Table created successfully");
	
uid = sys.argv[1]

  
if __name__ == '__main__':  
	try:
		Logger.Info(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
		Mushi.Start(uid,conn) 
		Logger.Info('任务结束\n') 		
	except:  
		info=sys.exc_info()  
		Logger.Error("{0}:{1}".format(info[0],info[1]))  
			
	conn.close();
