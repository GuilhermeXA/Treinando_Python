def count_substrings(s):
    unique_substrings = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            unique_substrings.add(s[i:j+1])
    return len(unique_substrings)

def main():
    while True:
        try:
            instructions = input()
            result = 0
            string = ""
            for instr in instructions:
                if instr == "?":
                    result += count_substrings(string)
                else:
                    string += instr
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()
