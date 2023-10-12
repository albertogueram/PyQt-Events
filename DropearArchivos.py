from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class EitquetaImagen(QLabel):
    def __init__(self, parent=None):
        super(EitquetaImagen,self).__init__(parent)
        self.setAcceptDrops(True)
        self.setMinimumSize(400,400)
        self.pixmap = QPixmap(400,400)
        self.pixmap.fill(Qt.black)
        self.setPixmap(self.pixmap)

    def dragEnterEvent(self, event):
        print("Funcionando")
        event.accept()

    def dropEvent(self,event):
        ruta = event.mimeData().urls()[0].toLocalFile() ## Solo queremos el primer valor de la lista
        self.setPixmap(QPixmap(ruta))
        print(ruta)

class LineEditPersonalizado(QLineEdit):
    def __init__(self, parent=None):
        super(LineEditPersonalizado,self).__init__(parent)
        self.setAcceptDrops(True)


    def dragEnterEvent(self, event):
        print("Funcionando")
        event.accept()

    def dropEvent(self,event):
        ruta = event.mimeData().urls()[0].toLocalFile()
        try:
            with open(ruta,"r") as f:
                self.setText(f.read())
        except:
            pass


class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion,self).__init__()
        vlyt = QVBoxLayout(self)
        etiqueta = EitquetaImagen(self)
        lned = LineEditPersonalizado(self)
        vlyt.addWidget(etiqueta)
        vlyt.addWidget(lned)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()
    sys.exit(app.exec_())