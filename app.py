from PyQt6.QtWidgets import QApplication
import sys
import Windows

if __name__=='__main__':
    App = QApplication(sys.argv)
    main = Windows.window()
    main.show()
    sys.exit(App.exec())
