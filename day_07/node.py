class Node:
    '''
    A filesystem Node which represents a single directory.
    '''
    def __init__(self, name) -> None:
        '''
        A new directory can be instantiated with a name. Adding files and sub directories to be done with methods.
        '''
        self.files = {}
        self.children = {}
        self.name = name
        self.size = 0

    def add_file(self, filename, size):
        '''
        Adds a new filename with a size to the files dictionary for this directory.
        Increases the directory size by file size.
        '''
        self.files[filename] = int(size)
        self.size += int(size)

    def add_child(self, child):
        '''
        Adds a new child directory Node
        '''
        self.children[child] = Node(child)

    def get_child(self, child_name):
        '''
        Returns a child Node instance with the given name
        '''
        try:
            return self.children[child_name]
        except KeyError:
            return None
