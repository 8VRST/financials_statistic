from scrappers.alfabank import pie
from google.engine import gsheet, worksheets


def update_pie():
    gold_sheet = gsheet.worksheet(worksheets["gold"])
    data = pie()
    gold_sheet.update_cell(8, 8, str(data))
