def process_list(lines: list):
    cave_map = set()
    for line in lines:
        line_points = parse_rock_formation(line)
        draw_rocks_on_map(line_points, cave_map)
    deepest_object = find_lowest_rock(cave_map)
    return fill_sand(cave_map, (500, 0), deepest_object)


def find_lowest_rock(cave_map: set[tuple]):
    return max([i[1] for i in cave_map])


def fill_sand(cave_map: set[tuple], sand_origin: tuple, deepest_object: int):
    cave_filled = False
    grains_of_sand = -1
    while not cave_filled:
        grains_of_sand += 1
        cave_filled = add_sand(sand_origin, cave_map, deepest_object)
    return grains_of_sand


def add_sand(sand_position, cave_map, deepest_object: int):
    sand_fell = False
    sand_position = [x for x in sand_position]
    while can_move(sand_position, cave_map, deepest_object):
        sand_fell = update_sand_position(sand_position, cave_map, deepest_object)
        if sand_fell:
            return True
    cave_map.add((sand_position[0], sand_position[1]))


def update_sand_position(sand_position: list[int], cave_map: set[tuple], deepest_rock: int):
    _, sand_y = sand_position
    if sand_y == deepest_rock:
        sand_position[1] += 1
        return True
    else:
        move_down(sand_position, cave_map)
    if can_move_sideways(sand_position, cave_map, deepest_rock):
        move_sideways(sand_position, cave_map)


def move_down(sand_position: list[int], cave_map: set[tuple]):
    sand_x = sand_position[0]
    for i in range(sand_position[1], len(cave_map) - 1):
        if (sand_x, i + 1) not in cave_map:
            sand_position[1] = i + 1
        else:
            return


def move_sideways(sand_position: list[int], cave_map: set[tuple]):
    if (sand_position[0] - 1, sand_position[1] + 1) not in cave_map:
        sand_position[1] += 1
        sand_position[0] -= 1
    else:
        sand_position[1] += 1
        sand_position[0] += 1


def can_move(sand_position: list[int], cave_map: set[tuple], deepest_object: int) -> bool:
    sand_x, sand_y = sand_position
    if at_bottom(sand_position, deepest_object):
        return True
    if sand_y < deepest_object and (
        (sand_x, sand_y + 1) not in cave_map or can_move_sideways(sand_position, cave_map, deepest_object)
    ):
        return True
    return False


def at_bottom(sand_position: list[int], deepest_object: int):
    return sand_position[1] == deepest_object


def can_move_sideways(sand_position: list[int], cave_map: set[tuple], deepest_object: int):
    if at_bottom(sand_position, deepest_object):
        return False
    sand_x, sand_y = sand_position
    if (sand_x - 1, sand_y + 1) not in cave_map or (sand_x + 1, sand_y + 1) not in cave_map:
        return True
    return False


def draw_rocks_on_map(rock_formation: list[str], cave_map: set[tuple]):
    for i in range(len(rock_formation) - 1):
        start_point = rock_formation[i]
        end_point = rock_formation[i + 1]
        draw_line_between_points(start_point, end_point, cave_map)


def draw_line_between_points(start: str, end: str, cave_map: set[tuple]):
    [start_j, start_i] = [int(x) for x in start.split(",")]
    [end_j, end_i] = [int(x) for x in end.split(",")]
    if start_i > end_i:
        start_i, end_i = end_i, start_i
    if start_j > end_j:
        start_j, end_j = end_j, start_j
    for i in range(start_i, end_i + 1):
        for j in range(start_j, end_j + 1):
            cave_map.add((j, i))


def parse_rock_formation(line_segments: str):
    """
    Turns a single entry of rock formation lines into a list of points
    """
    return [x.strip() for x in line_segments.split("->") if x.strip != ""]


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        ANSWER = process_list(input_file.readlines())
    print(f"Answer: {ANSWER}")
