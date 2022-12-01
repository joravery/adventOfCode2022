def find_max(lines: list):
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
    with open("../input.txt", "r") as input_file:
        max_calories = find_max(input_file.readlines())
        print(f"The maximum calories carried by any elf is: {max_calories}")