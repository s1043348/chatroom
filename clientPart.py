from PyQt5.QtWidgets import QMainWindow, QApplication
import clientwindow_ui
import sys
import threading
import socket
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QEventLoop
from PyQt5.QtWidgets import *


from pymongo import MongoClient
from bson.objectid import ObjectId




class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        pass
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList=None):
        pass
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname, upwd):
        self.collection.insert_one({'uname':uname, 'upwd':upwd})
        print("Client: user added!!")

    def updataUser(self, uname, upwd):
        temp = self.collection.find_one({'uname': uname})
        temp['upwd'] = upwd
        self.collection.save(temp)
        msg = QMessageBox()  ## by ping
        msg.setIcon(QMessageBox.Information)
        msg.setText("密碼修改成功")
        msg.setWindowTitle("密碼修改成功")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname):
        if self.collection.find({'uname': uname}).count() > 0:
            return True
        return False

        # check checkUserExist
    def checkAccountAandPassword(self, uname, upwd):  # by ping
        if self.collection.find({'uname': uname, 'upwd':upwd}).count() > 0:
            return True
        else:
            msg = QMessageBox()  ## by ping
            msg.setIcon(QMessageBox.Information)
            msg.setText("您輸入的帳號已存在 且帳號與密碼不匹配")
            msg.setWindowTitle("錯誤")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        return False
    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        pass
        return False

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        pass

    def colseClient(self):
        self.client.close()
"""
class DataCaptureThread(QThread):  #by ping
     def collectProcessData(self):
         print("Collecting Process Data")

     def __init__(self, *args, **kwargs):
         QThread.__init__(self, *args, **kwargs)
         self.dataCollectionTimer = QTimer()
         self.dataCollectionTimer.moveToThread(self)
         self.dataCollectionTimer.timeout.connect(self.collectProcessData)

     def run(self):
         self.dataCollectionTimer.start(1000)
         loop = QEventLoop()
         loop.exec_()
"""
class Main(QMainWindow, clientwindow_ui.Ui_MainWindow):

    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        socktemp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #by ChenPo
        self.sock = socktemp    #by ChenPo
        self.sock.connect((host, port)) #by ChenPo
        self.sock.send(b'1')    ##by ChenPo
        self.pushButton_3.setText("Send") ##by ChenPo
        self.pushButton_3.setEnabled(False)#by ChenPo
        self.pushButton_2.setEnabled(False)#by ChenPo
        self.pushButton.clicked.connect(self.onClick)#by ChenPo ##這顆是login
        self.pushButton_2.clicked.connect(self.updateclick)
        self.pushButton_3.clicked.connect(self.send)#by ChenPo
        self.pushButton_ans.clicked.connect(self.ans)  # by ChenPo

    def updateclick(self):
        dbChatRoom = DataBaseChatRoom()
        dbChatRoom.updataUser(self.lineEdit.text(), self.lineEdit_3.text())
        self.lineEdit_3.setText("")

    def onClick(self):
        global userID
        dbChatRoom = DataBaseChatRoom()
        userID = self.lineEdit.text()
        userPSWD = self.lineEdit_2.text()
        GameBegin = False  ## by ping
        if dbChatRoom.checkUserExist(userID):
            if(dbChatRoom.checkAccountAandPassword(userID, userPSWD)):
                GameBegin = True
        else:
            dbChatRoom.insertUser(userID, userPSWD) #update database by client
            GameBegin = True
        if GameBegin:
            self.sock.send(userID.encode())
            self.textBrowser.update()
            self.lineEdit_2.setEnabled(False)   #pswd lineEdit disabled
            self.lineEdit.setEnabled(False) #username lineEdit disabled
            self.pushButton.setEnabled(False)   #Login button disabled
            self.pushButton_3.setEnabled(True)  #Send button enabled
            self.pushButton_2.setEnabled(True)  #Change pswd enabled
            th2 = threading.Thread(target=self.recv)#by ChenPo
            th2.setDaemon(True)#by ChenPo
            th2.start()#by ChenP
    def recv(self):#by ChenPo
        while True:
            try:
                buf = self.sock.recv(1024).decode()
                #print(buf)
                #made by ping
                if '*' in buf:
                    messageword = self.sock.recv(1024)
                    self.textBrowser.append(messageword.decode())
                    self.textBrowser.update()
                elif '#' in buf:
                    answord = self.sock.recv(1024)
                    self.textBrowser_ans.append(answord.decode())
                    self.textBrowser_ans.update()
                buf = None
            except:
                pass

    def send(self):
        text = self.lineEdit_4.text()#Send message lineEdit by ChenPo
        self.sock.send(b'*')#made by ping
        self.sock.send(text.encode())   ##by ChenPo
        text = userID + ' : ' + text#by ChenPo
        #text = "{: >70}".format(text)#by ChenPo
        self.textBrowser.append(text)#by ChenPo
        self.textBrowser.update()#by ChenPo
        self.lineEdit_4.setText("")#by ChenPo

    def ans(self):
        text = self.lineEdit_ans.text()  # Send message lineEdit by ping
        self.sock.send(b'#')#made by ping
        self.sock.send(text.encode())  ##by ping
        text = userID + ' : ' + text  # by ping
        self.textBrowser_ans.append(text)  # by ping
        self.textBrowser_ans.update()  # by ping
        self.lineEdit_ans.setText("")  # by ping





"""
def main():#by ChenPo
    user = Main('localhost', 5550)
    th1 = threading.Thread(target=user.send)
    th2 = threading.Thread(target=user.recv)
    threads = [th1, th2]
    for i in threads:
        i.setDaemon(True)
        i.start()
    i.join()
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main('localhost', 5550)
    MainWindow.show()
    sys.exit(app.exec_())
    #main()#by ChenPo
