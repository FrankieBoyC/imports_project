def save_to_file(contents, filename):
    with open(filename, 'w') as file:
        file.write(contents)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()