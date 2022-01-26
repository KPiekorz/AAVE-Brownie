1. Swap some eth for weth
2. Deposit some eth to aave
3. Borrow some asset from ETH collateral
    1. Sell that borrowed asset. (Short selling)
4. Repay everything back

Two things needed when working with contract: ABI + address.

Examples of using similary programs: Paraswap,or uniswap...

Integration test: Kovan.

Unit test: Mainnet-fork (we will fork everything, which is on the mainnet, to not doing any oracles mock etc.).

Default testing networks (kovan testnet) = development with mocking.

Mainnet fork for testing = not oracles mock.