import math

def process_crate_stacks(stacks: list, instructions: list):
    '''
    Executes each instruction to move boxes between stacks and prints out the top most box of each stack when done
    '''
    for instruction in instructions:
        count, source, destination = parse_single_instruction(instruction)
        for _ in range(count):
            box = stacks[source].pop()
            stacks[destination].append(box)
    return stacks


def parse_single_instruction(instruction: str):
    '''
    Returns the number of boxes to move from one stack to another based on the instruction format:
    'move 3 from 3 to 9'
    '''
    [_, count, _ ,  source, _, destination] = instruction.split()
    count = int(count)
    source = int(source)
    destination = int(destination)
    return count, source, destination


def create_initial_stacks(stack_rows: list):
    '''
    Parser to create a list of lists representing starting package stacks.
    Creates an empty first element to make indexing easier when processing the move instructions
    '''
    stacks = []
    # Each stack is represented by 4 characters, and each row has a \n which requires taking the floor
    num_stacks = int(math.floor(len(stack_rows[0])/4))

    # Add an extra empty array here
    for i in range(0, num_stacks+1):
        stacks.append([])

    for row in stack_rows:
        for i in range(0, num_stacks):
            box = row[i*4 +1]
            if box != " ":
                # place the box into a 1-indexed system instead of 0
                stacks[i+1].insert(0, box)

    return stacks

def parse_input(input_lines: list):
    '''
    Splits the input into two sections: The initial crate stacks and the list of instrucitons.
    Between the two is an empty line.
    There is also a row of indicies after the crate stacks which is skipped.
    '''
    split = input_lines.index("\n")
    return (input_lines[0:split-1], input_lines[split+1:])

if __name__ == "__main__":
    # Assumes a list of lines as input
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        stack_lines, instructions = parse_input(input_file.readlines())
        stacks = create_initial_stacks(stack_lines)
        udpated_stacks = process_crate_stacks(stacks, instructions)
        print(''.join([x[-1] for x in stacks[1:]]))
