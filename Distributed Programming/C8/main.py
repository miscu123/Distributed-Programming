import file_utils
import analysis

def main():
    numbers = file_utils.read_txt('input.txt')

    mean = analysis.numbers_mean(numbers)
    mini, maxi = analysis.min_max(numbers)
    even = analysis.even_numbers(numbers)

    result = (
        f"Media: {mean}\n"
        f"Minim: {mini}\n"
        f"Maxim: {maxi}\n"
        f"Counter nr pare: {even}"
    )

    file_utils.write_txt('output.txt', result)

if __name__ == '__main__':
    main()
