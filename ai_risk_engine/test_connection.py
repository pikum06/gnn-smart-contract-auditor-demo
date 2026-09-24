from web3 import Web3

# Your unique Alchemy URL from the dashboard
ALCHEMY_URL = "https://eth-mainnet.g.alchemy.com/v2/8Z9xYiPUWR8aUp01CBpiP"

# Initialize the connection
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

def run_test():
    print("BLOCKCHAIN CONNECTION TEST")
    if w3.is_connected():
        # Get the latest block
        block_num = w3.eth.block_number
        print(f"SUCCESS: Connected to Ethereum Mainnet.")
        print(f"CURRENT BLOCK: {block_num}")
    else:
        print("FAILURE: Could not connect. Check your URL.")

if __name__ == "__main__":
    run_test()