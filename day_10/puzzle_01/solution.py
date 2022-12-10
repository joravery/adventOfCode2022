def process_instructions(instructions: list):
    '''
    Iterate through all instructions and execute them, checking for a special clock value after each clock tick
    '''
    clock = 0
    running_signal_strenth = 0
    register_value = 1
    for instruction in instructions:
        command, argument = parse_instruction(instruction)
        if command == 'noop':
            clock += 1
            running_signal_strenth += check_for_special_clock_timing(clock, register_value)
        if command == 'addx':
            add_time = 2
            while( add_time > 0):
                clock += 1
                running_signal_strenth += check_for_special_clock_timing(clock, register_value)
                add_time -= 1
            register_value += int(argument)
    return running_signal_strenth

def check_for_special_clock_timing(clock: int, register_value: int):
    '''
    In the event one of the magical clock values is encountered return the signal strenght; the product of clock cycle and register value
    '''
    if clock in [20, 60, 100, 140, 180, 220, 260]:
        print(f"clock: {clock}, register_value: {register_value}")
        return register_value * clock
    return 0

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
    print(f"Signal Strength: {FINAL_SIGNAL_STRENGTH}")
