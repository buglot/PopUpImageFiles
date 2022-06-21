from email.charset import QP
import imp
from PyQt6.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout
from PyQt6.QtGui import QPixmap
class showIMG(QWidget):
    def __init__(self,filenames):
        super().__init__()
        self.__pre_img = QPixmap(filenames)

        if len(filenames)<=10:
            self.__strs=filenames
        else:
            self.__strs=filenames[0:9]+"***"+filenames[-1:-5]
        self.__layout = QHBoxLayout()
        self.setWindowTitle("Show img"+self.__strs)
        self.setLayout(self.__layout)
        self.__img=QLabel()
        self.__img.setPixmap(self.__pre_img.scaled(200,200))