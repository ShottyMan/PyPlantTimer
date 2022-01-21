import time
class Debug:
    def __init__(self):
        #This is so that all of the variables are set up for the use of the functions
        self.first_line_count = -1
        self.PREFIX = "[DEBUG]: "
        self.NEWCONN_PREFIX = "[\x1b[38;5;48mNEW CONNECTION\x1b[0m]: "
        self.NOTICE_PREFIX = "[\x1b[38;5;220mNOTICE\x1b[0m]: "
        self.ERROR_PREFIX = "[\x1b[38;5;124mERROR\x1b[0m]: "
        self.WARNING_PREFIX = "[\x1b[38;5;202mWARNING\x1b[0m]: "
        self.ESCAPE_CODE = f"""\x1b[1A\x1b[{self.first_line_count}C"""
    def dlog_debug(self, Message):
        time.sleep(1)
        print(self.ESCAPE_CODE + self.PREFIX + Message)
        self.first_line_count = len(self.PREFIX + Message)
    def dlog_debugnewconn(self, Message):
        print(self.NEWCONN_PREFIX + Message)
    def dlog_notice(self, Message):
        print(self.NOTICE_PREFIX + Message)
    def dlog_error(self, Message):
        print(self.ERROR_PREFIX + Message)
    def dlog_warning(self, Message):
        print(self.WARNING_PREFIX + Message)


d = Debug()
