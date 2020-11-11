"""
设置单元格的字体和颜色
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor, QFont


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格的字体和颜色")
        self.resize(430, 300)
        layout = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["name", "gender", "weight"])

        tableWidget.setRowHeight(0,100)
        tableWidget.setColumnWidth(0,200)

        newItem = QTableWidgetItem("雷神")
        newItem.setFont(QFont("Times", 40, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("God")
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem("Rap")
        newItem.setFont(QFont("Times", 60, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(2, 0, newItem)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PlaceControlInCell()
    main.show()
    sys.exit(app.exec_())
