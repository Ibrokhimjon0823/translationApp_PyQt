from PySide2 import QtCore, QtGui, QtWidgets
from mainui import Ui_MainWindow

from dialogui import Ui_Dialog

class OptionsDialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(OptionsDialog, self).changeEvent(event)

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.translator = QtCore.QTranslator(self)
        self.actionConfigure.triggered.connect(self.showdialog)
        self.menuLanguage.triggered.connect(self.change_lang)
        # set translation for each submenu
        self.actionChinese.setData('zh_CN.qm')
        self.actionRussian.setData('zh_RU.qm')
        self.actionUzbek.setData('zh_UZ.qm')

    @QtCore.Slot()
    def showdialog(self):
        dlg = OptionsDialog(self)
        dlg.exec_()

    @QtCore.Slot(QtWidgets.QAction)
    def change_lang(self, action):
        QtCore.QCoreApplication.instance().removeTranslator(self.translator)
        if self.translator.load(action.data()):
            QtCore.QCoreApplication.instance().installTranslator(self.translator)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)
