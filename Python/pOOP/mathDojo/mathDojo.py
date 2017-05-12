

class mathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *num):
        if num is not None:
            for val in num:
                self.total += val
        return self
    def sub(self, *num):
        if num is not None:
            sub_total = 0
            for val in num:
                sub_total += val
            self.total -= sub_total
        return self
    def result(self):
        print self.total
        return self

mathDojo().add(2).add(2,5).sub(3,2).result()

class mathDojo2(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for arg in args:
            if type(arg) == int:
                self.total = self.total + arg
            if type(arg) == list or type(arg) == tuple:
                for val in arg:
                    self.total = self.total + val
        return self
    def sub(self, *args):
        for arg in args:
            sub_total = 0
            if type(arg) == int:
                sub_total += arg
            if type(arg) == list or type(arg) == tuple:
                for val in arg:
                    sub_total += val
            self.total = self.total - sub_total
        return self
    def result(self):
        print self.total
        return self

mathDojo2().add([1],1).add([1,1], [1, 1, 1]).sub(1, [1,1], [1, 2]).result().add([1,2,3]).add(1,1,[1,1,1]).sub(1,2,[1,1,1],(1,1)).result()
