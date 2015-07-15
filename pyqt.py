import sys
from PyQt4 import QtCore, QtGui, uic
import numpy as np 
form_class = uic.loadUiType("peb_volumeizer.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_d2vol.clicked.connect(self.btn_d2vol_clicked)  # Bind the event handlers
        self.btn_save.clicked.connect(self.btn_save_clicked)  # Bind the event handlers
        self.units_selector.currentIndexChanged['QString'].connect(self.handleChanged)
 
    def btn_save_clicked(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '','Text (*.txt *.dat)')
        filedata1 = self.area_output.text()
        filedata2 = self.vol_output.text()
        with open(fname, 'w') as file_:
            file_.write('Area, Volume\n')
            file_.write(filedata1+', '+filedata2)

    def btn_d2vol_clicked(self):
        d = float(self.diam_input.text())
        if self.units_selector.currentText() == 'mm3':
            vol = (np.pi/6.)*d**3
            area = np.pi*d**3
        else:
            vol = (np.pi/6.)*(d/1000.)**3
            area = np.pi*(d/1000.)**3
        self.vol_output.setText(str(vol))
        self.area_output.setText(str(area))
        return area, vol

    def handleChanged(self, text):
        self.vol_output.clear()
        self.area_output.clear()
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()