from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import frontend.pushButtons as pushButtons
import sys

#Einrichtung des MainFrames, in welchem die Buttons angezeigt werden
class mainWindow(QMainWindow):
    def __init__(self):    
        self.app = QApplication(sys.argv)
        self.window=QWidget()
        self.window.show()
        self.app.exec_()
        self.setWindowTitle('Portalübersicht')

    # Erstellung eines Button-Containers
    def createButtonContainer(self):
        self.buttonContainer=QWidget()
        self.buttonContainer.show()

    # Erstellung der Buttons
    def createButtons(self):
        self.button1=pushButtons.pushButton1()
        self.button2=pushButtons.pushButton2()
        self.button1.show()
        self.button2.show()
