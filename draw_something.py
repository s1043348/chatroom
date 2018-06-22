'''
簡單的畫板4.0 功能： 將按住滑鼠後移動的軌跡保留在窗體上
並解決二次作畫時與上次痕跡連續的問題 作者：PyLearn
部落格: http://www.cnblogs.com/PyLearn/ 最後修改日期: 2017/10/18
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPen)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        # resize設定寬高，move設定位置
        self.resize(1000, 600)
        self.move(100, 100)
        self.setWindowTitle("簡單的畫板4.0")
        # setMouseTracking設定為False，否則不按下滑鼠時也會跟蹤滑鼠事件
        self.setMouseTracking(False)
        # 要想將按住滑鼠後移動的軌跡保留在窗體上 需要一個列表來儲存所有移動過的點
        self.pos_xy = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        ''' 
            首先判斷pos_xy列表中是不是至少有兩個點了 
            然後將pos_xy中第一個點賦值給point_start 
            利用中間變數pos_tmp遍歷整個pos_xy列表 
                point_end = pos_tmp 
                
                判斷point_end是否是斷點，如果是 
                    point_start賦值為斷點 
                    continue 
                判斷point_start是否是斷點，如果是 
                    point_start賦值為point_end 
                    continue
                     
                畫point_start到point_end之間的線 
                point_start = point_end 
                這樣，不斷地將相鄰兩個點之間畫線，就能留下滑鼠移動軌跡了 
        '''
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
        '''
            按住滑鼠移動事件：將當前點新增到pos_xy列表中 呼叫update()函式在這裏相當於呼叫
            paintEvent()函式 每次update()時，之前呼叫的paintEvent()留下的痕跡都會清空
        '''
        # 中間變數pos_tmp提取當前點
        pos_tmp = (event.pos().x(), event.pos().y())
        # pos_tmp新增到self.pos_xy中
        self.pos_xy.append(pos_tmp)
        self.update()

    def mouseReleaseEvent(self, event):
        '''
            重寫滑鼠按住後鬆開的事件 在每次鬆開後向pos_xy列表中新增一個斷點(-1, -1) 然後在繪畫時
            判斷一下是不是斷點就行了 是斷點的話就跳過去，不與之前的連續
        '''
        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)
        self.update()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    pyqt_learn = Example()
    pyqt_learn.show()
    app.exec_()
