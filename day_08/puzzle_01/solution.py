def search_for_visible_trees(lines: list):
    tree_map = create_map(lines)
    tree_count = find_visible_trees(tree_map)
    return tree_count

def find_visible_trees(tree_map: list):
    visible_trees = 0
    for i in range(0, len(tree_map)):
        for j in range(0, len(tree_map[i])):
            if tree_is_visible(i, j, tree_map):
                visible_trees += 1
    return visible_trees

def tree_is_visible(y: int, x: int, tree_map:list):
    if x == 0 or y == 0 or x == len(tree_map)-1 or y == len(tree_map[x])-1:
        return True
    return check_left_right(y, x, tree_map) or check_up_down(y, x, tree_map)
    
def check_up_down(y: int, x: int, tree_map: list):
    return check_up(y, x, tree_map) or check_down(y, x, tree_map)

def check_up(y: int, x: int, tree_map: list):
    for j in range(0, y):
        if tree_map[j][x] >= tree_map[y][x]:
            return False
    return True

def check_down(y: int, x: int, tree_map: list):
    for j in range(y+1, len(tree_map)):
        if tree_map[j][x] >= tree_map[y][x]:
            return False
    return True

def check_left_right(y: int, x: int, tree_map: list):
    return check_left(y, x, tree_map) or check_right(y, x, tree_map)

def check_left(y: int, x: int, tree_map: list):
    for i in range(0, x):
        if tree_map[y][i] >= tree_map[y][x]:
            return False
    return True

def check_right(y: int, x: int, tree_map: list):
    for i in range(x+1, len(tree_map[y])):
        if tree_map[y][i] >= tree_map[y][x]:
            return False
    return True

def create_map(lines:list):
    tree_map = []
    for i, line in enumerate(lines):
        tree_map.append([])
        for tree_char in line:
            if tree_char != "\n":
                tree_map[i].append(int(tree_char))
    return tree_map


if __name__ == "__main__":
    # Assumes a list of lines as input
    pass
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        total_trees = search_for_visible_trees(input_file.readlines())
    print(f"Total trees visible: {total_trees}")
