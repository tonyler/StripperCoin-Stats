import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


async def get_holders(self)->int:  
    api_calls = 0
    next_is_0 = None 
    previous_is_100 = None
    success = False
    unsuccesful_api_calls = 0

    #This is not the best way to find all holders, but it's the fastest way minimizing blockfrost API calls.
    while True:    
        wallets_count=(self.pages-1)*100

        if unsuccesful_api_calls > 5: 
            break 

        try:
            api_calls += 1  #just for personal info..in case something goes wrong
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
                    success = True
                    break
                
            else:
                success = True
                break 

        except json.decoder.JSONDecodeError as e: #Error 504
            print (response.status_code)
            unsuccesful_api_calls += 1
            print ("continuing...")

        except Exception as e: #Any other error
            print (e)
            break

    if success == True:
        print (f"Success getting holders with {api_calls} api calls!")
        return wallets_count
    else :
        print (f"Error getting holders...{unsuccesful_api_calls} unsuccesful api calls!")
        return ("Error getting holders...")
        
