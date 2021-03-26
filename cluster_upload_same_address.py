from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
client = MongoClient('localhost', 27017)

db = cluster["three-step"]
localDb = client['localSameAddress']

cluster_collection = db['same_address']


def data():
    local_data = localDb['same_address']
    total_cnt = local_data.count_documents({})

    cnt = 0
    for store in local_data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", total_cnt, store)
        cluster_collection.insert_one(store)


# data()
