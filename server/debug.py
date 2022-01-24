import time, os
class keyboardDisable():
    def start(self):
        print("\x1b[?25l", end="")
    def stop(self):
        print("\x1b[?25h", end="")

        
class keyboardSaveNLoad:
    def terminal_save(self):
        print("\x1b[s", end="")
    def terminal_load(self):
        print("\x1b[u", end="")

disable = keyboardDisable()
terminal_manager = keyboardSaveNLoad()

#FIXME: Create an array to store all of the messages that are in the terminal based on the size of the terminal
#This is making me want to kermit not alive

class Display:
    def __init__(self):
        #This is so that all of the variables are set up for the use of the functions
        self.first_line_count = 0
        self.PREFIX = "[DEBUG]: "
        self.NEWCONN_PREFIX = "[\x1b[38;5;48mNEW CONNECTION\x1b[0m]: "
        self.NOTICE_PREFIX = "[\x1b[38;5;220mNOTICE\x1b[0m]: "
        self.ERROR_PREFIX = "[\x1b[38;5;124mERROR\x1b[0m]: "
        self.WARNING_PREFIX = "[\x1b[38;5;202mWARNING\x1b[0m]: "
        self.terminal_indicator = "\n>: "
        self.terminal_collumns, self.terminal_rows = os.get_terminal_size()
        self.terminal_rows = self.terminal_rows - 1
        self.display_buffer = []
        #This one is the Escape code and tells it to move one line up and to the end of the last printed message
        #Made it this way becasue trouble shooting it was a massive pain in the behing
        self.ESCAPE_CODE = "\x1b[" + str(self.terminal_rows) + ";" + str(self.first_line_count) + "H"+ "\x1b[2K"    
    def move_to_position(self, row, columns):
        print("\x1b[" + str(row) + ";" + str(columns) + "H", end="")
    def display_refresh(self):
        terminal_manager.terminal_save()
        if len(self.display_buffer) >= self.terminal_rows:
            self.move_to_position(0,0)
            print(self.display_buffer.pop(0))
            for lines in self.display_buffer:
                print(lines)
        else:
            self.move_to_position(self.terminal_rows-len(self.display_buffer), 0)
            current_index = 0
            for lines in self.display_buffer:
                if current_index != len(self.display_buffer):
                    print(lines)
                else:
                    print(lines,end="")
        terminal_manager.terminal_load()
    def dlog_debug(self, Message):
        self.display_buffer.append(self.PREFIX + Message)
        self.display_refresh()
    def dlog_debugnewconn(self, Message):
        self.display_buffer.append(self.NEWCONN_PREFIX + Message)
        self.display_refresh()
    def dlog_notice(self, Message):
        self.display_buffer.append(self.NOTICE_PREFIX + Message)
        self.display_refresh()
    def dlog_error(self, Message):
        self.display_buffer.append(self.ERROR_PREFIX + Message)
        self.display_refresh()
    def dlog_warning(self, Message):
        self.display_buffer.append(self.WARNING_PREFIX + Message)
        self.display_refresh()



d = Display()

#possible solution for unexpected error
"""class Thread_Debug(Debug):
    pass"""