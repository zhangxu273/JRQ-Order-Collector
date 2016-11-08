import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json

#发送账号配置
sender = 'password273@163.com'
senderAccount = 'password273'
senderPassword = 'password'
#接收方账号配置
receivers = ['im@program.dog','chenheng_bj@163.com']
#receivers = ['im@program.dog']
#邮件服务器配置


 
#邮件模板
MailTitleTpl = '订单{0}的状态发生改变，目前状态{1}'
MailContentTpl_Handle_Close = '{0} {1} {2} (手动平仓)\n，开仓价:{3} 平仓价{4},收益{5}'
MailContentTpl_Cancle_Close = '{0} {1} {2}(撤单)\n 委托价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_TP_Close = '{0} {1} {2} (止盈平仓)\n 开仓价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_SL_Close = '{0} {1} {2} (止损平仓)\n 开仓价:{3} 止赢价:{4} 止损价:{5}' 
MailContentTpl_00 = '{0} {1} {2} \n 开仓价:{2} 止赢价{3} 止损价{4}'
#测试模式 只显示 不发送
DEBUG_MODE = False
	
#发信
def SemdMail(_name , _json):
	server = smtplib.SMTP() 
	server.connect('smtp.163.com',25)  
	server.login(senderAccount,senderPassword)
	
	for recv in receivers:
		try:
			message = MIMEText(CreateMailMessage(_name,_json), 'plain', 'utf-8')
			message['From'] = sender
			message['To'] =  recv
			message['Subject'] = MailTitleTpl.format(_json['tr_order'],_json['state'])
			if DEBUG_MODE == False:
				server.sendmail(sender,recv,message.as_string()) 
			print("邮件发送成功") 
		except smtplib.SMTPException:
			print("Error:邮件发送失败")
			
	server.quit()
	return

def CreateMailMessage(_name,_json):
	state = _json['state']
	comment = _json['comment']
	print('state={0} comment = {1}'.format(state,comment))
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

	print('msg={0}'.format(msg))
	return msg

