#coding:utf-8

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


avg = Averager()
avg(100)

avg(99)
