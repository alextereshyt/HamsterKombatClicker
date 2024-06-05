import requests
import time

url = 'https://api.hamsterkombat.io/clicker/tap'
headers = {
    'Accept-Language': 'en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,de;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://hamsterkombat.io',
    'Referer': 'https://hamsterkombat.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'authorization': 'Bearer 1717581364428bKGCXvsCJNbdl8MzPoXWkHDO6Vw9jyOESsctVHy6aDFz51J65l7XPhrtWcm0CreR7394421163',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}   
data_for_taps = {
    "count": 10,
    "availableTaps": 0,
    "timestamp": int(time.time())
}

data_for_boost ={
    "boostId": "BoostFullAvailableTaps",
    "timestamp": int(time.time())
}

while True:
    data_for_taps["timestamp"] = int(time.time()) 
    response = requests.post(url, headers=headers, json=data_for_taps)   
    #requests.post('https://api.hamsterkombat.io/clicker/buy-boost', headers=headers, json=data_for_boost)  
    if response.status_code == 200:
        response_data = response.json()
        balance_coins = response_data.get("clickerUser", {}).get("balanceCoins")
        availableTaps = response_data.get("clickerUser", {}).get("availableTaps")
        #data["availableTaps"] = availableTaps   
        print(f'Current Balance: {balance_coins}')
        print(f'Available Taps: {availableTaps}')
        print()
    else:
        print(f'Error: Status Code {response.status_code}')
        print(response.reason)
        print()
        #exit() 
    time.sleep(2)
