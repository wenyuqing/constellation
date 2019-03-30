# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'constellation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1353, 819)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("#Form{border-image: url(:/huajing.JPG);}\n"
"\n"
"\n"
"")
        self.StarcomboBox = QtWidgets.QComboBox(Form)
        self.StarcomboBox.setGeometry(QtCore.QRect(600, 130, 311, 31))
        self.StarcomboBox.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 14pt \"Agency FB\";")
        self.StarcomboBox.setObjectName("StarcomboBox")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.StarcomboBox.addItem("")
        self.TimecomboBox = QtWidgets.QComboBox(Form)
        self.TimecomboBox.setGeometry(QtCore.QRect(600, 190, 311, 31))
        self.TimecomboBox.setStyleSheet("font: 14pt \"Agency FB\";\n"
"color: rgb(85, 0, 255);")
        self.TimecomboBox.setObjectName("TimecomboBox")
        self.TimecomboBox.addItem("")
        self.TimecomboBox.addItem("")
        self.TimecomboBox.addItem("")
        self.TimecomboBox.addItem("")
        self.TimecomboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(400, 190, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet("font: 75 12pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 130, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(320, 760, 112, 34))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(780, 760, 112, 34))
        self.clearBtn.setObjectName("clearBtn")
        self.resulttext = QtWidgets.QTextEdit(Form)
        self.resulttext.setGeometry(QtCore.QRect(280, 250, 811, 481))
        self.resulttext.setStyleSheet("background-color: rgba(236, 234, 255, 150);\n"
"font: 12pt \"Agency FB\";\n"
"")
        self.resulttext.setObjectName("resulttext")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 10, 591, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 9pt \"华文行楷\";\n"
"background-color: rgba(255, 255, 255, 150);\n"
"\n"
"font: 25pt \"Agency FB\";\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryConstell)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StarcomboBox.setItemText(0, _translate("Form", "白羊座"))
        self.StarcomboBox.setItemText(1, _translate("Form", "金牛座"))
        self.StarcomboBox.setItemText(2, _translate("Form", "双子座"))
        self.StarcomboBox.setItemText(3, _translate("Form", "巨蟹座"))
        self.StarcomboBox.setItemText(4, _translate("Form", "狮子座"))
        self.StarcomboBox.setItemText(5, _translate("Form", "处女座"))
        self.StarcomboBox.setItemText(6, _translate("Form", "天秤座"))
        self.StarcomboBox.setItemText(7, _translate("Form", "天蝎座"))
        self.StarcomboBox.setItemText(8, _translate("Form", "射手座"))
        self.StarcomboBox.setItemText(9, _translate("Form", "摩羯座"))
        self.StarcomboBox.setItemText(10, _translate("Form", "水瓶座"))
        self.StarcomboBox.setItemText(11, _translate("Form", "双鱼座"))
        self.TimecomboBox.setItemText(0, _translate("Form", "today"))
        self.TimecomboBox.setItemText(1, _translate("Form", "tomorrow"))
        self.TimecomboBox.setItemText(2, _translate("Form", "week"))
        self.TimecomboBox.setItemText(3, _translate("Form", "month"))
        self.TimecomboBox.setItemText(4, _translate("Form", "year"))
        self.label.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">选择查询时间</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>选择您的星座</p></body></html>"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))
        self.lineEdit.setText(_translate("Form", "          欢迎查询星座运势"))

import test1
