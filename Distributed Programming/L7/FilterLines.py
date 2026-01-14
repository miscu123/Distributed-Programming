def filter_lines(input_filename, output_filename, key_word):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            if line.__contains__(key_word):
                outfile.write(line)


keyword = input("Enter a keyword: ")
filter_lines("input.txt", "output.txt", keyword)