import day_09.puzzle_01.solution as s

TEST_INPUT = ["U 2", "L 2", "R 1", "L 2", "D 1", "U 1", "R 4", "D 1", "U 4", "R 4", "L 3", "U 3", "D 3"]
# def test_basic_happy_path():
#     assert s.process_list(TEST_INPUT) == 12

def test_left_right():
    assert s.process_list(["L 2", "R 1", "R 1", "R 2"]) == 3

def test_up_down():
    assert s.process_list(["U 2", "D 1", "D 3"]) == 3

def test_up_left():
    assert s.process_list(["U 3", "L 3"]) == 5

def test_down_left():
    assert s.process_list(["D 3", "L 3"]) == 5

def test_down_right():
    assert s.process_list(["D 3", "R 3"]) == 5

def test_up_right():
    assert s.process_list(["U 3", "R 3"]) == 5
