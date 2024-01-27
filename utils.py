import argparse
import sys

from be_like_bill_generate import create_image, gui
from constants import VERSION


def main(args_i=0):
    parser = argparse.ArgumentParser()
    parser.description = 'generate mem'
    parser.add_argument('--name', '-n', default='Билл')
    parser.add_argument('--text', '-t', default=['он знает сколько будет 2 + 2'], nargs='*',
                       help='create picture with your TEXT')
    parser.add_argument('--interface', '-gui', action='store_true')
    parser.add_argument('--version', '-ver', action='version', version=VERSION)
    args = parser.parse_args(sys.argv[args_i:])
    if args.interface:
        gui()
    else:
        create_image(args.name, ' '.join(args.text))


if __name__ == '__main__':
    main()
