class computer:
    def __init__(self,ram,screensize,processor):
        self.ram=ram
        self.screensize=screensize
        self.processor=processor
    def getspecs(self):
        print("enter specifications")
        self.ram=input("enter ram size")
        self.screensize=input("enter screen size")
        self.processor=input("enter processsor type")
    def display(self):
        print("specs of your system")
        print("Ram size:",self.ram,"\n","Screen size:",self.screensize,"\n","Processor:",self.processor)
class desktop(computer):
    def __init__(self,brand):
        self.brand=brand
    def getdesk(self):
        self.brand=input("enter the brand")
    def displaydesk(self):
        print(self.brand)

class laptop(computer):
    def __init__(self,color):
        self.color=color

    def gettop(self):
        self.color=input("enter color")

    def displaytop(self):
        print(self.color)



obj=desktop('')
obj.getspecs()
obj.display()
obj.getdesk()
obj.displaydesk()

