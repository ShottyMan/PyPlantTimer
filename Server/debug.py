


class Debug:
    
    def __init__(self):
        pass
    PREFIX = "[DEBUG]: "

    
    def Dlog(self, Message):
        print(self.PREFIX + Message)

d = Debug()