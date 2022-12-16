import day_15.puzzle_01.solution as s

FIRST_PROVIDED_INPUT = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
]

def test_forty_nine_seconds():
    assert s.process_list([
        "Sensor at x=1999954, y=1997417: closest beacon is at x=1996860, y=2000000"
    ], 2000000) == 6188

def test_ten_seconds():
    assert s.process_list([
        "Sensor at x=1999954, y=1997417: closest beacon is at x=1999860, y=2000000"
    ], 2000000) == 188

def test_first_line_N_seconds():
    assert s.process_list([
        "Sensor at x=1259754, y=1927417: closest beacon is at x=1174860, y=2000000"
    ], 2000000) == 169788

def test_process_list():
    assert s.process_list(FIRST_PROVIDED_INPUT, 10) == 26

def test_input_parsing():
    assert s.parse_input_location(FIRST_PROVIDED_INPUT[0]) == ((2, 18), (-2,15))

def test_occupied_count():
    occupied_map = {
        2: [[1,3], [4,5]]
    }
    beacon_map = set()
    assert s.find_occupied_position_count_for_row(2, occupied_map, beacon_map) == 3
