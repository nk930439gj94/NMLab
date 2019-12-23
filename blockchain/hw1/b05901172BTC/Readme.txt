Prerequisites:
	python3
	linux

How to use:
	python3 pseudoBitcoin.py createwallet
	python3 pseudoBitcoin.py createblockchain -address XXXXX
	python3 pseudoBitcoin.py getbalance -address XXXXX
	python3 pseudoBitcoin.py send -from XXXXX -to YYYYY -amount ZZZ
	python3 pseudoBitcoin.py printchain
	python3 pseudoBitcoin.py printblock -height N

Fuctionalities implemented:
	Prototype:	Block, Blockchain, Proof-of-Work
	Persistence:	Database, Client
	Transaction:	UTXO
	Address:	Sign & Verify
	Transaction:	Mining reward, Merkle tree