from PyQt5.QtWidgets import QApplication, QWidget
import frontendPushButtons
import sys

#Einrichtung des MainFrames, in welchem die Buttons angezeigt werden
class mainFrame:
    def __init__(self):    
        # super(mainFrame, self).__init__()  
        self.setWindowTitle("Portalzugänge für Senso")
        
        self.app = QApplication(sys.argv)
        self.window=QWidget()
        self.window.show()
        self.app.exec_()


        #Buttons werden erstellt
        self.button1=frontendPushButtons.pushButton1()
        self.button2=frontendPushButtons.pushButton2()