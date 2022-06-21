from email.charset import QP
import imp
from re import T
from tkinter.tix import Tree
from typing_extensions import Self
from PyQt6.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QSizePolicy,QScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize,Qt
import numpy
class showIMG(QWidget):
    def __init__(self,filenames):
        super().__init__()
        self.setGeometry(0,0,600,600)
        self.__Scroll = QScrollArea()
        self.__pre_img = QPixmap(filenames)
        self.__img=QLabel()
        self.__Scroll.setWidget(self.__img)
        self.__Scroll.setWidgetResizable(True)
        self.__la = QVBoxLayout()
        self.__img.setPixmap(self.__pre_img.scaled(600-5,600-5,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        if len(filenames)<=10:
            self.__strs=filenames
        else:
            self.__strs=filenames[0:9]+"***"+filenames[-1:-5:-1][::-1]
        self.__layout = QHBoxLayout()
        self.__la.addLayout(self.__layout)
        self.setWindowTitle("Show img"+self.__strs)
        self.setLayout(self.__la)
        self.__layout.addWidget(self.__Scroll)
        self.resizeEvent = self.__as
        self.__img.setScaledContents(1)
        self.__img.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
    def __as(self,e):
        print(e.oldSize())