from PyQt6.QtWidgets import *
from logic import *
import sys

def main():
   app = QtWidgets.QApplication(sys.argv)
   mainWindow = gameLogic()
   mainWindow.show()
   sys.exit(app.exec())
   
   
if __name__ == "__main__":
    main()
