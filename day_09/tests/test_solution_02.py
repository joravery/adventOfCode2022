import day_09.puzzle_02.solution as s

PROVIDED_PUZZLE_ONE_TEST = [
"R 4",
"U 4",
"L 3",
"D 1",
"R 4",
"D 1",
"L 5",
"R 2",
]

PROVIDED_PUZZLE_TWO_TEST = ["R 5",
"U 8",
"L 8",
"D 3",
"R 17",
"D 10",
"L 25",
"U 20"]

COMPLEX_TEST_INPUT = ["U 2", "L 2", "R 1", "L 2", "D 1", "U 1", "R 4", "D 1", "U 4", "R 4", "L 3", "U 3", "D 3"]

def test_solution_solves_both_puzzles():
    assert s.process_list(PROVIDED_PUZZLE_TWO_TEST)[1] == 36
    assert s.process_list(PROVIDED_PUZZLE_ONE_TEST)[1] == 1
    assert s.process_list(PROVIDED_PUZZLE_ONE_TEST)[0] == 13

def test_basic_happy_path():
    assert s.process_list(COMPLEX_TEST_INPUT)[0] == 12

def test_left_right():
    assert s.process_list(["L 2", "R 1", "R 1", "R 2"])[0] == 3

def test_up_down():
    assert s.process_list(["U 2", "D 1", "D 3"])[0] == 3

def test_up_left():
    assert s.process_list(["U 3", "L 3"])[0] == 5

def test_down_left():
    assert s.process_list(["D 3", "L 3"])[0] == 5

def test_down_right():
    assert s.process_list(["D 3", "R 3"])[0] == 5

def test_up_right():
    assert s.process_list(["U 3", "R 3"])[0] == 5
