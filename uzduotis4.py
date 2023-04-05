
def read_in_lines(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            yield line[:-1]

read = read_in_lines('tekstas2.txt')

while True:
    try:
        print(next(read))
    except StopIteration:
        print("Baigta")
        break
