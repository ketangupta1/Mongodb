import pymongo

mongoURI = "mongodb+srv://ketan123:ketan@cluster0.up5qiym.mongodb.net/test"

client = pymongo.MongoClient(mongoURI)

db = client["TODO"]
collection = db["todo"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({})
    # If we dont want id in the result then use collection.find({"_id":0}), then id will not fetched
    # we can modify output data which data is needed write 1 and which dont needed write 0
    data = []
    for doc in response:
        doc["_id"] = str(doc["_id"])
        data.append(doc)
    return data

def get_one(condition):
    response = collection.find_one({'name':condition})
    response["_id"] = str(response["_id"])
    return response

def update(data):
    data = dict(data)
    response = collection.update_one({"name":data["name"]},{"$set":{"description":data["description"]}})
    return response.modified_count

def delete(name):
    response = collection.delete_one({"name":name})
    return response.deleted_count

