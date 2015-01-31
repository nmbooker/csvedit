#!/usr/bin/env python3
"""Main window for CSV Editor.
"""

import sys
from PySide.QtGui import QMainWindow, QStyle, QFileDialog
from .ui.mainwindow import Ui_MainWindow
from .csv_table_model import CSVTableModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("untitled - csvedit")

        self.model = CSVTableModel()

        self.action_Open.triggered.connect(self.openfile)

        self.tableView.setModel(self.model)
    
    def openfile(self, checked=False):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "Files (*.*)")
        if filename:
            self.model.openfile(filename)
