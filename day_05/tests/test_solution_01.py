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
    input_file_contents = ["    [V]    \n",
             "[T] [J]    \n",
             "[C] [S]    \n",
             "[H] [G] [Z]\n",
             " 1   2   3",
             "\n",
             "move 5 from 8 to 2",
             "move 2 from 4 to 5",
             "move 3 from 3 to 9"]
    stack_lines, instruction_lines = s.parse_input(input_file_contents)
    assert stack_lines == [
            "    [V]    \n",
            "[T] [J]    \n",
            "[C] [S]    \n",
            "[H] [G] [Z]\n"]
    assert instruction_lines == [
            "move 5 from 8 to 2",
            "move 2 from 4 to 5",
            "move 3 from 3 to 9"]

def test_crate_mover():
    input_file_contents = ["    [V]    \n",
             "[T] [J]    \n",
             "[C] [S]    \n",
             "[H] [G] [Z]\n",
             " 1   2   3",
             "\n",
             "move 1 from 2 to 3",
             "move 2 from 3 to 1",
             "move 4 from 1 to 3"]
    stack_lines, instruction_lines = s.parse_input(input_file_contents)
    crate_stacks = s.create_initial_stacks(stack_lines)
    updated_crate_stacks = s.process_crate_stacks(crate_stacks, instruction_lines)
    assert updated_crate_stacks[1] == ["H",]
    assert updated_crate_stacks[2] == ["G", "S", "J"]
    assert updated_crate_stacks[3] == ["Z", "V", "T", "C"]
