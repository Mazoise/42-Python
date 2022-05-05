import sys


def print_error():
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('    python operation.py 10 3')
    exit()


def main(args=None):
    if (args is None or len(args) != 2):
        if len(args) == 1:
            print('InputError: too few arguments\n')
        elif len(args) > 2:
            print('InputError: too many arguments\n')
        print_error()
    try:
        a = int(args[0])
        b = int(args[1])
        print('Sum:       ', int(args[0]) + int(args[1]))
        print('Difference:', int(args[0]) - int(args[1]))
        print('Product:   ', int(args[0]) * int(args[1]))
        if int(args[1]) == 0:
            print('Quotient:   ERROR (div by zero)')
            print('Remainder:  ERROR (modulo by zero)')
        else:
            print('Quotient:  ', int(args[0]) / int(args[1]))
            print('Remainder: ', int(args[0]) % int(args[1]))
    except ValueError:
        print('InputError: only numbers\n')
        print_error()


if __name__ == '__main__':
    main(sys.argv[1::])
