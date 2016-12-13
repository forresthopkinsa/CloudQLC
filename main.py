import sys
from PyQt5 import QtWidgets
from ui.rootwindow import RootWindow

class Main(RootWindow):
    def __init__(self, window):
        RootWindow.__init__(self)
        self.setupui(window)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    running = Main(window)
    window.show()
    sys.exit(app.exec_())
