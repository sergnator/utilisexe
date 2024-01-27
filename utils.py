import argparse
import sys

from be_like_bill_generate import create_image, gui
def main(args_i=0):
    parse = argparse.ArgumentParser()
    parse.description = 'generate mem'
    parse.add_argument('--name', '-n', default='Билл')
    parse.add_argument('--text', '-t', default=['он знает сколько будет 2 + 2'], nargs='*',
                       help='create picture with your TEXT')
    parse.add_argument('--interface', '-gui', action='store_true')

    args = parse.parse_args(sys.argv[args_i:])
    if args.interface:
        gui()
    else:
        create_image(args.name, ' '.join(args.text))


if __name__ == '__main__':
    main()