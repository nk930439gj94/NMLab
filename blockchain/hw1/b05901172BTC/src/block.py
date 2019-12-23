import time
import hashlib
import binascii
import pickle
import sys


class Block(object):
    """
    Attributes:
        _timestamp (bytes): Creation timestamp of Block.
        _tx_lst (list): List of transaction.
        _prev_block_hash (bytes): Hash of the previous Block.
        _hash (bytes): Hash of the current Block.
        _nonce (int): A 32 bit arbitrary random number that is typically used once.
    """

    max_nonce = sys.maxsize
    target_bits = 12

    def __init__(self, transaction_lst, prev_block_hash=''):
        self._timestamp = str(int(time.time())).encode()
        self._tx_lst = transaction_lst
        self._prev_block_hash = prev_block_hash.encode()
        self._hash = None
        self._nonce = None

        self._target = 1 << (256 - Block.target_bits)

    @property
    def hash(self):
        return self._hash.decode()

    @property
    def prev_block_hash(self):
        return self._prev_block_hash.decode()

    @property
    def timestamp(self):
        return str(self._timestamp)

    @property
    def nonce(self):
        return str(self._nonce)

    @property
    def transactions(self):
        return self._tx_lst

    def pow_of_block(self):
        # Makes the proof of work of the current Block

        self._nonce = 0
        data_lst = [ self.prev_block_hash, self.hash_transactions(), self.timestamp, str(Block.target_bits), self.nonce ]
        print('Mining a new block')
        while self._nonce < self.max_nonce:
            data_lst[4] = self.nonce
            data = ( ''.join(data_lst) ).encode()

            m = hashlib.sha256()
            m.update( data )
            hash_hex = m.hexdigest()

            print( hash_hex, end='\r' )
            hash_int = int(hash_hex, 16)

            if hash_int < self._target:
                break
            else:
                self._nonce += 1

        print('\n')

        self._hash = hash_hex.encode()
        return self

    def hash_transactions(self):
        # return a hash of the transactions in the block
        # merkle tree implementation

        nodes = []
        for tx in self._tx_lst:
            m = hashlib.sha256()
            m.update( pickle.dumps(tx) )
            nodes.append( m.digest() )

        while( len(nodes) > 1 ):
            new_level = []
            for i in range( 0, len(nodes), 2 ):
                m = hashlib.sha256()
                m.update( nodes[i] )
                if( i < ( len(nodes)-1 ) ):
                    m.update( nodes[i+1] )
                new_level.append( m.digest() )

            nodes = new_level

        return (binascii.hexlify( nodes[0] )).decode()

    def valid(self):
        data_lst = [ self.prev_block_hash, self.hash_transactions(), self.timestamp, str(Block.target_bits), self.nonce ]
        data = ( ''.join(data_lst) ).encode()
        m = hashlib.sha256()
        m.update( data )
        hash_hex = m.hexdigest()

        return ( int(hash_hex, 16) < self._target )
