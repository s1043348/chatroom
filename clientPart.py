from PyQt5.QtWidgets import QMainWindow, QApplication
import clientwindow_ui
import sys
import threading
import socket
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QEventLoop
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPen)
from PyQt5.QtCore import Qt
import time
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
class CountDownThread(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)
    test = 0

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        count = 30
        while count >= 0:
            self.update.emit(count)
            count -= 1
            time.sleep(1)

class Main(QMainWindow, clientwindow_ui.Ui_MainWindow):

    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        socktemp = socket.socket()    # by ChenPo
        self.sock = socktemp    # by ChenPo
        self.sock.connect((host, port))  # by ChenPo
        self.sock.send(b'1')    # by ChenPo
        self.pushButton_3.setText("Send")  # by ChenPo
        self.pushButton_3.setEnabled(False)  # by ChenPo
        self.pushButton_2.setEnabled(False)  # by ChenPo
        self.pushButton.clicked.connect(self.onClick)  # by ChenPo ##這顆是login
        self.pushButton_2.clicked.connect(self.updateclick)
        self.pushButton_3.clicked.connect(self.send)  # by ChenPo
        self.pushButton_ans.clicked.connect(self.ans)  # by ChenPo
        self.setMouseTracking(False)
        # 要想將按住滑鼠後移動的軌跡保留在窗體上 需要一個列表來儲存所有移動過的點
        self.pos_xy = []
        self.contorl = False
        self.count_thread = CountDownThread()
        self.count_thread.update.connect(self.Set_Value)


    def Set_Value(self, data):
        self.label_remain_t.setText("剩餘時間: " + str(data) + "秒")
        if(data == 0):
            self.contorl = False
            painter = QPainter()
            painter.end()
            self.sock.send(b'+')
            self.pos_xy.clear()
            self.sock.sendall(str(self.pos_xy).encode())
            self.update()

    def updateclick(self):
        dbChatRoom = DataBaseChatRoom()
        dbChatRoom.updataUser(self.lineEdit.text(), self.lineEdit_3.text())
        self.lineEdit_3.setText("")

    def onClick(self):
        global userID
        dbChatRoom = DataBaseChatRoom()
        userID = self.lineEdit.text()
        userPSWD = self.lineEdit_2.text()
        GameBegin = False  # by ping
        if dbChatRoom.checkUserExist(userID):
            if(dbChatRoom.checkAccountAandPassword(userID, userPSWD)):
                GameBegin = True
        else:
            dbChatRoom.insertUser(userID, userPSWD) # update database by client
            GameBegin = True
        if GameBegin:
            self.sock.send(userID.encode())
            self.textBrowser.update()
            self.lineEdit_2.setEnabled(False)   # pswd lineEdit disabled
            self.lineEdit.setEnabled(False)  # username lineEdit disabled
            self.pushButton.setEnabled(False)   # Login button disabled
            self.pushButton_3.setEnabled(True)  # Send button enabled
            self.pushButton_2.setEnabled(True)  # Change pswd enabled
            th2 = threading.Thread(target=self.recv)  # by ChenPo
            th2.setDaemon(True)  # by ChenPo
            th2.start()  # by ChenPo

    def recv(self):  # by ChenPo
        while True:
            try:
                buf = self.sock.recv(1024).decode()
                # made by ping
                if '*' in buf:
                    messageword = self.sock.recv(1024)
                    self.textBrowser.append(messageword.decode())
                    self.textBrowser.update()
                elif '#' in buf:
                    answord = self.sock.recv(1024)
                    self.textBrowser_ans.append(answord.decode())
                    self.textBrowser_ans.update()
                    if 'paint' in answord.decode():
                        self.contorl = True
                        self.count_thread.start()
                        self.lineEdit_ans.setEnabled(False)
                    elif 'Question' in answord.decode():
                        self.count_thread.start()
                    elif 'hit' in answord.decode():
                        self.lineEdit_ans.setEnabled(False)
                elif '%' in buf:
                    opration = self.sock.recv(1024).decode()
                    if opration == 'Countdown':
                        self.count_thread.start()
                    elif opration == 'Draw':
                        self.contorl = True
                elif '+' in buf:
                    posxy = self.sock.recv(1024000000).decode()
                    self.pos_xy = eval(posxy)
                    painter = QPainter()
                    painter.begin(self)
                    pen = QPen(Qt.black, 2, Qt.SolidLine)
                    painter.setPen(pen)
                    if len(self.pos_xy) > 1:
                        point_start = self.pos_xy[0]
                        for pos_tmp in self.pos_xy:
                            point_end = pos_tmp
                            if point_end == (-1, -1):
                                point_start = (-1, -1)
                                continue
                            if point_start == (-1, -1):
                                point_start = point_end
                                continue

                            painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                            point_start = point_end
                    painter.end()
                    self.update()
                elif '$' in buf:
                    people_num = self.sock.recv(1024).decode()
                    self.label.setText("目前聊天室有" + str(people_num) + "人")

                else:
                    self.textBrowser.append(buf)
                    self.textBrowser.update()
                buf = None
            except:
                pass

    def send(self):
        text = self.lineEdit_4.text()  # Send message lineEdit by ChenPo
        if text == '':
            text = ' '
        self.sock.send(b'*')  # made by ping
        self.sock.send(text.encode())   # by ChenPo
        text = userID + ' : ' + text  # by ChenPo
        # text = "{: >70}".format(text) #by ChenPo
        self.textBrowser.append(text)  # by ChenPo
        self.textBrowser.update()  # by ChenPo
        self.lineEdit_4.setText("")  # by ChenPo

    def ans(self):
        text = self.lineEdit_ans.text()  # Send message lineEdit by ping
        if text == '':
            text = ' '
        self.sock.send(b'#')  # made by ping
        self.sock.send(text.encode())  # by ping
        text = userID + ' : ' + text  # by ping
        self.textBrowser_ans.append(text)  # by ping
        self.textBrowser_ans.update()  # by ping
        self.lineEdit_ans.setText("")  # by ping

    def paintEvent(self, event):
        if True:
            painter = QPainter()
            painter.begin(self)
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            painter.setPen(pen)
            if len(self.pos_xy) > 1:
                point_start = self.pos_xy[0]
                for pos_tmp in self.pos_xy:
                    point_end = pos_tmp
                    if point_end == (-1, -1):
                        point_start = (-1, -1)
                        continue
                    if point_start == (-1, -1):
                        point_start = point_end
                        continue

                    painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                    point_start = point_end
            painter.end()

    def mouseMoveEvent(self, event):
        if self.contorl:
            pos_tmp = (event.pos().x(), event.pos().y())
            # pos_tmp新增到self.pos_xy中
            self.pos_xy.append(pos_tmp)
            self.update()

    def mouseReleaseEvent(self, event):
        if self.contorl:
            pos_test = (-1, -1)
            self.pos_xy.append(pos_test)
            self.update()
            self.sock.send(b'+')
            self.sock.sendall(str(self.pos_xy).encode())




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
