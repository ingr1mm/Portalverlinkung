from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
import frontend.pushButtons as pushButtons
import sys

#Einrichtung des MainFrames, in welchem die Buttons angezeigt werden
class mainWindow(QMainWindow):
    def __init__(self):    
        super().__init__()        
        self.window=QWidget()
        self.setWindowTitle('Portalübersicht')
        self.createButtonContainer()
        self.createButtons()
        self.setCentralWidget(self.widget)

    layout=QVBoxLayout()
    widgets=[
        pushButtons.pushButton1(),
        pushButtons.pushButton2()
    ]

    for widget in widgets:
        layout.addWidget(widget())

    widget = QWidget()
    widget.setLayout(layout)

app = QApplication(sys.argv)
window=mainWindow()
window.show()
app.exec()