 # Hashing, encryption, HMAC, key management

import hashlib
import hmac
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization


# ---------- HASHING ----------
def sha256_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------- SYMMETRIC ENCRYPTION ----------
def generate_symmetric_key():
    return Fernet.generate_key()


def encrypt_data(key: bytes, data: bytes) -> bytes:
    return Fernet(key).encrypt(data)


def decrypt_data(key: bytes, ciphertext: bytes) -> bytes:
    return Fernet(key).decrypt(ciphertext)


# ---------- ASYMMETRIC ENCRYPTION ----------
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    return private_key, private_key.public_key()


def rsa_encrypt(public_key, data: bytes) -> bytes:
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def rsa_decrypt(private_key, ciphertext: bytes) -> bytes:
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


# ---------- HMAC ----------
def generate_hmac(secret: bytes, message: bytes) -> bytes:
    return hmac.new(secret, message, hashlib.sha256).digest()


def verify_hmac(secret: bytes, message: bytes, tag: bytes) -> bool:
    return hmac.compare_digest(
        generate_hmac(secret, message),
        tag
    )
