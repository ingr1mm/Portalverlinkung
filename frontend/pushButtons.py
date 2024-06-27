import webbrowser
import backend.controller as controller
from PyQt5.QtWidgets import QWidget, QPushButton


class pushButton:
    def __init__(self):
        self.widgetType=QPushButton()
        self.widgetSize=QWidget.size(100, 100)        

    def executeLink(self):
        webbrowser.open(controller.specifiedLink)        
        
class pushButton1(pushButton):
    def __init__(self):        
        self.specifiedLink=controller.linkPortal1
        self.specifiedName=controller.namePortal1 
        self.widgetName=QWidget.setObjectName(self.specifiedName)
        self.executeLink(self.specifiedLink)

    # beim Klick auf den Button wird die Internetadresse der Variablen linkPortal1 aus backend.py aufgerufen

class pushButton2(pushButton):
    def __init__(self):        
        self.specifiedLink=controller.linkPortal2
        self.specifiedName=controller.namePortal2 
        self.widgetName=QWidget.setObjectName(self.specifiedName)
        self.executeLink(self.specifiedLink)
