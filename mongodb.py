from pymongo import MongoClient

mongoURL = 'mongodb://192.168.1.25:27017'
client = MongoClient(mongoURL)
db = client.test
db.authenticate('tester','tester', mechanism='SCRAM-SHA-1')
for doc in db.stocks.find():
    print(doc)