from PyQt6.QtWidgets import QApplication
import sys
import Windows
import os
if __name__=='__main__':
    print(os.path.realpath('__file__'))
    App = QApplication(sys.argv)
    main = Windows.window()
    main.show()
    sys.exit(App.exec())
    
    
