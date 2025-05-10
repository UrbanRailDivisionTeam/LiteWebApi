from pymongo import MongoClient

debug_host = 'localhost'
product_host = '10.24.1.242'

connect = MongoClient(host=debug_host, port=27017)
