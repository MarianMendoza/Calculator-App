from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectButtons()
        self.show()

    def connectButtons(self):
        self.buttonClickedList = ["self.ui.button0.clicked.connect(self.clickedNumericButton)","self.ui.button1.clicked.connect(self.clickedNumericButton)"]

        for i in self.buttonClickedList:
            print(self.buttonClickedList[i])

        self.ui.button0.clicked.connect(self.clickedNumericButton)
        self.ui.button1.clicked.connect(self.clickedNumericButton)
        self.ui.button2.clicked.connect(self.clickedNumericButton)
        self.ui.button3.clicked.connect(self.clickedNumericButton)
        self.ui.button4.clicked.connect(self.clickedNumericButton)
        self.ui.button5.clicked.connect(self.clickedNumericButton)
        self.ui.button6.clicked.connect(self.clickedNumericButton)
        self.ui.button7.clicked.connect(self.clickedNumericButton)
        self.ui.button8.clicked.connect(self.clickedNumericButton)
        self.ui.button9.clicked.connect(self.clickedNumericButton)


        return
    
    def clickedNumericButton(self):
        print("Test")



def main():
    app = QApplication(sys.argv)
    instance = Main()
    #instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()