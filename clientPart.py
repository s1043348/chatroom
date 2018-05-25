from PyQt5.QtWidgets import QMainWindow, QApplication
import example_ui
import sys

class Main(QMainWindow, example_ui.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Send")
        self.pushButton.setEnabled(False)
        self.pushButton_2.clicked.connect(self.onClick)
        self.pushButton.clicked.connect(self.send)

    def onClick(self):
        global userID
        userID = self.lineEdit_2.text()
        self.lineEdit_2.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)

    def send(self):
        text = self.lineEdit.text()
        text = text + ' : ' + userID
        text = "{: >70}".format(text)
        self.textBrowser.append(text)
        self.textBrowser.update()
        self.lineEdit.setText("")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
