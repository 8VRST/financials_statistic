from pathlib import Path
import json
import datetime


def today_date():
    datestamp = datetime.date.today().strftime("%d.%m.%Y")
    return datestamp


def relative_date(date, days):
    format_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    final_date = ((format_date + datetime.timedelta(days=days)).strftime("%d.%m.%Y"))
    return final_date


def multiple_replace(target: str, replace_values: dict):
    for x, y in replace_values.items():
        target = target.replace(x, y)
    return target


def open_json_file(path_to_file):
    with open(Path(path_to_file), encoding="utf-8") as open_file:
        data = json.load(open_file)
    return data