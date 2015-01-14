#!/usr/bin/env python3
"""Main window for CSV Editor.
"""

import sys
from PySide.QtGui import QStyle
from .ui.mainwindow import Ui_MainWindow


class Ui_MainWindow(Ui_MainWindow):
    def setupUi(self, mainwin):
        super(Ui_MainWindow, self).setupUi(mainwin)

        self.action_New.setIcon(mainwin.style().standardIcon(
