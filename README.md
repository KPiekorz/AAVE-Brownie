1. Swap some eth for weth
2. Deposit some eth to aave
3. Borrow some asset from ETH collateral
    1. Sell that borrowed asset. (Short selling)
4. Repay everything back

Paraswap,or uniswap...

Integration test: Kovan

Unit test: Mainnet-fork (we will fork everything, which is on the mainnet, to not doing any oracles mock etc.)

Default tetsting networks = development with mocking

Mainnet fork for testing = not oracles mock