import random
import time

LiveStockType = ['Cow', 'Pig', 'Horse', 'Chicken']

ColumnHeaders = ['Farmer', 'LiveStockType', 'Weight', 'HarvestDate', 'Profit']

def random_date(start, end):
    format='%m/%d/%Y %I:%M %p'
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + random.random() * (etime - stime)
    return time.strftime(format, time.localtime(ptime))
