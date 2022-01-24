import time, os


class disable_keyboard:
    def start(self):
        print("\x1b[?25l", end="")

    def stop(self):
        print("\x1b[?25h", end="")


# Quite important it saves and loads the position of the cursor using the escape characters.
class keyboard_save_n_load:
    def terminal_save(self):
        print("\x1b[s", end="")

    def terminal_load(self):
        print("\x1b[u", end="")


disable = disable_keyboard()
terminal_manager = keyboard_save_n_load()

# This is fixed however this comment was actually exagerated and took less time than I thought to implement it.
# I want to keep it because it is hilarious
# FIXME: Create an array to store all of the messages that are in the terminal based on the size of the terminal.
# This is making me want to kermit not alive.


class Display:
    def __init__(self):
        # This is so that all of the variables are set up for the use of the functions
        self.first_line_count = 0
        self.PREFIX = "[DEBUG]: "
        # The \x1b codes only serve to add colours towards the pieces of text.
        self.NEWCONN_PREFIX = "[\x1b[38;5;48mNEW CONNECTION\x1b[0m]: "
        self.NOTICE_PREFIX = "[\x1b[38;5;220mNOTICE\x1b[0m]: "
        self.ERROR_PREFIX = "[\x1b[38;5;124mERROR\x1b[0m]: "
        self.WARNING_PREFIX = "[\x1b[38;5;202mWARNING\x1b[0m]: "
        self.terminal_collumns, self.terminal_rows = os.get_terminal_size()
        self.terminal_rows = self.terminal_rows - 1
        self.display_buffer = []
        # This one is the Escape code and tells it to move one line up and to the end of the last printed message
        # Made it this way becasue trouble shooting it was a massive pain in the behing

    def move_to_position(self, row, columns):
        print("\x1b[" + str(row) + ";" + str(columns) + "H", end="")

    def display_refresh(
        self,
    ):  # FIXME: starts with one empty when the terminal is not full but when it gets to the top it fills the last slot
        """
        This basically prints what is stored in the display buffer,
        It removes the items that are at the end of the buffer then
        it prints all of them out. The one at the end of the list is
        always the newest message and the one at the beginning is always
        the oldest message on the display.
        """
        terminal_manager.terminal_save()
        disable.start()
        if len(self.display_buffer) >= self.terminal_rows:
            self.move_to_position(0, 0)
            print(self.display_buffer.pop(0))
            for lines in self.display_buffer:
                print(lines)
        else:
            self.move_to_position(self.terminal_rows - len(self.display_buffer), 0)
            current_index = 0
            for lines in self.display_buffer:
                if current_index != len(self.display_buffer):
                    print(lines)
                else:
                    print(lines, end="")
        terminal_manager.terminal_load()
        disable.stop()

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

# possible solution for unexpected error
"""class Thread_Debug(Debug):
    pass"""
