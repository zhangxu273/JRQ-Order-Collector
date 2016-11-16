# coding=utf-8
import urllib.request
import sys
import re
import json
import DbManager
import MailManager
import Logger

def GetHtml(_uid):
	Logger.Info('开始采集' + _uid)
	_url = "https://copyfx.jrq.com/Widget/__user_published?uid="+_uid+"&type=user_published_trade&page=1"
	#爬网页
	headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	_data = opener.open(_url).read()
	_data = _data.decode('UTF-8')
	return _data
	
def ParseJson(_url,_name,_found,_conn):
	if(_found != None):
		#Logger.Info(found.group()+'\n')
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
			MailManager.SemdMail(_url,_name, jo)
		#入库
		cursor.execute(DbManager.GetInsertSQL(jo));
		cursor.close()
	return
	
def Start(_uid,_conn):
	data = GetHtml(_uid)
	#Logger.Info (data);
	resultArray = data.split("data-");
	#Logger.Info(resultArray[0])
	name_found = re.search('\s+uid.+">.+</a>\n', resultArray[0])
	userName = name_found.group().split('>')[1].replace('</a','')
	#分析数据
	Logger.Info ("Start ParseData {0}".format(userName));
	for res in resultArray:
		order_found = re.search('(?<=order=\')(.+)}', res);
		ParseJson(_uid,userName,order_found,_conn)
	_conn.commit()
	Logger.Info ("End ParseData");
	#关闭连接
	#MailManager.Logout()
	return
	

	
# data-order='{"tr_order":"13520584","wbid":"2016110415357","copied_order":"0","copied_order_type":"1","copied_count":"0","is_auto":"2","is_from_copier":"2","single_margin":"410","u_type":"1","symbol":"USDCAD","digits":"5","cmd":"1","volume":"41","open_time":"1478261953","state":"3","open_price":"1.342480","sl":"0.000000","tp":"0.000000","close_time":"1478262616","value_date":"0","expiration":"0","conv_reserv":"0","conv_rates0":"0.0","conv_rates1":"0.0","commission":"0.000000","commission_agent":"0.0","storage":"0.000000","close_price":"1.339440","profit":"93.050000","taxes":"0.000000","magic":"0","comment":"","internal_id":"0","activation":"0","spread":"0","margin_rate":"0.000000","timestamp":"1478261954","reserved0":"0","reserved1":"0","reserved2":"0","reserved3":"0","close_reason":"3","log_time":"1478262644","is_reverse":"0","rebate":"0.000000","turnover_open":"41



