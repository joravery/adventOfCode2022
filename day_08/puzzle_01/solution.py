from day_08.util import create_tree_map

def search_for_visible_trees(lines: list):
    '''
    A visible tree is any tree that can be seen from the perimiter
    That is, it has at least one direction (left, right, up, down) in which all the trees are smaller

    This function creates the map (2-d array) and then looks through the map for visible trees
    '''
    tree_map = create_tree_map(lines)
    return find_visible_trees(tree_map)

def find_visible_trees(tree_map: list):
    '''
    Checks each tree for visibiilty and returns the count of all visible trees
    '''
    return sum(tree_is_visible(y, x, tree_map) for y in range(len(tree_map)) for x in range(len(tree_map[y])))

def tree_is_visible(y: int, x: int, tree_map:list):
    '''
    Inspects a tree's visibility in all directions. Returns early upon first visible path
    '''
    return tree_on_perimiter(y, x, tree_map) or check_left_right(x, tree_map[y]) or check_up_down(y, x, tree_map)

def tree_on_perimiter(y: int, x: int, tree_map:list):
    '''
    Returns true if the tree is on the edge of the map
    '''
    return x == 0 or y == 0 or y == len(tree_map)-1 or x == len(tree_map[x])-1

def check_up_down(y: int, x: int, tree_map: list):
    '''
    Checks a tree for visibilty in the vertical path (column)
    '''
    return all(tree_map[i][x] < tree_map[y][x] for i in range(0, y)) or \
        all(tree_map[i][x] < tree_map[y][x] for i in range(y+1, len(tree_map)))

def check_left_right(x: int, row: list):
    '''
    Checks a tree for visibilty in the horizontal path (row)
    '''
    return all(row[i] < row[x] for i in range(x)) or \
        all(row[i] < row[x] for i in range(x+1, len(row)))

if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        TOTAL_TREES = search_for_visible_trees(input_file.readlines())
    print(f"Total trees visible: {TOTAL_TREES}")
