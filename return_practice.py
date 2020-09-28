
import json
object = {"One": 1,"Two": 2, "Three": 3}

def addition(x,y):
    print("X: {}, Y: {}".format(x,y))
    return x + y

#Unspepcified number of arguements
def varargs(*args):
    return sum(args)

#Keyword Arguements
def keyvargs(**kwargs):
    return kwargs

class Human:
    def __init__(self,name):
        self.name = name
        self.age = 0

    def say(self,msg):
        print("{name}:{message}".format(name=self.name,message=msg))
    
    def sing(self):
        return "perfect"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"




