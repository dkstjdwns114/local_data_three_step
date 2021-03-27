from bson import ObjectId
from pymongo import MongoClient
from multiprocessing import Process

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

localSameAddress = client['localSameAddress']


def cluster_data():
    same_address = db['same_address']

    cnt = 0
    total_cnt = same_address.count_documents({})
    for info in same_address.find({}).batch_size(1):
        cnt += 1
        if info['address'].split(' ')[0] == "부산광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "busan"}})
        elif info['address'].split(' ')[0] == "충청북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "chungbuk"}})
        elif info['address'].split(' ')[0] == "충청남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "chungnam"}})
        elif info['address'].split(' ')[0] == "대구광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "daegu"}})
        elif info['address'].split(' ')[0] == "대전광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "daejeon"}})
        elif info['address'].split(' ')[0] == "강원도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gangwon"}})
        elif info['address'].split(' ')[0] == "광주광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gwangju"}})
        elif info['address'].split(' ')[0] == "경기도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeonggi"}})
        elif info['address'].split(' ')[0] == "경상북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeongbuk"}})
        elif info['address'].split(' ')[0] == "경상남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeongnam"}})
        elif info['address'].split(' ')[0] == "인천광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "incheon"}})
        elif info['address'].split(' ')[0] == "제주특별자치도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeju"}})
        elif info['address'].split(' ')[0] == "전라북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeonbuk"}})
        elif info['address'].split(' ')[0] == "전라남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeonnam"}})
        elif info['address'].split(' ')[0] == "세종특별자치시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "sejong"}})
        elif info['address'].split(' ')[0] == "서울특별시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "seoul"}})
        elif info['address'].split(' ')[0] == "울산광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "ulsan"}})

        print("cluster", cnt, "/", total_cnt, info['address'])


def local_data():
    same_address = localSameAddress['same_address']

    cnt = 0
    total_cnt = same_address.count_documents({})
    for info in same_address.find({}).batch_size(1):
        cnt += 1
        if info['address'].split(' ')[0] == "부산광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "busan"}})
        elif info['address'].split(' ')[0] == "충청북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "chungbuk"}})
        elif info['address'].split(' ')[0] == "충청남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "chungnam"}})
        elif info['address'].split(' ')[0] == "대구광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "daegu"}})
        elif info['address'].split(' ')[0] == "대전광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "daejeon"}})
        elif info['address'].split(' ')[0] == "강원도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gangwon"}})
        elif info['address'].split(' ')[0] == "광주광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gwangju"}})
        elif info['address'].split(' ')[0] == "경기도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeonggi"}})
        elif info['address'].split(' ')[0] == "경상북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeongbuk"}})
        elif info['address'].split(' ')[0] == "경상남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "gyeongnam"}})
        elif info['address'].split(' ')[0] == "인천광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "incheon"}})
        elif info['address'].split(' ')[0] == "제주특별자치도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeju"}})
        elif info['address'].split(' ')[0] == "전라북도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeonbuk"}})
        elif info['address'].split(' ')[0] == "전라남도":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "jeonnam"}})
        elif info['address'].split(' ')[0] == "세종특별자치시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "sejong"}})
        elif info['address'].split(' ')[0] == "서울특별시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "seoul"}})
        elif info['address'].split(' ')[0] == "울산광역시":
            same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"city": "ulsan"}})

        print("local", cnt, "/", total_cnt, info['address'])


if __name__ == "__main__":
    p1 = Process(target=cluster_data)
    p2 = Process(target=local_data)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
