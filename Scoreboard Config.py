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

game = QtWidgets.QLabel("Naam wedstrijd")
text = QtWidgets.QTextEdit()
layout.addRow(game,text)

Team_thuis = QtWidgets.QLabel("Team thuis")
text2 = QtWidgets.QTextEdit()
layout.addRow(Team_thuis,text2)

Team_uit = QtWidgets.QLabel("Team uit")
text3 = QtWidgets.QTextEdit()
layout.addRow(Team_uit, text3)

Logo_thuis = QtWidgets.QLabel("Logo thuis")
text4 = QtWidgets.QTextEdit()
layout.addRow(Logo_thuis,text4)

Logo_uit = QtWidgets.QLabel("Logo uit")
text5 = QtWidgets.QTextEdit()
layout.addRow(Logo_uit, text5)

Save = QtWidgets.QPushButton('Save', wid)
layout.addWidget(Save)
Cancel = QtWidgets.QPushButton('Cancel', wid)
layout.addWidget(Cancel)

def Saved():
    print("Saved")

def Cancelled():
    print("Cancelled")

Save.clicked.connect(Saved)
Cancel.clicked.connect(Cancelled)

app.exec_()