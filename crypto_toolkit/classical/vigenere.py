"""
Module: crypto_toolkit.classical.vigenere

Educational implementation of the Vigenere cipher.

WARNING: This module is for learning only. Do not use the Vigenere cipher
to protect real information.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def vigenere_encrypt(plaintext: str, keyword: str) -> str:
    """Encrypt plaintext with a Vigenere cipher."""
    # TODO: Implement in Lab 01.
    raise NotImplementedError


def vigenere_decrypt(ciphertext: str, keyword: str) -> str:
    """Decrypt Vigenere ciphertext with a known shift."""
    # TODO: Implement in Lab 01.
    raise NotImplementedError


def vigenere_analysis(ciphertext: str) -> list[tuple[int, str]]:
    """Return analysis of various lengths of passphrase"""
    # TODO: Implement in Lab 01.
    raise NotImplementedError
