from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout, QHBoxLayout, QTextEdit

class Calc(QMainWindow):
  def __init__(self):
    super().__init__()
    
    # Create base layout stuff
    self.centralwidget = QWidget()
    self.baselayout = QGridLayout()
    self.centralwidget.setLayout(baselayout)
