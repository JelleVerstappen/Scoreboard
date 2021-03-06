import configparser
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
config = configparser.ConfigParser()
config.read("config.ini")

wid = QtWidgets.QWidget()
wid.resize(500, 500)
wid.setWindowTitle('Title')
wid.show()

layout=QtWidgets.QFormLayout(wid)

Team_thuis = QtWidgets.QLabel("Team thuis")
home_team = QtWidgets.QTextEdit()
layout.addRow(Team_thuis,home_team)

Team_uit = QtWidgets.QLabel("Team uit")
away_team = QtWidgets.QTextEdit()
layout.addRow(Team_uit, away_team)

Logo_thuis = QtWidgets.QLabel("Logo thuis")
home_logo  = QtWidgets.QTextEdit()
layout.addRow(Logo_thuis,home_logo)

Logo_uit = QtWidgets.QLabel("Logo uit")
away_logo = QtWidgets.QTextEdit()
layout.addRow(Logo_uit, away_logo)

Save = QtWidgets.QPushButton('Save', wid)
layout.addWidget(Save)
Cancel = QtWidgets.QPushButton('Cancel', wid)
layout.addWidget(Cancel)

def Saved():
    config["TeamA"]["naam"] = home_team.toPlainText()
    config["TeamB"]["naam"] = away_team.toPlainText()
    config["TeamA"]["logo"] = home_logo.toPlainText()
    config["TeamB"]["logo"] = away_logo.toPlainText()
    configfile = open("config.ini", "w")
    config.write(configfile)
    print("Saved")

def Cancelled():
    print("Cancelled")

Save.clicked.connect(Saved)
Cancel.clicked.connect(Cancelled)


app.exec_()