
"""Main window for CSV Editor.
"""

import sys
from PySide.QtGui import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    mainwin.show()

    app.exec_()
