from dataclasses import dataclass

COMMAND_LIST = ['filter', 'map', 'sort', 'unique', 'limit', 'regex']


@dataclass
class Commands:
    file_name: str
    cmd1: str
    value1: str | int
    cmd2: str
    value2: str | int

    def __post_init__(self) -> None:
        if self.cmd1 not in COMMAND_LIST or self.cmd2 not in COMMAND_LIST:
            raise ValueError(f'Available commands list is {", ".join(COMMAND_LIST)}')

        if self.cmd1 in ('map', 'limit'):
            self.value1 = int(self.value1)
        if self.cmd2 in ('map', 'limit'):
            self.value2 = int(self.value2)
