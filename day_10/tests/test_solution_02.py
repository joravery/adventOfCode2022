import day_10.puzzle_02.solution as s

SAMPLE_INPUT = ["addx 15",
"addx -11",
"addx 6",
"addx -3",
"addx 5",
"addx -1",
"addx -8",
"addx 13",
"addx 4"
]

def test_basic_happy_path():
    assert s.process_instructions(SAMPLE_INPUT) == ['#', '#', '.', '.', '#', '#', '.', '.', '#', '#', '.', '.', '#', '#', '.', '.', '#', '#']
