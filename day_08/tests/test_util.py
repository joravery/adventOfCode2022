from day_08.util import create_tree_map

SQUARE_INPUT = ["12", "34"]
RECTANGLE_INPUT = ["1234", "3456"]

def test_create_tree_map():
    assert create_tree_map(SQUARE_INPUT) == [[1, 2], [3,4]]
    assert create_tree_map(RECTANGLE_INPUT) == [[1, 2, 3, 4], [3, 4, 5, 6]]
