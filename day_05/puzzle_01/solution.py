
stack_one = ["Q","M","G","C","L"]
stack_two = ["R","D","L","C","T","F","H","G"]
stack_three = ["V","J","F","N","M","T","W","R"]
stack_four = ["J","F","D","V","Q","P"]
stack_five = ["N","F","M","S","L","B","T"]
stack_six = ["R","N","V","H","C","D","P"]
stack_seven = ["H","C","T"]
stack_eight = ["G","S","J","V","Z","N","H","P"]
stack_nine = ["Z","F","H","G"]

stacks = [[], stack_one, stack_two, stack_three, stack_four, stack_five, stack_six, stack_seven, stack_eight, stack_nine]

def process_crate_stacks(instructions: list):
    for instruction in instructions:
        [_, count, _ ,  source, _, destination] = instruction.split()
        count = int(count)
        source = int(source)
        destination = int(destination)
        for i in range(count):
            box = stacks[source].pop()
            stacks[destination].append(box)
        
    message = [x[-1] for x in stacks[1:]]
    print(''.join(message))
        
if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_crate_stacks(input_file.readlines())
