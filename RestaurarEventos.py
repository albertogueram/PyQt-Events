from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class Boton(QPushButton):
    def __init__(self,texto, parent = None):
        super(Boton,self).__init__(parent)
        self.setText(texto)

    def mousePressEvent(self, event):
        print("El boton fue clickeado con el evento modificado")
        super(Boton,self).mousePressEvent(event)

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion,self).__init__()
        vlyt = QVBoxLayout(self)

        btn = Boton("Click aqui", self)
        vlyt.addWidget(btn)

        btn.clicked.connect(self.clickeado)

    def clickeado(self):
        print("El boton fue clickeado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())



