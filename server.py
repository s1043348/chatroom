# -*- encoding: utf-8 -*-
import socket
import threading
import datetime
import sys
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import serverwindow_ui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem #by Wei
from time import gmtime, strftime


class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('192.168.43.120', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        pass
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList):
        self.collection.remove({'uname': unameList})

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname, upwd):
        self.collection.insert_one({'uname': uname, 'upwd': upwd})
        print("Server: user added!!")

    def updataUser(self, uname=None, upwd=None):
        pass
        return 'successful'

    # check checkUserExist
    def checkUserExist(self, uname):
        temp = self.collection.find({'uname': uname})
        if temp:
            return True
        else:
            return False

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname='A', upwd='A'):
        pass
        return False

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        self.collection.delete_many({})
        userList = []
        userList.append({'uname': 'A', 'upwd': 'A'})
        userList.append({'uname': 'B', 'upwd': 'B'})
        userList.append({'uname': 'C', 'upwd': 'C'})
        userList.append({'uname': 'D', 'upwd': 'D'})
        userList.append({'uname': 'E', 'upwd': 'E'})
        self.collection.insert_many(userList)
        print("Server: initialize database!!")

    def colseClient(self):
        self.client.close()




class Server(QMainWindow, serverwindow_ui.Ui_MainWindow):
    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        dbChatRoom = DataBaseChatRoom()
        dbChatRoom.Initdatabase()   #reset database 剩下user A, B, C, D, E
        self.count = 0
        self.mylist = list()
        self.pushButton.clicked.connect(self.Input)
        self.pushButton_2.clicked.connect(self.DelUser)
        self.pushButton_question.clicked.connect(self.QuestionInput)#送出問題按鍵
        self.questiontext = "你吃大便猜三小這是初始化"
        self.question = "幹你老師猜三小這是初始化"
        global namelist #by Wei
        namelist = []# by Wei
        self.model = QStandardItemModel() # by Wei

    def checkConnection(self):#監聽進入Client
        connection, addr = self.sock.accept()#接收
        self.count += 1
        self.tellALLcount()
        print(self.count)
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                Username = connection.recv(1024).decode()#by ChenPo
                welcome = "Weclome to Chat room, " + Username + "!\n"# 給登入者
                connection.send(welcome.encode())#by ChenPo
                lets = "Now Lets Chat " + Username#by ChenPo
                connection.send(lets.encode())#by ChenPo
                self.tellOthers(connection.fileno(),'SYSTEM: ' + Username + ' in the Chatroom.')#給其他使用者

                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, Username, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()

            else:
                connection.send(b'please go out!')
                self.count -= 1
                self.tellALLcount()
                self.tellOthers(connection.fileno(), "New chat room people number " + str(self.count))
                print(self.count)
                print("Someone leave! Chat room")
                connection.close()
        except:
            pass


    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):#廣播
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def tellALLcount(self):#更新人數
        for c in self.mylist:
            try:
                c.send(b'$')
                c.send(str(self.count).encode())
            except:
                pass

    def tellHit(self, exceptNum, whatToSay):  # 答題成功廣播
        for c in self.mylist:
            if c.fileno() == exceptNum:#答對的人
                try:
                    c.send(b'#')
                    c.send(whatToSay.encode())
                except:
                    pass
            else:#沒答對的人
                try:
                    c.send(b'#')
                    c.send("************".encode())
                except:
                    pass

    def tellnoHit(self, exceptNum, whatToSay):  # 答題錯誤廣播
        for c in self.mylist:
            if c.fileno() != exceptNum:#傳給答錯題以外的人
                try:
                    c.send(b'#')
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, myname,  connNumber):
        self.mylist.append(myconnection)

        while True:
            try:
                Buf = myconnection.recv(1024).decode()  # 聊天室訊息
                if Buf:
                    if Buf == '*':  # 聊天區
                        recvedMsg = myconnection.recv(1024).decode()
                        nowtime = datetime.datetime.now()  # by ChenPo
                        self.tellOthers(connNumber, '*')
                        self.tellOthers(connNumber, myname + ": " + recvedMsg + "\t" + "[ " + str(nowtime.hour).zfill(2) + ":" + str(nowtime.minute).zfill(2) + ":" + str(nowtime.second).zfill(2) + " ]")  # by ChenPo
                    elif Buf == '#':  # 答案區
                        recvedMsg = myconnection.recv(1024).decode()
                        # self.tellOthers(connNumber, '#')
                        if recvedMsg == self.question:  # 代表答對了
                            self.tellHit(connNumber, myname + "You Hit!!!!!!!")
                        else:  # 沒答對就跟一般對話一樣
                            nowtime = datetime.datetime.now()
                            self.tellnoHit(connNumber, myname + ": " + recvedMsg + "\t" + "[ " +str(nowtime.hour).zfill(2)+":" + str(nowtime.minute).zfill(2)+":"+str(nowtime.second).zfill(2)+" ]")#by ChenPo
                    elif Buf == '+':  # 畫畫區
                        recvedMsg = myconnection.recv(1024000000).decode()
                        self.tellOthers(connNumber, '+')
                        self.tellOthers(connNumber, recvedMsg)
                else:
                    pass

            except (OSError, ConnectionResetError):
                self.count -= 1
                self.tellALLcount()
                self.tellOthers(connNumber, "New chat room people number " + str(self.count))
                print("Someone leave! Chat room")
                print("Chat room people number: ", self.count)

                try:
                    self.mylist.remove(myconnection)

                except:
                    pass

                myconnection.close()
                return

    def QuestionInput(self):#問題傳送
        self.questiontext = "****Please paint : "+self.lineEdit_question.text()+"****"
        self.question = self.lineEdit_question.text()
        notu="****Question****"
        self.lineEdit_question.setText('')
        run=0
        numrandom=random.randint(0, len(self.mylist)-1)
        if self.count>=1:
            for c in self.mylist:
                if run==numrandom:#找到選中的人
                    c.send(b'#')#題目出在ANS區
                    c.send(self.questiontext.encode())
                else:#不是選中的人
                    c.send(b'#')# 提示在ANS區
                    c.send(notu.encode())
                    #c.send(str(numrandom).encode())
                run=run+1
                #print(numrandom)
        else:
            pass

    def Input(self):#server端加入使用者
        dbChatRoom = DataBaseChatRoom()
        #dbChatRoom.colseClient()
        user = self.lineEdit.text()
        print(user)
        namelist.append(user)
        psw = self.lineEdit_2.text()
        dbChatRoom.insertUser(user, psw)
        self.model.clear()
        for task in namelist:
            item = QStandardItem(task)
            item.setFont(QFont("微軟正黑體", 20))
            item.setCheckState(0)
            item.setCheckable(True)
            self.model.appendRow(item)
            self.listView.setModel(self.model)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

    def loopCheckConnect(self): #by ChenPo
        while True:
            print("wait for somebody...\n")
            self.checkConnection()
            print("somebody in!!\n")

    def DelUser(self):  #by ChenPo, not done yet
        dbChatRoom = DataBaseChatRoom()


def main():  # by ChenPo
    app = QApplication(sys.argv)
    MainWindow = Server('192.168.43.120', 5550)
    th1 = threading.Thread(target=MainWindow.loopCheckConnect)
    th1.start()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
