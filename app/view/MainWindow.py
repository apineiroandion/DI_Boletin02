
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QPushButton, QHBoxLayout

centralLayout = QVBoxLayout()
buttonsLayout = QHBoxLayout()
stackedLayout = QStackedLayout()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setWindowTitle("Boletin 2")
        self.setMinimumSize(400, 200)
        self.setMaximumSize(800, 400)

        container = Container()
        self.setCentralWidget(container)


class Container(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setLayout(centralLayout)
        panels_container = PanelsContainer()
        buttons_container = ButtonContainer()
        centralLayout.addWidget(panels_container)
        centralLayout.addWidget(buttons_container)


class PanelsContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setLayout(stackedLayout)
        self.layout().addWidget(ColorPanel(QColor("red")))
        self.layout().addWidget(ColorPanel(QColor("blue")))
        self.layout().addWidget(ColorPanel(QColor("green")))
        self.layout().setCurrentIndex(0)

class ColorPanel(QWidget):
    def __init__(self, color):
        super().__init__()
        self.show()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class ButtonContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.setLayout(buttonsLayout)
        self.layout().addWidget(Button("Rojo", 0))
        self.layout().addWidget(Button("Azul", 1))
        self.layout().addWidget(Button("Verde", 2))

class Button(QPushButton):
    def __init__(self, text, index):
        super().__init__(text)
        self.show()
        self.clicked.connect(lambda: stackedLayout.setCurrentIndex(index))