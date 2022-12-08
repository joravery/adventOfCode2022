import day_08.puzzle_02.solution as s
SQUARE_MAP_N_TREES = [
    [1,5,6,9],
    [9,3,9,1],
    [6,2,1,1],
    [1,4,7,8]
]

def test_maximum_total_score():
    assert s.find_maximum_visibility(SQUARE_MAP_N_TREES) == 4

def test_up_down_score():
    assert s.up_down_visibility(1, 1, SQUARE_MAP_N_TREES) == 2
    assert s.up_down_visibility(1, 2, SQUARE_MAP_N_TREES) == 2

def test_left_right_score():
    assert s.left_right_visibility(1, 1, SQUARE_MAP_N_TREES) == 1
    assert s.left_right_visibility(1, 2, SQUARE_MAP_N_TREES) == 2
