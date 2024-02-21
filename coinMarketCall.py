import requests
from datetime import date
import json
from pymongo import MongoClient


def bitcoin5years():
    print('bitcoin5years')
    request = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1DAY&time_start=2021-01-01T00:00:00&limit=4'
    r = requests.get(request)
    if r.status_code == 200:
        data_dict = json.loads(r.text)
        # Conectando-se ao MongoDB
        client = MongoClient('localhost', 27017)
        db = client['coinmarketcap']
        collection = db['bitcoin_data']
        # Inserindo o dicionário na coleção do MongoDB
        collection.insert_many(data_dict)
        return True
    else:
        print('Erro ao fazer a solicitação HTTP:', r.status_code)
        return False
    

def bitcoinLast360days():
    print("bitcoinLast360days")
    # startDay = date.today(-1)
    # endDay = date.month()
    # requests = '"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOTs_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1DAY&time_start=' + startDay +'&time_end={endday}'
    return

bitcoin5years()

bitcoinLast360days()
