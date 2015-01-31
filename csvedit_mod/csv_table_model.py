#!/usr/bin/env python3
"""Model for CSV Editor.
"""

import sys
import csv
from PySide.QtCore import QAbstractTableModel, Qt

class CSVTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CSVTableModel, self).__init__(parent)
        self._data = []

    def data(self, index, role=Qt.DisplayRole):
        return self._data[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0]) if self._data else 0

    def openfile(self, filename):
        with open(filename, 'r') as infile:
            csvdata = csv.reader(infile)
            self.modelAboutToBeReset.emit()
            self._data = list(csvdata)
            self.modelReset.emit()
