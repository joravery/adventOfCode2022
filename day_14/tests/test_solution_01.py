import day_14.puzzle_01.solution as s

PROVIDED_TEST_INPUT_ONE = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]


def test_basic_happy_path():
    assert s.process_list(PROVIDED_TEST_INPUT_ONE) == 24


def test_parse_rock_formation():
    assert s.parse_rock_formation(PROVIDED_TEST_INPUT_ONE[0]) == ["498,4", "498,6", "496,6"]
    assert s.parse_rock_formation(PROVIDED_TEST_INPUT_ONE[1]) == ["503,4", "502,4", "502,9", "494,9"]


def test_get_line_points():
    cave_map = set()
    s.draw_line_between_points("2,4", "2,2", cave_map)
    for point in [(2, 2), (2, 3), (2, 4)]:
        assert point in cave_map


if __name__ == "__main__":
    test_basic_happy_path()
