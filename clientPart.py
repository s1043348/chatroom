from PyQt5.QtWidgets import QMainWindow, QApplication
import clientwindow_ui
import sys
import threading
import socket

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
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname='A'):
        pass
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
        self.pushButton.clicked.connect(self.onClick)#by ChenPo
        self.pushButton_2.clicked.connect(self.updateclick)
        self.pushButton_3.clicked.connect(self.send)#by ChenPo

    def updateclick(self):
        dbChatRoom = DataBaseChatRoom()
        dbChatRoom.updataUser(self.lineEdit.text(), self.lineEdit_3.text())
        self.lineEdit_3.setText("")

    def onClick(self):
        global userID
        dbChatRoom = DataBaseChatRoom()
        userID = self.lineEdit.text()
        userPSWD = self.lineEdit_2.text()
        dbChatRoom.insertUser(userID, userPSWD) #update database by client
        self.sock.send(userID.encode())
        self.textBrowser.update()
        self.lineEdit_2.setEnabled(False)   #pswd lineEdit disabled
        self.lineEdit.setEnabled(False) #username lineEdit disabled
        self.pushButton.setEnabled(False)   #Login button disabled
        self.pushButton_3.setEnabled(True)  #Send button enabled
        self.pushButton_2.setEnabled(True)  #Change pswd enabled
        th2 = threading.Thread(target=self.recv)#by ChenPo
        th2.setDaemon(True)#by ChenPo
        th2.start()#by ChenPo

    def recv(self):#by ChenPo
        while True:
            otherword = self.sock.recv(1024)
            self.textBrowser.append(otherword.decode())
            self.textBrowser.update()

    def send(self):
        text = self.lineEdit_4.text()#Send message lineEdit by ChenPo
        self.sock.send(text.encode())   ##by ChenPo
        text = text + ' : ' + userID#by ChenPo
        text = "{: >70}".format(text)#by ChenPo
        self.textBrowser.append(text)#by ChenPo
        self.textBrowser.update()#by ChenPo
        self.lineEdit_4.setText("")#by ChenPo

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
