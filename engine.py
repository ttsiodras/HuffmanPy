#!/usr/bin/env python
"""
Huffman compression engine.

Modified (type-safe) version of:
    https://rosettacode.org/wiki/Huffman_coding#Python

"""
from typing import List, Dict, Tuple

from heapq import heappush, heappop, heapify
from collections import Counter

# The types used by the Huffman compression engine.
Symbol = int          # Our input data are just bytes
Weight = int          # We count their frequencies via Counter
BinaryString = str    # ...and encoded them into a binary string
HuffmanTable = List[Tuple[Symbol, BinaryString]]  # via this.

# Types needed during encoding
HeapEntry = Tuple[Weight, HuffmanTable]
Heap = List[HeapEntry]


# Let's make a Huffman table...
def make_huffman_table(
        symbol_to_weight: Dict[Symbol, Weight]) -> HuffmanTable:
    """
    From a dict of symbols to weights, make a Huffman table.
    Since our symbols are integers, the end result is a table of
    (integer, binary string to use for this integer).
    """
    heap = [
        (wt, [(sym, "")])
        for sym, wt in symbol_to_weight.items()]  # type: Heap
    heapify(heap)
    while len(heap) > 1:
        lo_weight, lo_entries = heappop(heap)
        hi_weight, hi_entries = heappop(heap)
        new_lo_entries = [
            (symbol, '0' + binary_string)
            for symbol, binary_string in lo_entries]
        new_hi_entries = [
            (symbol, '1' + binary_string)
            for symbol, binary_string in hi_entries]
        heappush(
            heap,
            (lo_weight + hi_weight, new_lo_entries + new_hi_entries))
    _, huffman_data = heappop(heap)
    return sorted(huffman_data, key=lambda p: (p[0], len(p[-1])))


def encode_with_table(
        huffman_table: HuffmanTable, data: List[Symbol]) -> BinaryString:
    """
    Huffman-encode a list of symbols, using a pre-computed
    Huffman table. Returns compressed output as a binary string.
    """
    compressed_output = []
    condensed_huffman_lookup = dict(huffman_table)
    for value in data:
        compressed_output.append(condensed_huffman_lookup[value])
    return ''.join(compressed_output)


def encode(data: List[Symbol]) -> Tuple[HuffmanTable, BinaryString]:
    """
    Huffman-encode a list of symbols.
    Returns the created Huffman table and the compressed output
    as a binary string.
    """
    symbol_to_weight = Counter(data)
    huffman_table = make_huffman_table(symbol_to_weight)
    compressed_output = encode_with_table(huffman_table, data)
    return huffman_table, compressed_output


def decode(
        huffman_table: HuffmanTable,
        compressed_input: BinaryString) -> List[Symbol]:
    """
    Decompress a compressed Huffman binary string input
    via a Huffman table. Returns list of symbols.
    """
    decompressed_output = []
    while compressed_input:
        for sym, binary_string in huffman_table:
            if compressed_input.startswith(binary_string):
                decompressed_output.append(sym)
                compressed_input = compressed_input[len(binary_string):]
                break
        else:
            print("[x] Invalid data! Aborting...")   # pragma: no cover
            return []   # pragma: no cover
    return decompressed_output
