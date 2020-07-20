#coding: UTF-8 

class Orange:
    def __init__(self,weight,color):
        self.weight=weight
        self.color=color

    def print(self):
        print("weight : " + str(self.weight))
        print("color : " + self.color)
