# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import AgendaApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgendaApp()
    window.show()
    sys.exit(app.exec_())

# gui.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class AgendaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automação de Agenda")
        self.setGeometry(100, 100, 600, 400)
        
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        
        self.label = QLabel("Bem-vindo à Automação de Agenda", self)
        layout.addWidget(self.label)
        
        self.add_event_button = QPushButton("Adicionar Evento", self)
        layout.addWidget(self.add_event_button)
        
        central_widget.setLayout(layout)

# database.py
import sqlite3

def create_db():
    conn = sqlite3.connect("data/agenda.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_event(titulo, data, hora):
    conn = sqlite3.connect("data/agenda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO eventos (titulo, data, hora) VALUES (?, ?, ?)", (titulo, data, hora))
    conn.commit()
    conn.close()

# config.py
APP_NAME = "Automação de Agenda"
DB_PATH = "data/agenda.db"

# requirements.txt
PyQt5
sqlite3
