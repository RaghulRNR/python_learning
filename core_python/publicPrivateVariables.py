#__test__=1
#print(__test__)

class Test:
    def __init__(self,a,b):
        self._a=a
        self._b=b
    def dispaly(self):
        print(self.a)

t=Test(10,20)
t.dispaly()