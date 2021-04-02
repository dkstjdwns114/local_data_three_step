from bson import ObjectId
from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster["three-step"]
local_realtime_close = db['local_realtime_close']
local_realtime_open = db['local_realtime_open']


def close_update():
    cnt = 0
    for info in local_realtime_close.find({}):
        cnt += 1
        print(cnt, info)
        if info['category_name'] == "animal":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "동물"}})
        elif info['category_name'] == "culture":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "문화"}})
        elif info['category_name'] == "environment":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "환경"}})
        elif info['category_name'] == "food":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "식품"}})
        elif info['category_name'] == "health":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "건강"}})
        elif info['category_name'] == "life":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "생활"}})
        elif info['category_name'] == "other":
            local_realtime_close.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "기타"}})


def open_update():
    cnt = 0
    for info in local_realtime_open.find({}):
        cnt += 1
        print(cnt, info)
        if info['category_name'] == "animal":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "동물"}})
        elif info['category_name'] == "culture":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "문화"}})
        elif info['category_name'] == "environment":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "환경"}})
        elif info['category_name'] == "food":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "식품"}})
        elif info['category_name'] == "health":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "건강"}})
        elif info['category_name'] == "life":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "생활"}})
        elif info['category_name'] == "other":
            local_realtime_open.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"category_kor": "기타"}})


close_update()
open_update()
