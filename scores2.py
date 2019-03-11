from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import json
import os
import time

event = {}
matches = {}
teams = {}


class MatchList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.hboxes = []
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.show()

    def createHbox(self, name):
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel(name.split("-")[-2], self))
        hbox.addStretch(1)
        hbox.addWidget(QLabel('Edit:', self))
        detailedButton = QPushButton('Detailed')
        detailedButton.clicked.connect(lambda: self.detailedWindow(matches[name]))
        generalButton = QPushButton('General')
        generalButton.clicked.connect(lambda: self.generalWindow(matches[name]))
        hbox.addWidget(detailedButton)
        hbox.addWidget(generalButton)
        self.hboxes.append(hbox)

    def createVbox(self):
        for hbox in self.hboxes:
            self.vbox.addLayout(hbox)

    def detailedWindow(self, data):
        print("Requesting detailed data for " + data['matchid'])

    def generalWindow(self, data):
        print("Requesting general data for " + data['matchid'])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusLabel = QLabel('Ready', self)
        self.statusbar.addPermanentWidget(self.statusLabel, stretch=0)

        self.menubar = self.menuBar()

        fileMenu = self.menubar.addMenu('&File')

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.confirmExit)

        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open match data')
        openAction.triggered.connect(self.openMatch)

        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        self.matchList = MatchList()
        self.scrollarea = QScrollArea()
        self.scrollarea.setWidget(self.matchList)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollarea.setWidgetResizable(True)
        self.setCentralWidget(self.scrollarea)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Scores Application')
        self.show()

    def openMatch(self, e):
        global matches
        global teams
        global event
        self.statusLabel.setText('Loading...')
        fname = str(QFileDialog.getExistingDirectory(self, 'Open folder', os.path.join(os.getcwd(), "data")))
        if fname:
            try:
                f = open(os.path.join(fname, "event.json"), 'r')
                with f:
                    event = json.loads(f.read())
            except json.decoder.JSONDecodeError as error:
                self.errorMessage(error, "File selected is not a valid json file.")
                return
            except FileNotFoundError as error:
                self.errorMessage(error, "File not found.")
                return

            try:
                f = open(os.path.join(fname, "matches.json"), 'r')
                with f:
                    matches = json.loads(f.read())
            except json.decoder.JSONDecodeError as error:
                self.errorMessage(error, "File selected is not a valid json file.")
                return
            except FileNotFoundError as error:
                self.errorMessage(error, "File not found.")
                return

            try:
                f = open(os.path.join(fname, "teams.json"), 'r')
                with f:
                    teams = json.loads(f.read())
            except json.decoder.JSONDecodeError as error:
                self.errorMessage(error, "File selected is not a valid json file.")
                return
            except FileNotFoundError as error:
                self.errorMessage(error, "File not found.")
                return

            if matches != None:
                self.matchIds = [match for match in matches]
                for matchid in self.matchIds:
                    self.matchList.createHbox(matchid)
                self.matchList.createVbox()

            self.statusLabel.setText('Event: ' + str("-".join(self.matchIds[0].split('-')[:3])) + ' - Matches: ' + str(len(self.matchIds)) + ' - Ready')
        else:
            self.statusLabel.setText('Ready')

    def errorMessage(self, error, message):
        self.statusLabel.setText("Error! - Ready")
        self.errorDialog = QMessageBox()
        self.errorDialog.setIcon(QMessageBox.Critical)
        self.errorDialog.setText(str(message))
        self.errorDialog.setInformativeText(str(error))
        self.errorDialog.setWindowTitle("Error")
        self.errorDialog.show()

    def closeEvent(self, e):
        self.confirmExit(e)

    def confirmExit(self, e):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                e.accept()
            except AttributeError:
                qApp.quit()
        else:
            try:
                e.ignore()
            except AttributeError:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
