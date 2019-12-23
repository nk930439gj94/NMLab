import os
import hashlib
import binascii

import ecdsa

import utils


class Wallet(object):
    """
    Attributes:
        _private_key (string): a private key.
        _public_key (string): a public key.
        _hash_public_key (string): a hash of public key.
        _address (string): a wallet address.
    """

    def __init__(self):
        self._private_key = os.urandom(32)

        self._public_key = utils.privatekey_to_publickey(self._private_key)
        self._hash_public_key = utils.hash_public_key(self._public_key)
        self._address = utils.get_address(self._hash_public_key)

    @property
    def private_key(self):
        return self._private_key

    @property
    def public_key(self):
        return self._public_key

    @property
    def hash_public_key(self):
        return self._hash_public_key

    @property
    def address(self):
        return self._address
