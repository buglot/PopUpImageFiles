from PyQt6.QtWidgets import QApplication
import sys
import Windows
import os
if __name__=='__main__':
    a=os.path.realpath("___s")
    a=a.split("___s")[0]
    print()
    if a.lower() ==  __file__.split("app.py")[0].lower():
        a=None    
    App = QApplication(sys.argv)
    main = Windows.window(a)
    main.show()
    sys.exit(App.exec())
    
    
