from eth_account import Account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    # create an eth account and recover the address (derived from the public key) and private key
    # your code here

    account = Account.create()

    eth_address = account.address  # Eth account
    private_key = account.privateKey

    # Encode the message
    message = encode_defunct(text=m)
    

    # generate signature
    # your code here

    signed_message = Account.sign_message(message, private_key)

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message
