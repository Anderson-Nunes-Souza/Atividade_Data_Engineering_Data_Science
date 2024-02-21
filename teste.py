from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['coinmarketcap']
collection = db['bitcoin_data_test']

dict = {
    "parametro3": "informação 4"
}

#print(type(dict))
print(collection.insert_one(dict))
#funciona, guardou parametro1 e parametro 2 no bd