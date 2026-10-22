"Diffie-Hellman Key Agreement Implementation"

import hashlib
import hmac
import secrets
from dataclasses import dataclass
from typing import Optional, Tuple, List


def dh_public(g: int, private: int, p: int) -> int:
    return pow(g, private, p)


def dh_shared(peer_public: int, private: int, p: int) -> int:
    return pow(peer_public, private, p)


def discrete_log_bruteforce(g: int, x: int, p: int) -> Optional[int]:
    for i in range(p):
        if pow(g, i, p) == x:
            return i
    return None

def int_to_bytes(x: int) -> bytes:
    """Convert a positive integer to big-endian bytes."""
    if x == 0:
        return b"\x00"
    length = (x.bit_length() + 7) // 8
    return x.to_bytes(length, "big")

def hkdf_extract(salt: bytes, ikm: bytes, hashmod=hashlib.sha256) -> bytes:
    """HKDF-Extract using HMAC."""
    return hmac.new(salt, ikm, hashmod).digest()

def hkdf_expand(prk: bytes, info: bytes, length: int, hashmod=hashlib.sha256) -> bytes:
    """HKDF-Expand for length bytes."""
    output = b""
    previous = b""
    counter = 1
    while len(output) < length:
        previous = hmac.new(prk, previous + info + bytes([counter]), hashmod).digest()
        output += previous
        counter += 1
    return output[:length]

def derive_session_key(shared_secret: int, context: bytes = b"CYBR3570-DH-demo", salt: bytes = b"CYBR3570 fixed demo salt") -> bytes:
    ikm = int_to_bytes(shared_secret)
    prk = hkdf_extract(salt, ikm)
    return hkdf_expand(prk, context, 32)


def is_generator(g: int, p: int) -> bool:
    return set(pow(g, k, p) for k in range(1,p)) == set(range(1, p))