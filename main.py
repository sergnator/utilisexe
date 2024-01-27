import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args(sys.argv[1:2])
if args.command == 'randstr':
    parser.add_argument('--count', '-c',  type=int, default=10)
    args = parser.parse_args(sys.argv[2:])

else:

