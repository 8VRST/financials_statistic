import time
import random
import logging

from google.sheets import alfabank, myfin, nbrb, statistic


while True:
    try:

        nbrb.update_usd_rate()
        myfin.Update().silver()
        myfin.Update().gold()
        statistic.Update().byn()
        statistic.Update().usd()
        alfabank.update_pie()

    except Exception as error:
        logging.error(msg=error)

    time.sleep(random.randint(450, 650))
