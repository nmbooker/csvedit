#!/usr/bin/env python3
"""Model for CSV Editor.
"""

import sys
from PySide.QtCore import QAbstractTableModel, Qt

class CSVTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CSVTableModel, self).__init__(parent)
        self._data = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
        ]

    def data(self, index, role=Qt.DisplayRole):
        return self._data[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0]) if self._data else 0

    def openfile(self, checked=False):
        print("Open file")
