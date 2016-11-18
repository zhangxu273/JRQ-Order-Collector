# coding=utf-8
#字段名索引
orderColumeName = [
	'tr_order',
	'copied_order',
	'copied_order_type',
	'copied_count',       
	'is_auto',            
	'is_from_copier',     
	'single_margin',    
	'u_type',             
	'symbol',             
	'digits',             
	'cmd',                
	'volume',             
	'open_time',          
	'state',              
	'open_price',         
	'sl',                 
	'tp',                 
	'close_time',         
	'value_date',         
	'expiration',         
	'conv_reserv',        
	'conv_rates0',        
	'conv_rates1',        
	'commission',         
	'commission_agent',   
	'storage',            
	'close_price',        
	'profit',             
	'taxes',              
	'magic',              
	'comment',            
	'internal_id',        
	'activation',         
	'spread',             
	'margin_rate',        
	'timestamp',          
	'reserved0',          
	'reserved1',          
	'reserved2',          
	'reserved3',          
	'close_reason',       
	'log_time',           
	'is_reverse',         
	'rebate',             
	'turnover_open',      
	'turnover_close',     
	'order_flag',         
	'bonus_equity_rate',  
	'basic_ask',          
	'basic_bid',          
	'basic_currency',     
	'order_status',       
	'order_status2',      
	'sym_name',           
	'sym_brief',
	'trader_id'
	]
	
traderColumeName = [
	'uid',
	'trader_name'
]

#sql创建语句
def GetCreateDB():
	sql = 'CREATE DATABASE ORDER_DATA'
	return sql
	
#sql创建语句
def GetCreateOrderSQL():
	sql = '''CREATE TABLE IF NOT EXISTS ORDER_DATA ({0} VARCHAR(200) PRIMARY KEY NOT NULL,
		{1} TEXT,{2} TEXT,{3} TEXT,{4} TEXT,{5} TEXT,{6} TEXT,{7} TEXT,{8} TEXT,{9} TEXT,{10} TEXT,
		{11} TEXT,{12} TEXT,{13} TEXT,{14} TEXT,{15} TEXT,{16} TEXT,{17} TEXT,{18} TEXT,{19} TEXT,{20} TEXT,
		{21} TEXT,{22} TEXT,{23} TEXT,{24} TEXT,{25} TEXT,{26} TEXT,{27} TEXT,{28} TEXT,{29} TEXT,{30} TEXT,
		{31} TEXT,{32} TEXT,{33} TEXT,{34} TEXT,{35} TEXT,{36} TEXT,{37} TEXT,{38} TEXT,{39} TEXT,{40} TEXT,
	    {41} TEXT,{42} TEXT,{43} TEXT,{44} TEXT,{45} TEXT,{46} TEXT,{47} TEXT,{48} TEXT,{49} TEXT,{50} TEXT,
		{51} TEXT,{52} TEXT,{53} TEXT,{54} TEXT,{55} TEXT);'''.format(orderColumeName[0],
		orderColumeName[1],orderColumeName[2],orderColumeName[3],orderColumeName[4],orderColumeName[5],orderColumeName[6],orderColumeName[7],orderColumeName[8],orderColumeName[9],orderColumeName[10],
		orderColumeName[11],orderColumeName[12],orderColumeName[13],orderColumeName[14],orderColumeName[15],orderColumeName[16],orderColumeName[17],orderColumeName[18],orderColumeName[19],orderColumeName[20],
		orderColumeName[21],orderColumeName[22],orderColumeName[23],orderColumeName[24],orderColumeName[25],orderColumeName[26],orderColumeName[27],orderColumeName[28],orderColumeName[29],orderColumeName[30],
		orderColumeName[31],orderColumeName[32],orderColumeName[33],orderColumeName[34],orderColumeName[35],orderColumeName[36],orderColumeName[37],orderColumeName[38],orderColumeName[39],orderColumeName[40],
		orderColumeName[41],orderColumeName[42],orderColumeName[43],orderColumeName[44],orderColumeName[45],orderColumeName[46],orderColumeName[47],orderColumeName[48],orderColumeName[49],orderColumeName[50],
		orderColumeName[51],orderColumeName[52],orderColumeName[53],orderColumeName[54],orderColumeName[55])
	
	return sql
def GetCreateTraderSQL():
	sql = '''CREATE TABLE IF NOT EXISTS TRADER_DATA ({0} VARCHAR(200) PRIMARY KEY NOT NULL,{1} TEXT);'''.format(traderColumeName[0],traderColumeName[1])
	return sql
		
		
#插入语句
def GetInsertOrderSQL(_uid,jo):
	sql = '''REPLACE INTO ORDER_DATA(
		{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},
		{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},
		{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},
		{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},
		{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},
		{51},{52},{53},{54},{55}
		)'''.format(orderColumeName[0],
		orderColumeName[1],orderColumeName[2],orderColumeName[3],orderColumeName[4],orderColumeName[5],orderColumeName[6],orderColumeName[7],orderColumeName[8],orderColumeName[9],orderColumeName[10],
		orderColumeName[11],orderColumeName[12],orderColumeName[13],orderColumeName[14],orderColumeName[15],orderColumeName[16],orderColumeName[17],orderColumeName[18],orderColumeName[19],orderColumeName[20],
		orderColumeName[21],orderColumeName[22],orderColumeName[23],orderColumeName[24],orderColumeName[25],orderColumeName[26],orderColumeName[27],orderColumeName[28],orderColumeName[29],orderColumeName[30],
		orderColumeName[31],orderColumeName[32],orderColumeName[33],orderColumeName[34],orderColumeName[35],orderColumeName[36],orderColumeName[37],orderColumeName[38],orderColumeName[39],orderColumeName[40],
		orderColumeName[41],orderColumeName[42],orderColumeName[43],orderColumeName[44],orderColumeName[45],orderColumeName[46],orderColumeName[47],orderColumeName[48],orderColumeName[49],orderColumeName[50],
		orderColumeName[51],orderColumeName[52],orderColumeName[53],orderColumeName[54],orderColumeName[55]) + BuildOrderValues(_uid,jo);
	return sql;
		
#拼装values的函数
def BuildOrderValues(_uid,jo):
	return '''VALUES(
			{0},{1},{2},{3},{4},{5},{6},{7},'{8}',{9},{10},
			{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},
			{21},{22},{23},{24},{25},{26},{27},{28},{29},'{30}',
			{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},
			{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},
			'{51}','{52}','{53}','{54}',{55}
			)
			;'''.format(
			jo[orderColumeName[0]],
			jo[orderColumeName[1]],jo[orderColumeName[2]],jo[orderColumeName[3]],jo[orderColumeName[4]],jo[orderColumeName[5]],jo[orderColumeName[6]],jo[orderColumeName[7]],jo[orderColumeName[8]],jo[orderColumeName[9]],jo[orderColumeName[10]],
			jo[orderColumeName[11]],jo[orderColumeName[12]],jo[orderColumeName[13]],jo[orderColumeName[14]],jo[orderColumeName[15]],jo[orderColumeName[16]],jo[orderColumeName[17]],jo[orderColumeName[18]],jo[orderColumeName[19]],jo[orderColumeName[20]],
			jo[orderColumeName[21]],jo[orderColumeName[22]],jo[orderColumeName[23]],jo[orderColumeName[24]],jo[orderColumeName[25]],jo[orderColumeName[26]],jo[orderColumeName[27]],jo[orderColumeName[28]],jo[orderColumeName[29]],jo[orderColumeName[30]],
			jo[orderColumeName[31]],jo[orderColumeName[32]],jo[orderColumeName[33]],jo[orderColumeName[34]],jo[orderColumeName[35]],jo[orderColumeName[36]],jo[orderColumeName[37]],jo[orderColumeName[38]],jo[orderColumeName[39]],jo[orderColumeName[40]],
			jo[orderColumeName[41]],jo[orderColumeName[42]],jo[orderColumeName[43]],jo[orderColumeName[44]],jo[orderColumeName[45]],jo[orderColumeName[46]],jo[orderColumeName[47]],jo[orderColumeName[48]],jo[orderColumeName[49]],jo[orderColumeName[50]],
			jo[orderColumeName[51]],jo[orderColumeName[52]],jo[orderColumeName[53]],jo[orderColumeName[54]],_uid)
			
			
def GetInsertTraderSQL(_uid,_name):
	sql = "REPLACE INTO TRADER_DATA({0},{1})".format(traderColumeName[0],traderColumeName[1]) + BuildTraderValues(_uid,_name);
	return sql
	
def BuildTraderValues(_uid,_name):
	return "VALUES({0},'{1}');".format(_uid,_name)

def GetSelectOrderSQL(orderId):
	return 'SELECT tr_order,state FROM ORDER_DATA WHERE (tr_order = {0});'.format(orderId)

			