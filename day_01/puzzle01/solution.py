def find_max(lines: list):
    '''
    Returns the total calories for the elf carrying the most calories
    An elf is a sequence of numbers in a list followed by a newline in the list
    '''
    max_calories = 0
    elf_calories = 0
    for line in lines:
        if line == "\n":
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line)
    return max_calories

if __name__ == "__main__":
    with open("../input.txt", "r", encoding='utf-8') as input_file:
        MAX_CALORIES = find_max(input_file.readlines())
        print(f"The maximum calories carried by any elf is: {MAX_CALORIES}")
