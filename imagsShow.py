from email.charset import QP
import imp
from re import T
from tkinter.tix import Tree
from typing_extensions import Self
from PyQt6.QtWidgets import QWidget,QGraphicsView,QHBoxLayout,QVBoxLayout,QSizePolicy,QScrollArea,QPushButton,QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize,Qt
import numpy
class showIMG(QWidget):
    def __init__(self,filenames):
        super().__init__()
        self.setGeometry(0,0,600,600)
        self.__pre_img = QPixmap(filenames)
        self.sase=QGraphicsScene()
        self.mainPhoto=QGraphicsView(self.sase)
        self.__img=QGraphicsPixmapItem(self.__pre_img)
        self.sase.addItem(self.__img)

        self.__la = QVBoxLayout()
        self.__buttons = QPushButton("Full")
        self.__buttons.clicked.connect(self.full_click)
        if len(filenames)<=10:
            self.__strs=filenames
        else:
            self.__strs=filenames[0:9]+"***"+filenames[-1:-5:-1][::-1]
        self.__layout = QHBoxLayout()
        self.__la.addLayout(self.__layout)
        self.setWindowTitle("Show img"+self.__strs)
        self.setLayout(self.__la)
        self.__layout.addWidget(self.mainPhoto)
        self.__la.addWidget(self.__buttons)
        self.resizeEvent = self.__autoREsize
        self.mainPhoto.fitInView(self.sase.sceneRect(),Qt.AspectRatioMode.KeepAspectRatio)
        self.mainPhoto.moveEvent =self.a
        self.wheelEvent =self.WheelEvents
        self.mainPhoto.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
    def a(self,s):
        self.pointMouse =s
        print(s.pos())
    def WheelEvents(self,event):
        
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor
        self.mainPhoto.setTransformationAnchor(QGraphicsView.ViewportAnchor.NoAnchor)
        self.mainPhoto.setResizeAnchor(QGraphicsView.ViewportAnchor.NoAnchor)
        oldPos = self.mainPhoto.mapToScene(self.pointMouse.pos())
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.mainPhoto.scale(zoomFactor, zoomFactor)
        newPos = self.mainPhoto.mapToScene(self.pointMouse.pos())
        delta = newPos - oldPos
        self.mainPhoto.translate(delta.x(), delta.y())

    def __autoREsize(self,e):
        self.mainPhoto.fitInView(self.sase.sceneRect(),Qt.AspectRatioMode.KeepAspectRatio)
    def full_click(self):
        self.mainPhoto.fitInView(self.sase.sceneRect(),Qt.AspectRatioMode.KeepAspectRatioByExpanding)