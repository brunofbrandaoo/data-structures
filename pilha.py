from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.components()

        self.show()
        
        return
    
    def components(self):

        self.setWindowTitle("PILHA")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.number_label = QLabel("Número:")
        self.layout.addWidget(self.number_label)
        self.number_box = QLineEdit()
        self.layout.addWidget(self.number_box)

        self.add_button = QPushButton("Adicionar na pilha")
        self.add_button.clicked.connect(self.push)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover da pilha")
        self.remove_button.clicked.connect(self.pop)
        self.layout.addWidget(self.remove_button)

        self.topo_button = QPushButton("Consulta topo da pilha")
        self.topo_button.clicked.connect(self.consulta)
        self.layout.addWidget(self.topo_button)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        
        self.layout.addWidget(self.table)

        return

    ### AUXS ###
    def animate(self, st = 0.7):
        self.table.repaint()
        self.table.viewport().update()
        time.sleep(st)

        return
    
    def remove_color(self):
        self.table.item(0, 0).setBackground( QColor("transparent") )
        self.table.item(0, 1).setBackground( QColor("transparent") )

        return
    
    def clear(self):
        self.table.clear()
        
        return
    
    
    ### METHODS PILHA ###
    # FIRST IN, LAST OUT
    def push(self):        
        if self.number_box.text() == "":
            print("Digite um número")
            return
        
        number = self.number_box.text()
        
        if self.table.columnCount() == 0:
            self.table.insertColumn(0)
            self.table.insertColumn(1)
            self.table.insertRow(0)
            self.table.setItem(0, 0, QTableWidgetItem(number) )
            self.animate()
            self.table.setItem(0, 1, QTableWidgetItem("<-- TOPO") )
            self.animate()
            self.table.item(0, 1).setBackground( QtGui.QColor(169 ,169, 169) )
            self.animate()
            self.table.item(0, 0).setBackground( QtGui.QColor(169 ,169, 169) )
            self.animate()
            self.table.item(0, 0).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.table.item(0, 1).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.animate()

        else:
            self.remove_color()
            
            self.table.insertRow(0)
            self.animate()

            [ self.table.setItem(x, 1, QTableWidgetItem("")) for x in range(1, self.table.rowCount()) ]


            self.table.setItem(0, 0, QTableWidgetItem(number))
            self.table.setItem(0, 1, QTableWidgetItem("<-- TOPO") )
            self.animate()
            self.table.item(0, 1).setBackground( QtGui.QColor(169 ,169, 169) )
            self.animate()
            self.table.item(0, 0).setBackground( QtGui.QColor(169 ,169, 169) )
            self.animate()
            self.table.item(0, 0).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.table.item(0, 1).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.animate()

        return
    
    def pop(self):
        if self.table.rowCount() == 0:
            print("Pilha vazia")
            return

        self.remove_color()
        self.table.item(0, 0).setBackground( QtGui.QColor(255, 50, 50) )
        self.table.item(0, 1).setBackground( QtGui.QColor(255, 50, 50) )
        self.animate()
        self.table.removeRow(0)
        if self.table.rowCount() == 0: 
            self.table.removeColumn(0)
            self.table.removeColumn(0)
            return
        
        self.table.setItem(0, 1, QTableWidgetItem("<-- TOPO") )
        self.table.item(0, 1).setBackground( QtGui.QColor(155, 100, 100) )
        self.animate()
        self.table.item(0, 0).setBackground( QtGui.QColor(155, 100, 100) )
        self.animate()
        self.remove_color()
                
        return 
    
    def consulta(self):
        self.remove_color()
        self.table.item(0, 1).setBackground( QtGui.QColor(169 ,169, 169) )
        self.animate()
        self.table.item(0, 0).setBackground( QtGui.QColor(169 ,169, 169) )
        self.animate()
        self.table.item(0, 1).setBackground( QtGui.QColor(173 ,255 , 47) )
        self.animate()
        self.remove_color()

        return
        
### MAIN ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet('.QListWidget, .QLabel, .QPushButton, .QLineEdit, .QTableWidgetItem, .QTableWidget { font-size: 14pt;}')
    sys.exit(app.exec_())    