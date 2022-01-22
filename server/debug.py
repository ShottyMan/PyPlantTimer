import time
class keyboardDisable():
    def start(self):
        self.on = True
    def stop(self):
        self.on = False

        
class keyboardSaveNLoad:
    def terminal_save(self):
        print("\x1b[s")
    def terminal_load(self):
        print("\x1b[u")

disable = keyboardDisable()
terminal_manager = keyboardSaveNLoad()

class Debug:
    def __init__(self):
        #This is so that all of the variables are set up for the use of the functions
        self.first_line_count = -1
        self.PREFIX = "[DEBUG]: "
        self.NEWCONN_PREFIX = "[\x1b[38;5;48mNEW CONNECTION\x1b[0m]: "
        self.NOTICE_PREFIX = "[\x1b[38;5;220mNOTICE\x1b[0m]: "
        self.ERROR_PREFIX = "[\x1b[38;5;124mERROR\x1b[0m]: "
        self.WARNING_PREFIX = "[\x1b[38;5;202mWARNING\x1b[0m]: "
        self.terminal_indicator = "\n>:"
        #This one is the Escape code and tells it to move one line up and to the end of the last printed message
        self.ESCAPE_CODE = f"""\x1b[1A\x1b[K"""
        #self.ERASE_CODE = "\x1b[k"
    def dlog_debug(self, Message):
        disable.start()
        terminal_manager.terminal_save()
        print(self.ESCAPE_CODE + self.PREFIX + Message, end="") # FIXME: For some reason starts a newline even though I dont want it to
        self.first_line_count = len(self.PREFIX + Message)
        #terminal_manager.terminal_load()
        disable.stop()
        print(self.terminal_indicator, end="")
    def dlog_debugnewconn(self, Message):
        disable.start()
        terminal_manager.terminal_save()
        print(self.ESCAPE_CODE + self.NEWCONN_PREFIX + Message)
        self.first_line_count = len(self.NEWCONN_PREFIX + Message)
        terminal_manager.terminal_load()
        disable.stop()
    def dlog_notice(self, Message):
        disable.start()
        terminal_manager.terminal_save()
        print(self.ESCAPE_CODE + self.NOTICE_PREFIX + Message)
        self.first_line_count = len(self.NOTICE_PREFIX + Message)
        terminal_manager.terminal_load()
        disable.stop()
    def dlog_error(self, Message):
        disable.start()
        terminal_manager.terminal_save()
        print(self.ESCAPE_CODE + self.ERROR_PREFIX + Message)
        self.first_line_count = len(self.ERROR_PREFIX + Message)
        terminal_manager.terminal_load()
        disable.stop()
    def dlog_warning(self, Message):
        disable.start()
        terminal_manager.terminal_save()
        print(self.ESCAPE_CODE + self.WARNING_PREFIX + Message)
        self.first_line_count = len(self.WARNING_PREFIX + Message)
        terminal_manager.terminal_load()
        disable.stop()


d = Debug()

#possible solution for unexpected error
"""class Thread_Debug(Debug):
    pass"""