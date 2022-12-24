from utils.methods import relative_date
from scrappers.nbrb import usd_on_date
from utils.methods import today_date
from google.engine import gsheet, worksheets


def update_usd_rate():
    datestamp = today_date()
    rate_worksheet = gsheet.worksheet(worksheets["nbrb"])

    for date, usd_rate in zip(rate_worksheet.col_values(1)[int(int(rate_worksheet.find("0,0000").row) - 2)::],
                              rate_worksheet.col_values(2)[int(int(rate_worksheet.find("0,0000").row) - 2)::]):

        date_position = rate_worksheet.find(date).row

        if date == datestamp and str(usd_rate) != str(usd_on_date(relative_date(date, 1))):
            if usd_on_date(relative_date(date, 1)) == 404:
                rate_worksheet.update_cell(date_position, 2, float(usd_on_date(relative_date(date, 0))))
            else:
                rate_worksheet.update_cell(date_position, 2, float(usd_on_date(relative_date(date, 1))))
        elif usd_on_date(relative_date(date, 1)) == 404:
            break
        elif date != str(datestamp) and str(usd_rate) != str(usd_on_date(relative_date(date, 1))):
            rate_worksheet.update_cell(date_position, 2, float(usd_on_date(relative_date(date, 1))))
        if usd_on_date(relative_date(date, 1)) == 404:
            rate_worksheet.update_cell(2, 4, float(usd_on_date(relative_date(date, 0))))
        else:
            rate_worksheet.update_cell(2, 4, float(usd_on_date(relative_date(date, 1))))
