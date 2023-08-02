import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configura a janela principal
        self.setWindowTitle('Menu')
        self.setGeometry(0, 0, 1000, 800)
        self.window
        #self.setStyleSheet(f'background-color: #FFFFFF')
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('edmenu3.png');
                background-size: cover;
            }
        """)
        
        
        
        # Cria os botões
        self.btn_lista_sequencial = QPushButton('SEQUENCIAL', self)
        self.btn_lista_sequencial.move(100,200)
        self.btn_lista_sequencial.setFixedSize(200,50)
        self.btn_lista_sequencial.clicked.connect(self.lista_sequencial)
        self.btn_lista_sequencial.setStyleSheet("""
            QPushButton {
                background-color: #add8e6;
                color: #23238E;
                border-style: solid;
                border-width: 2px;
                border-color: #add8e6;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #23238E;
            }
        """)

        
        self.btn_simplesmente_encadeada = QPushButton('LSE', self)
        self.btn_simplesmente_encadeada.move(100, 382)
        self.btn_simplesmente_encadeada.setFixedSize(200,50)
        self.btn_simplesmente_encadeada.clicked.connect(self.lista_simplesmente_encadeada)
        self.btn_simplesmente_encadeada.setStyleSheet("""
            QPushButton {
                background-color: #F5DEB3;
                color: #800000;
                border-style: solid;
                border-width: 2px;
                border-color: #F5DEB3;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #800000;
            }
        """)
        
        self.btn_duplamente_encadeada = QPushButton(QIcon('LDE.png'),'LDE', self)
        self.btn_duplamente_encadeada.move(100, 570)
        self.btn_duplamente_encadeada.setFixedSize(200,50)
        self.btn_duplamente_encadeada.clicked.connect(self.lista_duplamente_encadeada)
        self.btn_duplamente_encadeada.setStyleSheet("""
            QPushButton {
                background-color: #ffb6c1;
                color: #FF0000;
                border-style: solid;
                border-width: 2px;
                border-color: #ffb6c1;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #FF0000;
            }
        """)

        self.btn_pilha = QPushButton('pilha', self)
        self.btn_pilha.move(700,200)
        self.btn_pilha.setFixedSize(200,50)
        self.btn_pilha.clicked.connect(self.pilha)
        self.btn_pilha.setStyleSheet("""
            QPushButton {
                background-color: #EE82EE;
                color: #8B008B;
                border-style: solid;
                border-width: 2px;
                border-color: #EE82EE;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #8B008B;
            }
        """)
        
        self.btn_fila = QPushButton('fila', self)
        self.btn_fila.move(700,382)
        self.btn_fila.setFixedSize(200,50)
        self.btn_fila.clicked.connect(self.fila)
        self.btn_fila.setStyleSheet("""
            QPushButton {
                background-color: #F0E68C;
                color: #FF8C00;
                border-style: solid;
                border-width: 2px;
                border-color: #F0E68C;
                padding: 5px 10px;
                font-family: League Spartan;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                text-shadow: 0.1em 0.1em 0.2em black;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #fff;
                color: #FF8C00;
            }
        """)
        
        
    
    #funções para chamar cada script de cada lista   
    def lista_sequencial(self):
        subprocess.call(['python', 'ListaSequencial.py'])
        
    def lista_simplesmente_encadeada(self):
        subprocess.call(['python', 'LSE.py'])
        
    def lista_duplamente_encadeada(self):
        subprocess.call(['python', 'LDE.py'])
        
    def pilha(self):
        subprocess.call(['python', 'pilha.py'])
        
    def fila(self):
        subprocess.call(['python', 'fila.py'])
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
