#coding=utf-8
__author__ = '盖比旭'
import time
import pymysql
import Mushi
import MailManager
import DbManager
import Logger
import sys

#全局数据库连接

conn = pymysql.connect(host='localhost',user='root',passwd='djdgrsjh273',db='ORDER_DATA',port=3306,charset='utf8')
Logger.Info("Opened database successfully");
cur=conn.cursor()#
cur.execute(DbManager.GetCreateSQL())
cur.close()
Logger.Info ("Table created successfully");

		
uid = sys.argv[1]
if __name__ == '__main__':  
	#Logger.Info(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
	#Mushi.Start(uid,conn) 
	#Logger.Info('任务结束\n')
	try:
		Logger.Info(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
		Mushi.Start(uid,conn) 
		Logger.Info('任务结束\n') 		
	except:  
		info=sys.exc_info()  
		Logger.Error("{0}:{1}".format(info[0],info[1])) 
			
	conn.close();
