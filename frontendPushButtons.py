import webbrowser
import backend
from PyQt5.QtWidgets import QWidget, QPushButton


class pushButton:
    def __init__(self):
        self.widgetSize=QWidget.size(100, 100)

class pushButton1(pushButton, backend.namePortal1, backend.linkPortal1):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName(backend.namePortal1)

    # beim Klick auf den Button wird die Internetadresse der Variablen linkPortal1 aus backend.py aufgerufen
    def executeLink(self):
        webbrowser.open(backend.linkPortal1)        
        
class pushButton2(pushButton, backend.namePortal2, backend.linkPortal2):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName(backend.namePortal2)
        self.widgetNumber=2
        self.widgetLink=backend.linkPortal2
