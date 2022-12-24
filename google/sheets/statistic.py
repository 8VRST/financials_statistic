from utils.methods import today_date
from google.engine import gsheet, worksheets


class Update:

    datestamp = today_date()
    main_worksheet = gsheet.worksheet(worksheets["main"])
    earnings_worksheet = gsheet.worksheet(worksheets["earnings"])

    def byn(self):
        self._pattern(cell="L2")

    def usd(self):
        self._pattern(cell="M2")

    def _pattern(self, cell: str):
        for date_earnings in self.earnings_worksheet.col_values(1)[int(int(self.earnings_worksheet.find(self.datestamp).row) - 1)::]:
            date_position_earnings = self.earnings_worksheet.find(date_earnings).row
            if str(date_earnings) == self.datestamp:
                self.earnings_worksheet.update_cell((date_position_earnings), 2, float(self.main_worksheet.acell(cell).value.replace(",", ".")))
            else:
                break
