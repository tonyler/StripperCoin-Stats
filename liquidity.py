import requests
import asyncio 
import os
from dotenv import load_dotenv
load_dotenv()
import minswap.pools


async def strip_pool(retries=0, max_retries = 5): #Getting the current price of StripperCoin in ADA using the Minswap DEX
    while retries < max_retries :
        try:
            pool_state = minswap.pools.get_pool_by_id(os.environ.get("POOL_ID"))
            price = pool_state.price[0]
            tvl = (int(2*float(pool_state.tvl))) #Minswap pools are 50:50, so I *2 to get both assets value.
            price = float(round(price,4))
            print (f"Price and TVL calculated succesfully with {retries} retries")
            break
        except Exception as e:
            print (f"MinSwap error: {e}")
            print ("trying to get minswap price again")
            retries += 1
            await asyncio.sleep(5)
    if retries == max_retries : 
        price = tvl = "Minswap error"              
    return price, tvl   


async def ada_price(retries = 0, max_retries = 5): #Getting the current price of ADA from Coingecko
    while retries < max_retries :
        try:
            gecko_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd")
            data = gecko_data.json()
            price = float(data["cardano"]["usd"])
            print (f"Succesfull Coingecko request with {retries} retries")
            break
        except Exception as e:
            print (f"Coingecko ADA Api Error: {e}")
            print ("trying to get coingecko's cardano price again")
            await asyncio.sleep(5)
            retries+=1
    if retries == max_retries : 
        price = "Coingecko Error"
    return price