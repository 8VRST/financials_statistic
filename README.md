Financials goal: quickly and automatically receive info about the currency, assets and metal prices to upload the data to Google Sheet.


**Deployment:**<br />
Everything is working and tested on Windows 10 machine with Python 3.8 and Ubuntu 18.04 with Python 3.7
1. Create virtual environment
2. Install in virtual environment requirements.txt
3. Rename google/config_example.json to config.json and set the names for your sheets.
4. Put your credentials file for Google API instead of google/creds_example.json (the file need to be downloaded from Google API page)
5. Run run_updater.py to start receive data into your Google Sheet