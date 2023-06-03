class amountx:
    amount = 500
    x = 200

    @property        #getter
    def t(self):
        return self.amount + self.x
    
    @t.setter         # setter
    def t(self, v):
        self.x = v - self.amount

a = amountx ()
print(a.t)
a.t = 1000
print(a.amount)
print(a.x)