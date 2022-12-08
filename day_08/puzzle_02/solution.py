from day_08.util import create_tree_map

def search_for_best_position(lines: list):
    '''
    Finds the tree with the best visibility score and returns that score value
    '''
    tree_map = create_tree_map(lines)
    return find_maximum_visibility(tree_map)

def find_maximum_visibility(tree_map: list):
    '''
    Gets the visibility score for each tree and returns the maximum score
    '''
    max_visibility = 0
    for i in range(1, len(tree_map)-1):
        for j in range(1, len(tree_map[i])-1):
            tree_visibility = get_visibility_score(i, j, tree_map)
            max_visibility = max(max_visibility, tree_visibility)
    return max_visibility

def get_visibility_score(y: int, x: int, tree_map:list):
    '''
    Calculates the visibility score for a single tree.
    The visibility score for a tree is the visibility score in each direction multiplied together.
    The score for a given direction is the number of consecutive trees from the beginning tree that are less than or equal to the height of the tree
    The first tree in a direction that is the same height is considered visible, but any beyond that are not
    '''
    left_right_score = left_right_visibility(y, x, tree_map)
    up_down_score = up_down_visibility(y, x, tree_map)
    return left_right_score * up_down_score

def up_down_visibility(y: int, x: int, tree_map: list):
    '''
    Returns the visibility for both up and downfrom the tree
    '''
    return up_down(y, x, tree_map, y-1, -1, -1) * up_down(y, x, tree_map, y+1, len(tree_map), 1)

def up_down(y, x, tree_map, start, stop, step):
    '''
    Calculates visibility for one direction in a column
    '''
    visibility = 0
    for j in range(start, stop, step):
        visibility += 1
        if tree_map[j][x] >= tree_map[y][x]:
            break
    return visibility

def left_right_visibility(y: int, x: int, tree_map:list):
    '''
    Returns the visibility for both left and right from the tree
    '''
    return left_right(y, x, tree_map, x-1, -1, -1) * left_right(y, x, tree_map, x+1, len(tree_map[y]), 1)

def left_right(y: int, x: int, tree_map: list, start, stop, step):
    '''
    Calculates the visibility for one direction in a row
    '''
    visibility = 0
    for i in range(start, stop, step):
        visibility += 1
        if tree_map[y][i] >= tree_map[y][x]:
            break
    return visibility

if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        BEST_VISIBILITY = search_for_best_position(input_file.readlines())
    print(f"The tree with the best visibility has a score of: {BEST_VISIBILITY}")
