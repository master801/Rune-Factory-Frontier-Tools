# Rune Factory Frontier Scripts


## Info

Please give credit where it's due if using my tool.</br>
I've put too much work and effort into this only to be discredited. I don't want to end up keeping these tools for private use only and would rather share them publicly.


## Before using:

Install [Python](https://www.python.org/downloads/) (project was made using [3.7.0](https://www.python.org/downloads/release/python-370/))</br>
Install [kaitaistruct](https://pypi.org/project/kaitaistruct/) with the command: `pip install kaitaistruct`</br>



## Extraction

To extract the file `RUNEFACTORY.dat`, you must have the header file  `RUNEFACTORY.bin` using the script [`main_bin_dat.py`](#main_bin_dat)


## Usage

#### [main_bin_dat.py](#main_bin_dat)

Extracts `RUNEFACTORY.dat` using the header file `RUNEFACTORY.bin`

##### Arguments:
- `--bin` [`BIN_FILE`] - `RUNEFACTORY.bin`
- `--dat` [`DAT_FILE`] - `RUNEFACTORY.dat`
- `--output` [`OUTPUT DIRECTORY`] - Directory to output extracted files
- `--no_map` - If extracted files should be remapped to its correct name. This argument is not needed unless you know what you're doing

##### Example usage:
```
python main_bin_dat.py --bin=RUNEFACTORY.bin --dat=RUNEFACTORY.dat --output=OUTPUT_DIR
```

#### main_fbti.py

**TODO**
