import sys
from PyQt4 import QtGui, QtCore

class Calc(QtGui.QMainWindow):

    def __init__(self):
        super(Calc,self).__init__()
        self.setGeometry(50,50,220,300)
        self.setWindowTitle('PyCalc')
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.string = ''
        
        self.home()

    def home(self):

        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcd.move(20,20)
        self.lcd.resize(125,50)

        btn1 = QtGui.QPushButton('1', self)   # first argument is the text
        btn1.clicked.connect(self.button1)  # note the lack of parens on method
        btn1.resize(50,50) # sizeHint - automatic sizing
        btn1.move(10,180)    # x and y location

        btn2 = QtGui.QPushButton('2', self)  
        btn2.clicked.connect(self.button2)  
        btn2.resize(50,50) 
        btn2.move(60,180)

        btn3 = QtGui.QPushButton('3', self)  
        btn3.clicked.connect(self.button3)  
        btn3.resize(50,50) 
        btn3.move(110,180)

        btn4 = QtGui.QPushButton('4', self)  
        btn4.clicked.connect(self.button4)  
        btn4.resize(50,50) 
        btn4.move(10,130)

        btn5 = QtGui.QPushButton('5', self)  
        btn5.clicked.connect(self.button5)  
        btn5.resize(50,50) 
        btn5.move(60,130)

        btn6 = QtGui.QPushButton('6', self)  
        btn6.clicked.connect(self.button6)  
        btn6.resize(50,50) 
        btn6.move(110,130)

        btn7 = QtGui.QPushButton('7', self)  
        btn7.clicked.connect(self.button7)  
        btn7.resize(50,50) 
        btn7.move(10,80)

        btn8 = QtGui.QPushButton('8', self)  
        btn8.clicked.connect(self.button8)  
        btn8.resize(50,50) 
        btn8.move(60,80)

        btn9 = QtGui.QPushButton('9', self)  
        btn9.clicked.connect(self.button9)  
        btn9.resize(50,50) 
        btn9.move(110,80)

        btn0 = QtGui.QPushButton('0', self)  
        btn0.clicked.connect(self.button0)  
        btn0.resize(50,50) 
        btn0.move(60,230)

        btnDec = QtGui.QPushButton('.', self)  
        btnDec.clicked.connect(self.decimal)  
        btnDec.resize(50,50) 
        btnDec.move(110,230)

        btnEquals = QtGui.QPushButton('=', self)  
        btnEquals.clicked.connect(self.equals)
        btnEquals.resize(50,50) 
        btnEquals.move(10,230)

        btnAdd = QtGui.QPushButton('+', self)  
        btnAdd.clicked.connect(self.plus)  
        btnAdd.resize(50,50) 
        btnAdd.move(160,230)

        btnSubtract = QtGui.QPushButton('-', self)  
        btnSubtract.clicked.connect(self.minus)  
        btnSubtract.resize(50,50) 
        btnSubtract.move(160,180)

        btnMult = QtGui.QPushButton('x', self)  
        btnMult.clicked.connect(self.mult)  
        btnMult.resize(50,50) 
        btnMult.move(160,130)

        btnDiv = QtGui.QPushButton('/', self)  
        btnDiv.clicked.connect(self.divide)  
        btnDiv.resize(50,50) 
        btnDiv.move(160,80)

        btnClear = QtGui.QPushButton('C', self)  
        btnClear.clicked.connect(self.clear)  
        btnClear.resize(50,50) 
        btnClear.move(160,30)

        # this should always be last
        self.show()

    def button0(self):
        self.string += '0'
        self.lcd.display(self.string)

    def button1(self):
        self.string += '1'
        self.lcd.display(self.string)

    def button2(self):
        self.string += '2'
        self.lcd.display(self.string)

    def button3(self):
        self.string += '3'
        self.lcd.display(self.string)

    def button4(self):
        self.string += '4'
        self.lcd.display(self.string)

    def button5(self):
        self.string += '5'
        self.lcd.display(self.string)
        
    def button6(self):
        self.string += '6'
        self.lcd.display(self.string)

    def button7(self):
        self.string += '7'
        self.lcd.display(self.string)

    def button8(self):
        self.string += '8'
        self.lcd.display(self.string)

    def button9(self):
        self.string += '9'
        self.lcd.display(self.string)

    def mult(self):
        self.val1 = float(self.string)
        self.string = ''
        self.op = '*'

    def plus(self):
        self.val1 = float(self.string)
        self.string = ''
        self.op = '+'

    def minus(self):
        if self.string == '':
            self.string = '-'
            self.lcd.display(self.string)
        else:
            self.val1 = float(self.string)
            self.string = ''
            self.op = '-'

    def divide(self):
        self.val1 = float(self.string)
        self.string = ''
        self.op = '/'

    def clear(self):
        self.val1   = ''
        self.string = ''
        self.lcd.display(0)

    def equals(self):
       if self.op == '*':
           self.ans = self.val1.__mul__(float(self.string))
       elif self.op == '+':
           self.ans =  self.val1.__add__(float(self.string))
       elif self.op == '-':
           self.ans = self.val1.__sub__(float(self.string))
       elif self.op == '/':
           self.ans = self.val1.__truediv__(float(self.string))
           
       self.string = ''
       self.val1 = ''
       print self.ans
       self.lcd.display(self.ans)
       

    def decimal(self):
        self.string += '.'
        self.lcd.display(self.string)

    def close_application(self):
        # add functionality to see if we want to exit
        choice = QtGui.QMessageBox.question(self,'Exit','Are you sure you want to exit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def main(): 
    app = QtGui.QApplication(sys.argv)
    GUI = Calc()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
