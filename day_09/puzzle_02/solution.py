def process_list(lines: list):
    visited_positions = [set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0)), set((0,0))]
    knots = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]


    for movement in lines:
        [direction, magnitude] = movement.split()
        execute_move(direction, int(magnitude), knots, visited_positions)
    print(f"Total spots visited after executing all commands: {get_total_spots_visited(visited_positions[1])}")
    first_tail_position_count = len(visited_positions[1])
    last_tail_position_count = len(visited_positions[-1])
    return (first_tail_position_count, last_tail_position_count)

def execute_move(direction: str, magnitude: int, knots, visited_positions: list[set]):
    while magnitude > 0:
        update_position(direction, knots[0])
        for i in range(1, len(knots)):
            if should_move_tail(knots[i-1], knots[i]):
                update_tail(knots[i-1], knots[i])
                update_visited_positions(knots[i], visited_positions[i])
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

def update_visited_positions(tail_pos: list, visited_position: set):
    visited_position.add(tuple(tail_pos))

def get_total_spots_visited(visted_map):
    return len(visted_map)


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        FIRST_TAIL, LAS_TAIL = process_list(input_file.readlines())
    print(f"One tail visited {FIRST_TAIL} unique positions")
    print(f"The last of 9 tails visited {LAS_TAIL} unique positions")
