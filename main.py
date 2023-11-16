import random
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_UI


class StrangeClass(QMainWindow, Ui_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.strangeButton.clicked.connect(self.start_strange_things)

    def start_strange_things(self):
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        self.qp.begin(self)
        self.qp.setBrush(QColor("#FFF200"))
        self.qp.setPen(QColor("#FFDD00"))

        for i in range(random.randint(10, 30)):
            r = random.randint(1, 100)
            self.qp.drawEllipse(QPoint(random.randint(1, self.width()), random.randint(1, self.height())), r, r)

        self.qp.end()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StrangeClass()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())