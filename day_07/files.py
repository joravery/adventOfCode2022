from day_07.commands import parse_command, execute_cd, process_ls_output

def calculate_directory_sizes(root):
    '''
    Recursively adds the size of all child directories to each directory
    '''
    children_size = 0
    for child in root.children:
        child_node = root.get_child(child)
        calculate_directory_sizes(child_node)
        children_size += child_node.size
    root.size += children_size

def build_file_system(lines: list):
    '''
    Iterates through a list of CLI commands and subsequent output and creates a file system structure.
    '''
    cwd = []
    for line in lines:
        if line[0] == "$":
            command, args = parse_command(line)
            if command == 'cd':
                execute_cd(args, cwd)
            if command == 'ls':
                continue
        else:
            process_ls_output(line, cwd)
    calculate_directory_sizes(cwd[0])
    return cwd[0]
