import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from utils.methods import open_json_file, multiple_replace


def pie():
    headers = open_json_file("scrappers/config.json")["headers"]
    url = "https://www.alfabank.by/investments/fbu/"
    response = requests.get(url, verify=False, headers=headers)
    page = BeautifulSoup(response.text, "html.parser")
    data_div = page.find_all("div", {"class": "line-chart-details__price"})

    pie_items = []
    for pie_item in data_div:
        item = pie_item.text
        pie_items.append(item)

    replace_values = {" $": "", ".": ","}

    pie = multiple_replace(pie_items[1], replace_values)

    return pie
