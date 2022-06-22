from PyQt6.QtWidgets import QApplication
import sys
import Windows
import os
if __name__=='__main__':
    print( os.path.dirname("dist"))
    a= os.getcwd()
    if a.lower() ==  __file__.split("app.py")[0].lower():
        a=None    
    App = QApplication(sys.argv)
    main = Windows.window(a)
    main.show()
    sys.exit(App.exec())
    
    
