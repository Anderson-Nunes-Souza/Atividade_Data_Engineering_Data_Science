import requests
import datetime
import json
from pymongo import MongoClient

def bitcoin5years():
    data_atual = datetime.datetime.now()
    # Subtraia 5 anos da data atual
    data_menos_5_anos = data_atual - datetime.timedelta(days=5*365)
    # Formate a data no formato ISO 8601
    data_formatada = data_menos_5_anos.replace(microsecond=0).isoformat()
    # Refatorar data atual para formato ISO 8601
    data_atual = datetime.datetime.now().replace(microsecond=0).isoformat()
    request = f"https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1MTH&time_start={data_formatada}&limit=360&time_end={data_atual}"
    r = requests.get(request)
    #Validar se a requisição retorna 200
    if r.status_code == 200:
        data_dict = json.loads(r.text)
        # Conectando-se ao MongoDB
        client = MongoClient('localhost', 27017)
        db = client['coinmarketcap']
        collection = db['bitcoin_data_last_5_years']
        # Inserindo o dicionário na coleção do MongoDB
        collection.insert_many(data_dict)
        print("Informações adicionadas ao Collection bitcoin_data_last_5_years! - Verifique o seu MongoDB")
        return True
    else:
        print('Erro ao fazer a solicitação HTTP:', r.status_code)
    return 
    

def bitcoinLast30days():
    print("bitcoinLast30days")
    data_atual = datetime.datetime.now()
    # Subtraia 1 ano da data atual
    data_menos_30_dias = data_atual - datetime.timedelta(days=30)
    # Formate a data no formato ISO 8601
    data_formatada = data_menos_30_dias.replace(microsecond=0).isoformat()
    # Refatorar data atual para formato ISO 8601
    data_atual = datetime.datetime.now().replace(microsecond=0).isoformat()
    request = f'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?apikey=DC035A41-F1B1-4EF9-AD10-0349474586C3&period_id=1DAY&time_start={data_formatada}&limit=30&time_end={data_atual}'
    print(request)
    r = requests.get(request)
    #Validar se a requisição retorna 200
    if r.status_code == 200:
        data_dict = json.loads(r.text)
        # Conectando-se ao MongoDB
        client = MongoClient('localhost', 27017)
        db = client['coinmarketcap']
        collection = db['bitcoin_data_last_30_days']
        # Inserindo o dicionário na coleção do MongoDB
        collection.insert_many(data_dict)
        print("Informações adicionadas ao Collection bitcoin_data_last_30_days! - Verifique o seu MongoDB")
        return True
    else:
        print('Erro ao fazer a solicitação HTTP:', r.status_code)
    return 

def main():
    bitcoin5years()
    bitcoinLast30days()
    return

main()