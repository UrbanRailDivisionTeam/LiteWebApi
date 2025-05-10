from pymongo import MongoClient

debug_host = 'localhost'
product_host = 'mongodb'

connect = MongoClient(host=product_host, port=27017)
