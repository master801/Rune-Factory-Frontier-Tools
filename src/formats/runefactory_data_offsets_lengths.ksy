meta:
  id: runefactory_data_offsets_lengths
  file-extension: .bin
seq:
  - id: header
    size: 0x4
    contents: [0x4E, 0x4C, 0x43, 0x4D]
    doc: "Header of this table"
  - id: idk_1
    type: u4be
  - id: idk_2
    type: u4be
  - id: entries
    type: u4be
  - id: idk_3
    type: u4be
  - id: data_file_name
    size: 0xF
    contents: [0x52, 0x55, 0x4E, 0x45, 0x46, 0x41, 0x43, 0x54, 0x4F, 0x52, 0x59, 0x2E, 0x64, 0x61, 0x74]
    doc: "Name of the file containing the actual data"
  - id: padding
    size: 0x15
  - id: entry_headers
    type: entry
    size: 0x10
    repeat: expr
    repeat-expr: entries
types:
  entry:
    seq:
      - id: size
        type: u4be
      - id: padding_1
        size: 0x4
        doc: "Filled with zeros. Not sure what this is used for."
      - id: offset
        type: u4be
      - id: padding_2
        size: 0x4
        doc: "Filled with zeros. Not sure what this is used for."
