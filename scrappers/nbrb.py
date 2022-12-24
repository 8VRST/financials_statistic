import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from utils.methods import open_json_file


def usd_on_date(date):
    config = open_json_file("scrappers/config.json")
    date = "-".join(date.split(".")[::-1])
    url = "https://www.nbrb.by/api/exrates/rates/431?ondate=" + date
    data = requests.get(url, verify=False, headers=config["headers"])
    if data.status_code == 404:
        return 404
    else:
        usd_rate = data.json()["Cur_OfficialRate"]
        return usd_rate
