meta:
  id: fbti
  file-extension: bin
seq:
  - id: header
    type: header
  - id: entries_amt
    type: u4be
  - id: type # idk what this does
    type: u4be
  - id: entry_headers
    type: entry_header
    repeat: expr
    repeat-expr: entries_amt
types:
  header:
    seq:
    - id: magic
      contents: [0x46, 0x42, 0x54, 0x49, 0x30, 0x30, 0x30, 0x31]
      size: 0x8
  entry_header:
    seq:
    - id: offset
      type: u4be
    - id: size
      type: u4be
