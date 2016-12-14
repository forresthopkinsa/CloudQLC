from PyQt5 import QtCore, QtGui, QtWidgets

class RootWindow():
    def setupui(self, window):
        window.setObjectName("RootWindow")
        window.resize(400, 400)
        
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("CentralWidget")

        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(20, 320, 70, 40))
        self.exitbtn.setText("Exit")
        self.exitbtn.setObjectName("ExitButton")

        self.pullbtn = QtWidgets.QPushButton(self.centralwidget)
        self.pullbtn.setGeometry(QtCore.QRect(310, 320, 70, 40))
        self.pullbtn.setText("Pull")
        self.pullbtn.setObjectName("PullButton")

        self.pushbtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushbtn.setGeometry(QtCore.QRect(230, 320, 70, 40))
        self.pushbtn.setText("Push")
        self.pushbtn.setObjectName("PushButton")

        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(20, 20, 360, 280))
        self.console.setReadOnly(True)
        self.console.setText("This is the output console")
        self.console.setObjectName("Console")

        self.divider = QtWidgets.QFrame(self.centralwidget)
        self.divider.setGeometry(QtCore.QRect(20, 300, 360, 20))
        self.divider.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider.setObjectName("Divider")

        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("MenuBar")

        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setTitle("File")
        self.filemenu.setObjectName("FileMenu")

        self.savebtn = QtWidgets.QAction(window)
        self.savebtn.setText("Save...")
        self.savebtn.setObjectName("SaveButton")

        self.filemenu.addAction(self.savebtn)
        self.menubar.addAction(self.filemenu.menuAction())

        window.setWindowTitle("Root Window")

        window.setCentralWidget(self.centralwidget)
        window.setMenuBar(self.menubar)
