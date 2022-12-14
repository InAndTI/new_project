from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from pars import translate
from bd import *
import random


class Ui_MainWindow(object):
    def setupUi(self, Settings):
        self.error = 0
        Settings.setObjectName("MainWindow")
        Settings.resize(819, 570)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 80, 55, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 171, 256, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 360, 190, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 480, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 410, 190, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 70, 55, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_verb = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_verb.setGeometry(QtCore.QRect(610, 150, 93, 28))
        self.pushButton_verb.setObjectName("pushButton_verb")
        self.pushButton_word = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_word.setGeometry(QtCore.QRect(90, 150, 93, 28))
        self.pushButton_word.setObjectName("pushButton_word")
        self.pushButton_word.clicked.connect(self.bd)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 460, 190, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 360, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 410, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(280, 460, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 420, 55, 16))
        self.label_12.setObjectName("label_12")
        self.spinBox_start_verb = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_start_verb.setGeometry(QtCore.QRect(570, 210, 42, 22))
        self.spinBox_start_verb.setMaximum(1001)
        self.spinBox_start_verb.setSingleStep(20)
        self.spinBox_start_verb.setObjectName("spinBox_start_verb")
        self.spinBox_amount_verb = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_amount_verb.setGeometry(QtCore.QRect(680, 210, 42, 22))
        self.spinBox_amount_verb.setMinimum(50)
        self.spinBox_amount_verb.setMaximum(1002)
        self.spinBox_amount_verb.setSingleStep(50)
        self.spinBox_amount_verb.setObjectName("spinBox_amount_verb")
        self.spinBox_start_word = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_start_word.setGeometry(QtCore.QRect(60, 210, 42, 22))
        self.spinBox_start_word.setMaximum(999)
        self.spinBox_start_word.setSingleStep(20)
        self.spinBox_start_word.setObjectName("spinBox_start_word")
        self.spinBox_amount_word = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_amount_word.setGeometry(QtCore.QRect(150, 210, 42, 22))
        self.spinBox_amount_word.setMinimum(50)
        self.spinBox_amount_word.setMaximum(1000)
        self.spinBox_amount_word.setSingleStep(50)
        self.spinBox_amount_word.setObjectName("spinBox_amount_word")
        self.translate = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(580, 380, 191, 41))
        self.translate.setObjectName("translate")
        self.engl_word = QtWidgets.QLineEdit(self.centralwidget)
        self.engl_word.setGeometry(QtCore.QRect(250, 260, 201, 41))
        self.engl_word.setText("engl_word")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.google)
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 26))
        self.menubar.setObjectName("menubar")
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def google(self):
        self.label_5.setText(QtCore.QCoreApplication.translate("MainWindow", translate(self.translate.toPlainText())))

    def bd(self):
        self.word_dict = the_word(self.spinBox_start_word.text(), self.spinBox_amount_word.text())
        self.textBrowser.setHtml(
            QtCore.QCoreApplication.translate("MainWindow", random.choice(list(self.word_dict.keys()))))
        self.engl_word.setText("")
        self.label_12.setText(
            QtCore.QCoreApplication.translate("MainWindow", str(len(self.word_dict.keys()))))

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "verb"))
        self.textBrowser.setHtml(_translate("MainWindow", "ru_word"))
        self.label_4.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "answer"))
        self.label_6.setText(_translate("MainWindow", "2"))
        self.label_7.setText(_translate("MainWindow", "word"))
        self.pushButton_verb.setText(_translate("MainWindow", "start"))
        self.pushButton_word.setText(_translate("MainWindow", "start"))
        self.label_8.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "ru"))
        self.label_10.setText(_translate("MainWindow", "en_your"))
        self.label_11.setText(_translate("MainWindow", "trye_en"))
        self.label_12.setText(_translate("MainWindow", "num"))
        self.translate.setPlainText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "translate"))


class Settings(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == 13:
            self.test()

    def test(self):
        if self.engl_word.text() in self.word_dict[self.textBrowser.toPlainText()]:
            self.word_dict[self.textBrowser.toPlainText()].remove(self.engl_word.text())
            self.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", self.textBrowser.toPlainText()))
            self.label_6.setText(QtCore.QCoreApplication.translate("MainWindow", self.engl_word.text()))
            self.label_8.setText(QtCore.QCoreApplication.translate("MainWindow", self.engl_word.text()))
            self.engl_word.setText("")
            self.label_4.setStyleSheet("color: rgb(25, 255, 0);")
            self.label_6.setStyleSheet("color: rgb(25, 255, 0);")
            self.label_8.setStyleSheet("color: rgb(25, 255, 0);")
            self.label_9.setStyleSheet("color: rgb(25, 255, 0);")
            self.label_10.setStyleSheet("color: rgb(25, 255, 0);")
            self.label_11.setStyleSheet("color: rgb(25, 255, 0);")
        else:
            self.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", self.textBrowser.toPlainText()))
            self.label_6.setText(QtCore.QCoreApplication.translate("MainWindow", self.engl_word.text()))
            self.label_8.setText(
                QtCore.QCoreApplication.translate("MainWindow", ','.join(self.word_dict[self.textBrowser.toPlainText()])))
            self.textBrowser.setHtml(
                QtCore.QCoreApplication.translate("MainWindow", random.choice(list(self.word_dict.keys()))))
            self.engl_word.setText("")
            self.label_4.setStyleSheet("color: rgb(255, 0, 4);")
            self.label_6.setStyleSheet("color: rgb(255, 0, 4);")
            self.label_8.setStyleSheet("color: rgb(255, 0, 4);")
            self.label_9.setStyleSheet("color: rgb(255, 0, 4);")
            self.label_10.setStyleSheet("color: rgb(255, 0, 4);")
            self.label_11.setStyleSheet("color: rgb(255, 0, 4);")
            self.error += 1

        if not len(self.word_dict[self.textBrowser.toPlainText()]):
            self.word_dict.pop(self.textBrowser.toPlainText())
            if len(self.word_dict.keys()):
                self.textBrowser.setHtml(
                    QtCore.QCoreApplication.translate("MainWindow", random.choice(list(self.word_dict.keys()))))
                self.label_12.setText(
                    QtCore.QCoreApplication.translate("MainWindow", str(len(self.word_dict.keys()))))
            else:
                self.textBrowser.setHtml(
                    QtCore.QCoreApplication.translate("MainWindow", ""))
                self.label_12.setText(QtCore.QCoreApplication.translate("MainWindow", str(self.error)))
                self.error = 0
            self.engl_word.setText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Settings()
    ui.show()
    sys.exit(app.exec_())
