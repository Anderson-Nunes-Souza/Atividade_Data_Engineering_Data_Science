import pandas as pd
from pymongo import MongoClient
import pprint

def bitcoinLast360days():
    #Configurar o MongoClient
    client = MongoClient('localhost', 27017)
    db = client['coinmarketcap']
    collection = db['bitcoin_data_last_360_days']
    #criar Dicionário
    data_dict=[]
    #alimentar dicionário com dados do BD
    for x in collection.find():
       data_dict.append(x)
    return data_dict 


def bitcoinLast360days_Graphs():
    bitcoin_data = bitcoinLast360days()
    # Criar DataFrame do pandas com os dados recuperados
    df = pd.DataFrame(bitcoin_data)
    # Imprimir o DataFrame
    print(df) # Funcionou
    return
    

def main():
    bitcoinLast360days_Graphs()
