# -*- encoding: utf-8 -*-
import socket
import threading
import datetime
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
import windowserver
from PyQt5.QtWidgets import QMainWindow, QApplication
from time import gmtime, strftime
global count
global id

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
    def deleteUser(self, unameList):
        self.collection.remove({'uname':unameList})

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname, upwd):
        self.collection.insert_one({'uname':uname,'upwd':upwd})


    def updataUser(self, uname=None, upwd=None):
        pass
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
class Server(QMainWindow, windowserver.Ui_MainWindow):
    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.namelist = list()
        self.pushButton.clicked.connect(self.Input)

    def checkConnection(self):
        global count
        connection, addr = self.sock.accept()
        count += 1
        print(count)
        print('Accept a new connection', connection.getsockname(), connection.fileno())


        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                Username = connection.recv(1024).decode()#by ChenPo
                welcome = "Weclome to Chat room, " + Username + "!\n"#by ChenPo
                connection.send(welcome.encode())#by ChenPo
                lets = "Now Lets Chat " + Username#by ChenPo
                connection.send(lets.encode())#by ChenPo
                self.tellOthers(connection.fileno(),'SYSTEM: ' + Username + ' in the Chatroom.')#by ChenPo
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, Username, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()


            else:
                connection.send(b'please go out!')
                count-=1
                self.tellOthers(connection.fileno(), "New chat room people number " + str(count))
                print(count)
                print("Someone leave! Chat room")
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass


    def subThreadIn(self, myconnection, myname,  connNumber):
        global count
        global id
        self.mylist.append(myconnection)

        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    nowtime = datetime.datetime.now()#by ChenPo
                    self.tellOthers(connNumber, myname + ": " + recvedMsg + "\t" + "[ " +str(nowtime.hour).zfill(2)+":" + str(nowtime.minute).zfill(2)+":"+str(nowtime.second).zfill(2)+" ]")#by ChenPo
                else:
                    pass

            except (OSError, ConnectionResetError):
                count -= 1
                self.tellOthers(connNumber, "New chat room people number " + str(count))
                print(count)
                print("Someone leave! Chat room")
                try:
                    self.mylist.remove(myconnection)

                except:
                    pass

                myconnection.close()
                return
    def Input(self):
        dbChatRoom = DataBaseChatRoom()
        dbChatRoom.Initdatabase()
        dbChatRoom.colseClient()
        user = self.lineEdit.text()
        print(user)
        psw = self.lineEdit_2.text()
        dbChatRoom.insertUser(user,psw)





def main():
    #s = Server('140.138.145.9', 5550)#by Ping
    s = Server('140.138.145.16', 5550)#by ChenPo
    global count
    global id
    id = list()
    count = 0
    while True:
        s.checkConnection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Server('140.138.145.16', 5550)
    MainWindow.show()
    sys.exit(app.exec_())
    main()
