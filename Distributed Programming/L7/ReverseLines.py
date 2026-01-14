def reverse_lines(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            new_line = line.endswith('\n')

            if new_line:
                text = line[:-1] # luam linia fara \n
            else:
                text = line

            reversed_text = text[::-1]

            if new_line:
                outfile.write(reversed_text + '\n')
            else:
                outfile.write(reversed_text)


reverse_lines('input.txt', 'output.txt')