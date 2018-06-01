from PyQt5.QtWidgets import QMainWindow, QApplication
import main_window
import sys
import threading
import socket
class Main(QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        socktemp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    ##by ChenPo
        self.sock = socktemp    ##by ChenPo
        self.sock.connect((host, port)) ##by ChenPo
        self.sock.send(b'1')    ##by ChenPo
        self.pushButton.setText("Send") ##by ChenPo
        self.pushButton.setEnabled(False)#by ChenPo
        self.pushButton_2.clicked.connect(self.onClick)#by ChenPo
        self.pushButton.clicked.connect(self.send)#by ChenPo

    def onClick(self):
        global userID
        userID = self.lineEdit_2.text()
        self.sock.send(userID.encode())
        self.textBrowser.update()
        self.lineEdit_2.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        th2 = threading.Thread(target=self.recv)#by ChenPo
        th2.setDaemon(True)#by ChenPo
        th2.start()#by ChenPo

    def recv(self):#by ChenPo
        while True:
            otherword = self.sock.recv(1024)
            self.textBrowser.append(otherword.decode())
            self.textBrowser.update()

    def send(self):
        text = self.lineEdit.text()#by ChenPo
        self.sock.send(text.encode())   ##by ChenPo
        text = text + ' : ' + userID#by ChenPo
        text = "{: >70}".format(text)#by ChenPo
        self.textBrowser.append(text)#by ChenPo
        self.textBrowser.update()#by ChenPo
        self.lineEdit.setText("")#by ChenPo



def main():#by ChenPo
    user = Main('localhost', 5550)
    th1 = threading.Thread(target=user.send)
    th2 = threading.Thread(target=user.recv)
    threads = [th1, th2]
    for i in threads:
        i.setDaemon(True)
        i.start()
    i.join()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main('localhost', 5550)
    MainWindow.show()
    sys.exit(app.exec_())
    main()#by ChenPo
