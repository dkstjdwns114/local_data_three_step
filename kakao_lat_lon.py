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


# my_func()


def err_data():
    same_address = localSameAddress['same_address']

    err_id = []
    err_addr = []
    err_id.append(ObjectId("605de6bbf18e98579e436354"))
    err_addr.append("부산광역시 사상구 덕포동 368-7")
    err_id.append(ObjectId("605de6d4d78b420e42881ad9"))
    err_addr.append("인천광역시 계양구 작전동 765-1")
    err_id.append(ObjectId("605de6e8ecff50efcb766063"))
    err_addr.append("경상북도 영천시 교촌동 236-1")
    err_id.append(ObjectId("605de6f1c087cb832b4c8cf8"))
    err_addr.append("대구광역시 중구 달성동 294-1")
    err_id.append(ObjectId("605de716ecff50efcb766090"))
    err_addr.append("경상북도 포항시 남구 송내동 1")
    err_id.append(ObjectId("605de717c087cb832b4c8d2f"))
    err_addr.append("대구광역시 동구 율암동 1104")
    err_id.append(ObjectId("605de720a4b450d4046e2094"))
    err_addr.append("세종특별자치시 조치원읍 침산리 167-21")
    err_id.append(ObjectId("605de729c087cb832b4c8d4f"))
    err_addr.append("대구광역시 서구 중리동 1029-5")
    err_id.append(ObjectId("605de7367f6f14832759b6b7"))
    err_addr.append("전라남도 목포시 죽교동 465-46")
    err_id.append(ObjectId("605de737defc8519a3d512f8"))
    err_addr.append("제주특별자치도 서귀포시 서귀동 370-3")
    err_id.append(ObjectId("605de758f18e98579e436442"))
    err_addr.append("부산광역시 부산진구 초읍동 206-98")
    err_id.append(ObjectId("605de75fbfc302260dd17668"))
    err_addr.append("울산광역시 남구 달동 580-8")
    err_id.append(ObjectId("605de766a039b4bfe1188f2b"))
    err_addr.append("전라북도 김제시 신풍동 484")
    err_id.append(ObjectId("605de77aa4546687b166a8cb"))
    err_addr.append("경상남도 사천시 선구동 41-60")
    err_id.append(ObjectId("605de77adefc8519a3d5136a"))
    err_addr.append("제주특별자치도 서귀포시 서귀동 272-17")
    err_id.append(ObjectId("605de790a039b4bfe1188fb0"))
    err_addr.append("전라북도 전주시 완산구 고사동 96-1")
    err_id.append(ObjectId("605de7a97f6f14832759b85e"))
    err_addr.append("전라남도 보성군 벌교읍 벌교리 878-3")
    err_id.append(ObjectId("605de7b3ecff50efcb766163"))
    err_addr.append("경상북도 김천시 지례면 도곡리 산44")
    err_id.append(ObjectId("605de7d4a039b4bfe11890ef"))
    err_addr.append("전라북도 부안군 주산면 돈계리")
    err_id.append(ObjectId("605de7dd508b0f4f488183ff"))
    err_addr.append("광주광역시 남구 백운동 636-7")
    err_id.append(ObjectId("605de83011eb28ab6ed32bb4"))
    err_addr.append("충청남도 서천군 서면 마량리 275-5")
    err_id.append(ObjectId("605de857a4546687b166ac55"))
    err_addr.append("경상남도 창원시 성산구 성주동 42")
    err_id.append(ObjectId("605de857f18e98579e436714"))
    err_addr.append("부산광역시 금정구 부곡동 736-6")
    err_id.append(ObjectId("605de888ecff50efcb76643f"))
    err_addr.append("경상북도 구미시 공단동 130-19")
    err_id.append(ObjectId("605de8aaa4546687b166add7"))
    err_addr.append("경상남도 창원시 성산구 성주동 28")
    err_id.append(ObjectId("605de931c087cb832b4c956d"))
    err_addr.append("대구광역시 중구 남산동 611-11")
    err_id.append(ObjectId("605de959a4546687b166b36a"))
    err_addr.append("경상남도 창원시 의창구 소계동 715-12")
    err_id.append(ObjectId("605de965a4546687b166b399"))
    err_addr.append("경남 창원시 성산구 성주동 5")
    err_id.append(ObjectId("605dea9f2d4d783a62c71354"))
    err_addr.append("서울특별시 강남구 대치동 962-14")
    err_id.append(ObjectId("605dead8ef0d07c6cfb63cd4"))
    err_addr.append("경기 수원시 권선구 권선동 1011-8")
    err_id.append(ObjectId("605deb75ef0d07c6cfb63d80"))
    err_addr.append("경기도 화성시 반송동 157-14")
    err_id.append(ObjectId("605defbfef0d07c6cfb64cf4"))
    err_addr.append("경기 양주시 장흥면 울대리 387-5")
    err_id.append(ObjectId("605df2bd2d4d783a62c72e93"))
    err_addr.append("서울특별시 강북구 미아동 316-3")
    err_id.append(ObjectId("605df55a2d4d783a62c73ae3"))
    err_addr.append("서울특별시 마포구 노고산동 117-10")
    err_id.append(ObjectId("605df5d72d4d783a62c73ba7"))
    err_addr.append("서울특별시 강동구 명일동 312-90")

    cnt = 0
    total = len(err_id)
    for info in err_id:

        address = err_addr[cnt]

        url = 'https://dapi.kakao.com/v2/local/search/address.json?&query=' + address
        result = requests.get(urlparse(url).geturl(),
                              headers={'Authorization': 'KakaoAK 81ac01545c21ab8306908436ee2f9183'}).json()
        if len(result['documents']) == 0:
            continue
        match_first = result['documents'][0]['address']
        lat = float(match_first['y'])
        lng = float(match_first['x'])

        same_address.update_one({"_id": info}, {"$set": {"lon": lng}})
        same_address.update_one({"_id": info}, {"$set": {"lat": lat}})
        print(cnt, "/", total, lat, lng)  # 위도(lat) 경도(long)
        cnt += 1


err_data()
