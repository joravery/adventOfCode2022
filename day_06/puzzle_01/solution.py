def process_signall(signal: str):
    for i in range(4, len(signal)-4):
        if len(set(signal[i-4:i])) ==4 :
            print(f"len(set(signal)): {len(set(signal[i-4:i]))}, signal: {signal[i-4:i]}")
            print(f"First four characters end at: {i}")
            return


if __name__ == "__main__":
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_signall(input_file.readlines()[0])