import utils


class TXInput(object):
    """
    Attributes:
        _tx_id (bytes): Transaction ID.
        _vout (int): Transaction output value.
        _sig (string): Signature.
        _public_key (string): Public key.
    """

    def __init__(self, txid, vout, sig, pubkey):
        self._tx_id = txid.encode()
        self._vout = vout
        self._sig = sig
        self._public_key = pubkey

    @property
    def tx_id(self):
        return self._tx_id.decode()

    @property
    def vout(self):
        return self._vout

    @property
    def signature(self):
        return self._sig

    @property
    def public_key(self):
        return self._public_key

    @signature.setter
    def signature(self, sig):
        self._sig = sig

    @public_key.setter
    def public_key(self, public_key):
        self._public_key = public_key
