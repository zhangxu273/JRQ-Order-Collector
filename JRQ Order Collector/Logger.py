# coding=utf-8
import logging
import datetime
import os


filename = datetime.datetime.now().strftime("%Y-%m-%d")
path = './{0}.log'.format(filename)
logger = logging.getLogger("loggingmodule.NomalLogger")
formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")    
handler = logging.FileHandler(path)  
handler.setFormatter(formatter)  
logger.addHandler(handler)  
logger.setLevel(logging.DEBUG)
   
#test  
def Debug(str):
	print(str)
	logger.debug(str)
	
def Info(str):
	print(str)
	logger.info(str) 

def Error(str):
	print(str)
	logger.error(str)
