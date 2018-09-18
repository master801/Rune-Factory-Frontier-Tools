#!/usr/bin/env python3

import argparse
import os

if not __debug__:
    from src import mode
    from src.bin_dat import extract
else:
    import mode
    from bin_dat import extract


def __main__():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--bin', dest='bin', required=True, nargs=1, type=str)  # bin
    arg_parser.add_argument('--dat', dest='dat', required=True, nargs=1, type=str)  # dat
    arg_parser.add_argument('--out', dest='out', required=True, nargs=1, type=str)
    arg_parser.add_argument('--mode', dest='mode', choices=[mode.EXTRACT, mode.CREATE], required=True, nargs=1, type=str)
    arg_parser.add_argument('--no_map', dest='no_map', required=False, action='store_true')
    args = arg_parser.parse_args()

    _bin = args.bin[0]
    dat = args.dat[0]
    out = args.out[0]
    _mode = args.mode[0]
    no_map = args.no_map

    func_mode(_mode, _bin, dat, out, no_map)
    return


def func_mode(_mode, _bin, dat, output, should_not_map):
    if _mode.upper() == mode.EXTRACT:
        if dat is None:
            print('Argument \"{0}\" not specified for mode \"{1}\"'.format('input_2', _mode))
            return

        if not os.path.isfile(_bin):
            print('Bin file does not exist!')
            return

        if not os.path.isfile(dat):
            print('Dat file does not exist!')
            return

        if os.path.exists(output) and not os.path.isdir(output):
            print('Specified output directory is not a directory!')
            return
        elif not os.path.exists(output):
            print('Output directory \"{0}\" does not exist... creating...'.format(output))
            os.mkdir(output, 0o775)
            pass

        _extract(_bin, dat, output, should_not_map)
        pass
    elif _mode.upper() == mode.CREATE:
        _create(_bin, output)
        pass
    return


def _extract(_bin, dat, output_dir, should_not_map):
    print('Parsing bin file...')
    parsed_bin_file = extract.parse_bin_file(_bin)
    print('Found {0} entries from bin file'.format(parsed_bin_file.entries))
    print()  # Pretty

    mapped_bin_file = extract.parse_headers(should_not_map, parsed_bin_file)
    print()  # Pretty
    print()  # Pretty

    if mapped_bin_file is None:
        print('Failed to parse bin and dat files!')
        return

    print('Extracting from dat file...')
    print()  # Pretty
    extract.extract_dat_file(mapped_bin_file, dat, output_dir)
    return


def _create(input_1, output):
    print('TODO')
    # create.create()  # TODO
    return


if __name__ == '__main__':
    __main__()
    pass
