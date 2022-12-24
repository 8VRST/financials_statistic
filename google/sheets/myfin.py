from utils.methods import today_date
from google.engine import gsheet, worksheets
from scrappers.myfin import Metals


class Update:

    def __init__(self):
        self.metals = Metals()
        self.silver_sheet = gsheet.worksheet(worksheets["silver"])
        self.gold_sheet = gsheet.worksheet(worksheets["gold"])
        self.datestamp = today_date()

    def silver(self):
        data = self.metals.silver()
        self._gram_pointer(data=data, worksheet=self.silver_sheet)

    def gold(self):
        data = self.metals.gold()
        self._gram_pointer(data=data, worksheet=self.gold_sheet)

    def _pattern(self, data_elements1: list,  data_elements2: list, worksheet, cell_coordinates: tuple):
        """
        :param cell_coordinates: the first element is row, the second and third are the columns
        """
        bank_and_buy = dict(zip(data_elements1, data_elements2))
        bank_best_buy = max(list(bank_and_buy.keys()))
        bank_best_name = bank_and_buy[bank_best_buy]

        worksheet.update_cell(cell_coordinates[0], cell_coordinates[1], bank_best_name)
        worksheet.update_cell(cell_coordinates[0], cell_coordinates[2], bank_best_buy)

    def _gram_pointer(self, data: list, worksheet):
        worksheet.update_cell(2, 1, self.datestamp)

        # from one gram to 1kg
        for data_slice, column1, column2 in zip(range(1, 19, 2), range(2, 20, 2), range(3, 21, 2)):
            self._pattern(data_elements1=data[data_slice::19], data_elements2=data[0::19],
                          worksheet=worksheet, cell_coordinates=(2, column1, column2))