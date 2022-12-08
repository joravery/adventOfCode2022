import day_08.puzzle_01.solution as s
THREE_VISIBLE_ROW = [9,3,9,1]
SQUARE_MAP_14_VISIBLE_TREES = [
    [1,5,6,9],
    THREE_VISIBLE_ROW,
    [6,2,1,1],
    [1,4,7,8]
]

def test_basic_happy_path():
    assert s.find_visible_trees(SQUARE_MAP_14_VISIBLE_TREES) == 14

def test_visibility_of_single_tree_left_right():
    assert not s.check_left_right(1, THREE_VISIBLE_ROW)
    assert s.check_left_right(2, THREE_VISIBLE_ROW)

def test_visibility_of_single_tree_up_down():
    assert not s.check_up_down(1, 1, SQUARE_MAP_14_VISIBLE_TREES)
    assert s.check_up_down(1, 2, SQUARE_MAP_14_VISIBLE_TREES)
