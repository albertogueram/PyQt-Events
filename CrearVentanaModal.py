from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QCursor
import sys

class QColorDialogPersonalizado(QDialog):
    def __init__(self):
        super(QColorDialogPersonalizado,self).__init__()
        self.setModal(True)

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion,self).__init__()
        self.resize(100,100)
        boton = QPushButton("Seleccionar color", self)
        boton.clicked.connect(self.abrir_ventana)

    def abrir_ventana(self):
        self.seleccion_color = QColorDialogPersonalizado()
        self.seleccion_color.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())