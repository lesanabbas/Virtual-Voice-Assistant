# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FridayGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import psutil

class Ui_Gui(object):
    def setupUi(self, Gui):
        Gui.setObjectName("Gui")
        Gui.resize(1402, 850)
        self.centralwidget = QtWidgets.QWidget(Gui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1401, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Abbas\\OneDrive\\Desktop\\Friday Voice Assistant\\assets\\bg-img.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 641, 481))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("assets/center.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 256, 41))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"border-radius: none; font-size: 20px; font-weight: bold;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1170, 20, 256, 41))
        self.textBrowser_2.setStyleSheet("background-color: transparent;\n"
"border-radius: none; font-size: 20px; font-weight: bold;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 312, 61, 61))
        self.pushButton.setStyleSheet("border-radius: 25px;\n"
"background-color: transparent;\n"
"color: rgb(0, 253, 253);\n"
"font-size: 20px;\n"
"font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 700, 181, 41))
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: red;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(570, 810, 240, 51))
        self.textBrowser_3.setStyleSheet("background-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: red;\n"
"\n"
"border-radius: none;\n"
"")
        battery = psutil.sensors_battery()
        self.textBrowser_3.setText(f"Battery Percent: {battery.percent}%")
        self.textBrowser_3.setObjectName("textBrowser_3")
        
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(592, 740, 300, 52))
        self.textBrowser_4.setStyleSheet("background-color: transparent;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: red;\n"
"\n"
"border-radius: none;\n"
"")
        if battery.power_plugged:
                self.textBrowser_4.setText("Power Plugged In")
        else:
                self.textBrowser_4.setText("Power Plugged Out")
        self.textBrowser_4.setObjectName("textBrowser_4")
        
        Gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(Gui)
        QtCore.QMetaObject.connectSlotsByName(Gui)

    def retranslateUi(self, Gui):
        import platform
        my_system = platform.uname()
        _translate = QtCore.QCoreApplication.translate
        Gui.setWindowTitle(_translate("Gui", "Voice Assistant"))
        self.pushButton.setText(_translate("Gui", "Start"))
        self.pushButton_2.setText(_translate("Gui", "Terminate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QMainWindow()
    ui = Ui_Gui()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())