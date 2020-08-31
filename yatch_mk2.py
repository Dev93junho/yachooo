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

    def unfixDice(self, idx):
        self.dices.append(self.fixed.pop(idx))

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
                    print(self.fixed, 'is fixed')
                    print(self.dices, 'will be rolled')
                    
                elif func == 'u':
                    print (self.fixed[idx],'is unfixed')
                    self.unfixDice(idx)
                    print(self.fixed, 'is fixed')
                    print(self.dices, 'will be rolled')

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

