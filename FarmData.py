import random
from pyfaker import Fake
import time
import sys
import csv
import FarmDataConfig as config

TotalRecords=10
fake=Fake()
if (len(sys.argv)>2):
    print("Usage: FarmData <OutputFileName>")
else:
    with open(sys.argv[1], 'w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(config.ColumnHeaders)

        for i in range(1, TotalRecords+1):
            writer.writerow([
            fake.Name.name(),
            random.choice(config.LiveStockType),
            random.randrange(1, 200),
            config.random_date("1/1/2019 1:34 PM", "9/12/2020 1:34 PM"),
            str(random.randrange(1000, 100000))
            ])
