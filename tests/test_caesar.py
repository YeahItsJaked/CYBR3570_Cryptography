# It wouldn't find the crypto_toolkit module in the import statement, so that's why this is here.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from crypto_toolkit.classical.caesar import caesar_encrypt, caesar_decrypt, brute_force_caesar


def test_caesar_round_trip():
    msg = "Attack at dawn!"
    shift = 5
    assert caesar_decrypt(caesar_encrypt(msg, shift), shift) == msg


def test_caesar_known_value():
    assert caesar_encrypt("ABC XYZ", 3) == "DEF ABC"

# Run these inside the notebook for a quick check.
test_caesar_round_trip()
test_caesar_known_value()
print("Notebook tests passed.")
