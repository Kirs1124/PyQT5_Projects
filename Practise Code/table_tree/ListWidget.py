"""
扩展的列表控件（QListWidget）
"""
from PyQt5.QtWidgets import *
import sys


class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle("QListWidget 例子")
        self.resize(300, 270)
        self.listwidget = QListWidget()
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        self.listwidget.addItem("item4")
        self.listwidget.addItem("item5")
        self.listwidget.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidget)

    def clicked(self, index):
        QMessageBox.information(self, "QListWidget", "您选择了" + self.listwidget.item(self.listwidget.row(index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())
