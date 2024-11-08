import sys

from pprint import pprint

import requests
from gridiron_insights.ncaa.models import RootModel

def fetch_ncaa_scoreboard(division: str, year: int, month: int) -> RootModel:
    url = f"https://data.ncaa.com/casablanca/scoreboard/football/{division}/{year}/{month}/scoreboard.json"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Host": "data.ncaa.com",
        "Origin": "https://www.ncaa.com",
        "Referer": "https://www.ncaa.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return RootModel(**data)
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":
    try:
        scoreboard = fetch_ncaa_scoreboard("fcs", 2024, 11)
        pprint(scoreboard.model_dump())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    sys.exit(0)
