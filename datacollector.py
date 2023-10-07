from Value_Locked import TVL
from prices import strip_price, ada_price
from holders import get_holders

import os 
from dotenv import load_dotenv 
load_dotenv()


class DataCollector():
    def __init__(self):
        self.pages = 317
        self.project_id = os.environ.get("PROJECT_ID")
        self.asset = os.environ.get("ASSET")
        self.headers = {'project_id': self.project_id,'Content-Type': 'application/json'}
        self.base_url = 'https://cardano-mainnet.blockfrost.io/api/v0/assets'
        self.supply = 69000000

    async def dynamic_data(self): 
        self.ada = strip_price()
        self.price = round(ada_price()* self.ada,4)
        self.market_cap = int(self.price * 69000000) 
        self.holders = await get_holders(self)
        self.tvl = await TVL()
