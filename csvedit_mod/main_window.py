#!/usr/bin/env python3
"""Main window for CSV Editor.
"""

import sys
from PySide.QtGui import QMainWindow, QStyle
from .ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.action_Open.triggered.connect(self.openfile)
    
    def openfile(self, checked=False):
        print("Open file")
