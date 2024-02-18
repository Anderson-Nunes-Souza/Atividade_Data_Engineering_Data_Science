import requests
from datetime import date

def bitcoin5years():
    request = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1DAY&time_start=2021-01-01T00:00:00&limit=360'
    r = requests.get(request)
    print("teste")
    print(r.status_code)
    return 

def bitcoinLast360days():
    startday = date.today(-1)
    requests = '"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1DAY&time_start=' + startday +'&time_end={endday}'
    return

bitcoin5years()

bitcoinLast360days()
