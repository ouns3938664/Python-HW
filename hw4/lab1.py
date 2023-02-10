class cylinder():
    r = 0
    h = 0

    def cal(self):
        self.volume = 3.14*(self.r*self.r)*self.h
        return self.volume


cylinder1 = cylinder()
cylinder1.r = 5
cylinder1.h = 10

cylinder2 = cylinder()
cylinder2.r = 7
cylinder2.h = 13

print(str(cylinder1.cal()))
print(str(cylinder2.cal()))
