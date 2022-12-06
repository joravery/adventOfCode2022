import day_06.puzzle_01.solution as s

def test_basic_happy_path():
    assert s.find_first_unique_substring("avavbkvoilli", 4) == 6
    assert s.find_first_unique_substring("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert s.find_first_unique_substring("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert s.find_first_unique_substring("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert s.find_first_unique_substring("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

def test_ends_contain_unique():
    assert s.find_first_unique_substring("avcdbkvoilli", 4) == 4
    assert s.find_first_unique_substring("avadakaoabc", 4) == 11

def test_no_answer():
    assert s.find_first_unique_substring("avcaacaaccacac", 4) == -1

def test_no_invalid_string_length():
    assert s.find_first_unique_substring("avcaacaaccacac", 99) == -1

def test_different_substring_lengths():
    assert s.find_first_unique_substring("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert s.find_first_unique_substring("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert s.find_first_unique_substring("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert s.find_first_unique_substring("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert s.find_first_unique_substring("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
