import math
from typing import Any


class Bitmap:
    def __init__(self, size: int) -> None:
        self.bytes = bytearray([0] * math.ceil(size / 8))

    def get(self, index: int) -> bool:
        return bool(self.bytes[index // 8] & pow(2, index % 8))

    def set(self, index: int):
        self.bytes[index//8] |= pow(2, index % 8)

    def __str__(self) -> str:
        return " ".join(['{0:08b}'.format(b) for b in self.bytes])

