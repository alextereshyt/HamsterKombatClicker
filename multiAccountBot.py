import requests
import time

url = 'https://api.hamsterkombat.io/clicker'
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
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}   
authorizations = [
 'Bearer 1717581364428bKGCXvsCJNbdl8MzPoXWkHDO6Vw9jyOESsctVHy6aDFz51J65l7XPhrtWcm0CreR7394421163',
 'Bearer 171758805251307GgcWgqIkEEO5rb3Y7HRJhdxgumGFqudLV8XsnHSKzoxydG3qx3VnioVsSdMisu7268318527',
 'Bearer 1717588319461LSvtcKMFcFOQTZ7rwObeVqItZpT3WfadgFi4KhJuGvM0A0ybYzj2qxuuyMAAMpEN7423052397'
]

data_for_taps = {
    "count": 100,
    "availableTaps": 0,
    "timestamp": ""
}


data_for_boost ={
    "boostId": "BoostFullAvailableTaps",
    "timestamp": ""
}


data_for_upgrade ={
    "upgradeId": "",
    "timestamp": ""
}

upgrades = ["fan_tokens","staking","btc_pairs","etc_pairs","top_10_cmc_pairs","gamefi_tokens"]



while True:
    for a in authorizations:
     data_for_taps["timestamp"] = int(time.time()) 
     data_for_boost["timestamp"] = int(time.time()) 
     data_for_upgrade["timestamp"]= int(time.time()) 
     headers["authorization"] = a;
     info = requests.post(url + "/tap", headers=headers, json=data_for_taps)
     requests.post(url + '/buy-boost', headers=headers, json=data_for_boost)  
     for b in upgrades:
        requests.post(url + '/buy-upgrade', headers=headers, json=data_for_upgrade) 
         
     response_data = info.json()
     level = response_data.get("clickerUser", {}).get("level")
     total_coins = response_data.get("clickerUser", {}).get("totalCoins")
     id = response_data.get("clickerUser", {}).get("id")
     balance_coins = response_data.get("clickerUser", {}).get("balanceCoins")
     availableTaps = response_data.get("clickerUser", {}).get("availableTaps")
     print(id)
     print(f'Level: {balance_coins}')
     print(f'Current Balance: {balance_coins}')
     print(f'Total Balance: {balance_coins}')
     print(f'Available Taps: {availableTaps}')
     print()

    print("--------------------------")
    #time.sleep(2)
