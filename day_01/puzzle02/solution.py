def top_three(lines: list):
    '''
    Returns the 3 elves who are carrying the most calories.
    An elf\'s calories is a sequence of non-newline characters in an array
    '''
    max_calories = [0,0,0]
    elf_calories = 0
    for line in lines:
        if line == "\n":
            for i, calories in enumerate(max_calories):
                if elf_calories > calories:
                    max_calories.insert(i, elf_calories)
                    max_calories = max_calories[:3]
                    break
            elf_calories = 0
        else:
            elf_calories += int(line)
    return max_calories

if __name__ == "__main__":
    with open("../input.txt", "r", encoding='utf-8') as input_file:
        TOP_THREE_CALORIES = top_three(input_file.readlines())
        print(f"The top three elves are carrying: {TOP_THREE_CALORIES} for a total of {sum(TOP_THREE_CALORIES)}")
