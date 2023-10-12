from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QCursor
import sys

class Aplicacion(QMainWindow):
    def __init__(self):
        super(Aplicacion,self).__init__()
        pixmap = QPixmap("lapiz.png").scaled(QSize(24,24),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        cursor = QCursor(pixmap,0,24)
        self.setCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())