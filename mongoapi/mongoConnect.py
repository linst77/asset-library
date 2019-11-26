import pymongo, dns
import pprint

client = pymongo.MongoClient("mongodb+srv://linst77:a0022001@testdb-iulbg.mongodb.net/test?retryWrites=true&w=majority")
db = client.testdb

client = pymongo.MongoClient("mongodb+srv://linst77:a0022001@testdb-iulbg.mongodb.net/test?retryWrites=true&w=majority")
db = client.testdb
db.list_collection_names()

