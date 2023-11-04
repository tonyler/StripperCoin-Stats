import requests
import os
from dotenv import load_dotenv
load_dotenv()
import minswap.pools

def strip_price(): #Getting the current price of StripperCoin in ADA using the Minswap DEX
    while True:
        try:
            price = float((minswap.pools.get_pool_by_id(os.environ.get("POOL_ID")).price)[0])
            price = round(price,4)
            break
        except Exception as e:
            print (f"MinSwap error: {e}")
            print ("trying to get minswap price again")
    return price   


def ada_price(): #Getting the current price of ADA from Coingecko
    while True:
        try:
            gecko_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd")
            data = gecko_data.json()
            price = float(data["cardano"]["usd"])
            break
        except Exception as e:
            print (f"Coingecko ADA Api Error: {e}")
            print ("trying to get coingecko's cardano price again")
    return price

