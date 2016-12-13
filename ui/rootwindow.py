from PyQt5 import QtCore, QtGui, QtWidgets

class RootWindow():
    def setupui(self, window):
        window.setObjectName("RootWindow")
        window.resize(400, 400)
        
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("CentralWidget")

        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(20, 180, 70, 40))
        self.exitbtn.setObjectName("ExitButton")

        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("MenuBar")

        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("FileMenu")

        self.savebtn = QtWidgets.QAction(window)
        self.savebtn.setObjectName("SaveButton")

        self.filemenu.addAction(self.savebtn)
        self.menubar.addAction(self.filemenu.menuAction())

        window.setMenuBar(self.menubar)
