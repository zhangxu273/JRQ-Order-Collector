# JRQ-Order-Collector
金融圈 订单 采集系统

#Main.py 为主执行文件
	UserList 可配置 打算监听的牛人
#MailManager.py  为邮件服务器配置
	receivers 可以配置收信邮箱
	DEBUG_MODE 初次执行请设置成True (否则会短时间内收到很多信)
	

#后续计划
	此版本只实现了采集功能 
	之后加入订单解析
	后续计划:
		a.订单解析
		b.独立出配置文件,保密发信帐户密码
		c.Sqlite 改成 MySql
		d.订单跟踪功能
		e.做一个网页,可以单独跟踪统计一些订单
