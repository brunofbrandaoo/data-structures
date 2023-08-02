from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.components()

        self.show()
        
        return
    
    def components(self):

        self.setWindowTitle("FILA")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.number_label = QLabel("Número:")
        self.layout.addWidget(self.number_label)
        self.number_box = QLineEdit()
        self.layout.addWidget(self.number_box)

        self.add_button = QPushButton("Adicionar na fila")
        self.add_button.clicked.connect(self.push)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover da fila")
        self.remove_button.clicked.connect(self.pop)
        self.layout.addWidget(self.remove_button)

        self.topo_button = QPushButton("Consulta topo da fila")
        self.topo_button.clicked.connect(self.consulta)
        self.layout.addWidget(self.topo_button)
        
        self.fila = QListWidget()
        self.fila.setFlow(0)
        self.layout.addWidget(self.fila)

    ### AUXS ###
    def animate(self):
        self.fila.repaint()
        self.fila.viewport().update()
        time.sleep(0.7)

        return

    def remove_color(self):
        for i in range(self.fila.count()):
            self.fila.item(i).setBackground( QColor("transparent") )

        return
    
    def clear(self):
        self.fila.clear()
        
        return
    
    ### METHODS FILA ###
    def push(self):
        if self.number_box.text() == "": 
            return
        
        if self.fila.count() == 0:
            self.fila.addItem("TOPO -->")
            self.animate()
            self.fila.item(0).setBackground( QtGui.QColor(169, 169, 169) )
            self.animate()
            self.fila.addItem( self.number_box.text() )
            self.animate()
            self.fila.item(1).setBackground( QtGui.QColor(169, 169, 169) )
            self.animate()
            self.fila.item(1).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.animate()
            self.remove_color()
        else:
            self.remove_color()    
            self.fila.addItem( self.number_box.text() )
            self.animate()
            self.fila.item(self.fila.count() - 1).setBackground( QtGui.QColor(169, 169, 169) )
            self.animate()
            self.fila.item(self.fila.count() - 1).setBackground( QtGui.QColor(173 ,255 , 47) )
            self.animate()
            self.remove_color()
        
        return
    
    def pop(self):
        self.remove_color() 
        self.animate()
        self.fila.item(0).setBackground( QtGui.QColor(169, 169, 169) )
        self.animate()
        self.fila.item(1).setBackground( QtGui.QColor(169, 169, 169) )        
        self.animate()
        self.fila.item(0).setBackground( QtGui.QColor(255, 0, 0) )
        self.fila.item(1).setBackground( QtGui.QColor(255, 0, 0) )        
        self.animate()
        self.fila.takeItem(1)
        if self.fila.count() == 1:
            self.clear()
            return
        self.animate()
        self.remove_color()
        
        return
    
    def consulta(self):
        self.remove_color()
        self.animate()
        self.fila.item(0).setBackground( QtGui.QColor(169, 169, 169) )
        self.animate()
        self.fila.item(1).setBackground( QtGui.QColor(169, 169, 169) )
        self.animate()
        self.fila.item(0).setBackground( QtGui.QColor(173 ,255 , 47) )
        self.fila.item(1).setBackground( QtGui.QColor(173 ,255 , 47) )
        self.animate()
        self.remove_color()
        
        return
    
### MAIN ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet('.QListWidget, .QLabel, .QPushButton, .QLineEdit { font-size: 14pt;}')
    sys.exit(app.exec_())    
