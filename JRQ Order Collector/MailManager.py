import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json


#发送账号配置
sender = 'password273@163.com'
senderAccount = 'password273'
senderPassword = 'password'
#接收方账号配置
#receivers = ['im@proram.dog','chenheng_bj@163.com']
receivers = ['im@program.dog']
#邮件服务器配置
server = smtplib.SMTP() 
server.connect('smtp.163.com',25)  
 
#邮件模板
MailTitleTpl = '订单{0}的状态发生改变，目前状态{1}'
MailContentTpl3 = '{0}以{1}的价位，手动平仓{2}的{3}单，盈利{4}'

#测试模式 只显示 不发送
DEBUG_MODE = True


#登陆
def Login():
	server.login(senderAccount,senderPassword)
	return

#登出
def Logout():
	server.quit()
	return
	
#发信
def SemdMail(_name , _json):
	for recv in receivers:
		try:
			message = MIMEText(CreateMailMessage(_name,_json), 'plain', 'utf-8')
			message['From'] = sender
			message['To'] =  recv
			message['Subject'] = "新的订单"
			if DEBUG_MODE == False:
				server.sendmail(sender,recv,message.as_string()) 
			print("邮件发送成功") 
		except smtplib.SMTPException:
			print("Error:邮件发送失败")
	return

def CreateMailMessage(_name,_json):
	state = _json['state']
	print('state={0}'.format(state))
	msg = '';
	if(int(state) == 3):
		msg = MailContentTpl3.format(_name,_json['close_price'],_json['symbol'],_json['order_status2'],_json['profit'])
	
	print('msg={0}'.format(msg))
	return msg

