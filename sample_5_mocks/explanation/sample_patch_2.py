def read_file_first_line(path):
    file = open(path, 'r')
    file_lines = file.readline()
    file.close()
    return file_lines


def get_first_line_length(path):
    line = read_file_first_line(path)
    return len(line)
