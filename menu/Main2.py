from PyQt5 import QtWidgets, QtGui, QtCore


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # create table:
        self.table = QtWidgets.QTableWidget()
        [self.table.insertRow(i) for i in [0,1,2]]
        [self.table.insertColumn(i) for i in [0,1]]
        # set values for first column:
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem('A') )
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem('B') )
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem('C') )
        # add checkboxes to second column:
        cb0  = QtWidgets.QCheckBox( parent=self.table )
        cb1  = QtWidgets.QCheckBox( parent=self.table )
        cb2  = QtWidgets.QCheckBox( parent=self.table )
        self.table.setCellWidget(0, 1, cb0)
        self.table.setCellWidget(1, 1, cb1)
        self.table.setCellWidget(2, 1, cb2)
        # connect table signals:
        self.table.cellChanged.connect(self.cell_changed)
        self.table.itemChanged.connect(self.item_changed)
        # connect checkbox signals:
        cb0.clicked.connect(self.checkbox_clicked)
        cb1.clicked.connect(self.checkbox_clicked)
        cb2.clicked.connect(self.checkbox_clicked)
        # show:
        self.setCentralWidget(self.table)
        self.setWindowTitle('TableWidget, CheckBoxes')
        self.show()

    def cell_changed(self, row, col):
        print(row, col)
    def checkbox_clicked(self, checked):
        print(checked)
    def item_changed(self, item):
        print(item)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    app.exec_()