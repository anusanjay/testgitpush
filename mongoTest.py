import pymongo
client = pymongo.MongoClient("mongodb+srv://anu:Test@cluster0.uhlpq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={
    "name":"anu",
    "email":"anu@test",
    "surname":"rp"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)