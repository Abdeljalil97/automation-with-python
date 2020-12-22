import delorean
from decimal import Decimal
class Price_log(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp,self.product_id,self.price)
    @classmethod
    def parse(cls,text_log):
        devide_it = log.split(' - ')
        timestamp_string, _, product_string, price_string = devide_it
        timestamp = delorean.parse(timestamp_string.strip('[]'))
        product_id = int(product_string.split(':')[-1])
        price = Decimal(price_string.split('$')[-1])
        return cls(timestamp = timestamp , product_id = product_id, price = price)

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'
print(Price_log.parse(log))