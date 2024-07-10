import sys
import webbrowser
import pandas as pd
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

# Einlesen der Excel-Datei. Falls der Pfad angepasst werden muss, dann nur den Pfad in den Klammern ändern (r'...') bleibt gleich.
df = pd.read_excel(r'Pfad der Excel-Datei.xlsx')

class PortalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('SensoApp')
        self.setGeometry(100, 100, 600, 600)  # Setzen der Fenstergröße
        layout = QVBoxLayout()

        # Hinzufügen der Buttons über Auslesen der Werte in der Excel-Datei
        for index, row in df.iterrows():
            # Erstellen des Buttons mit dem Portalnamen
            button = QPushButton(row['Portalname'], self)
            # Falls eine Farbe in der Excel-Datei angegeben ist, wird diese als Hintergrundfarbe des Buttons gesetzt
            button_color = row['Farbe'] if 'Farbe' in row and pd.notna(row['Farbe']) else '#4CAF50'
            # Setzen der Hintergrundfarbe, Schriftfarbe und Schriftgröße des Buttons
            button.setStyleSheet(f"background-color: {button_color}; color: white; font-size: 20px;")
            # Verknüpfen des Buttons mit der Methode open_link, um den Link zu öffnen
            button.clicked.connect(lambda checked, typ=row['Typ'], runtime=row['Runtime'], link=row['Link']: self.open_link(typ, runtime, link))
            layout.addWidget(button)
        
        self.setLayout(layout)
        # Setzen der Hintergrundfarbe des Fensters
        self.setStyleSheet("background-color: #f0f0f0;")  
        self.show()
    
    def open_link(self, typ, runtime, link):        

        # Öffnen des Links je nach Typ
        if typ == 'java':      
            # Falls es sich um eine Java Web Start-Anwendung handelt      
            command = f'"{runtime}" "{link}"'
            try:
                subprocess.Popen(command, shell=True)
            except Exception as e:
                print(f"Java Web App konnte nicht gestartet werden: {e}")
        elif typ == 'web':
            # Falls es sich um eine Web-URL handelt
            if not link.startswith(('http://', 'https://')):
                link = 'http://' + link            
            try:
                webbrowser.open(link)
            except webbrowser.Error as e:
                print(f"URL konnte nicht gestartet werden: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PortalApp()
    sys.exit(app.exec_())
