import random

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
                return 0
            elif func == 'f' and len(cmd)==2:
                idx = int(cmd[1])-1
                self.fixDice(idx)
            elif func == 'u' and len(cmd)==2:
                idx = int(cmd[1])-1
                self.unfixDice(idx)
            elif func == 'z':
                return 1
            else:
                print('Wrong command')

if __name__ == "__main__":
    y = Yatch()

    print ('--------------------------------')
    print ('고정: f idx (ex. f 1)')
    print ('고정 해제: u idx (ex. u 1)')
    print ('리롤: r (ex. r)')
    print ('--------------------------------')

    y.rollDices()

    for i in range(2):
        if y.execCmd() == 1:
            break

    y.mergeDices()
    
    print (y.result)


