import sys

from PyQt6.QtWidgets import QApplication

from app.view.MainWindow import MainWindow

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    window = MainWindow()
    aplicacion.exec()