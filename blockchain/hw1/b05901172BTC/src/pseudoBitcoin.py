import argparse

import utils
from wallet import Wallet
from wallets import Wallets
from blockchain import Blockchain
from transaction import UTXOTx, CoinbaseTx
from utxo_set import UTXOSet

import os

def argParser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers( dest='command' )

    # wallet
    wallet_parser = sub_parser.add_parser( 'createwallet', help='create a wallet' )
    
    # blockchain
    bc_parser = sub_parser.add_parser( 'createblockchain', help='create a block chain' )
    bc_parser.add_argument( '-address', type=str, help='address of creator' )

    # balance
    balance_parser = sub_parser.add_parser( 'getbalance', help='get someone\'s balance' )
    balance_parser.add_argument( '-address', type=str, help='someone\'s wallet' )

    # send
    send_parser = sub_parser.add_parser( 'send', help='send amount of coins from sender to receiver' )
    send_parser.add_argument( '-from', type=str, dest='f', help='address of sender' )
    send_parser.add_argument( '-to', type=str, dest='t', help='address of receiver' )
    send_parser.add_argument( '-amount', type=int, help='amount of coins' )

    # printchain
    printchain_parser = sub_parser.add_parser( 'printchain', help='print the block chain' )

    # printblock
    printblock_parser = sub_parser.add_parser( 'printblock', help='print the block' )
    printblock_parser.add_argument( '-height', type=int, help='the height of the block' )

    return parser.parse_args()

def create_wallet():
    wallets = Wallets()
    wallet = Wallet()
    address = wallet.address
    wallets.add_wallet(address, wallet)
    wallets.save_to_file()

    print("Your new address: {}".format(address))

def create_blockchain(address):
    bc = Blockchain(address)
    UTXOSet(bc).create_first_utxo()

    print('Done!')

def get_balance(address):
    bc = Blockchain()
    utxo_set = UTXOSet(bc)
    pubkey_hash = utils.address_to_pubkey_hash(address)
    utxos = utxo_set.find_utxo(pubkey_hash)
    balance = 0

    for out in utxos:
        balance += out.value

    print('Balance: {0}'.format(balance))

def send(from_addr, to_addr, amount):
    bc = Blockchain()
    utxo_set = UTXOSet(bc)

    tx = UTXOTx(from_addr, to_addr, amount, utxo_set)
    cb_tx = CoinbaseTx(from_addr)
    new_block = bc.MineBlock([tx, cb_tx])
    utxo_set.update(new_block)

    print('Success!')

def print_chain():
    bc = Blockchain()

    for block in bc.blocks:
        print("Prev. hash: {0}".format(block.prev_block_hash))
        print("hash:       {0}".format(block.hash))
        print("PoW:        {0}".format( block.valid() ))
        print()

def print_block( height ):
    if( height<0 ):
        print( 'height has to be greater than or equal to 0' )
        return
    bc = Blockchain()
    idx = bc.height - height - 1
    if( idx < 0 ):
        print( 'height has to be less than', bc.height )
        return
    for i, block in enumerate(bc.blocks):
        if i == idx:
            print("Prev. hash: {0}".format(block.prev_block_hash))
            print("hash:       {0}".format(block.hash))
            print("PoW:        {0}".format( block.valid() ))
            print( 'Transactions: ' )
            for tx in block.transactions :
                print( '    ', tx )
            print()
            return


if __name__ == '__main__':
    args = argParser()
    
    if( args.command == 'createwallet' ):
        create_wallet()
    elif( args.command == 'createblockchain' ):
        if(  not args.address ):
            print( 'Please follow the format' )
        else:
            create_blockchain( args.address )
    elif( args.command == 'getbalance' ):
        if(  not args.address ):
            print( 'Please follow the format' )
        else:
            get_balance( args.address )
    elif( args.command == 'send' ):
        if(  not args.f or not args.t or not args.amount  ):
            print( 'Please follow the format' )
        else:
            send( args.f, args.t, args.amount )
    elif( args.command == 'printchain' ):
        print_chain()
    elif( args.command == 'printblock' ):
        if(  args.height == None ):
            print( 'Please follow the format' )
        else:
            print_block( args.height )