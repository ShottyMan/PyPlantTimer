class Debug:
    PREFIX = "[DEBUG]: "

    def __init__(self):
        pass

    def Dlog(self, Message):
        print(self.PREFIX + Message)


d = Debug()
