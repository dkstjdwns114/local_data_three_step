from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster["three-step"]
local_realtime_close = db['local_realtime_close']
local_realtime_open = db['local_realtime_open']


local_realtime_close.delete_many({"closed_date": "20210413"})
local_realtime_open.delete_many({"authorization_date": "20210413"})
