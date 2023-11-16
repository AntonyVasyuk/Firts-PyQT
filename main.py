from random import randint
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

        for i in range(randint(10, 30)):
            r = randint(1, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(QPoint(randint(1, self.width()), randint(1, self.height())), r, r)

        self.qp.end()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StrangeClass()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())