"""
QSS基础

QSS(Qt Style Sheets)
Qt样式表

用于设置控件的风格

CSS

"""

from PyQt5.QtWidgets import *
import sys


class BasicQSS(QWidget):
    def __init__(self):
        super(BasicQSS, self).__init__()
        self.setWindowTitle("QSS Style")
        btn1 = QPushButton(self)
        btn1.setText("按钮1")
        btn2 = QPushButton(self)
        btn2.setText("按钮2")

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = BasicQSS()
    # 选择器
    qssButton = """
        QPushButton {
            background-color:red;
        }
    """
    form.setStyleSheet(qssButton)
    form.show()
    sys.exit(app.exec_())
