from PyQt6.QtWidgets import QMainWindow,QMenuBar,QFileDialog
from PyQt6.QtGui import QAction
import inList
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PopUp Images")
        self.setGeometry(0,0,200,300)
        #make munubar
        self.__menubar = QMenuBar()
        self.__menu_File = self.__menubar.addMenu("File")
        self.__menubar.addMenu(self.__menu_File)
        #in menu File

            #files
        self.__inFile_file = QAction('Files')
        self.__inFile_file.triggered.connect(self.__Openfiles)
            #exit
        self.__inFile_exit = QAction('Exit 5')
        self.__inFile_exit.triggered.connect(self.__eixt)

            #add ลงไป ลง menu File
        self.__menu_File.addActions((self.__inFile_file,self.__inFile_exit))
        self.setMenuBar(self.__menubar)
        self.setCentralWidget(inList.applist_image())
    def __Openfiles(self):
        o = QFileDialog()
        a= o.getExistingDirectory(self,'Open dir',"",QFileDialog.Option.ShowDirsOnly)
        self.setCentralWidget(inList.applist_image(a))
        print(a)
    def __eixt(self):
        exit()