from HuffmanPy.engine import encode, decode


def test_round_trips() -> None:
    import random
    TESTS = 5000
    data = [
        10 if random.randint(0, 10) < 7
        else random.randint(0, 65536)
        for i in range(TESTS)]
    huffman_table, encoded_bitstream = encode(data)
    decoded_data = decode(huffman_table, encoded_bitstream)
    print("[-] Compression ratio: %5.2f%%\n" % (
        100.*len(encoded_bitstream) / (TESTS*16)))
    assert data == decoded_data
