import imagsShow
from PyQt6.QtWidgets import QWidget,QListWidget,QHBoxLayout,QMessageBox
from PyQt6.QtCore import Qt
import os
class applist_image(QWidget):
    def __init__(self,Path=None):
        super().__init__()
        #Create widget
        self.__next =self.__checkPath(path=Path)
        self.__layout = QHBoxLayout()
        self.__list = QListWidget()
        self.__PATH = Path
        self.Works(self.__next)
        #setlaout
        self.setLayout(self.__layout)
        self.__list.itemClicked.connect(self.clicks_list)

        self.__layout.addWidget(self.__list)
    def Works(self,bools):
        self.__dirs={}
        if bools==1:
            for file in os.listdir(self.__PATH):
                self.__list.addItem(file)
                self.__dirs[file] = name_and_path(file,self.__PATH)
        elif bools==2:
            self.e =imagsShow.showIMG(self.__PATH)
            self.e.show()
            for file in os.listdir(os.path.dirname(self.__PATH)):
                self.__list.addItem(file)
                self.__dirs[file] = name_and_path(file,os.path.dirname(self.__PATH))
    def clicks_list(self,ss):
        if os.path.exists(self.__dirs[self.__list.currentItem().text()].getFilePath()):
            self.e =imagsShow.showIMG(self.__dirs[self.__list.currentItem().text()].getFilePath())
            self.e.show()
        else:
            QMessageBox.warning(self,"Error",'หาไฟล์ไม่เจอ',QMessageBox.StandardButton.Ok)

        

    def __checkPath(self,path):
        if path!=None:
            if os.path.isdir(os.path.realpath(path)):
                return 1
            else:
                return 2
        else:
            return False

class name_and_path:
    def __init__(self,filename:str ,path:str) -> None:
        self.__Files = filename
        self.__path = path
    def getFilename(self):
        return self.__Files
    def getPath(self):
        return self.__path
    def getFilePath(self):
        return os.path.join(self.__path,self.__Files)
    def __str__(self):
        return "สร้าง type ใหม่ ไว้ง่ายต่อทำงาน ส่งค่าง่ายกว่า"
