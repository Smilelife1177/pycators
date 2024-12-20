from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("pydicators")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("cOOL")
    main_text.move(100, 100)



    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()