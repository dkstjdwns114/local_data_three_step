import requests, time
from urllib.parse import urlparse
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("localhost", 27017)

localSameAddress = client['localSameAddress']


def my_func():
    same_address = localSameAddress['same_address']

    cnt = 0
    total = same_address.count_documents({"lon": {"$exists": False}})
    for info in same_address.find({"lon": {"$exists": False}}):
        cnt += 1
        split1 = info['address'].split(',')[0]
        address = split1.split("(")[0]

        url = 'https://dapi.kakao.com/v2/local/search/address.json?&query=' + address
        result = requests.get(urlparse(url).geturl(), headers={'Authorization': 'KakaoAK 81ac01545c21ab8306908436ee2f9183'}).json()
        if len(result['documents']) == 0:
            continue
        match_first = result['documents'][0]['address']
        lat = float(match_first['y'])
        lng = float(match_first['x'])

        same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"lon": lng}})
        same_address.update_one({"_id": ObjectId(info['_id'])}, {"$set": {"lat": lat}})
        print(cnt, "/", total, lat, lng)  # 위도(lat) 경도(long)
        # time.sleep(1)


my_func()
