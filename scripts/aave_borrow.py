 

from eth_utils import address
from scripts.helpful_script import (
    LOCAL_BLOCKCHAIN_ENVIROMENTS, 
    get_account
)
from brownie import (
    config, 
    network,
    accounts,
    interface
)
from scripts.get_weth import get_weth
from web3 import Web3

amount = Web3.toWei(0.1, "ether")

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        tx = get_weth()
    else:
        print("Remote testnet nwtwork, will not get another WETH!")
    lending_pool = get_lending_pool()
    print(f"Lending pool address: {lending_pool}")
    print("Approving erc20 token to be usabe by contract...")
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("Depositing...")
    tx = lending_pool.deposit(
        erc20_address,
        amount,
        account.address,
        0,
        {"from": account}
    )
    tx.wait(1)
    print("Deposited!")
    borrowable_eth, total_debt = get_borrowale_data(lending_pool, account)
    print("Let's borrow!")
    

def get_lending_pool():
    # ABI
    # address
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # ABI
    # address
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool

def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1) # one block confirmation
    print("Approved!")
    return tx

def get_borrowale_data(lending_pool, account):
    (
        total_collateral_eth,
        total_debt_eth,
        avaiable_brrow_eth,
        current_liquidation_threshold,
        ltv,
        health_factor
    ) = lending_pool.getUserAccountData(account.address)
    avaiable_brrow_eth = Web3.fromWei(avaiable_brrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"You have {total_collateral_eth} worth of ETH deposited.")
    print(f"You have {total_debt_eth} worth of ETH borrowed.")
    print(f"You can borrow {avaiable_brrow_eth} worth of ETH.")
    return (float(avaiable_brrow_eth), float(total_debt_eth))