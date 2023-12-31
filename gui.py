# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1100, 700)
        StackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        StackedWidget.setMaximumSize(QtCore.QSize(10000, 10000))
        StackedWidget.setStyleSheet("")
        self.mainScreen = QtWidgets.QWidget()
        self.mainScreen.setMinimumSize(QtCore.QSize(1100, 700))
        self.mainScreen.setMaximumSize(QtCore.QSize(1100, 700))
        self.mainScreen.setSizeIncrement(QtCore.QSize(0, 0))
        self.mainScreen.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.mainScreen.setStyleSheet("background-color: rgb(97,42,14)")
        self.mainScreen.setObjectName("mainScreen")
        self.GameTitle = QtWidgets.QLabel(parent=self.mainScreen)
        self.GameTitle.setGeometry(QtCore.QRect(50, 10, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(33)
        self.GameTitle.setFont(font)
        self.GameTitle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.GameTitle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.GameTitle.setAutoFillBackground(False)
        self.GameTitle.setStyleSheet("color: rgb(138, 170, 121)")
        self.GameTitle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.GameTitle.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.GameTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GameTitle.setObjectName("GameTitle")
        self.OutputText = QtWidgets.QTextBrowser(parent=self.mainScreen)
        self.OutputText.setGeometry(QtCore.QRect(40, 100, 1021, 311))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(12)
        self.OutputText.setFont(font)
        self.OutputText.setStyleSheet("color: rgb(138, 170, 121);")
        self.OutputText.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.OutputText.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.OutputText.setObjectName("OutputText")
        self.InputText = QtWidgets.QLineEdit(parent=self.mainScreen)
        self.InputText.setGeometry(QtCore.QRect(40, 430, 951, 111))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(12)
        self.InputText.setFont(font)
        self.InputText.setStyleSheet("color: rgb(65, 74, 41);\n"
"background-color: rgb(209, 163, 113);")
        self.InputText.setText("")
        self.InputText.setFrame(False)
        self.InputText.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.InputText.setObjectName("InputText")
        self.statusButton = QtWidgets.QPushButton(parent=self.mainScreen)
        self.statusButton.setGeometry(QtCore.QRect(880, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(14)
        self.statusButton.setFont(font)
        self.statusButton.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99,111,63)")
        self.statusButton.setObjectName("statusButton")
        self.mapButton = QtWidgets.QPushButton(parent=self.mainScreen)
        self.mapButton.setGeometry(QtCore.QRect(510, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(16)
        self.mapButton.setFont(font)
        self.mapButton.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99,111,63)")
        self.mapButton.setObjectName("mapButton")
        self.inventoryButton = QtWidgets.QPushButton(parent=self.mainScreen)
        self.inventoryButton.setGeometry(QtCore.QRect(100, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(12)
        self.inventoryButton.setFont(font)
        self.inventoryButton.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99,111,63)")
        self.inventoryButton.setObjectName("inventoryButton")
        self.submitInputButton = QtWidgets.QPushButton(parent=self.mainScreen)
        self.submitInputButton.setGeometry(QtCore.QRect(1000, 430, 93, 111))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        self.submitInputButton.setFont(font)
        self.submitInputButton.setStyleSheet("color: rgb(65, 74, 41);\n"
"background-color: rgb(209, 163, 113);")
        self.submitInputButton.setObjectName("submitInputButton")
        StackedWidget.addWidget(self.mainScreen)
        self.InventoryScreen = QtWidgets.QWidget()
        self.InventoryScreen.setMinimumSize(QtCore.QSize(1100, 700))
        self.InventoryScreen.setMaximumSize(QtCore.QSize(1100, 700))
        self.InventoryScreen.setStyleSheet("background-color: rgb(97,42,14)")
        self.InventoryScreen.setObjectName("InventoryScreen")
        self.inventoryTitle = QtWidgets.QLabel(parent=self.InventoryScreen)
        self.inventoryTitle.setGeometry(QtCore.QRect(50, 20, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(33)
        self.inventoryTitle.setFont(font)
        self.inventoryTitle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.inventoryTitle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.inventoryTitle.setAutoFillBackground(False)
        self.inventoryTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(99, 111, 63);")
        self.inventoryTitle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.inventoryTitle.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.inventoryTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inventoryTitle.setObjectName("inventoryTitle")
        self.inventoryChangeEButton = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.inventoryChangeEButton.setGeometry(QtCore.QRect(50, 130, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(14)
        self.inventoryChangeEButton.setFont(font)
        self.inventoryChangeEButton.setToolTip("")
        self.inventoryChangeEButton.setStyleSheet("color: rgb(65, 74, 41);\n"
"background-color: rgb(209, 163, 113);")
        self.inventoryChangeEButton.setObjectName("inventoryChangeEButton")
        self.inventoryChangeMButton = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.inventoryChangeMButton.setGeometry(QtCore.QRect(850, 130, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(14)
        self.inventoryChangeMButton.setFont(font)
        self.inventoryChangeMButton.setToolTip("")
        self.inventoryChangeMButton.setStyleSheet("color: rgb(65, 74, 41);\n"
"background-color: rgb(209, 163, 113);")
        self.inventoryChangeMButton.setObjectName("inventoryChangeMButton")
        self.inventoryChangeCButton = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.inventoryChangeCButton.setGeometry(QtCore.QRect(450, 130, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(14)
        self.inventoryChangeCButton.setFont(font)
        self.inventoryChangeCButton.setToolTip("")
        self.inventoryChangeCButton.setStyleSheet("color: rgb(65, 74, 41);\n"
"background-color: rgb(209, 163, 113);")
        self.inventoryChangeCButton.setObjectName("inventoryChangeCButton")
        self.IButton1 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton1.setGeometry(QtCore.QRect(50, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton1.setFont(font)
        self.IButton1.setToolTip("")
        self.IButton1.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton1.setObjectName("IButton1")
        self.IButton8 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton8.setGeometry(QtCore.QRect(50, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton8.setFont(font)
        self.IButton8.setToolTip("")
        self.IButton8.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton8.setObjectName("IButton8")
        self.IButton15 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton15.setGeometry(QtCore.QRect(50, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton15.setFont(font)
        self.IButton15.setToolTip("")
        self.IButton15.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton15.setObjectName("IButton15")
        self.IButton22 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton22.setGeometry(QtCore.QRect(50, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton22.setFont(font)
        self.IButton22.setToolTip("")
        self.IButton22.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton22.setObjectName("IButton22")
        self.IButton2 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton2.setGeometry(QtCore.QRect(200, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton2.setFont(font)
        self.IButton2.setToolTip("")
        self.IButton2.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton2.setObjectName("IButton2")
        self.IButton16 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton16.setGeometry(QtCore.QRect(200, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton16.setFont(font)
        self.IButton16.setToolTip("")
        self.IButton16.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton16.setObjectName("IButton16")
        self.IButton9 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton9.setGeometry(QtCore.QRect(200, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton9.setFont(font)
        self.IButton9.setToolTip("")
        self.IButton9.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton9.setObjectName("IButton9")
        self.IButton23 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton23.setGeometry(QtCore.QRect(200, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton23.setFont(font)
        self.IButton23.setToolTip("")
        self.IButton23.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton23.setObjectName("IButton23")
        self.IButton3 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton3.setGeometry(QtCore.QRect(350, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton3.setFont(font)
        self.IButton3.setToolTip("")
        self.IButton3.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton3.setObjectName("IButton3")
        self.IButton17 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton17.setGeometry(QtCore.QRect(350, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton17.setFont(font)
        self.IButton17.setToolTip("")
        self.IButton17.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton17.setObjectName("IButton17")
        self.IButton10 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton10.setGeometry(QtCore.QRect(350, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton10.setFont(font)
        self.IButton10.setToolTip("")
        self.IButton10.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton10.setObjectName("IButton10")
        self.IButton24 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton24.setGeometry(QtCore.QRect(350, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton24.setFont(font)
        self.IButton24.setToolTip("")
        self.IButton24.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton24.setObjectName("IButton24")
        self.IButton4 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton4.setGeometry(QtCore.QRect(500, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton4.setFont(font)
        self.IButton4.setToolTip("")
        self.IButton4.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton4.setObjectName("IButton4")
        self.IButton18 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton18.setGeometry(QtCore.QRect(500, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton18.setFont(font)
        self.IButton18.setToolTip("")
        self.IButton18.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton18.setObjectName("IButton18")
        self.IButton11 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton11.setGeometry(QtCore.QRect(500, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton11.setFont(font)
        self.IButton11.setToolTip("")
        self.IButton11.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton11.setObjectName("IButton11")
        self.IButton25 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton25.setGeometry(QtCore.QRect(500, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton25.setFont(font)
        self.IButton25.setToolTip("")
        self.IButton25.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton25.setObjectName("IButton25")
        self.IButton5 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton5.setGeometry(QtCore.QRect(650, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton5.setFont(font)
        self.IButton5.setToolTip("")
        self.IButton5.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton5.setObjectName("IButton5")
        self.IButton19 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton19.setGeometry(QtCore.QRect(650, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton19.setFont(font)
        self.IButton19.setToolTip("")
        self.IButton19.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton19.setObjectName("IButton19")
        self.IButton12 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton12.setGeometry(QtCore.QRect(650, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton12.setFont(font)
        self.IButton12.setToolTip("")
        self.IButton12.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton12.setObjectName("IButton12")
        self.IButton26 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton26.setGeometry(QtCore.QRect(650, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton26.setFont(font)
        self.IButton26.setToolTip("")
        self.IButton26.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton26.setObjectName("IButton26")
        self.IButton6 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton6.setGeometry(QtCore.QRect(800, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton6.setFont(font)
        self.IButton6.setToolTip("")
        self.IButton6.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton6.setObjectName("IButton6")
        self.IButton20 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton20.setGeometry(QtCore.QRect(800, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton20.setFont(font)
        self.IButton20.setToolTip("")
        self.IButton20.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton20.setObjectName("IButton20")
        self.IButton13 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton13.setGeometry(QtCore.QRect(800, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton13.setFont(font)
        self.IButton13.setToolTip("")
        self.IButton13.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton13.setObjectName("IButton13")
        self.IButton27 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton27.setGeometry(QtCore.QRect(800, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton27.setFont(font)
        self.IButton27.setToolTip("")
        self.IButton27.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton27.setObjectName("IButton27")
        self.IButton7 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton7.setGeometry(QtCore.QRect(950, 230, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton7.setFont(font)
        self.IButton7.setToolTip("")
        self.IButton7.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton7.setObjectName("IButton7")
        self.IButton21 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton21.setGeometry(QtCore.QRect(950, 450, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton21.setFont(font)
        self.IButton21.setToolTip("")
        self.IButton21.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton21.setObjectName("IButton21")
        self.IButton14 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton14.setGeometry(QtCore.QRect(950, 340, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton14.setFont(font)
        self.IButton14.setToolTip("")
        self.IButton14.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton14.setObjectName("IButton14")
        self.IButton28 = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.IButton28.setGeometry(QtCore.QRect(950, 560, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(8)
        self.IButton28.setFont(font)
        self.IButton28.setToolTip("")
        self.IButton28.setStyleSheet("background-color: rgb(188, 120, 75);\n"
"color: rgb(99, 111, 63)")
        self.IButton28.setObjectName("IButton28")
        self.closeButton = QtWidgets.QPushButton(parent=self.InventoryScreen)
        self.closeButton.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.closeButton.setObjectName("closeButton")
        StackedWidget.addWidget(self.InventoryScreen)
        self.mapScreen = QtWidgets.QWidget()
        self.mapScreen.setStyleSheet("background-color: rgb(97,42,14)")
        self.mapScreen.setObjectName("mapScreen")
        self.mapTitle = QtWidgets.QLabel(parent=self.mapScreen)
        self.mapTitle.setGeometry(QtCore.QRect(60, 20, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(33)
        self.mapTitle.setFont(font)
        self.mapTitle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.mapTitle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.mapTitle.setAutoFillBackground(False)
        self.mapTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(99, 111, 63);")
        self.mapTitle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.mapTitle.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.mapTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mapTitle.setObjectName("mapTitle")
        self.mapPlaceholder = QtWidgets.QLabel(parent=self.mapScreen)
        self.mapPlaceholder.setGeometry(QtCore.QRect(60, 110, 1001, 561))
        self.mapPlaceholder.setText("")
        self.mapPlaceholder.setObjectName("mapPlaceholder")
        self.closeButton_2 = QtWidgets.QPushButton(parent=self.mapScreen)
        self.closeButton_2.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.closeButton_2.setFont(font)
        self.closeButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.closeButton_2.setObjectName("closeButton_2")
        StackedWidget.addWidget(self.mapScreen)
        self.statusScreen = QtWidgets.QWidget()
        self.statusScreen.setStyleSheet("background-color: rgb(97,42,14)")
        self.statusScreen.setObjectName("statusScreen")
        self.statusTitle = QtWidgets.QLabel(parent=self.statusScreen)
        self.statusTitle.setGeometry(QtCore.QRect(50, 20, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(33)
        self.statusTitle.setFont(font)
        self.statusTitle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.statusTitle.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.statusTitle.setAutoFillBackground(False)
        self.statusTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(99, 111, 63);")
        self.statusTitle.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.statusTitle.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.statusTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.statusTitle.setObjectName("statusTitle")
        self.statusMenu = QtWidgets.QLabel(parent=self.statusScreen)
        self.statusMenu.setGeometry(QtCore.QRect(50, 110, 1001, 561))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(12)
        self.statusMenu.setFont(font)
        self.statusMenu.setStyleSheet("background-color: rgb(209, 163, 113);\n"
"color: rgb(65, 74, 41);")
        self.statusMenu.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.statusMenu.setObjectName("statusMenu")
        self.closeButton_3 = QtWidgets.QPushButton(parent=self.statusScreen)
        self.closeButton_3.setGeometry(QtCore.QRect(1060, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.closeButton_3.setFont(font)
        self.closeButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.closeButton_3.setObjectName("closeButton_3")
        StackedWidget.addWidget(self.statusScreen)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.GameTitle.setText(_translate("StackedWidget", "Tavern Tales"))
        self.OutputText.setHtml(_translate("StackedWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Matura MT Script Capitals\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.statusButton.setText(_translate("StackedWidget", "Status"))
        self.mapButton.setText(_translate("StackedWidget", "Map"))
        self.inventoryButton.setText(_translate("StackedWidget", "Inventory"))
        self.submitInputButton.setText(_translate("StackedWidget", "Submit Input"))
        self.inventoryTitle.setText(_translate("StackedWidget", "Inventory"))
        self.inventoryChangeEButton.setText(_translate("StackedWidget", "Equipment"))
        self.inventoryChangeMButton.setText(_translate("StackedWidget", "Miscellaneous"))
        self.inventoryChangeCButton.setText(_translate("StackedWidget", "Consumables"))
        self.IButton1.setText(_translate("StackedWidget", "S1"))
        self.IButton8.setText(_translate("StackedWidget", "S8"))
        self.IButton15.setText(_translate("StackedWidget", "S15"))
        self.IButton22.setText(_translate("StackedWidget", "S22"))
        self.IButton2.setText(_translate("StackedWidget", "S2"))
        self.IButton16.setText(_translate("StackedWidget", "S16"))
        self.IButton9.setText(_translate("StackedWidget", "S9"))
        self.IButton23.setText(_translate("StackedWidget", "S23"))
        self.IButton3.setText(_translate("StackedWidget", "S3"))
        self.IButton17.setText(_translate("StackedWidget", "S17"))
        self.IButton10.setText(_translate("StackedWidget", "S10"))
        self.IButton24.setText(_translate("StackedWidget", "S24"))
        self.IButton4.setText(_translate("StackedWidget", "S4"))
        self.IButton18.setText(_translate("StackedWidget", "S18"))
        self.IButton11.setText(_translate("StackedWidget", "S11"))
        self.IButton25.setText(_translate("StackedWidget", "S25"))
        self.IButton5.setText(_translate("StackedWidget", "S5"))
        self.IButton19.setText(_translate("StackedWidget", "S19"))
        self.IButton12.setText(_translate("StackedWidget", "S12"))
        self.IButton26.setText(_translate("StackedWidget", "S26"))
        self.IButton6.setText(_translate("StackedWidget", "S6"))
        self.IButton20.setText(_translate("StackedWidget", "S20"))
        self.IButton13.setText(_translate("StackedWidget", "S13"))
        self.IButton27.setText(_translate("StackedWidget", "S27"))
        self.IButton7.setText(_translate("StackedWidget", "S7"))
        self.IButton21.setText(_translate("StackedWidget", "S21"))
        self.IButton14.setText(_translate("StackedWidget", "S14"))
        self.IButton28.setText(_translate("StackedWidget", "S28"))
        self.closeButton.setText(_translate("StackedWidget", "X"))
        self.mapTitle.setText(_translate("StackedWidget", "Map"))
        self.closeButton_2.setText(_translate("StackedWidget", "X"))
        self.statusTitle.setText(_translate("StackedWidget", "Status"))
        self.statusMenu.setText(_translate("StackedWidget", "~Status~"))
        self.closeButton_3.setText(_translate("StackedWidget", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec())
