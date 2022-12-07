from day_07.node import Node

def execute_cd(destination: str, cwd: list):
    '''
    Allows for moving up or down one directory.
    If moving down it adds the destination to the end of the current working directory
    If moving up it shortens the current working directory by one
    '''
    if destination == "..":
        cwd = cwd.pop()
    else:
        if len(cwd) == 0:
            cwd.append(Node(destination))
        else:
            cwd.append(cwd[-1].get_child(destination))

def process_ls_output(console_line: str, cwd: list):
    '''
    Adds either a file or directory to the current working directory
    '''
    if console_line.split()[0] == "dir":
        add_dir_to_current_dir(console_line, cwd)
    else:
        add_file_to_current_dir(console_line, cwd)


def add_dir_to_current_dir(console_line: str, cwd: list):
    '''
    Adds a new directory to the current working directory
    '''
    cwd[-1].add_child(console_line.split()[1])

def add_file_to_current_dir(console_line: str, cwd: list):
    '''
    Adds a new files to the current working directory
    '''
    cwd[-1].add_file(console_line.split()[1], console_line.split()[0])

def parse_command(command: str):
    '''
    Splits a command line and returns a tuple for either a directory change or directory listing
    '''
    command_parts = command.split()
    if len(command_parts) == 3:
        return command_parts[1], command_parts[2]
    return command_parts[1], None
