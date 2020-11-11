"""
在单元格中实现图文混排的效果
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中实现图文混排的效果")
        self.resize(430, 300)
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)

        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(["name", "gender", "weight","显示图片"])

        newItem = QTableWidgetItem("jjy")
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem("女")
        self.tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem("160")
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon('../img/jjy.jpg'),'kiki')
        self.tableWidget.setItem(0,3,newItem)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()
    sys.exit(app.exec_())