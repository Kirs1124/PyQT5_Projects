"""
改变单元格中图片的尺寸

setIconSize(QSize(width,height))


"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中图片的尺寸")
        self.resize(1000, 900)
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setIconSize(QSize(300,200))
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(["img1","img2","img3"])

        # 让列的宽度和图片的宽度相同
        for i in range(3):
            self.tableWidget.setColumnWidth(i,300)

        # 让行的高度和图片的高度相同
        for i in range(5):
            self.tableWidget.setRowHeight(i, 200)

        for k in range(15):
            i = k // 3   # 行
            j = k % 3   # 列
            item = QTableWidgetItem()
            item.setIcon(QIcon('../img/%d.png' % (k+1)))
            self.tableWidget.setItem(i,j,item)

        layout.addWidget(self.tableWidget)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellImageSize()
    main.show()
    sys.exit(app.exec_())