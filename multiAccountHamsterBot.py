import requests
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

url = "https://api.hamsterkombat.io/clicker"

headers_template = {
    "Accept-Language": "en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,de;q=0.6",
    "Connection": "keep-alive",
    "Origin": "https://hamsterkombat.io",
    "Referer": "https://hamsterkombat.io/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "accept": "application/json",
    "content-type": "application/json",
    "sec-ch-ua": '"Not.A/Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"iOS"',
}

authorizations = {
    #"name": "your token", 
}

data_for_taps = {"count": 300, "availableTaps": 0, "timestamp": ""}
data_for_boost = {"boostId": "BoostFullAvailableTaps", "timestamp": ""}
data_for_upgrade = {"upgradeId": "", "timestamp": ""}

upgrades = [
    "fan_tokens",
    "staking",
    "p2p_trading",
    "web3_integration",
    "security_audition",
    "btc_pairs",
    "eth_pairs",
    "top_10_cmc_pairs",
    "derivatives",
    "prediction_markets",
    "gamefi_tokens",
    "defi2.0_tokens",
    "socialfi_tokens",
    "meme_coins",
    "shit_coins",
    "margin_trading_x10",
    "margin_trading_x20",
    "margin_trading_x30",
    "margin_trading_x50",
    "margin_trading_x75",
    "margin_trading_x100",
    "kyc",
    "kyb",
    "legal_opinion",
    "sec_transparancy",
    "anti_money_loundering",
    "licence_uae",
    "licence_europe",
    "licence_asia",
    "licence_south_america",
    "licence_nigeria",
    "trading_bots",
    "support_team",
    "facebook_ads",
    "x",
    "medium",
    "youtube",
    "instagram",
    "tiktok",
    "reddit",
    "it_team",
    "marketing",
]

def process_account(auth_pair):

    name, auth_token = auth_pair
    try:
        headers = headers_template.copy()
        headers["authorization"] = auth_token

        data_for_taps["timestamp"] = int(time.time())
        data_for_boost["timestamp"] = int(time.time())
        data_for_upgrade["timestamp"] = int(time.time())

        tap_response = requests.post(url + "/tap", headers=headers, json=data_for_taps)
        requests.post(url + "/buy-boost", headers=headers, json=data_for_boost)

        for upgrade in upgrades:
            data_for_upgrade["upgradeId"] = upgrade
            requests.post(url + "/buy-upgrade", headers=headers, json=data_for_upgrade)

        if tap_response.status_code != 200:
            print(f"Error: Status Code {tap_response.status_code}")
            print(tap_response.reason)
        else:
            response_data = tap_response.json()
            level = response_data.get("clickerUser", {}).get("level")
            total_coins = response_data.get("clickerUser", {}).get("totalCoins")
            balance_coins = response_data.get("clickerUser", {}).get("balanceCoins")
            available_taps = response_data.get("clickerUser", {}).get("availableTaps")
            passive = response_data.get("clickerUser", {}).get("earnPassivePerHour")

            print(datetime.now().strftime("%H:%M:%S"))
            print(f"Name: {name}")
            print(f"Level: {level}")
            print(f"Current Balance: {balance_coins}")
            print(f"Total Balance: {total_coins}")
            print(f"Available Taps: {available_taps}")
            print(f"Passive income per hour: {passive}")
            print()

    except Exception as e:
        print(f"Exception occurred for token {auth_token}: {str(e)}")
    print("--------------------------")

def main():
    print(
        "   _  __ __                         __            ____        __ \r\n  | |/ // /_  __  ______ ___  _____/ /____  _____/ __ )____  / /_\r\n  |   // __ \\/ / / / __ `__ \\/ ___/ __/ _ \\/ ___/ __  / __ \\/ __/\r\n /   |/ / / / /_/ / / / / / (__  ) /_/  __/ /  / /_/ / /_/ / /_  \r\n/_/|_/_/ /_/\\__,_/_/ /_/ /_/____/\\__/\\___/_/  /_____/\\____/\\__/  \r\n                                                                 "
    )
    print("V1.0                                            Created by LaLeX")
    with ThreadPoolExecutor(max_workers=len(authorizations)) as executor:
        while True:
            executor.map(process_account, authorizations.items())
            time.sleep(2)  # Add a sleep time if you want to avoid spamming requests too frequently

if __name__ == "__main__":
    main()
