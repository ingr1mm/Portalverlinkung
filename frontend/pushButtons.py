import webbrowser
import backend.controller as controller
from PyQt5.QtWidgets import QWidget, QPushButton

class pushButton:
    def __init__(self):
        self.widgetType=QPushButton()
        #self.widgetSize=QWidget.size(100, 100)        

    def executeLink(self, link):
        webbrowser.open(link)        
        
class pushButton1(pushButton):
    def __init__(self):        
        self.link=controller.linkPortal1
        self.specifiedName=controller.namePortal1 
        #self.widgetName=QWidget.setObjectName(self.specifiedName)
        self.executeLink(self.link)

class pushButton2(pushButton):
    def __init__(self):        
        self.link=controller.linkPortal2
        #self.specifiedName=controller.namePortal2 
        #self.widgetName=QWidget.setObjectName(self.specifiedName)
        self.executeLink(self.link)

 
