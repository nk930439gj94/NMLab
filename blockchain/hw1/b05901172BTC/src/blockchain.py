import sys
import pickle
from collections import defaultdict


from block import Block
from db import Bucket
from transaction import CoinbaseTx


class Blockchain(object):
    """ 
    Attributes:
        _tip (bytes): Point to the latest hash of block.
        _bucket (dict): bucket of DB 
    """
    db_file = 'blockchain.db'
    block_bucket = 'blocks'
    genesis_coinbase_data = 'mother fucker first block'

    def __init__(self, address=None):
        self._bucket = Bucket(Blockchain.db_file, Blockchain.block_bucket)

        try:
            self._tip = self._bucket.get('l')
        except KeyError:
            cb_tx = CoinbaseTx(address, Blockchain.genesis_coinbase_data)
            genesis = Block([cb_tx]).pow_of_block()
            self._block_put(genesis)

    def _block_put(self, block):
        self._bucket.put( block.hash, pickle.dumps(block) )
        self._bucket.put('l', block.hash)
        self._tip = block.hash
        self._bucket.commit()

    def MineBlock(self, transaction_lst):
        # Mines a new block with the provided transactions
        last_hash = self._bucket.get('l')

        for tx in transaction_lst:
            if not self.verify_transaction(tx):
                print("ERROR: Invalid transaction")
                sys.exit()
        print( 'Verifying complete\n' )

        new_block = Block(transaction_lst, last_hash).pow_of_block()
        self._block_put(new_block)
        return new_block

    @property
    def latest_block(self):
        return pickle.loads( self._bucket.get( self._tip ) )

    @property
    def blocks(self):
        current_tip = self._tip
        while True:
            if not current_tip:
                raise StopIteration
            encoded_block = self._bucket.get(current_tip)
            block = pickle.loads(encoded_block)
            yield block
            current_tip = block.prev_block_hash

    @property
    def height(self):
        return len( self._bucket.kv )-1

    def find_transaction(self, ID):
        # finds a transaction by its ID
        for block in self.blocks:
            for tx in block.transactions:
                if tx.ID == ID:
                    return tx

        return None

    def sign_transaction(self, tx, priv_key):
        prev_txs = {}
        for vin in tx.vin:
            prev_tx = self.find_transaction(vin.tx_id)
            prev_txs[prev_tx.ID] = prev_tx

        tx.sign(priv_key, prev_txs)

    def verify_transaction(self, tx):
        if isinstance(tx, CoinbaseTx):
            return True

        prev_txs = {}
        for vin in tx.vin:
            prev_tx = self.find_transaction(vin.tx_id)
            prev_txs[prev_tx.ID] = prev_tx

        return tx.verify(prev_txs)
