with open("../input.txt", "r") as input_file:
    max_calories = [0,0,0]
    elf_calories = 0
    for line in input_file.readlines():
        if line == "\n":
            for i in range(0, len(max_calories)):
                if elf_calories > max_calories[i]:
                    max_calories.insert(i, elf_calories)
                    max_calories = max_calories[:3]
                    break
            elf_calories = 0
        else:
            elf_calories += int(line)
    print(f"The top three elves are carrying: {max_calories} for a total of {sum(max_calories)}")
