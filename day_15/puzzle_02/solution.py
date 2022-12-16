from day_15.util import manhattan_distance
import re
from collections import defaultdict
from itertools import chain
from functools import reduce

def process_list(positions: list, max_val: int):
    occupied_map = defaultdict(list)
    beacon_map = set()
    for position in positions:
        sensor_coordinates, beacon_coordinates = parse_input_location(position)
        beacon_map.add(beacon_coordinates)
        beacon_distance = manhattan_distance(sensor_coordinates, beacon_coordinates)
        mark_positions_covered(sensor_coordinates, beacon_distance, occupied_map, beacon_map)
    empty_spots = find_un_occupied_positions(occupied_map, beacon_map, max_val)
    print(empty_spots)
    for k in empty_spots:
        print(k)
        print(f"{k[0] * 4000000 + k[1]}")
    return empty_spots[0][0] * 4000000 + empty_spots[0][1]


def mark_positions_covered(
    sensor_coordinates: tuple[int], distance_to_beacon: int, occupied_map: dict, beacon_map: set[tuple]
):
    sensor_x, sensor_y = sensor_coordinates
    for i in range(sensor_y - distance_to_beacon, sensor_y + distance_to_beacon + 1):
        y_dist = distance_to_beacon - abs(sensor_y - i)
        new_list_range =[sensor_x - y_dist, sensor_x + y_dist + 1]
        add_single_range_to_row(occupied_map[i], new_list_range)


def add_single_range_to_row(row_ranges_lists: list[list], new_range: list[int]):
    if len(row_ranges_lists) == 0:
        row_ranges_lists.append(new_range)
    else:
        new_left, new_right = new_range
        for i in range(len(row_ranges_lists)):
            existing_left, existing_right = row_ranges_lists[i]
            if new_left <= existing_left:
                if new_right >= existing_right:
                    row_ranges_lists[i] = new_range
                    merge_ranges_in_list(row_ranges_lists)
                    return
                elif existing_left <= new_right <= existing_right:
                    row_ranges_lists[i][0] = new_left
                    return
                else:
                    row_ranges_lists.insert(i, new_range)
                    return
            elif existing_left <= new_left <= existing_right:
                if existing_right >= new_right:
                    return
                if i == len(row_ranges_lists) - 1:
                    # at the end of list, append
                    row_ranges_lists.append(new_range)
                    return
                row_ranges_lists.insert(i+1, new_range)
                merge_ranges_in_list(row_ranges_lists)
                return
            else:
                # check next item since it isn't before or in current item
                continue
        # If we didn't insert and return, then append and no need to merge anything.
        row_ranges_lists.append(new_range)

def merge_ranges_in_list(row_lists: list[list]):
    i, j = 0, 1
    while j < len(row_lists):
        if ranges_overlap(row_lists[i], row_lists[j]):
            combine_ranges(row_lists[i], row_lists[j])
            j += 1
        else:
            i += 1
            row_lists[i] = row_lists[j]
            j += 1
    del row_lists[i+1:]

def ranges_overlap(range_1, range_2):
    return range_1[1] > range_2[0]

def combine_ranges(range_1: list, range_2: list):
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return
    range_1[0] = min(range_1[0], range_2[0])
    range_1[1] = max(range_1[1], range_2[1])

def combine_single_row(row: list[list[int]], max_val: int):
    return [range(x[0], x[1]) for x in row ]

def find_un_occupied_positions(occupied_map: dict, beacon_map: set[tuple], max_val: int):
    # Look through each row in the dict
    # Find the empty spots by set(range(search)) - set(row)
    print(f"Started the search for unoccupied space ..")
    search_space = set(range(0, max_val+1))
    possible_spots = []
    current_key = 0
    for row in occupied_map.keys():
        if row < 0 or row >=max_val:
            continue
        current_key += 1
        merge_ranges_in_list(occupied_map[row])
        ranges = combine_single_row(occupied_map[row], max_val)
        if len(ranges) == 1 and 0 in ranges[0] and max_val in ranges[0]:
            continue
        print(f"Found a non length 1 list: {ranges}")
        combined_range_object = set(reduce(chain, ranges))
        empty_spots = search_space - combined_range_object
        for spot in empty_spots:
            possible_spots.append((spot, row))
    return possible_spots


def parse_input_location(input_location: str):
    pattern = r"\w=(-?\d+)"
    m = re.findall(pattern, input_location)
    coordinates = [int(x) for x in m]
    return (coordinates[0], coordinates[1]), (coordinates[2], coordinates[3])


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        occupied_territories = process_list(input_file.readlines(), 4000001)
    print(f"Number of positions a beacon cannot exist: {occupied_territories}")
