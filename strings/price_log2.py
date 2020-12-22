import delorean
from decimal import Decimal
import parse
class Price_log(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp,self.product_id,self.price)
    @classmethod
    def parse(cls,text_log):
        def price(string):
            return Decimal(string)
        def isodate(string):
            return delorean.parse(string)
        FORMAT = ('[{timestamp:isodate}] - SALE - PRODUCT: {product:d} - ''PRICE: ${price:price}')
        formats = {'price': price, 'isodate': isodate}
        result = parse.parse(FORMAT, text_log, formats)
        return cls(timestamp=result['timestamp'],
        product_id=result['product'],
        price=result['price'])       

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'
print(Price_log.parse(log).timestamp.datetime.year)