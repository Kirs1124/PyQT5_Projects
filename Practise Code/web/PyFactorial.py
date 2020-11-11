"""
JavaScript调用Python函数计算阶乘
将Python的一个对象映射到JavaScript中
将槽函数映射到JavaScript中

"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
from factorial import *

channel = QWebChannel()
factorial = Factorial()


class PyFactorial(QWidget):
    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle("Python计算阶乘")
        self.resize(600, 300)
        layout = QVBoxLayout()
        self.browse = QWebEngineView()
        url = os.getcwd() + '/f.html'
        self.browser.load(QUrl.fromLocalFile(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyFactorial()
    main.show()
    sys.exit(app.exec_())
