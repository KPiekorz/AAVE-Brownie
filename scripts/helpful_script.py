from web3 import Web3
from brownie import (
    network, 
    config, 
    accounts, 
    Contract,
    interface
)

LOCAL_BLOCKCHAIN_ENVIROMENTS = [
    "development", 
    "ganache-local", 
    "mainnet-fork"
]

def  get_account(index=None, id=None):

    if index:
        return accounts[index]

    if id:
        return accounts.load(id)

    if  network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    
    # this is for remote blockchain
    return accounts.add(config["wallets"]["from_key"])