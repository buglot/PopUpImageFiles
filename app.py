from PyQt6.QtWidgets import QApplication
import sys
import Windows
import os
if __name__=='__main__':
    try:
        a=sys.argv[1]
    except:
        a=None   
    App = QApplication(sys.argv)
    main = Windows.window(a)
    main.show()
    sys.exit(App.exec())
    
    
