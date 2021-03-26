from pymongo import MongoClient

client = MongoClient('localhost', 27017)

localSameAddress = client['localSameAddress']


def test_func():
    data = localSameAddress['same_address']

    total_cnt = data.count_documents({})

    cnt = 0
    for info in data.find({}):
        current_data = localSameAddress['same_address']
        current_cnt = current_data.count_documents({})
        for is_overlap in current_data.find({"address": info['address'], "_id": {"$ne": info['_id']}}):
            current_data.delete_one({"_id": is_overlap['_id']})
        cnt += 1
        print(cnt, "/", current_cnt, "/", total_cnt, info)


'''
test_func()
'''


def view_func():
    data = localSameAddress['same_address']

    total_cnt = data.count_documents({})

    cnt = 0
    max_cnt = 0
    for info in data.find({}):
        cnt += 1
        if len(info['stores_info']) > max_cnt:
            max_cnt = len(info['stores_info'])
            max_cnt_id = info['_id']
        print(cnt, "/", total_cnt, len(info['stores_info']))
        print(info)

    print(max_cnt_id, max_cnt)


# view_func()
