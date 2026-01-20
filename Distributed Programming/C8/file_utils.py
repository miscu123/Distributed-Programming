def read_txt(filename):
    with open(filename, 'r') as f:
        content = f.read().split()
        numbers = [int(x) for x in content]

    return numbers

def write_txt(filename, content):
    with open(filename, 'w') as f:
        f.write(str(content))