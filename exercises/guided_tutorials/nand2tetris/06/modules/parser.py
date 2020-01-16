from enum import Enum


class CommandType(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3
    SYNTAX_ERROR = 4


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.file = self.file_generator()
        self.current_line = None
        self._next_line = self.get_next_command()

    @staticmethod
    def clean_command_of_whitespace(command):
        # no comments please
        command = command.rsplit('//')[0]
        # and get rid of all whitespace
        command = ''.join(command.rsplit())
        return command

    @property
    def has_more_commands(self):
        return bool(self._next_line)

    @has_more_commands.setter
    def has_more_commands(self, current):
        if not current:
            self._next_line = None
        else:
            self._next_line = current

    @property
    def command_type(self):
        try:
            if self.current_line[0] == '@':
                return CommandType.A_COMMAND

            if ';' in self.current_line or '=' in self.current_line:
                return CommandType.C_COMMAND

            if self.current_line[0] == '(' and self.current_line[-1] == ')':
                return CommandType.L_COMMAND

            return CommandType.SYNTAX_ERROR
        except TypeError:
            return None

    @property
    def symbol(self):
        if self.command_type == CommandType.A_COMMAND:
            return self.current_line[1:]
        elif self.command_type == CommandType.L_COMMAND:
            return self.current_line[1:-1]
        else:
            return None

    @property
    def dest(self):
        if self.command_type == CommandType.C_COMMAND and '=' in self.current_line:
            return self.current_line.split('=')[0]
        else:
            return None

    @property
    def comp(self):
        if self.command_type == CommandType.C_COMMAND:
            if '=' in self.current_line:
                return self.current_line.split('=')[1]
            else:
                return self.current_line.split(';')[0]
        else:
            return None

    @property
    def jump(self):
        if self.command_type == CommandType.C_COMMAND and ';' in self.current_line:
            return self.current_line.split(';')[1]
        else:
            return None

    def file_generator(self):
        try:
            with open(self.filename) as file_handler:
                while True:
                    data = file_handler.readline()
                    if not data:
                        break
                    yield data
        except (IOError, OSError):
            print("Error opening / processing file {}".format(self.filename))

    def advance(self):
        if self.has_more_commands:
            self.current_line = self._next_line
            self.has_more_commands = self.get_next_command()

    def get_next_command(self):
        while True:
            try:
                candidate = next(self.file)
                candidate = self.clean_command_of_whitespace(candidate)
                if len(candidate) > 0:
                    return candidate
            except StopIteration:
                self.has_more_commands = None
                return None
