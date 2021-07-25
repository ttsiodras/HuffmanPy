This is my Python library for Huffman coding.
    
It is a modified, type-safe, and arguably better commented
version of
[this code](https://rosettacode.org/wiki/Huffman_coding#Python).
    
My updates include:

- lots of type-based commenting
- passing Flake8 tests
- passing Pylint tests
- passing Mypy tests (in strict mode).

In addition, I included simple tests reaching 100% coverage.

Typical output:

    $ make all
    ...
    ============================================
     Running flake8...
    ============================================
    .venv/bin/flake8 huffman.py test_huffman.py
    ...
    ============================================
     Running pylint...
    ============================================
    .venv/bin/pylint --disable=I --rcfile=pylint.cfg huffman.py test_huffman.py
    ...
    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

    ============================================
     Running mypy...
    ============================================
    .venv/bin/mypy --strict huffman.py test_huffman.py
    Success: no issues found in 2 source files
    ...
    ============================= test session starts ==============================
    platform linux -- Python 3.9.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- 
    collecting ... collected 1 item

    test_huffman.py::test_round_trips [-] Compression ratio: 31.45%

    PASSED

    ============================== 1 passed in 0.25s ===============================
    ...
    .venv/bin/coverage run -a -m pytest
    ============================= test session starts ==============================
    platform linux -- Python 3.9.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: /home/ttsiod/Github/HuffmanPy
    collected 1 item

    test_huffman.py .                                                        [100%]

    ============================== 1 passed in 0.81s ===============================
    [-] Coverage checking... 
    Name                                                                         Stmts   Miss  Cover
    ------------------------------------------------------------------------------------------------
    huffman.py                                                                      39      0   100%
    huffman_types.py                                                                 5      0   100%
    test_huffman.py                                                                  9      0   100%
    ------------------------------------------------------------------------------------------------
    TOTAL                                                                        17510   9366    47%
