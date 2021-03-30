from pymongo import MongoClient

client = MongoClient('localhost', 27017)

localSameAddress = client['localSameAddress']


def test_func():
    data = localSameAddress['same_address_20']

    total_cnt = data.count_documents({})

    cnt = 0
    for info in data.find({}).batch_size(1):
        current_data = localSameAddress['same_address_20']
        for is_overlap in current_data.find({"address": info['address'], "_id": {"$ne": info['_id']}}):
            current_data.delete_one({"_id": is_overlap['_id']})
        cnt += 1
        print(cnt, "/", total_cnt, info)


test_func()
