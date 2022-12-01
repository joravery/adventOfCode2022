with open("../input.txt", "r") as input_file:
    max_calories = 0
    elf_calories = 0
    for line in input_file.readlines():
        if line == "\n":
            if elf_calories > max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line)
    print(f"The maximum calories carried by any elf is: {max_calories}")