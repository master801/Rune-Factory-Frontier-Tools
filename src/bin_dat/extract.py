#!/usr/bin/env python3

import os
from pathlib import Path

if not __debug__:
    from src.formats import runefactory_data_offsets_lengths
    from src.bin_dat.constants import FILE_ENTRY_MAPPING
else:
    from formats import runefactory_data_offsets_lengths
    from bin_dat.constants import FILE_ENTRY_MAPPING


def parse_bin_file(bin_file_path):
    bin_file = open(bin_file_path, 'r+b')
    try:
        parsed = runefactory_data_offsets_lengths.RunefactoryDataOffsetsLengths.from_io(bin_file)
        pass
    finally:
        bin_file.close()
        pass
    return parsed


def parse_headers(should_not_map, parsed_bin_file):
    if parsed_bin_file.entries != 1931:  # Must have 1391 entries, otherwise mapping will not work
        print('Bin file does not have exactly 1931 entries!')
        return None

    if not should_not_map:
        print('Has {0} current mapped entries'.format(len(FILE_ENTRY_MAPPING)))
        print()  # Pretty
        print()  # Pretty
        pass

    mapped_files = []

    for entry_index in range(parsed_bin_file.entries):
        entry_header = parsed_bin_file.entry_headers[entry_index]

        if (entry_index not in FILE_ENTRY_MAPPING) or should_not_map:  # Do not map if not in mapping or if we should not map, from the program argument
            file_name = 'entry' + str(entry_index) + '.bin'
            print('Entry {0} is not yet mapped. File name \"{1}\" will be used instead.'.format(entry_index, file_name))
            pass
        else:
            file_name = FILE_ENTRY_MAPPING[entry_index]
            print('Entry {0} has been mapped as \"{1}\"'.format(entry_index, file_name))
            pass

        mapped_files.append([file_name, entry_header])
        continue

    return mapped_files


def extract_dat_file(mapped_bin_file, dat_file_path, output_dir):
    dat_file = open(dat_file_path, 'r+b')

    for mapped_entry_index in range(len(mapped_bin_file)):
        mapped_entry = mapped_bin_file[mapped_entry_index]

        file_name = mapped_entry[0]
        mapped_entry_header = mapped_entry[1]

        offset = mapped_entry_header.offset
        size = mapped_entry_header.size

        dat_file.seek(offset)
        read_bytes = dat_file.read(size)

        entry_file_path = '{0}/{1}'.format(output_dir, file_name)

        path = Path(file_name)

        if path.parent.name is not '':
            new_dir = '{0}/{1}'.format(output_dir, str.join('/', path.parent.parts))
            if not os.path.isdir(new_dir):
                # os.mkdir(new_dir, 0o775)
                os.makedirs(new_dir, 0o775)
                pass

        entry_file = None
        if os.path.exists(entry_file_path) and os.path.isfile(entry_file_path):
            entry_file = open(entry_file_path, 'w+b')
            pass
        elif not os.path.exists(entry_file_path):
            entry_file = open(entry_file_path, 'x+b')
            pass

        try:
            entry_file.write(read_bytes)
            pass
        finally:
            entry_file.close()
            pass

        print('Extracted entry ({0}) \"{1}\" to \"{2}\"'.format(mapped_entry_index, file_name, output_dir))
        continue

    dat_file.close()
    return None
