import day_05.puzzle_01.solution as s

def test_stack_parser():
    input_stack_rows = ["    [V]    \n",
             "[T] [J]    \n",
             "[C] [S]    \n",
             "[H] [G] [Z]\n"]
    stacks = s.create_initial_stacks(input_stack_rows)
    assert len(stacks) == 4
    assert stacks[1] == ["H", "C", "T"]
    assert stacks[2] == ["G", "S", "J", "V"]
    assert stacks[3] == ["Z"]

def test_input_parser():
    input_file_contents = ["    [V]    ",
             "[T] [J]    ",
             "[C] [S]    ",
             "[H] [G] [Z]",
             " 1   2   3",
             "\n",
             "move 5 from 8 to 2",
             "move 2 from 4 to 5",
             "move 3 from 3 to 9"]
    stack_lines, instruction_lines = s.parse_input(input_file_contents)
    assert stack_lines == [
            "    [V]    ",
            "[T] [J]    ",
            "[C] [S]    ",
            "[H] [G] [Z]"]
    assert instruction_lines == [
            "move 5 from 8 to 2",
            "move 2 from 4 to 5",
            "move 3 from 3 to 9"]
