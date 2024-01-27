import argparse
import random
import sys
import string
from utils import main as generate_meme



parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args(sys.argv[1:2])
if args.command == 'randstr':
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', '-c',  type=int, default=10)
    args = parser.parse_args(sys.argv[2:])
    res = ''
    for i in range(args.count):
        res += random.choice(string.digits + string.ascii_letters + string.punctuation)
    print(res)
elif args.command == 'mkmem':
    generate_meme(args_i=2)
