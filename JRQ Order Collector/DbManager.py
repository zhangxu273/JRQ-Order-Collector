# coding=utf-8
#字段名索引
columeName = [
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
	'sym_brief'
	]

#sql创建语句
def GetCreateDB():
	sql = 'CREATE DATABASE ORDER_DATA'
	return sql
#sql创建语句
def GetCreateSQL():
	sql = '''CREATE TABLE IF NOT EXISTS ORDER_DATA ({0} VARCHAR(200) PRIMARY KEY NOT NULL,
		{1} TEXT,{2} TEXT,{3} TEXT,{4} TEXT,{5} TEXT,{6} TEXT,{7} TEXT,{8} TEXT,{9} TEXT,{10} TEXT,
		{11} TEXT,{12} TEXT,{13} TEXT,{14} TEXT,{15} TEXT,{16} TEXT,{17} TEXT,{18} TEXT,{19} TEXT,{20} TEXT,
		{21} TEXT,{22} TEXT,{23} TEXT,{24} TEXT,{25} TEXT,{26} TEXT,{27} TEXT,{28} TEXT,{29} TEXT,{30} TEXT,
		{31} TEXT,{32} TEXT,{33} TEXT,{34} TEXT,{35} TEXT,{36} TEXT,{37} TEXT,{38} TEXT,{39} TEXT,{40} TEXT,
	    {41} TEXT,{42} TEXT,{43} TEXT,{44} TEXT,{45} TEXT,{46} TEXT,{47} TEXT,{48} TEXT,{49} TEXT,{50} TEXT,
		{51} TEXT,{52} TEXT,{53} TEXT,{54} TEXT);'''.format(columeName[0],
		columeName[1],columeName[2],columeName[3],columeName[4],columeName[5],columeName[6],columeName[7],columeName[8],columeName[9],columeName[10],
		columeName[11],columeName[12],columeName[13],columeName[14],columeName[15],columeName[16],columeName[17],columeName[18],columeName[19],columeName[20],
		columeName[21],columeName[22],columeName[23],columeName[24],columeName[25],columeName[26],columeName[27],columeName[28],columeName[29],columeName[30],
		columeName[31],columeName[32],columeName[33],columeName[34],columeName[35],columeName[36],columeName[37],columeName[38],columeName[39],columeName[40],
		columeName[41],columeName[42],columeName[43],columeName[44],columeName[45],columeName[46],columeName[47],columeName[48],columeName[49],columeName[50],
		columeName[51],columeName[52],columeName[53],columeName[54])
	return sql
		
		
#插入语句
def GetInsertSQL(jo):
	return '''REPLACE INTO ORDER_DATA(
		{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},
		{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},
		{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},
		{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},
		{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},
		{51},{52},{53},{54}
		)'''.format(columeName[0],
		columeName[1],columeName[2],columeName[3],columeName[4],columeName[5],columeName[6],columeName[7],columeName[8],columeName[9],columeName[10],
		columeName[11],columeName[12],columeName[13],columeName[14],columeName[15],columeName[16],columeName[17],columeName[18],columeName[19],columeName[20],
		columeName[21],columeName[22],columeName[23],columeName[24],columeName[25],columeName[26],columeName[27],columeName[28],columeName[29],columeName[30],
		columeName[31],columeName[32],columeName[33],columeName[34],columeName[35],columeName[36],columeName[37],columeName[38],columeName[39],columeName[40],
		columeName[41],columeName[42],columeName[43],columeName[44],columeName[45],columeName[46],columeName[47],columeName[48],columeName[49],columeName[50],
		columeName[51],columeName[52],columeName[53],columeName[54]) + BuildValues(jo);
		
#拼装values的函数
def BuildValues(jo):
	return '''VALUES(
			{0},{1},{2},{3},{4},{5},{6},{7},'{8}',{9},{10},
			{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},
			{21},{22},{23},{24},{25},{26},{27},{28},{29},'{30}',
			{31},{32},{33},{34},{35},{36},{37},{38},{39},{40},
			{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},
			'{51}','{52}','{53}','{54}'
			)
			;'''.format(
			jo[columeName[0]],
			jo[columeName[1]],jo[columeName[2]],jo[columeName[3]],jo[columeName[4]],jo[columeName[5]],jo[columeName[6]],jo[columeName[7]],jo[columeName[8]],jo[columeName[9]],jo[columeName[10]],
			jo[columeName[11]],jo[columeName[12]],jo[columeName[13]],jo[columeName[14]],jo[columeName[15]],jo[columeName[16]],jo[columeName[17]],jo[columeName[18]],jo[columeName[19]],jo[columeName[20]],
			jo[columeName[21]],jo[columeName[22]],jo[columeName[23]],jo[columeName[24]],jo[columeName[25]],jo[columeName[26]],jo[columeName[27]],jo[columeName[28]],jo[columeName[29]],jo[columeName[30]],
			jo[columeName[31]],jo[columeName[32]],jo[columeName[33]],jo[columeName[34]],jo[columeName[35]],jo[columeName[36]],jo[columeName[37]],jo[columeName[38]],jo[columeName[39]],jo[columeName[40]],
			jo[columeName[41]],jo[columeName[42]],jo[columeName[43]],jo[columeName[44]],jo[columeName[45]],jo[columeName[46]],jo[columeName[47]],jo[columeName[48]],jo[columeName[49]],jo[columeName[50]],
			jo[columeName[51]],jo[columeName[52]],jo[columeName[53]],jo[columeName[54]])
			
			
def GetSelectSQL(orderId):
	return 'SELECT tr_order,state FROM ORDER_DATA WHERE (tr_order = {0});'.format(orderId)

			