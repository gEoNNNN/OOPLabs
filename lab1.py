class Computer:
    def __init__(self):
        self.temperature = 20
        self.Power = False
    def PowerOn(self):
        self.Power = True
    def Heat(self, amount):
        self.temperature += amount
        self.Power = self.speed != 20
    def printTemperature(self):
        print("Temperature:", self.temperature)
    def printPower(self):
        if self.Power:
            print("The computer is ON")
        else:
            print("The computer is not OFF")


class Computer:
    def __init__(self):
        self.number = 10
        self.values = []
        self.sum = 0

    def Mof3(self):
        i = 0
        while i < self.number:
            if i != 0 and i != self.number:
                self.values.append(i)
            i = i + 3

    def Mof5(self):
        i = 0
        while i <= self.number:
            if i != 0 and i != self.number:
                self.values.append(i)
            i = i + 5

    def add(self):
        for i in self.values:
            self.sum += i

    def printResult(self):
        self.add()
        print(self.number, '=>', self.sum, self.values)

comp = Computer()
comp.Mof3()
comp.Mof5()
comp.printResult()