import liquidity
from holders import get_holders
from datetime import datetime
import pytz
import asyncio

utc_timezone = pytz.timezone('UTC')

import os 
from dotenv import load_dotenv 
load_dotenv()


class DataCollector():
    def __init__(self):
        self.pages = 305
        self.project_id = os.environ.get("PROJECT_ID")
        self.asset = os.environ.get("ASSET")
        self.headers = {'project_id': self.project_id,'Content-Type': 'application/json'}
        self.base_url = 'https://cardano-mainnet.blockfrost.io/api/v0/assets'
        self.supply = 69000000

    async def dynamic_data(self): 
        self.ada, self.tvl = await liquidity.strip_pool() #self.ada is price in ada
        try:
            self.price = round(await liquidity.ada_price()* self.ada,4)
            self.market_cap = int(self.price * 69000000) 
        except Exception as e: 
            print (e)
            self.price = "CoinGecko Error"
            self.market_cap = "Error" 
        self.holders =  await get_holders(self)
        self.update = str(datetime.now(utc_timezone).strftime("%H:%M:%S")+" UTC")


hi = DataCollector()
asyncio.run(hi.dynamic_data())
print (hi.price, hi.market_cap)