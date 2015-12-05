#!/usr/bin/env python

'''
Created on Sun Sep 06 13:17:09 2015

@author: rakeshbhat9

Below code should be able to compare close prices on index/stock of your choice versus
any index/stock and plot it on graph
'''
import pandas as pd
import datetime as dt
import pandas.io.data
from pandas import *
import matplotlib.pyplot as plt
import PyQt4
from PyQt4 import *
from ScripCompare_ui import Ui_MainWindow
import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui



stc = "A"
ind = "A"
sdt = "%d/%m/%y"
edt = "%d/%m/%y"

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.LetsGetInput)

    def LetsGetInput(self):
        stc = self.ui.lineEdit.text()
        ind = self.ui.lineEdit_2.text()
        d1 = self.ui.dateEdit.date()
        d2 = self.ui.dateEdit_2.date()

        format = "MM/dd/yy";
        d1s = d1.toString(format)
        d2s = d2.toString(format)


        stcd = pd.io.data.get_data_yahoo(stc,d1s,d2s)
        indd = pd.io.data.get_data_yahoo(ind,d1s,d2s)
        stcd[stc.upper()+' Close'] = stcd['Close']
        indd[ind.upper()+' Close'] = indd['Close']

        print ""
        print "These are first five lines of your  Stock's Data"
        print stcd.head()
        print ""
        print "These are first five lines of your  Index's Data"
        print indd.head()
        print ""
        print "Crunching data in background to get you a cool graph!"
        dfs = stcd[stc.upper()+' Close']
        dfi = indd[ind.upper()+' Close']

        ax = dfs.plot()
        dfi.plot(ax=ax)
        plt.title('Scrip Compare')
        plt.legend()
        plt.ylabel('Price in $')
        plt.show()


if __name__== '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

