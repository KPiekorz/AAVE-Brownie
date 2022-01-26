from web3 import Web3
from brownie import (
    network, 
    config, 
    accounts, 
    Contract,
    interface
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev", "rinkeby-fork"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]

def  get_account(index=None, id=None):

    if index:
        return accounts[index]

    if id:
        return accounts.load(id)

    if  (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    
    # this is for remote blockchain
    return accounts.add(config["wallets"]["from_key"])