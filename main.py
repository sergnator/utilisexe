import argparse
import random
import sys
import string
from utils import main as generate_meme
from constants import *

commands = ['randstr', 'mkmem', 'newns', 'sort']

parser = argparse.ArgumentParser()
parser.add_argument('command', choices=commands)
parser.add_argument('--version', '-ver', action='version', version=VERSION)
args = parser.parse_args(sys.argv[1:2])
if args.command == 'randstr':
    parser = argparse.ArgumentParser(description='generate random string with length = count')
    parser.add_argument('--version', '-ver', action='version', version=VERSION)
    parser.add_argument('--count', '-c', type=int, default=10)
    args = parser.parse_args(sys.argv[2:])
    res = ''
    for i in range(args.count):
        res += random.choice(string.digits + string.ascii_letters + string.punctuation)
    print(res)

elif args.command == 'mkmem':
    generate_meme(args_i=2)

elif args.command == 'newns':
    parser = argparse.ArgumentParser(description='transfer to decimal number')
    parser.add_argument('int', metavar='number')
    parser.add_argument('--base', type=int, default=2, help='choose base for int')
    args = parser.parse_args(sys.argv[2:])
    try:
        print(int(args.int, args.base))
    except ValueError as e:
        print(f'ERROR: the number {args.int} is not in the base {args.base} number system')

elif args.command == 'sort':
    parser = argparse.ArgumentParser(description='sort files or text')
    parser.add_argument('text', nargs='*', help='text for sorting')
    parser.add_argument('--version', '-ver', action='version', version=VERSION)
    parser.add_argument('--input-file', '-infile', help='file where text for sorting')
    parser.add_argument('--output-file', '-outfile', default=False, help='file where text saving')
    parser.add_argument('--reverse', '-rev', action='store_true', help='reverse flag')
    parser.add_argument('--upper', '-up', action='store_true', help='upper flag')
    parser.add_argument('--lower', '-l', action='store_true', help='lower flag')
    parser.add_argument('--capitalize', '-cap', action='store_true', help='capitalize flag')
    parser.add_argument('--separation', '-sep', default='\n', help='separation text')
    args = parser.parse_args(sys.argv[2:])
    text = args.input_file

    if not args.input_file:
        text = args.text[:]
    else:
        try:
            with open(text, 'r') as f:
                text = f.readlines()
        except FileNotFoundError:
            print(f'ERROR: No such file or directory: "{args.input_file}"')
            sys.exit()

    text.sort(reverse=args.reverse)

    if args.upper:
        text = list(map(lambda x: x.upper(), text))

    if args.lower:
        text = list(map(lambda x: x.lower(), text))

    if args.capitalize:
        text = list(map(lambda x: x.capitalize(), text))
    text = list(map(str.strip, text))
    text = args.separation.join(text)

    if not args.output_file:
        print(text)
    else:
        with open(args.output_file, 'w') as f:
            f.write(text)

