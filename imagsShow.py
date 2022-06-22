from email.charset import QP
import imp
from re import T
from time import sleep
from tkinter.tix import Tree
from typing_extensions import Self
from PyQt6.QtWidgets import QWidget,QGraphicsView,QHBoxLayout,QVBoxLayout,QSizePolicy,QScrollArea,QPushButton,QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize,Qt,QRectF
import time
import numpy
class showIMG(QWidget):
    def __init__(self,filenames):
        super().__init__()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.ew=self.geometry()
        self.setWindowState(Qt.WindowState.WindowNoState)
        self.setGeometry(60,100,600,600)
        self.__pre_img = QPixmap(filenames)
        if self.__pre_img.height() >=self.ew.height():
            self.setWindowState(Qt.WindowState.WindowMaximized)
        self.sase=QGraphicsScene()
        self.mainPhoto=QGraphicsView(self.sase)
        self.__img=QGraphicsPixmapItem(self.__pre_img)
        self.sase.addItem(self.__img)

        self.__la = QVBoxLayout()
        self.__buttons = QPushButton("Full Image")
        self.__buttons1 = QPushButton("Fit Full")
        self.__buttons.clicked.connect(self.full_click)
        self.__buttons1.clicked.connect(self.fitFulll_click)
        if len(filenames)<=10:
            self.__strs=filenames
        else:
            self.__strs=filenames[0:9]+"***"+filenames[-1:-22:-1][::-1]
        self.__layout = QHBoxLayout()
        self.__la.addLayout(self.__layout)
        self.setWindowTitle("Show img :"+self.__strs)
        self.setLayout(self.__la)
        self.__layout.addWidget(self.mainPhoto)
        self.__layout2 = QHBoxLayout()
        self.__layout2.addWidget(self.__buttons1)
        self.__layout2.addWidget(self.__buttons)
        self.__la.addLayout(self.__layout2)
        self.resizeEvent = self.__autoREsize
        self.mainPhoto.moveEvent =self.a
        self.wheelEvent =self.WheelEvents
        self.mainPhoto.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.mainPhoto.fitInView(self.sase.sceneRect(),Qt.AspectRatioMode.IgnoreAspectRatio)
    def a(self,s):
        self.pointMouse =s
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
        self.mainPhoto.fitInView(QRectF(self.ew),Qt.AspectRatioMode.KeepAspectRatioByExpanding)
    def fitFulll_click(self):
        self.mainPhoto.fitInView(self.sase.sceneRect(),Qt.AspectRatioMode.KeepAspectRatioByExpanding)