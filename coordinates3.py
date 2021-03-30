import csv
from multiprocessing import Process

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

localSameAddress = client['localSameAddress']


def first():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_202012_1.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        for local in same_address.find({"$and": [{"lon": {"$exists": False}}, {"$or": [{"city": "seoul"}, {"city": "busan"}]}]}).batch_size(1):
            split1 = local['address'].split(',')[0]
            split2 = split1.split("(")[0]
            local_address = split2.strip()

            if local_address == rdnmAdr:
                cnt += 1
                print(cnt, line[37], line[38], local)
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": line[37]}})
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": line[38]}})
                break


def second():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_202012_2.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        for local in same_address.find({"$and": [{"lon": {"$exists": False}}, {"$or": [{"city": "daegu"}, {"city": "incheon"}, {"city": "gwangju"}, {"city": "daejeon"}, {"city": "ulsan"}, {"city": "sejong"}]}]}).batch_size(1):
            split1 = local['address'].split(',')[0]
            split2 = split1.split("(")[0]
            local_address = split2.strip()

            if local_address == rdnmAdr:
                cnt += 1
                print(cnt, line[37], line[38], local)
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": line[37]}})
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": line[38]}})
                break


def third():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_202012_3.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        for local in same_address.find({"$and": [{"lon": {"$exists": False}}, {"$or": [{"city": "gyeonggi"}, {"city": "gangwon"}, {"city": "chungbuk"}]}]}).batch_size(1):
            split1 = local['address'].split(',')[0]
            split2 = split1.split("(")[0]
            local_address = split2.strip()

            if local_address == rdnmAdr:
                cnt += 1
                print(cnt, line[37], line[38], local)
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": line[37]}})
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": line[38]}})
                break


def fourth():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_202012_4.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        for local in same_address.find({"$and": [{"lon": {"$exists": False}}, {"$or": [{"city": "chungnam"}, {"city": "jeonbuk"}, {"city": "jeonnam"}, {"city": "gyeongbuk"}, {"city": "gyeongnam"}, {"city": "jeju"}]}]}).batch_size(1):
            split1 = local['address'].split(',')[0]
            split2 = split1.split("(")[0]
            local_address = split2.strip()

            if local_address == rdnmAdr:
                cnt += 1
                print(cnt, line[37], line[38], local)
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": line[37]}})
                same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": line[38]}})
                break


if __name__ == "__main__":
    p1 = Process(target=second)
    p2 = Process(target=third)
    p3 = Process(target=fourth)
    p4 = Process(target=first)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
