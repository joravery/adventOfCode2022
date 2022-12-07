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