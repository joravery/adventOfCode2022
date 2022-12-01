def top_three(lines: list):
    max_calories = [0,0,0]
    elf_calories = 0
    for line in lines:
        if line == "\n":
            for i in range(0, len(max_calories)):
                if elf_calories > max_calories[i]:
                    max_calories.insert(i, elf_calories)
                    max_calories = max_calories[:3]
                    break
            elf_calories = 0
        else:
            elf_calories += int(line)
    return max_calories

if __name__ == "__main__":
    with open("../input.txt", "r") as input_file:
        top_three_calories = top_three(input_file.readlines())
        print(f"The top three elves are carrying: {top_three_calories} for a total of {sum(top_three_calories)}")