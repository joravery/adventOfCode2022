from day_12.node import Node


def process_list(lines: list, target_letter: str, starting_letter: str):
    '''
    Searches for all paths from starting character to target character returning the shortest path length
    '''
    shortest = float("inf")
    topo_map = build_topo_map(lines)
    starting_positions = find_all_starting_positions(topo_map, starting_letter)
    for starting_position in starting_positions:
        topo_map = build_topo_map(lines)
        peak_node = find_peak(target_letter, starting_position, topo_map)
        shortest = peak_node.shortest_path if peak_node.shortest_path < shortest else shortest
    return shortest


def print_shortest_path_to_node(node: Node):
    '''
    Prints the character path from start to destination
    '''
    path = []
    while node.predecessor is not None:
        path.insert(0, node.letter)
        node = node.predecessor
    print(path)


def find_peak(target: str, starting_position: tuple, topo_map: list[list[Node]]):
    '''
    Use BFS with node memory of shortest previous path to find shortest path (Dijkstra)
    '''
    i, j = starting_position
    starting_node = topo_map[i][j]
    starting_node.shortest_path = 0
    queue = [(i, j)]

    # Initialize a dummy node object in case of bad input
    target_node = Node(0, 0, "TARGET_NOT_FOUND")

    while len(queue) > 0:
        currrent_position = queue.pop(0)
        current_node = topo_map[currrent_position[0]][currrent_position[1]]
        for coords in get_neighbors(currrent_position, topo_map):
            neighbor_node = topo_map[coords[0]][coords[1]]
            if neighbor_node.letter == target:
                target_node = neighbor_node
            if can_visit(current_node.letter, neighbor_node.letter) and should_visit(current_node, neighbor_node):
                neighbor_node.shortest_path = current_node.shortest_path + 1
                neighbor_node.predecessor = current_node
                queue.append(coords)
    return target_node


def should_visit(current_node, next_node):
    '''
    Should only visit a node if it hasn't been visited before, or if the current path to that node is shorter than the previous path
    '''
    if next_node.shortest_path > current_node.shortest_path + 1:
        return True
    return False


def can_visit(current_character, next_character):
    '''
    Determines if the next character is at most 1 letter higher than the current character
    '''
    if next_character == "S" or next_character == "E" and current_character != "z":
        return False
    return ord(next_character) - ord(current_character) < 2 or current_character == "S"


def get_neighbors(coords: tuple, topo_map: list[list[str]]):
    '''
    Creates a list of coordinate tuples that are up/down or left/right of the current position and in-bounds of the current map
    '''
    i, j = coords
    neighbor_coords = []
    if i > 0:
        neighbor_coords.append((i-1, j))
    if i < len(topo_map)-1:
        neighbor_coords.append((i+1, j))
    if j > 0:
        neighbor_coords.append((i, j-1))
    if j < len(topo_map[i])-1:
        neighbor_coords.append((i, j+1))
    return neighbor_coords


def find_all_starting_positions(topo_map: list[list[Node]], target_start: str):
    '''
    Checks every character in the topo map to find all potential starting positions
    '''
    starting_positions = []
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j].letter == target_start:
                starting_positions.append((i, j))
    return starting_positions


def build_topo_map(lines: list) -> list[list[Node]]:
    '''
    Initializes a topographical (relief) map from the provided character grid
    '''
    topo_map = []
    for i, line in enumerate(lines):
        row = []
        for j, character in enumerate(line):
            if character != "\n":
                row.append(Node(i, j, character))
        topo_map.append(row)
    return topo_map


if __name__ == "__main__":
    TARGET_CHARACTER = "E"
    PUZZLE_01_STARTING_CHARACTER = "S"
    PUZZLE_02_STARTING_CHARACTER = "a"

    with open("./input.txt", "r", encoding="utf-8") as input_file:
        INPUT_MAP = input_file.readlines()
    PUZZLE_01_SHORTEST_PATH = process_list(INPUT_MAP, "E", "S")
    PUZZLE_02_SHORTEST_PATH = process_list(INPUT_MAP, "E", "a")
    print(f"Puzzle 01 shortest path to E: {PUZZLE_01_SHORTEST_PATH}")
    print(f"Puzzle 02 shortest path to E: {PUZZLE_02_SHORTEST_PATH}")
