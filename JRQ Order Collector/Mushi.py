import urllib.request
import sys
import re
import json
import DbManager
import MailManager

def GetHtml(_uid):
	print('开始采集' + _uid)
	_url = "https://copyfx.jrq.com/Widget/__user_published?uid="+_uid+"&type=user_published_trade&page=1"
	#爬网页
	_data = urllib.request.urlopen(_url).read()
	_data = _data.decode('UTF-8')
	return _data
	
def ParseJson(_uid,_found,_conn):
	if(_found != None):
		#print(found.group()+'\n')
		isNew = False
		jo = json.loads(_found.group());
		cursor = _conn.cursor()
		cursor.execute(DbManager.GetSelectSQL(jo['tr_order']))
		rows = cursor.fetchall()
		#库里没有说明是新的
		if(len(rows) == 0): 
			isNew = True;
		#库里有 但状态和之前不一样 说明是新的
		elif(len(rows) == 1 and int(rows[0][1]) != int(jo['state'])):
			isNew = True;
		#发邮件
		if (isNew == True):
			MailManager.SemdMail(_uid, jo)
		#入库
		_conn.execute(DbManager.GetInsertSQL(jo));
		
	return
	
def Start(_uid,_conn):
	
	
	data = GetHtml(_uid)

	resultArray = data.split("data-");
	
	#分析数据
	print ("Start ParseData");
	for res in resultArray:
		found = re.search('(?<=order=\')(.+)}', res);
		ParseJson(_uid,found,_conn)
	_conn.commit()
	#关闭连接
	#MailManager.Logout()
	return
	
print()

	
# data-order='{"tr_order":"13520584","wbid":"2016110415357","copied_order":"0","copied_order_type":"1","copied_count":"0","is_auto":"2","is_from_copier":"2","single_margin":"410","u_type":"1","symbol":"USDCAD","digits":"5","cmd":"1","volume":"41","open_time":"1478261953","state":"3","open_price":"1.342480","sl":"0.000000","tp":"0.000000","close_time":"1478262616","value_date":"0","expiration":"0","conv_reserv":"0","conv_rates0":"0.0","conv_rates1":"0.0","commission":"0.000000","commission_agent":"0.0","storage":"0.000000","close_price":"1.339440","profit":"93.050000","taxes":"0.000000","magic":"0","comment":"","internal_id":"0","activation":"0","spread":"0","margin_rate":"0.000000","timestamp":"1478261954","reserved0":"0","reserved1":"0","reserved2":"0","reserved3":"0","close_reason":"3","log_time":"1478262644","is_reverse":"0","rebate":"0.000000","turnover_open":"41



