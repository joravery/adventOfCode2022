def process_instructions(instructions: list):
    '''
    Iterate through all instructions and execute them, updating the screen after each clock tick
    '''
    clock = 0
    register_value = 1
    screen = []
    for instruction in instructions:
        command, argument = parse_instruction(instruction)
        if command == 'noop':
            clock += 1
            update_screen(register_value, clock, screen)
        if command == 'addx':
            add_time = 2
            while add_time > 0:
                clock += 1
                update_screen(register_value, clock, screen)
                add_time -= 1
            register_value += int(argument)
    return screen

def update_screen(register_value: int, clock, screen: list):
    '''
    The screen is 40px wide and 6px tall, but only addressable by a single int.
    The screen is updated every clock cycle, and will print a special character if the clock points at a pixel addressed to the register or either side
    '''
    if (clock-1) % 40 in [register_value-1, register_value, register_value+1]:
        screen.append("#")
    else:
        screen.append('.')

def parse_instruction(instruction: str):
    '''
    Return the parts of an instruction
    '''
    parts = instruction.split()
    if len(parts) == 1:
        parts.append(None)
    return parts


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as input_file:
        FINAL_SIGNAL_STRENGTH = process_instructions(input_file.readlines())
    for i in range(0, len(FINAL_SIGNAL_STRENGTH), 40):
        print(''.join(FINAL_SIGNAL_STRENGTH[i:i+40]))
