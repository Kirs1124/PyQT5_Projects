"""
停靠控件（QDockWIdget）
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self):
        super(DockDemo, self).__init__()
        self.setWindowTitle("停靠控件")
        # layout = QHBoxLayout()
        self.items = QDockWidget("Dockable",self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")

        self.items.setWidget(self.listWidget)

        self.items.setFloating(True)

        self.setCentralWidget(QLineEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DockDemo()
    main.show()
    sys.exit(app.exec_())