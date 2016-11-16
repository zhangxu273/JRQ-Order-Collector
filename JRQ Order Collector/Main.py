#coding=utf-8
__author__ = '盖比旭'
import time
import pymysql
import Mushi
import MailManager
import DbManager
import Logger
import sys
import configparser

config = configparser.ConfigParser()
config.readfp(open('config.ini',encoding='utf-8'))
#全局数据库连接
sqlhost = config.get("Mysql","host")
sqlport = int(config.get("Mysql","port"))
sqluser = config.get("Mysql","user")
sqlpwd = config.get("Mysql","passwd")
sqldb = config.get("Mysql","db")


conn = pymysql.connect(host=sqlhost,user=sqluser,passwd=sqlpwd,db=sqldb,port=sqlport,charset='utf8')
Logger.Info("Opened database successfully");
cur=conn.cursor()#
cur.execute(DbManager.GetCreateSQL())
cur.close()
Logger.Info ("Table created successfully");

		
uid = sys.argv[1]
if __name__ == '__main__':  
	Logger.Info(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
	Mushi.Start(uid,conn) 
	Logger.Info('任务结束\n')
	try:
		Logger.Info(time.strftime('%Y-%m-%d %X',time.localtime()) ) 
		Mushi.Start(uid,conn) 
		Logger.Info('任务结束\n') 		
	except:  
		info=sys.exc_info()  
		Logger.Error("{0}:{1}".format(info[0],info[1])) 
			
	conn.close();
