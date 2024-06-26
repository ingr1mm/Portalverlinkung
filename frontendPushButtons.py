import webbrowser
import backend
from PyQt5.QtWidgets import QWidget, QPushButton


class pushButton:
    def __init__(self):
        self.widgetSize=QWidget.size(100, 100)

class pushButton1(pushButton):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName("pushButton1")

    # beim Klick auf den Button wird die Internetadresse der Variablen linkPortal1 aus backend.py aufgerufen
    def executeLink(backend.linkPortal1):
        webbrowser.open(backend.linkPortal1)        
        
class pushButton2(pushButton):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName("pushButton2")
        self.widgetNumber=2
        self.widgetLink=backend.linkPortal2
