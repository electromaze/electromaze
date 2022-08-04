import sys
import os
import logging
import datetime
import time

import serial
from PyQt5.QtCore import QTimer
from pymongo import MongoClient
from ui.home import Ui_home_window
from ui.login import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets
from passlib.hash import sha256_crypt
from threading import Thread
import serial.tools.list_ports as ports
from ui.register import Ui_RegisterWindow
from applogging.app_logger import AppLogger
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox

currPath = os.path.dirname(os.path.abspath(__file__))
debugFile = os.path.join(currPath, 'logs', 'app.log')
AppLogger('debug', debugFile)
appLog = logging.getLogger('debug')


class UI(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Variables
        self.RFIDComPort = None
        self.registerUi = None
        self.registerWin = None
        self.homeUi = None
        self.homeWin = None
        self.loginUi = Ui_MainWindow()
        self.loginUi.setupUi(self)
        self.closeApp = False
        self.t = Thread(target=self.ShowDataOnTerminal)

        # Check if db installed
        appLog.error("Checking if db is installed")
        dbClient = MongoClient('localhost', 27017)
        dbs = dbClient.list_database_names()
        dbFound = False
        for db in dbs:
            if db == "ELECTROMAZE":
                dbFound = True
                break
            else:
                dbFound = False
        if not dbFound:
            appLog.error("DB not found creating it")
            emDb = dbClient["ELECTROMAZE"]
            self.userColl = emDb["users"]
            demo_data = dict()
            demo_data['created'] = datetime.datetime.utcnow()
            demo_data['firstName'] = "test"
            demo_data['lastName'] = "test"
            demo_data['username'] = "test"
            demo_data['password'] = "test"
            demo_data['email'] = "test"
            demo_data['userType'] = "test"
            x = self.userColl.insert_one(demo_data).inserted_id
            print(x)
            appLog.error("Db setup complete")
        else:
            emDb = dbClient["ELECTROMAZE"]
            self.userColl = emDb["users"]

        logoImgPath = os.path.join(currPath, 'img', 'login.jpeg')
        self.loginUi.label.setPixmap(QtGui.QPixmap(logoImgPath))
        self.loginUi.pwdLineEdit.setEchoMode(QLineEdit.Password)

        self.loginUi.registerBtn.clicked.connect(self.ShowRegistrationWindow)
        self.loginUi.signInbtn.clicked.connect(self.SignIn)

    def ShowRegistrationWindow(self):
        self.registerWin = QtWidgets.QMainWindow()
        self.registerUi = Ui_RegisterWindow()
        self.registerUi.setupUi(self.registerWin)
        self.registerUi.registerBtn.clicked.connect(self.RegisterUser)
        self.registerWin.show()

    def RegisterUser(self):
        firstName = self.registerUi.firstNameLineEdit.text()
        lastName = self.registerUi.lastNameLineEdit.text()
        username = self.registerUi.usernameLineEdit.text()
        email = self.registerUi.emailLineEdit.text()
        pwd = self.registerUi.pwdLineEdit.text()
        doc_list = list(self.userColl.find({'username': username}))
        if doc_list:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error. Username already exist")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        if '@' in email:
            if firstName != "" and lastName != "" and username != "" and email != "" and pwd != "":
                hashPwd = sha256_crypt.encrypt(pwd)
                dbData = dict()
                dbData['created'] = datetime.datetime.utcnow()
                dbData['firstName'] = firstName
                dbData['lastName'] = lastName
                dbData['username'] = username
                dbData['password'] = hashPwd
                dbData['email'] = email
                dbData['userType'] = "test"
                # x = self.userColl.insert_one(dbData).inserted_id
                x = self.userColl.insert_one(dbData).inserted_id
                print(x)
                appLog.error("{} {} user created")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Success. User created")
                msg.setWindowTitle("Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.registerWin.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error. Please fill in all details")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error. Incorrect email address")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def SignIn(self):
        username = self.loginUi.usernameLineEdit.text()
        userPwd = self.loginUi.pwdLineEdit.text()
        docList = list(self.userColl.find({'username': username}))
        if not docList:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error. User not found")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        else:
            dbPwd = docList[0]['password']
            res = sha256_crypt.verify(userPwd, dbPwd)
            if not res:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error. Incorrect username or password")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sign in success")
                msg.setWindowTitle("Information")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.homeWin = QtWidgets.QMainWindow()
                self.homeUi = Ui_home_window()
                self.homeUi.setupUi(self.homeWin)
                # main_window.close()
                self.homeWin.show()
                self.homeUi.imgLabel.setPixmap(QtGui.QPixmap(os.path.join(currPath, 'img', 'logo1.jpeg')))
                setupIcon = QtGui.QIcon()
                setupIcon.addPixmap(QtGui.QPixmap(os.path.join(currPath, 'img', 'cil-settings.png')),
                                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.homeUi.setupPageBtn.setIcon(setupIcon)
                self.homeUi.devicePageBtn.clicked.connect(self.ShowDevicePage)
                self.homeUi.setupPageBtn.clicked.connect(self.ShowSetupPage)
                com_ports = list(ports.comports())
                for i in com_ports:
                    self.homeUi.comPortComboBox.addItem(i.device)
                self.homeUi.baudrateComboBox.addItems(
                    ["1200", "2400", "4800", "9600", "14400", "19200", "28800", "38400", "57600"])
                self.homeUi.baudrateComboBox.setCurrentIndex(3)
                self.homeUi.parityComboBox.addItems(["PARITY_EVEN", "PARITY_MARK", "PARITY_NONE", "PARITY_ODD"])
                self.homeUi.parityComboBox.setCurrentIndex(2)
                self.homeUi.dataBitsComboBox.addItems(["5", "6", "7", "8"])
                self.homeUi.dataBitsComboBox.setCurrentIndex(3)
                self.homeUi.stopBitComboBox.addItems(["1", "1.5", "2"])
                self.homeUi.stopBitComboBox.setCurrentIndex(0)
                self.homeUi.connectComPortBtn.clicked.connect(self.ConnectComPort)
                self.homeUi.comPortStatusLineEdit.setText("N/A")

    def ShowSetupPage(self):
        self.homeUi.stackedWidget.setCurrentWidget(self.homeUi.setupPage)

    def ConnectComPort(self):
        try:
            self.RFIDComPort = serial.Serial(port=self.homeUi.comPortComboBox.currentText(),
                                             baudrate=int(self.homeUi.baudrateComboBox.currentText()))
            # bytesize=int(self.homeUi.dataBitsComboBox.currentText()),
            # parity=str(self.homeUi.parityComboBox.currentText()),
            # stopBits=int(self.homeUi.stopBitComboBox.currentText()))
            if self.RFIDComPort.isOpen():
                self.homeUi.comPortStatusLineEdit.setText("Connected")
                self.homeUi.terminalTextEdit.append("Connected to {}".format(self.homeUi.comPortComboBox.currentText()))
                # Thread(target=self.ShowDataOnTerminal).start()
                self.t.start()
            else:
                self.homeUi.comPortStatusLineEdit.setText("N/A")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error {}".format(e))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def ShowDataOnTerminal(self):
        print("T")
        while not self.closeApp:
            print("S1")
            if self.closeApp:
                print("Breaking")
                break
            print("S2")
            if self.RFIDComPort.isOpen:
                print("S3")
                bytesToRead = self.RFIDComPort.inWaiting()
                serialData = ""
                print("S4")
                if bytesToRead != 0:
                    print(bytesToRead)
                    for i in range(bytesToRead):
                        dt = self.RFIDComPort.read()
                        serialData = serialData + dt.decode('utf-8')
                    self.homeUi.terminalTextEdit.append(serialData)
                    print("S5")
                print("S6")
            time.sleep(0.5)
        print("B")

    def ShowDevicePage(self):
        self.homeUi.stackedWidget.setCurrentWidget(self.homeUi.devicePage)


    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self, "QUIT", "Are you sure want to exit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.closeApp = True
            if self.RFIDComPort is not None:
                self.RFIDComPort.close()
        else:
            event.ignore()


app = QApplication(sys.argv)
main_window = UI()
# main_window.setWindowIcon(QIcon(icon_path))
main_window.show()
sys.exit(app.exec_())
