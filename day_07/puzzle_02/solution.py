def process_terminal_output(lines: list):
    file_root = Node("/")
    cwd = [file_root]
    for line in lines:
        if line[0] == "$":
            command, args = parse_command(line)
            if command == 'cd':
                if args == "..":
                    cwd = cwd[:-1]
                else:
                    if cwd[-1].get_child(args) == None:
                        cwd[-1].add_child(args)
                    cwd.append(cwd[-1].get_child(args))
            if command == 'ls':
                continue
        else:
            if line.split()[0] == "dir":
                cwd[-1].add_child(line.split()[1])
            else:
                cwd[-1].add_file(line.split()[1], line.split()[0])
    assign_sizes(file_root)
    total_disk_size = 70000000
    size_needed = 30000000 - (total_disk_size - file_root.size)
    print(size_needed)
    print(sorted(find_dirs_greater_than(file_root, size_needed)))

def find_dirs_greater_than(root, size_thresh):
    total = []
    if root.size >= size_thresh:
        total.append(root.size)
    for child in root.children:
        total += find_dirs_greater_than(root.get_child(child), size_thresh)
    
    return total

    
def parse_command(command: str):
    command_parts = command.split()
    if len(command_parts) == 3:
        return command_parts[1], command_parts[2]
    return command_parts[1], None

def assign_sizes(root):
    children_size = 0
    for child in root.children:
        child_node = root.get_child(child)
        assign_sizes(child_node)
        children_size += child_node.size
    root.size += children_size

    

class Node:
    def __init__(self, name) -> None:
        self.files = {}
        self.children = {}
        self.name = name
        self.size = 0
    
    def add_file(self, filename, size):
        self.files[filename] = int(size)
        self.size += int(size)

    def add_child(self, child):
        self.children[child] = Node(child)
    
    def get_child(self, child_name):
        try:
            return self.children[child_name]
        except KeyError:
            return None

if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_terminal_output(input_file.readlines())