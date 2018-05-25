from PyQt5.QtWidgets import QMainWindow, QApplication
import example_ui
import sys

class Main(QMainWindow, example_ui.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Send")
        self.pushButton_2.clicked.connect(self.onClick)


    def onClick(self):
        self.lineEdit_2.setEnabled(False)
        self.pushButton_2.setEnabled(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
