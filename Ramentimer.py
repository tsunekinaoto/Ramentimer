# -*- coding: utf-8 -*-
import sys
import PySide.QtGui
import PySide.QtCore
import PySide.QtUiTools


class MainForm(PySide.QtGui.QDialog):
	def __init__(self, parent=None):
		super(MainForm, self).__init__(parent)
		self.ui = PySide.QtUiTools.QUiLoader().load('./MainDialog.ui')
        self.establishConnection()
        self.initUI()

    def initUI(self):
        self.is_run = False
        self.count = 180
        self.timer = PySide.QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.countdown)
        self.ui.LCDTimer.display(self.count)

    def countdown(self):
        if self.count > 0:
            self.count -= 1
            self.updateLCD()

    def updateLCD(self):
        self.ui.LCDTimer.display(self.count)
        self.ui.LCDTimer.update()

    def pushStartStopButton(self):
        if self.is_run:
            self.timer.stop()
            self.is_run = False
        else:
            self.timer.start()
            self.is_run = True

    def pushResetButton(self):
        self.initTimer()
        self.updateLCD()

    def establishConnection(self):
        self.ui.StartStopButton.clicked.connect(self.pushStartStopButton)
        self.ui.ResetButton.clicked.connect(self.pushResetButton)

if __name__ == '__main__':
	app = PySide.QtGui.QApplication(sys.argv)

	main_form = MainForm()
	main_form.ui.show()

	sys.exit(app.exec_())