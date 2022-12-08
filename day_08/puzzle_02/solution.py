def search_for_visible_trees(lines: list):
    tree_map = create_map(lines)
    tree_count = find_visible_trees(tree_map)
    return tree_count

def find_visible_trees(tree_map: list):
    max_visibility = 0
    for i in range(0, len(tree_map)):
        for j in range(0, len(tree_map[i])):
            tree_visibility = get_visibility(i, j, tree_map)
            if tree_visibility > max_visibility:
                max_visibility = tree_visibility
    return max_visibility

def get_visibility(y: int, x: int, tree_map:list):
    if x == 0 or y == 0 or x == len(tree_map)-1 or y == len(tree_map[x])-1:
        return 0
    left, right = get_left_right_visibility(y, x, tree_map) 
    up, down = get_up_down_visitility(y, x, tree_map)
    return (left * right * up * down)
    
def get_up_down_visitility(y: int, x: int, tree_map: list):
    return (get_up_visibility(y, x, tree_map), get_down_visibility(y, x, tree_map))

def get_up_visibility(y: int, x: int, tree_map: list):
    up_visibility = 0
    for j in range(y-1, -1, -1):
        if tree_map[j][x] >= tree_map[y][x]:
            return up_visibility + 1
        else:
            up_visibility += 1
    return up_visibility

def get_down_visibility(y: int, x: int, tree_map: list):
    down_visibility = 0
    for j in range(y+1, len(tree_map)):
        if tree_map[j][x] >= tree_map[y][x]:
            return down_visibility + 1
        else:
            down_visibility += 1
    return down_visibility

def get_left_right_visibility(y: int, x: int, tree_map: list):
    return (get_left_visibility(y, x, tree_map), get_right_visibility(y, x, tree_map))

def get_left_visibility(y: int, x: int, tree_map: list):
    left_visibility = 0
    for i in range(x-1, -1, -1):
        if tree_map[y][i] >= tree_map[y][x]:
            return left_visibility + 1
        else:
            left_visibility += 1
    return left_visibility

def get_right_visibility(y: int, x: int, tree_map: list):
    right_visibility = 0
    for i in range(x+1, len(tree_map[y])):
        if tree_map[y][i] >= tree_map[y][x]:
            return right_visibility + 1
        else:
            right_visibility += 1
    return right_visibility

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
