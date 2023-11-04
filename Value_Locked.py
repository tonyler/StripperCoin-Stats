from dotenv import load_dotenv
load_dotenv()
import os
import minswap.pools
import asyncio 

async def TVL():
    tvl_found = False
    efforts = 0

    while True: 
        try:
            pool_state = minswap.pools.get_pool_by_id(os.environ.get("POOL_ID"))
            Value_In_LP = (int(2*float(pool_state.tvl))) #Minswap pools are 50:50, so I *2 to get both assets value.
            tvl_found = True
        except Exception as e:
            print (f"Minswap TVL error: {e}")
            efforts+=1
            await asyncio.sleep(10)

        if efforts == 3 or tvl_found == True :
            if efforts == 3: 
                Value_In_LP = "Problem with Minswap atm!"
            break 
    return Value_In_LP