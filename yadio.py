import requests

from collections import OrderedDict


_BASE_URL = 'https://api.yadio.io/'

_EXRATES = 'exrates/{currency}'
_CONVERT = 'convert/{amount}/{from_}/{to}'
_MARKET_ADS = 'market/ads'
_EXCHANGES = 'market/exchanges'
_PAY_METHODS = 'market/pay_methods'
_STATS = 'market/stats'
_JSON = 'json/{currency}'
_RATE = 'rate/{currency0}/{currency1}'
_TODAY = 'today/{range_}/{currency}'
_HIST = 'hist/{range_}/{currency}'
_COMPARE = 'compare/{range_}/{currency}'
_CURRENCIES = 'currencies'
_PING = 'ping'


class yadio:
    def exrates(self, currency: str = ''):
        return self._v1(_EXRATES.format(currency=currency))

    def convert(self, amount: int, from_: str, to: str):
        return self._v1(_CONVERT.format(amount=amount, from_=from_, to=to))

    def market_ads(self, currency: str, side: str, limit: int = None):
        return self._v1(_MARKET_ADS, currency=currency, side=side, limit=limit)

    def exchanges(self):
        return self._v1(_EXCHANGES)

    def pay_methods(self, currency: str):
        return self._v1(_PAY_METHODS, currency=currency)

    def stats(self, currency: str, side: str):
        return self._v1(_STATS, currency=currency, side=side)

    def json(self, currency: str):
        return self._v1(_JSON.format(currency=currency))

    def rate(self, currency0: str, currency1: str):
        return self._v1(_RATE.format(currency0=currency0, currency1=currency1))

    def today(self, range_: int, currency: str):
        return self._v1(_TODAY.format(range_=range_, currency=currency))

    def hist(self, range_: int, currency: str):
        return self._v1(_HIST.format(range_=range_, currency=currency))

    def compare(self, range_: int, currency: str):
        return self._v1(_COMPARE.format(range_=range_, currency=currency))

    def currencies(self):
        return self._v1(_CURRENCIES)

    def ping(self):
        return self._v1(_PING)

    def _v1(self, path: str, method: str = 'get', **params):
        params = OrderedDict(sorted(params.items()))

        if method == 'post':
            resp = requests.post(_BASE_URL + path, json=params)
        else:
            func = getattr(requests, method)
            resp = func(_BASE_URL + path, params=params)

        return resp.json()
