import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from constellation import Ui_Form
import requests


class MainWindow(QMainWindow ):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.ui.queryBtn.clicked.connect(self.queryConstell)
	def queryConstell(self):#查询星座的函数
		#key = 'key=b5d96224be3690689ef4fc5f15eb4e81'
		key='key=0262875d4c8c047fa659cb7ca42567cb'
		url = 'http://web.juhe.cn:8080/constellation/getAll?'
		constell = self.ui.StarcomboBox.currentText()
		consName = self.transConstell(constell)
		Time = self.ui.TimecomboBox.currentText()
		type = self.gettype(Time)#得到所需参数
		rep = requests.get(url + consName + type + key)
		rep.encoding = 'utf-8'
		rep.json()
		print('返回结果: %s' % rep.json())

		result=''
		if type=='type=today&'or type=='type=tomorrow&':#判断要查询的时间
			name1 = '星座 ： %s' % rep.json()['name'] + '\n\n'
			date1 = '日期 :  %s' % rep.json()['datetime'] + '\n\n'
			all1 = '综合指数 : %s' % rep.json()['all'] + '\n\n'
			color1= '幸运色 : %s' % rep.json()['color'] + '\n\n'
			health1='健康指数 : %s' %rep.json()['health'] + '\n\n'
			love1 ='爱情指数 : %s' %rep.json()['love'] +'\n\n'
			QFriend1='速配星座 : %s' %rep.json()['QFriend'] + '\n\n'
			work1='工作指数 : %s' %rep.json()['work'] + '\n\n'
			summary1='今日概述: %s' %rep.json()['summary'] + '\n\n'
			result = name1 + date1 + all1 + color1 + health1 + QFriend1 + love1 + work1 + summary1
		elif type == 'type=week&':
			name2 = '星座 ： %s' % rep.json()['name'] + '\n\n'
			date2 = '日期 :  %s' % rep.json()['date'] + '\n\n'
			health2 = '健康指数 : %s' % rep.json()['health'] + '\n\n'
			love2 = '恋情 : %s' % rep.json()['love'] + '\n\n'
			work2 = '工作: %s' % rep.json()['work'] + '\n\n'
			money2 ='财运 :%s' % rep.json()['money'] + '\n\n'
			result = name2 + date2 +health2 + love2 + work2 +money2
		elif type == 'type=month&':
			name3 = '星座 ： %s' % rep.json()['name'] + '\n\n'
			date3 = '日期 :  %s' % rep.json()['date'] + '\n\n'
			happyMagic ='快乐魔法 : %s' % rep.json()['happyMagic'] +'\n\n'
			health3 = '健康指数 : %s' % rep.json()['health'] + '\n\n'
			love3 = '恋情 : %s' % rep.json()['love'] + '\n\n'
			work3 = '工作: %s' % rep.json()['work'] + '\n\n'
			money3 ='财运 : %s' % rep.json()['money'] + '\n\n'
			all3 ='总结 : %s' % rep.json()['all'] + '\n\n'
			result = name3 + date3 + happyMagic+health3 + love3 + work3 +money3 +all3
		elif type == 'type=year&':
			name4 = '星座 ： %s' % rep.json()['name'] + '\n\n'
			date4 = '日期 :  %s' % rep.json()['date'] + '\n\n'
			mima = '年度密码 : %s' % rep.json()['mima']['text'] + '\n\n'
			love4 = '恋情 : %s' % rep.json()['love'] + '\n\n'
			career4 = '事业运: %s' % rep.json()['career'] + '\n\n'
			money4 ='财运 :%s' % rep.json()['finance'] + '\n\n'
			result = name4 + date4 +mima + love4 + career4 +money4
		else:
			result='wrong!'#错误信息提示
		self.ui.resulttext.setText(result)


	def transConstell(self,constell):#更改星座函数
		consName=''
		if constell=='白羊座':
			consName='consName=%E7%99%BD%E7%BE%8A%E5%BA%A7&'
		elif constell=='金牛座':
			consName='consName=%E9%87%91%E7%89%9B%E5%BA%A7&'
		elif constell == '双子座':
			consName = 'consName=%E5%8F%8C%E5%AD%90%E5%BA%A7&'
		elif constell=='巨蟹座':
			consName='consName=%E5%B7%A8%E8%9F%B9%E5%BA%A7&'
		elif constell=='狮子座':
			consName='consName=%E7%8B%AE%E5%AD%90%E5%BA%A7&'
		elif constell=='处女座':
			consName='consName=%E5%A4%84%E5%A5%B3%E5%BA%A7&'
		elif constell=='天秤座':
			consName='consName=%E5%A4%A9%E7%A7%A4%E5%BA%A7&'
		elif constell=='天蝎座':
			consName='consName=%E5%A4%A9%E8%9D%8E%E5%BA%A7&'
		elif constell=='射手座':
			consName='consName=%E5%B0%84%E6%89%8B%E5%BA%A7&'
		elif constell=='摩羯座':
			consName='consName=%E6%91%A9%E7%BE%AF%E5%BA%A7&'
		elif constell=='水瓶座':
			consName='consName=%E6%B0%B4%E7%93%B6%E5%BA%A7&'
		elif constell=='双鱼座':
			consName='consName=%E5%8F%8C%E9%B1%BC%E5%BA%A7&'

		return consName
	def gettype(self,Time):#得到完整type参数
		type='type='+Time+'&'
		return type

		self.ui.clearBtn.clicked.connect(self.clearResult)
	def clearResult(self):#清空文本内容
		print('* clearResult  ')
		self.ui.resulttext.clear()

if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())