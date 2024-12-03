#!/usr/bin/env python

import sys
from PyQt6.QtWidgets import QApplication
sys.path.append("/home/tul16619/SD1/MLADP_GUI/src/functs/")
from main_page import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
