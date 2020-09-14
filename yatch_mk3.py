import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication, QRect
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self, y):
        super().__init__()
        self.initUI(y)

    def show_full_dices(self, y):
        self.full_dices.setText(str(y.dices))

    def show_fixed_dices(self, y):
        self.fixed_dices.setText(str(y.fixed))

    def initUI(self, y):

        self.fixed_dices = QLabel(self)
        self.fixed_dices.setGeometry(QRect(125,10,100,20))
        self.fixed_dices.setObjectName("fixed")
        self.fixed_dices.setText(str(y.fixed))

        self.full_dices = QLabel(self)
        self.full_dices.setGeometry(QRect(125,30,100,20))
        self.full_dices.setObjectName("dices")
        self.full_dices.setText(str(y.dices))

        self.btn_dice_0 = QPushButton(str(y.dices[0]),self)
        self.btn_dice_0.move(50,50)
        self.btn_dice_0.resize(25,25)
        self.btn_dice_0.clicked.connect(lambda: y.fixDice(0))
        self.btn_dice_0.clicked.connect(lambda: self.show_fixed_dices(y))

        self.btn_dice_1 = QPushButton(str(y.dices[1]),self)
        self.btn_dice_1.move(100,50)
        self.btn_dice_1.resize(25,25)
        self.btn_dice_1.clicked.connect(lambda: y.fixDice(1))
        self.btn_dice_1.clicked.connect(lambda: self.show_fixed_dices(y))

        self.btn_dice_2 = QPushButton(str(y.dices[2]),self)
        self.btn_dice_2.move(150,50)
        self.btn_dice_2.resize(25,25)
        self.btn_dice_2.clicked.connect(lambda: y.fixDice(2))
        self.btn_dice_2.clicked.connect(lambda: self.show_fixed_dices(y))

        self.btn_dice_3 = QPushButton(str(y.dices[3]),self)
        self.btn_dice_3.move(200,50)
        self.btn_dice_3.resize(25,25)
        self.btn_dice_3.clicked.connect(lambda: y.fixDice(3))
        self.btn_dice_3.clicked.connect(lambda: self.show_fixed_dices(y))

        self.btn_dice_4 = QPushButton(str(y.dices[4]),self)
        self.btn_dice_4.move(250,50)
        self.btn_dice_4.resize(25,25)
        self.btn_dice_4.clicked.connect(lambda: y.fixDice(4))
        self.btn_dice_4.clicked.connect(lambda: self.show_fixed_dices(y))

        btn_reroll = QPushButton('reroll',self)
        btn_reroll.move(50,100)
        btn_reroll.resize(btn_reroll.sizeHint())
        btn_reroll.clicked.connect(y.rollDices)
        btn_reroll.clicked.connect(lambda: self.show_full_dices(y))


        btn = QPushButton('stop',self)
        btn.move(200,100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(y.stop_roll)
        
        self.setWindowTitle('GUI TEST')
        self.setWindowIcon(QIcon('icon_yachoo.png'))
        self.move(300, 300)
        self.resize(800, 600)
        self.show()


class Yatch:
    def __init__(self):
        self.dices = [0]*5
        self.fixed = []
        self.result = []

    def rollDices(self):
        n = len(self.dices)
        self.dices = list(map(lambda x: random.randint(1,6), [0]*n))
        print (self.dices)

    def fixDice(self, idx):
        self.fixed.append(self.dices.pop(idx))
        print(self.fixed, 'is fixed')
        print(self.dices, 'will be rolled')

    def unfixDice(self, idx):
        print (self.fixed[idx],'is unfixed')
        self.dices.append(self.fixed.pop(idx))
        print(self.fixed, 'is fixed')
        print(self.dices, 'will be rolled')

    def mergeDices(self):
        self.result = self.dices + self.fixed

    def stop_roll(self):
        print('stop')
        return 1

    def execCmd(self):
        while True:
            cmd = input().split(' ')
            func = cmd[0]

            if func == 'r':
                self.rollDices()
                break
            else:
                idx = int(cmd[1])-1

                if func == 'f':
                    self.fixDice(idx)
                    
                elif func == 'u':
                    self.unfixDice(idx)

'''
class Yatch:
    def __init__(self):
        self.dices = [0]*5
        self.fixed = []
        self.result = []

    def rollDices(self):
        n = len(self.dices)
        self.dices = list(map(lambda x: random.randint(1,6), [0]*n))
        print (self.dices)

    def fixDice(self, idx):
        self.fixed.append(self.dices.pop(idx))
        print(self.fixed, 'is fixed')
        print(self.dices, 'will be rolled')

    def unfixDice(self, idx):
        print (self.fixed[idx],'is unfixed')
        self.dices.append(self.fixed.pop(idx))
        print(self.fixed, 'is fixed')
        print(self.dices, 'will be rolled')

    def mergeDices(self):
        self.result = self.dices + self.fixed

    def execCmd(self):
        while True:
            cmd = input().split(' ')
            func = cmd[0]

            if func == 'r':
                self.rollDices()
                break
            else:
                idx = int(cmd[1])-1

                if func == 'f':
                    self.fixDice(idx)
                    
                elif func == 'u':
                    self.unfixDice(idx)
'''

if __name__ == '__main__':
   app = QApplication(sys.argv)
   y = Yatch()
   y.rollDices()

   ex = MyApp(y)
 

   sys.exit(app.exec_())

'''
if __name__ == "__main__":
    y = Yatch()

    print ('--------------------------------')
    print ('고정: f idx (ex. f 1)')
    print ('고정 해제: u idx (ex. u 1)')
    print ('만족하셨다면 리롤: r (ex. r)')
    print ('--------------------------------')

    y.rollDices()

    for i in range(2):
        y.execCmd()

    y.mergeDices()
    
    print (y.result)
'''
