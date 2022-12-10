def process_list(movements: list, tail_count: int = 9):
    '''
    Moves a rope with knots through the movements, updating the position of the trailing knots(tails) after moving the first one(head)
    '''
    visited_positions = [set() for _ in range(tail_count+1)]
    knots = [[0,0] for _ in range(tail_count+1)]

    for i, knot in enumerate(knots):
        update_visited_positions(knot, visited_positions[i])

    for movement in movements:
        [direction, magnitude] = movement.split()
        execute_move(direction, int(magnitude), knots, visited_positions)
    first_tail_position_count = len(visited_positions[1])
    last_tail_position_count = len(visited_positions[-1])
    return (first_tail_position_count, last_tail_position_count)

def execute_move(direction: str, magnitude: int, knots, visited_positions: list[set]):
    '''
    Iteratively moves the head knot, and then updates all following knots (tails) based on the new position
    '''
    while magnitude > 0:
        update_position(direction, knots[0])
        for i in range(1, len(knots)):
            if should_move_tail(knots[i-1], knots[i]):
                update_tail(knots[i-1], knots[i])
                update_visited_positions(knots[i], visited_positions[i])
        magnitude -= 1

def update_position(direction: str, knot: list):
    '''
    Moves a given knot by one position
    '''
    if direction == "U":
        knot[0] =  knot[0] + 1
    if direction == "D":
        knot[0] =  knot[0] - 1
    if direction == "L":
        knot[1] =  knot[1] - 1
    if direction == "R":
        knot[1] =  knot[1] + 1

def should_move_tail(head, tail):
    '''
    A tail (following knot) should only  move if it is more than one position away in any direction
    '''
    return abs(head[0] - tail[0]) > 1 or \
        abs(head[1] - tail[1]) > 1

def update_tail(head: list, tail: list):
    '''
    Determines if a knot should move 2 directions (diagonally) or only 1 (laterally) and then updates accordingly
    '''
    move_diagonally(head, tail) if should_move_diaganolly(head, tail) else move_laterally(head, tail)

def move_diagonally(head: list, tail: list):
    '''
    Moves a following knot in both the horizontal and vertical positions towards the leading knot
    '''
    if head[0] > tail[0]:
        update_position("U", tail)
    else:
        update_position("D", tail)
    if head[1] > tail[1]:
        update_position("R", tail)
    else:
        update_position("L", tail)

def move_laterally(head: list, tail: list):
    '''
    Moves a following knot in either the horizontal or vertical positions towards the leading knot
    '''
    if head[0] > tail[0]:
        update_position("U", tail)
    elif head[0] < tail[0]:
        update_position("D", tail)
    elif head[1] > tail[1]:
        update_position("R", tail)
    else:
        update_position("L", tail)

def should_move_diaganolly(head, tail):
    '''
    If a trailing knot is more than 2 positions away from the leading knot it should move diagonally
    '''
    return abs(head[0] - tail[0]) + abs(head[1] - tail[1]) > 2

def update_visited_positions(tail: list, visited_position: set):
    '''
    Records a knot's position in a set so all unique positions can be easily counted
    '''
    visited_position.add(tuple(tail))

if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        FIRST_TAIL, LAS_TAIL = process_list(input_file.readlines())
    print(f"The first tail visited {FIRST_TAIL} unique positions")
    print(f"The last of 9 tails visited {LAS_TAIL} unique positions")
