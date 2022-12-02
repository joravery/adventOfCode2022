def process_input(lines: list):
    '''
    Splits the input into the elf shape and desired outcome for a game of rock paper scissors.
    Elf's shapes for rock, paper, scissors are a, b, c
    Desired outcome for lose, win, draw is x, y, z
    '''
    total = 0
    for line in lines:
        if line != "":
            [elf_shape, desired_outcome] = line.split()
            my_shape = get_my_shape(elf_shape, desired_outcome)
            total += get_round_score(elf_shape, my_shape)
    print(f"total: {total}")

def get_my_shape(elf_shape: str, desired_outcome: str):
    '''
    Given elf's shape and a desired outcome the correct shape to play is returned
    Desired outcome for lose, win, draw is x, y, z
    Elf shape for rock, paper, scissors is a, b, c
    Opposing shape to play for rock, paper, scissors is X, Y, Z
    '''
    if elf_shape.lower() == "a" and desired_outcome.lower() == 'x':
        return "Z"
    if elf_shape.lower() == "a" and desired_outcome.lower() == 'y':
        return "X"
    if elf_shape.lower() == "a" and desired_outcome.lower() == 'z':
        return "Y"
    if elf_shape.lower() == "b" and desired_outcome.lower() == 'x':
        return "X"
    if elf_shape.lower() == "b" and desired_outcome.lower() == 'y':
        return "Y"
    if elf_shape.lower() == "b" and desired_outcome.lower() == 'z':
        return "Z"
    if elf_shape.lower() == "c" and desired_outcome.lower() == 'x':
        return "Y"
    if elf_shape.lower() == "c" and desired_outcome.lower() == 'y':
        return "Z"
    if elf_shape.lower() == "c" and desired_outcome.lower() == 'z':
        return "X"
    return "F"

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
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_input(input_file.readlines())
