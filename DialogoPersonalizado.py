from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super(DialogoPersonalizado,self).__init__(parent)
        self.lned_texto = QLineEdit(self)
        self.lned_texto.setPlaceholderText("Escribe un texto")
        self.btn_ok = QPushButton("Ok",self)

        vlyt = QVBoxLayout(self)
        vlyt.addWidget(self.lned_texto)
        vlyt.addWidget(self.btn_ok)

        self.btn_ok.clicked.connect(self.texto)

    def texto(self):
        self.texto = self.lned_texto.text()
        self.close()

    @classmethod
    def get_value(cls,parent):
        dialogo = cls(parent)
        dialogo.exec_()
        return dialogo.texto


class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion,self).__init__()
        vlyt = QVBoxLayout(self)
        self.btn = QPushButton("Presioname",self)
        self.lbl = QLabel("Sin texto", self)
        vlyt.addWidget(self.btn)
        vlyt.addWidget(self.lbl, alignment=Qt.AlignCenter)

        self.btn.clicked.connect(self.abrir_dialogo)

    def abrir_dialogo(self):
        texto = DialogoPersonalizado.get_value(self)
        self.lbl.setText(texto)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())
