#!/usr/bin/env python3
"""Model for CSV Editor.
"""

import sys
import csv
import os.path
from PySide.QtCore import QAbstractTableModel, Qt

class CSVTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(CSVTableModel, self).__init__(parent)
        self._data = []

    def data(self, index, role=Qt.DisplayRole):
        """Return the data at the given index.
        """
        return self._data[index.row()][index.column()]

    def rowCount(self, parent):
        """Return current number of rows.
        """
        return len(self._data)

    def columnCount(self, parent):
        """Return current number of columns.
        """
        return len(self._data[0]) if self._data else 0

    def openfile(self, filename):
        """Open file with given filename.
        """
        with open(filename, 'r') as infile:
            csvdata = csv.reader(infile)
            self.modelAboutToBeReset.emit()
            self._data = list(csvdata)
            self.modelReset.emit()


    def savefile(self, filename, overwrite=False):
        if (not overwrite) and os.path.exists(filename):
            raise FileExistsError(filename)
        mode = 'w' if overwrite else 'x'
        with open(filename, mode) as outfile:
            csvout = csv.writer(outfile)
            csvout.writerows(self._data)


class FileExistsError(StandardError):
    """The given file already exists."""
    pass
