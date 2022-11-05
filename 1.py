import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(300, 300)


class Settings(QtWidgets.QWidget, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_F:
            self.test()

    def test(self):
        print("Hello world")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Settings()
    MainWindow.show()
    sys.exit(app.exec_())