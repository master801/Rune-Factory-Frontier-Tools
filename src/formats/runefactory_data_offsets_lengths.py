# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class RunefactoryDataOffsetsLengths(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._io.ensure_fixed_contents(b"\x4E\x4C\x43\x4D")
        self.idk_1 = self._io.read_u4be()
        self.idk_2 = self._io.read_u4be()
        self.entries = self._io.read_u4be()
        self.idk_3 = self._io.read_u4be()
        self.data_file_name = self._io.ensure_fixed_contents(b"\x52\x55\x4E\x45\x46\x41\x43\x54\x4F\x52\x59\x2E\x64\x61\x74")
        self.padding = self._io.read_bytes(21)
        self._raw_entry_headers = [None] * (self.entries)
        self.entry_headers = [None] * (self.entries)
        for i in range(self.entries):
            self._raw_entry_headers[i] = self._io.read_bytes(16)
            io = KaitaiStream(BytesIO(self._raw_entry_headers[i]))
            self.entry_headers[i] = self._root.Entry(io, self, self._root)


    class Entry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u4be()
            self.padding_1 = self._io.read_bytes(4)
            self.offset = self._io.read_u4be()
            self.padding_2 = self._io.read_bytes(4)



