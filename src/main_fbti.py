#!/usr/bin/env python3

import argparse

if not __debug__:
    from src import mode
else:
    import mode


def __main__():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--mode', dest='mode', required=True, type=str, choices=[mode.EXTRACT, mode.CREATE])
    arg_parser.add_argument('--input', dest='input', required=True, type=str, nargs=1)
    arg_parser.add_argument('--output', dest='input', required=True, type=str, nargs=1)
    args = arg_parser.parse_args()

    _mode = args.mode
    input = args.input[0]
    output = args.output[0]

    if _mode == mode.EXTRACT:
        extract()
    elif _mode == mode.CREATE:
        create()
    else:
        print('Something bad happened! Mode was not detected?!')
        return

    print('')
    return


def extract():
    return


def create():
    return


if __name__ == '__main__':
    __main__()
