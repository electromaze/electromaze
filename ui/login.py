# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(500, 0, 500, 500))
        self.frame.setMaximumSize(QtCore.QSize(500, 500))
        self.frame.setStyleSheet("background-color: rgb(44, 28, 28);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameLineEdit.setGeometry(QtCore.QRect(160, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.pwdLineEdit = QtWidgets.QLineEdit(self.frame)
        self.pwdLineEdit.setGeometry(QtCore.QRect(160, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.pwdLineEdit.setFont(font)
        self.pwdLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwdLineEdit.setText("")
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.signInbtn = QtWidgets.QPushButton(self.frame)
        self.signInbtn.setGeometry(QtCore.QRect(200, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.signInbtn.setFont(font)
        self.signInbtn.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 154, 3);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 154, 3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 154, 3);\n"
"}")
        self.signInbtn.setObjectName("signInbtn")
        self.registerBtn = QtWidgets.QPushButton(self.frame)
        self.registerBtn.setGeometry(QtCore.QRect(450, 450, 31, 31))
        self.registerBtn.setStyleSheet("QPushButton {\n"
"    color: rgb(228, 76, 52);\n"
"    \n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 154, 3);\n"
"    color: rgb(228, 76, 52);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 154, 3);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.registerBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/rocketsystemsai-face.ai-8158af615e56/img/icons/24x24/cil-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registerBtn.setIcon(icon)
        self.registerBtn.setObjectName("registerBtn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.frame_2.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/login.jpeg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "True Tracker - Login"))
        self.usernameLineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pwdLineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Welcome to name"))
        self.label_3.setText(_translate("MainWindow", "Sign in to continue"))
        self.signInbtn.setText(_translate("MainWindow", "Sign In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
