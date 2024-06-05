import requests
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

url = 'https://api.hamsterkombat.io/clicker'

headers_template = {
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
    'Bearer 1717593688842WqjrvsZzb7x3ZS3oPFurFYJKFitshCdbllUNcfZtOgOsJoLnjTJlcvDvjdEFHHMQ811097437',  # main
    'Bearer 1717581364428bKGCXvsCJNbdl8MzPoXWkHDO6Vw9jyOESsctVHy6aDFz51J65l7XPhrtWcm0CreR7394421163',  # typo splash
    'Bearer 171758805251307GgcWgqIkEEO5rb3Y7HRJhdxgumGFqudLV8XsnHSKzoxydG3qx3VnioVsSdMisu7268318527',  # ab
    'Bearer 1717588319461LSvtcKMFcFOQTZ7rwObeVqItZpT3WfadgFi4KhJuGvM0A0ybYzj2qxuuyMAAMpEN7423052397',  # aa
    'Bearer 17176001519425DY8SEYHv9XgReyo2rU4pz9MuWMJh6RjpZmpt4aCWsw9pHXp8xKx2Pv1fAvfBveQ1613514064',  # leva
    'Bearer 1717600670064NyHbMRtYtXO1BpBUVZZCfF9TLP0wMqD9FNnALD0Wnx0hLsB77XxbP5cz8rPcDLQc6030860255'  # nazar
]

data_for_taps = {
    "count": 300,
    "availableTaps": 0,
    "timestamp": ""
}

data_for_boost = {
    "boostId": "BoostFullAvailableTaps",
    "timestamp": ""
}

data_for_upgrade = {
    "upgradeId": "",
    "timestamp": ""
}

upgrades = [
    "fan_tokens", "staking", "p2p_trading", "web3_integration", "security_audition", "btc_pairs", "etc_pairs",
    "top_10_cmc_pairs", "derivatives", "gamefi_tokens", "defi2.0_tokens", "socialfi_tokens", "meme_coins",
    "shit_coins", "margin_trading_x10", "margin_trading_x20", "margin_trading_x30", "margin_trading_x50",
    "margin_trading_x75", "margin_trading_x100", "kyc", "kyb", "legal_opinion", "sec_transparancy",
    "anti_money_loundering", "licence_uae", "licence_europe", "licence_asia", "licence_south_america", "licence_nigeria"
]


def process_account(auth_token):
    headers = headers_template.copy()
    headers['authorization'] = auth_token

    data_for_taps["timestamp"] = int(time.time())
    data_for_boost["timestamp"] = int(time.time())
    data_for_upgrade["timestamp"] = int(time.time())

    tap_response = requests.post(url + "/tap", headers=headers, json=data_for_taps)
    requests.post(url + '/buy-boost', headers=headers, json=data_for_boost)

    for upgrade in upgrades:
        data_for_upgrade["upgradeId"] = upgrade
        requests.post(url + '/buy-upgrade', headers=headers, json=data_for_upgrade)

    if tap_response.status_code != 200:
        print(f'Error: Status Code {tap_response.status_code}')
        print(tap_response.reason)
    else:
        response_data = tap_response.json()
        level = response_data.get("clickerUser", {}).get("level")
        total_coins = response_data.get("clickerUser", {}).get("totalCoins")
        user_id = response_data.get("clickerUser", {}).get("id")
        balance_coins = response_data.get("clickerUser", {}).get("balanceCoins")
        available_taps = response_data.get("clickerUser", {}).get("availableTaps")
        passive = response_data.get("clickerUser", {}).get("earnPassivePerHour")

        print(datetime.now().strftime("%H:%M:%S"))
        print(f'ID: {user_id}')
        print(f'Level: {level}')
        print(f'Current Balance: {balance_coins}')
        print(f'Total Balance: {total_coins}')
        print(f'Available Taps: {available_taps}')
        print(f'Passive per hour: {passive}')
        print()

    print("--------------------------")


def main():
    print("   _  __ __                         __            ____        __ \r\n  | |/ // /_  __  ______ ___  _____/ /____  _____/ __ )____  / /_\r\n  |   // __ \\/ / / / __ `__ \\/ ___/ __/ _ \\/ ___/ __  / __ \\/ __/\r\n /   |/ / / / /_/ / / / / / (__  ) /_/  __/ /  / /_/ / /_/ / /_  \r\n/_/|_/_/ /_/\\__,_/_/ /_/ /_/____/\\__/\\___/_/  /_____/\\____/\\__/  \r\n                                                                 ")
    print("V1.0                                            Created by LaLeX")
    with ThreadPoolExecutor(max_workers=len(authorizations)) as executor:
        while True:
            executor.map(process_account, authorizations)
            time.sleep(2)  # Add a sleep time if you want to avoid spamming requests too frequently


if __name__ == "__main__":
    main()
