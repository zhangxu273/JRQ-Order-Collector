# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import Logger
import time
import configparser

config = configparser.ConfigParser()
config.readfp(open('config.ini',encoding='utf-8'))
mail_ssl = config.get("Mail","ssl")
mail_server = config.get("Mail","server")
mail_port = config.get("Mail","port")



#发送账号配置
sender = config.get("Mail","sender")
senderAccount = config.get("Mail","senderAccount")
senderPassword = config.get("Mail","senderPassword")
#接收方账号配置
receivers = config.get("Mail","receivers").replace('[',"").replace(']',"").split(',')
#receivers = ['im@program.dog']
#邮件服务器配置


 
#邮件模板
MailTitleTpl = '{0}:订单{1}的状态发生改变，目前状态{2}'
MailContentTpl_Handle_Close = '{0} {1} {2} (手动平仓)\n，开仓价:{3} 平仓价{4},收益{5}'
MailContentTpl_Cancle_Close = '{0} {1} {2}(撤单)\n 委托价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_TP_Close = '{0} {1} {2} (止盈平仓)\n 开仓价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_SL_Close = '{0} {1} {2} (止损平仓)\n 开仓价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_00 = '{0} {1} {2} \n 开仓价:{3} 止赢价{4} 止损价{5}'
#测试模式 只显示 不发送
DEBUG_MODE = False
#跳转用url
jumpingURL = 'https://copyfx.jrq.com/Overview/{0}'

	
#发信
def SemdMail(_uid, _name , _json):
	server = smtplib.SMTP() 
	server.connect('smtp.163.com',25)  
	server.login(senderAccount,senderPassword)
	print(receivers)
	for recv in receivers:
		try:
			message = MIMEText(CreateMailMessage(_uid,_name,_json), 'plain', 'utf-8')
			message['From'] = sender
			message['To'] =  recv
			message['Subject'] = CreateMailTitle(_json)
		if DEBUG_MODE == False:
			server.sendmail(sender,recv,message.as_string()) 
			Logger.Info("邮件发送成功") 
		except smtplib.SMTPException:
			Logger.Error("邮件发送失败")
			
	server.quit()
	return
	
def formatTime(_time):
	createValue = float(_time)
	return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(createValue))
	
def CreateMailTitle(_json):
	otime = formatTime(_json['open_time'])
	ctime = formatTime(_json['close_time'])
	ret = ''
	if(int(_json['state']) == 3):
		ret = MailTitleTpl.format(ctime,_json['tr_order'],_json['state'])
	else:
		ret = MailTitleTpl.format(otime,_json['tr_order'],_json['state'])
		
	return ret
		
def CreateMailMessage(_uid , _name,_json):
	state = _json['state']
	comment = _json['comment']
	Logger.Info('state={0} comment = {1}'.format(state,comment))
	msg = '';
	
	if(int(state) == 3):
		if(comment == ''):
			msg = MailContentTpl_Handle_Close.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['close_price'],_json['profit'])
		elif(comment == 'cancelled'):
			msg = MailContentTpl_Cancle_Close.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['tp'],_json['sl'])
		elif(comment == '[tp]'):
			msg = MailContentTpl_TP_Close.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['tp'],_json['sl'])
		elif(comment == '[sl]'):
			msg = MailContentTpl_SL_Close.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['tp'],_json['sl'])
		else:
			msg = MailContentTpl_Handle_Close.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['close_price'],_json['profit'])
	elif(int(state) == 0):
		msg = MailContentTpl_00.format(_name,_json['order_status2'],_json['symbol'],_json['open_price'],_json['tp'],_json['sl'])
	else:
		msg = json.dumps(_json)

	jurl = jumpingURL.format(_uid)
	Logger.Info('msg={0}\n{1}'.format(msg,jurl))
	return '{0}\n{1}'.format(msg,jurl)

