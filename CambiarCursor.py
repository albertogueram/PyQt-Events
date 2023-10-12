from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion,self).__init__()
        vlyt_principal = QVBoxLayout(self)

        btn_1 = QPushButton("Boton 1", self)
        btn_2 = QPushButton("Boton 2", self)
        vlyt_principal.addWidget(btn_1)
        vlyt_principal.addWidget(btn_2)

        btn_1.setCursor(Qt.IBeamCursor)
        btn_2.setCursor(Qt.OpenHandCursor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())