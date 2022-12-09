def process_list(lines: list):
    visited_positions = set()
    head_pos = [0,0]
    tail_pos = [0,0]
    update_visited_map(tail_pos, visited_positions)

    print(f"Total spots visited before starting: {get_total_spots_visited(visited_positions)}")
    for movement in lines:
        [direction, magnitude] = movement.split()
        execute_move(direction, int(magnitude), head_pos, tail_pos, visited_positions)
    print(f"Total spots visited after executing all commands: {get_total_spots_visited(visited_positions)}")
    return get_total_spots_visited(visited_positions)

def execute_move(direction: str, magnitude: int, head_pos, tail_pos, visdited_map):
    while magnitude > 0:
        update_position(direction, head_pos)
        if should_move_tail(head_pos, tail_pos):
            update_tail(head_pos, tail_pos)
            update_visited_map(tail_pos, visdited_map)
        magnitude -= 1


def update_position(direction: str, pos: list):
    if direction == "U":
        pos[0] =  pos[0] + 1
    if direction == "D":
        pos[0] =  pos[0] - 1
    if direction == "L":
        pos[1] =  pos[1] - 1
    if direction == "R":
        pos[1] =  pos[1] + 1

def should_move_tail(head_pos, tail_pos):
    return abs(head_pos[0] - tail_pos[0]) > 1 or \
        abs(head_pos[1] - tail_pos[1]) > 1

def update_tail(head_pos, tail_pos):
    # gross
    if should_move_diaganolly(head_pos, tail_pos):
        if head_pos[0] > tail_pos[0]:
            update_position("U", tail_pos)
        else:
            update_position("D", tail_pos)
        if head_pos[1] > tail_pos[1]:
            update_position("R", tail_pos)
        else:
            update_position("L", tail_pos)
    else:
        if head_pos[0] > tail_pos[0]:
            update_position("U", tail_pos)
        elif head_pos[0] < tail_pos[0]:
            update_position("D", tail_pos)
        elif head_pos[1] > tail_pos[1]:
            update_position("R", tail_pos)
        else:
            update_position("L", tail_pos)

def should_move_diaganolly(head_pos, tail_pos):
    return abs(head_pos[0] - tail_pos[0])+ abs(head_pos[1] - tail_pos[1]) > 2

def update_visited_map(tail_pos: tuple, visited_map: set):
    visited_map.add(tuple(tail_pos))

def get_total_spots_visited(visted_map):
    return len(visted_map)


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        process_list(input_file.readlines())
