from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
import sys

app = QApplication(sys.argv)
w = QWidget()
w.show()
sys.exit(app.exec())