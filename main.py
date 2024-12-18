import sys

from random import randint
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)
        self.setFixedSize(self.width(), self.height())
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def circle(self, qp):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setPen(QPen(QColor(*color)))
        qp.setBrush(QBrush(QColor(*color)))
        x = randint(0, 399)
        y = randint(50, 449)
        radius = randint(1, min(400 - x, 450 - y))
        qp.drawEllipse(x, y, radius, radius)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
