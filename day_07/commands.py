from day_07.node import Node

def execute_cd(destination: str, cwd: list):
    if destination == "..":
        cwd = cwd.pop()
    else:
        if len(cwd) == 0:
            cwd.append(Node(destination))
        else:
            cwd.append(cwd[-1].get_child(destination))

def process_ls_output(console_line: str, cwd: list):
    if console_line.split()[0] == "dir":
        add_dir_to_current_dir(console_line, cwd)
    else:
        add_file_to_current_dir(console_line, cwd)


def add_dir_to_current_dir(console_line: str, cwd: list):
    cwd[-1].add_child(console_line.split()[1])

def add_file_to_current_dir(console_line: str, cwd: list):
    cwd[-1].add_file(console_line.split()[1], console_line.split()[0])

def parse_command(command: str):
    command_parts = command.split()
    if len(command_parts) == 3:
        return command_parts[1], command_parts[2]
    return command_parts[1], None