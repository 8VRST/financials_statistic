from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from utils.methods import open_json_file, multiple_replace


class Metals:

    def __init__(self):
        self._headers = open_json_file("scrappers/config.json")["headers"]
        self._silver_url = "https://myfin.by/bank/metally/silver"
        self._gold_url = "https://myfin.by/bank/metally/gold"

    def silver(self):
        data = self._get_data(self._silver_url)
        return data

    def gold(self):
        data = self._get_data(self._gold_url)
        return data

    def _get_data(self, metal_url):
        response = requests.get(metal_url, verify=False, headers=self._headers)
        page = BeautifulSoup(response.text, "html.parser")
        metal_table = page.find("div", {"class": "table-responsive"}).find_all("td")

        replace_values = {" ": "", "-": "0"}

        metal_data_list = []

        for metal_data in metal_table:
            metal_data = multiple_replace(metal_data.text, replace_values)
            if metal_data.isnumeric() == True:
                metal_data_list.append(int(metal_data))
            else:
                metal_data_list.append(metal_data)

        return metal_data_list
