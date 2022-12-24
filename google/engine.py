import gspread

from utils.methods import open_json_file


config = open_json_file("google/config.json")
worksheets = config["worksheets"]


google_credentials = gspread.service_account(filename=config["credentials"])
gsheet = google_credentials.open(config["gsheet"])