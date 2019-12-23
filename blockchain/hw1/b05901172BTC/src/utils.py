import hashlib
import binascii
import pickle

import ecdsa
import base58


def hash_public_key(pubkey):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(binascii.unhexlify(pubkey)).digest())
    return ripemd160.hexdigest()

def get_address(pubkey_hash):
    return base58.base58CheckEncode(0x00, pubkey_hash)

def address_to_pubkey_hash(address):
    return base58.base58CheckDecode(address)

def privatekey_to_publickey(key):
    sk = ecdsa.SigningKey.from_string(key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return binascii.hexlify(vk.to_string()).decode()

def pubkey_to_verifykey(pub_key, curve=ecdsa.SECP256k1):
    vk_string = binascii.unhexlify( pub_key.encode() )
    return ecdsa.VerifyingKey.from_string(vk_string, curve=curve)
