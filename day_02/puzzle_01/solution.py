def process_input(lines: list):
    '''
    Splits the input into the elf shape and my shape for a game of rock paper scissors.
    Elf's shapes for rock, paper, scissors are a, b, c
    My shapes for rock, paper, scissors is x, y, z
    '''
    total = 0
    for line in lines:
        if line != "":
            [elf_shape, my_shape] = line.split()
            total += get_round_score(elf_shape, my_shape)
    print(f"total: {total}")

def get_round_score(elf_shape: str, my_shape: str):
    '''
    A round of rock paper scissors awards points for each shape as well as the outcome
    '''
    shape_score = get_shape_score(my_shape)
    outcome_score = get_outcome_score(elf_shape, my_shape)
    return shape_score + outcome_score

def get_shape_score(my_shape: str):
    '''
    A shape score for shapes rock, paper, scissors as represented by x, y, z is 1, 2, 3
    '''
    if my_shape.lower() == "x":
        return 1
    if my_shape.lower() == "y":
        return 2
    if my_shape.lower() == "z":
        return 3
    return 0

def get_outcome_score(elf_shape: str, my_shape: str):
    '''
    Plays a game of rock paper scissors.
    Elf's shapes for rock, paper, scissors is a, b, c
    My shapes for rock, paper scissors is x, y, z
    Points for lose, draw, win are 0, 3, 6
    '''
    print(f"elf:{elf_shape} me:{my_shape}")
    if elf_shape.lower() == "a" and my_shape.lower() == 'x':
        return 3
    if elf_shape.lower() == "a" and my_shape.lower() == 'y':
        return 6
    if elf_shape.lower() == "a" and my_shape.lower() == 'z':
        return 0
    if elf_shape.lower() == "b" and my_shape.lower() == 'x':
        return 0
    if elf_shape.lower() == "b" and my_shape.lower() == 'y':
        return 3
    if elf_shape.lower() == "b" and my_shape.lower() == 'z':
        return 6
    if elf_shape.lower() == "c" and my_shape.lower() == 'x':
        return 6
    if elf_shape.lower() == "c" and my_shape.lower() == 'y':
        return 0
    if elf_shape.lower() == "c" and my_shape.lower() == 'z':
        return 3
    return 0

if __name__ == "__main__":
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_input(input_file.readlines())
