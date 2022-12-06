def process_signall(signal: str):
    for i in range(14, len(signal)-14):
        if len(set(signal[i-14:i])) ==14 :
            print(f"len(set(signal)): {len(set(signal[i-14:i]))}, signal: {signal[i-14:i]}")
            print(f"First four characters end at: {i}")
            return


if __name__ == "__main__":
    with open("../input.txt", "r", encoding="utf-8") as input_file:
        process_signall(input_file.readlines()[0])