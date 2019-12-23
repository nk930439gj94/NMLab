import utils


class TXOutput(object):
    """
    Attributes:
        _value (int): Transaction output.
        _public_key_hash (string): Hash of a public key.
    """

    # the amount of reward
    subsidy = 10

    def __init__(self, value, address):
        self._value = value
        self._address = address
        self._public_key_hash = utils.address_to_pubkey_hash(address)

    def __repr__(self):
        return 'TXOutput( address={0!r}, value={1!r} )'.format(
            self._address, self._value)

    def is_locked_with_key(self, pubkey_hash):
        return self._public_key_hash == pubkey_hash

    @property
    def value(self):
        return self._value

    @property
    def address(self):
        return self._address

    @property
    def public_key_hash(self):
        return self._public_key_hash
