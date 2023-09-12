# script to generate ethereum sepolia wallet
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/4273f63174564cd4827eb9af8d0f2df4'))
account = w3.eth.account.create()
privKey = account._private_key.hex()
pubKey = account.address

print(f'privKey: {privKey}')
print(f'pubKey: {pubKey}')
