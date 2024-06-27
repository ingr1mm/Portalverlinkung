import webbrowser
import backend.controller as controller
from PyQt5.QtWidgets import QWidget, QPushButton


class pushButton:
    def __init__(self):
        self.widgetSize=QWidget.size(100, 100)

    def executeLink(self):
        webbrowser.open(controller.specifiedLink)        
        
class pushButton1(pushButton):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName(controller.namePortal1)
        self.specifiedLink=controller.linkPortal1

    # beim Klick auf den Button wird die Internetadresse der Variablen linkPortal1 aus backend.py aufgerufen

class pushButton2(pushButton):
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetName=QWidget.setObjectName(controller.namePortal2)
        self.specifiedLink=controller.linkPortal2
