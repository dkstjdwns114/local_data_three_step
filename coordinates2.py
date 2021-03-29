import csv
from multiprocessing import Process

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

localSameAddress = client['localSameAddress']


def second():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_201912_02.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        result = line[0].split("|")
        if len(result) == 39:
            rdnmAdr = result[31]
            for local in same_address.find({"$or": [{"city": "daegu"}, {"city": "incheon"}, {"city": "gwangju"}, {"city": "daejeon"}, {"city": "ulsan"}, {"city": "sejong"}]}):
                split1 = local['address'].split(',')[0]
                split2 = split1.split("(")[0]
                local_address = split2.strip()
                # print(local_address, rdnmAdr)

                if local_address == rdnmAdr:
                    cnt += 1
                    print(cnt, result[37], result[38], local)
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": result[37]}})
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": result[38]}})
                    break


def third():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_201912_03.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        result = line[0].split("|")
        if len(result) == 39:
            rdnmAdr = result[31]
            for local in same_address.find({"$or": [{"city": "gyeonggi"}, {"city": "gangwon"}, {"city": "chungbuk"}]}):
                split1 = local['address'].split(',')[0]
                split2 = split1.split("(")[0]
                local_address = split2.strip()
                # print(local_address, rdnmAdr)

                if local_address == rdnmAdr:
                    cnt += 1
                    print(cnt, result[37], result[38], local)
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": result[37]}})
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": result[38]}})
                    break


def fourth():
    same_address = localSameAddress['same_address']
    f = open('./prev_csv_data/상가업소정보_201912_03.csv', 'r', encoding='utf-8')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt = 0
    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        result = line[0].split("|")
        if len(result) == 39:
            rdnmAdr = result[31]
            for local in same_address.find({"$or": [{"city": "chungnam"}, {"city": "jeonbuk"}, {"city": "jeonnam"}, {"city": "gyeongbuk"}, {"city": "gyeongnam"}, {"city": "jeju"}]}):
                split1 = local['address'].split(',')[0]
                split2 = split1.split("(")[0]
                local_address = split2.strip()
                # print(local_address, rdnmAdr)

                if local_address == rdnmAdr:
                    cnt += 1
                    print(cnt, result[37], result[38], local)
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": result[37]}})
                    same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": result[38]}})
                    break


if __name__ == "__main__":
    p1 = Process(target=second)
    p2 = Process(target=third)
    p3 = Process(target=fourth)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
