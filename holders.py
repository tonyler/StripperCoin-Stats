import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

async def get_holders(self)->int:  

    #This is not the best way to find all holders, but it's the fastest way minimizing blockfrost API calls.
    wallets_count=(self.pages-1)*100

    while True:

        next_is_0 = None 
        previous_is_100 = None

        try:
            url = f'{self.base_url}/{self.asset}/addresses?page={self.pages}'
            response = requests.get(url,headers=self.headers)
            data = response.json()
            wallets_count+=len(data)

            if not(previous_is_100 and next_is_0):

                if len(data)==100: #if the page is full, it's probable it is not the last one
                    self.pages+=1 
                    previous_is_100 = True
                    next_is_0 = False

                elif len(data)==0:#if the page is totally empty
                    if next_is_0 == True: 
                        wallets_count-=100
                    self.pages-=1
                    next_is_0 = True
                else: 
                    break
            else:
                break 

        except json.decoder.JSONDecodeError as e: #Error 504
            print (response.status_code)
            print ("continuing...")

        except Exception as e: #Any other error
            wallets_count = 'Error'
            print (e)
            break
    return wallets_count

