import matplotlib as mtl

class Neuronio:

    def __init__(self, n):
        self.w = [0.0] * n

    def setW(self, w):
        self.w = w

    def getW(self):
        return self.w

print('teste')