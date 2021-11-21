import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.status = None
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.draw(self.status)
        self.qp.end()

    def draw(self, status):
        a = random.randint(20, 200)
        self.qp.setBrush(QColor(255, 255, 0))
        if status == 1:
            self.qp.drawEllipse(*[random.randint(0, 450), random.randint(0, 450)], a, a)

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.show()

    def run(self, event):
        self.status = 1
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())