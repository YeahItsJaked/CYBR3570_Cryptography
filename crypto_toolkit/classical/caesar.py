"""
Module: crypto_toolkit.classical.caesar

Educational implementation of the Caesar cipher.

WARNING: This module is for learning only. Do not use the Caesar cipher
to protect real information.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypt plaintext using the Caesar cipher.

    This is an educational implementation only.
    Do not use this algorithm to protect real information.
    """
    result = []
    for ch in plaintext:
        if ch.upper() in ALPHABET:
            original_is_lower = ch.islower()
            n = char_to_num(ch.upper())
            encrypted = num_to_char(n + shift)
            result.append(encrypted.lower() if original_is_lower else encrypted)
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt Caesar ciphertext by reversing the shift."""
    return caesar_encrypt(ciphertext, -shift)


def brute_force_caesar(ciphertext: str) -> list[tuple[int, str]]:
    """Return all possible Caesar decryptions."""
    candidates = []
    for shift in range(26):
        candidates.append((shift, caesar_decrypt(ciphertext, shift)))
    return candidates
