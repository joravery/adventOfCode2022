def create_tree_map(lines:list):
    '''
    Builds a 2-d array of numbers from a list of strings
    '''
    tree_map = []
    for i, line in enumerate(lines):
        tree_map.append([])
        for tree_char in line:
            if tree_char != "\n":
                tree_map[i].append(int(tree_char))
    return tree_map
