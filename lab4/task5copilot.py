def count_lines_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())

if __name__ == "__main__":
    num_lines = count_lines_in_file('a.txt')
    print(f"Number of lines in a.txt: {num_lines}")