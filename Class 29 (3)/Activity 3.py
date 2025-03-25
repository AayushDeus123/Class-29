#Super Function super()
class Bird:
    def __init__(self):
        print('Bird is ready')
   
    def WhoIsThis(self):
        print('Bird')
    
    def Swim(self):
        print('Swim faster!')
        
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print('Penguin is ready')
        
    def WhoIsThis(self):
        print('Penguin')
        
    def Run(self):
        print('Run faster!')
        
peggy = Penguin()
peggy.WhoIsThis()
peggy.Swim()
peggy.Run()