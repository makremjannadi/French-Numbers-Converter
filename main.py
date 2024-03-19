import argparse
from Classes.NumberConverter import NumberConverter

def main(number):
    # initiate a converter
    converter = NumberConverter(number)

    # convert french number
    result = converter.convert()
    print(f'The string version of the number {number} is: {result}')

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create a parser')
    parser.add_argument('--number', metavar='number', required=True,
                        help='The number to convert')
    args = parser.parse_args()

    main(number=args.number)