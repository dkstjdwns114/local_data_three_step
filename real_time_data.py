from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from pymongo import MongoClient
import xmltodict, json
from datetime import date, timedelta
from multiprocessing import Process

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster["three-step"]
local_realtime_close = db['local_realtime_close']
local_realtime_open = db['local_realtime_open']

jsonObj = {}

url = 'http://www.localdata.go.kr/platform/rest/TO0/openDataApi'

today_form = date.today()
yesterday_form = date.today() - timedelta(1)

today = today_form.strftime('%Y%m%d')
yesterday = yesterday_form.strftime('%Y%m%d')


def close(yesterday_str, today_str):
    queryParams = '?' + urlencode({
        quote_plus("authKey"): "uZ98I03VR/zZ3zAvdNIVEl8EWJy6llSwLtDAMDlOYkE=",

        quote_plus("lastModTsBgn"): yesterday_str,

        quote_plus("lastModTsEnd"): today_str,

        quote_plus("state"): "03",

        quote_plus("pageSize"): "10000",

        quote_plus("resultType"): "xml"
    })

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'

    response_body = urlopen(request).read()

    dict = xmltodict.parse(response_body)

    jsonString = json.dumps(dict['result']['body'], ensure_ascii=False)

    jsonObj = json.loads(jsonString)

    if jsonObj['rows']:
        cnt = 0
        for item in jsonObj['rows']['row']:
            if item['dcbYmd'] == yesterday_str:
                cnt += 1
                city_name = ""
                category_name = ""
                category_kor = ""
                city_split = ""
                if item['rdnWhlAddr']:
                    city_split = item['rdnWhlAddr'].split(' ')[0]
                    address = item['rdnWhlAddr']
                else:
                    city_split = item['siteWhlAddr'].split(' ')[0]
                    address = item['siteWhlAddr']

                if city_split == "부산광역시":
                    city_name = "busan"
                elif city_split == "충청북도":
                    city_name = "chungbuk"
                elif city_split == "충청남도":
                    city_name = "chungnam"
                elif city_split == "대구광역시":
                    city_name = "daegu"
                elif city_split == "대전광역시":
                    city_name = "daejeon"
                elif city_split == "강원도":
                    city_name = "gangwon"
                elif city_split == "광주광역시":
                    city_name = "gwangju"
                elif city_split == "경기도":
                    city_name = "gyeonggi"
                elif city_split == "경상북도":
                    city_name = "gyeongbuk"
                elif city_split == "경상남도":
                    city_name = "gyeongnam"
                elif city_split == "인천광역시":
                    city_name = "incheon"
                elif city_split == "제주특별자치도":
                    city_name = "jeju"
                elif city_split == "전라북도":
                    city_name = "jeonbuk"
                elif city_split == "전라남도":
                    city_name = "jeonnam"
                elif city_split == "세종특별자치시":
                    city_name = "sejong"
                elif city_split == "서울특별시":
                    city_name = "seoul"
                elif city_split == "울산광역시":
                    city_name = "ulsan"

                open_service_id_split = item['opnSvcId'][0:2]

                if open_service_id_split == "01":
                    category_name = "health"
                    category_kor = "건강"
                elif open_service_id_split == "02":
                    category_name = "animal"
                    category_kor = "동물"
                elif open_service_id_split == "03" or open_service_id_split == "04":
                    category_name = "culture"
                    category_kor = "문화"
                elif open_service_id_split == "05" or open_service_id_split == "06" or open_service_id_split == "08" or open_service_id_split == "10":
                    category_name = "life"
                    category_kor = "생활"
                elif open_service_id_split == "07":
                    category_name = "food"
                    category_kor = "식품"
                elif open_service_id_split == "09":
                    category_name = "environment"
                    category_kor = "환경"
                elif open_service_id_split == "11":
                    category_name = "other"
                    category_kor = "기타"

                info = {
                    "data": "close",
                    "update_date": item['updateDt'],
                    "authorization_date": item['apvPermYmd'],
                    "closed_date": item['dcbYmd'],
                    "store_name": item['bplcNm'],
                    "address": address,
                    "state_code": item['trdStateGbn'],
                    "state": item['trdStateNm'],
                    "open_service_id": item['opnSvcId'],
                    "open_service": item['opnSvcNm'],
                    "detailed_classification": item['uptaeNm'],
                    "city_name": city_name,
                    "category_name": category_name,
                    "category_kor": category_kor,
                }
                print(cnt, "close", info)
                local_real_time_close_id = local_realtime_close.insert_one(info).inserted_id


def today_open(yesterday_str):
    queryParams = '?' + urlencode({
        quote_plus("authKey"): "uZ98I03VR/zZ3zAvdNIVEl8EWJy6llSwLtDAMDlOYkE=",

        quote_plus("bgnYmd"): yesterday_str,

        quote_plus("endYmd"): yesterday_str,

        quote_plus("state"): "01",

        quote_plus("pageSize"): "10000",

        quote_plus("resultType"): "xml"
    })

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'

    response_body = urlopen(request).read()

    dict = xmltodict.parse(response_body)

    jsonString = json.dumps(dict['result']['body'], ensure_ascii=False)

    jsonObj = json.loads(jsonString)

    if jsonObj['rows']:
        cnt = 0
        for item in jsonObj['rows']['row']:
            if item['apvPermYmd'] == yesterday_str:
                cnt += 1
                city_name = ""
                category_name = ""
                category_kor = ""
                city_split = ""
                if item['rdnWhlAddr']:
                    city_split = item['rdnWhlAddr'].split(' ')[0]
                    address = item['rdnWhlAddr']
                else:
                    city_split = item['siteWhlAddr'].split(' ')[0]
                    address = item['siteWhlAddr']

                if city_split == "부산광역시":
                    city_name = "busan"
                elif city_split == "충청북도":
                    city_name = "chungbuk"
                elif city_split == "충청남도":
                    city_name = "chungnam"
                elif city_split == "대구광역시":
                    city_name = "daegu"
                elif city_split == "대전광역시":
                    city_name = "daejeon"
                elif city_split == "강원도":
                    city_name = "gangwon"
                elif city_split == "광주광역시":
                    city_name = "gwangju"
                elif city_split == "경기도":
                    city_name = "gyeonggi"
                elif city_split == "경상북도":
                    city_name = "gyeongbuk"
                elif city_split == "경상남도":
                    city_name = "gyeongnam"
                elif city_split == "인천광역시":
                    city_name = "incheon"
                elif city_split == "제주특별자치도":
                    city_name = "jeju"
                elif city_split == "전라북도":
                    city_name = "jeonbuk"
                elif city_split == "전라남도":
                    city_name = "jeonnam"
                elif city_split == "세종특별자치시":
                    city_name = "sejong"
                elif city_split == "서울특별시":
                    city_name = "seoul"
                elif city_split == "울산광역시":
                    city_name = "ulsan"

                open_service_id_split = item['opnSvcId'][0:2]

                if open_service_id_split == "01":
                    category_name = "health"
                    category_kor = "건강"
                elif open_service_id_split == "02":
                    category_name = "animal"
                    category_kor = "동물"
                elif open_service_id_split == "03" or open_service_id_split == "04":
                    category_name = "culture"
                    category_kor = "문화"
                elif open_service_id_split == "05" or open_service_id_split == "06" or open_service_id_split == "08" or open_service_id_split == "10":
                    category_name = "life"
                    category_kor = "생활"
                elif open_service_id_split == "07":
                    category_name = "food"
                    category_kor = "식품"
                elif open_service_id_split == "09":
                    category_name = "environment"
                    category_kor = "환경"
                elif open_service_id_split == "11":
                    category_name = "other"
                    category_kor = "기타"

                info = {
                    "data": "open",
                    "update_date": item['updateDt'],
                    "authorization_date": item['apvPermYmd'],
                    "closed_date": item['dcbYmd'],
                    "store_name": item['bplcNm'],
                    "address": item['rdnWhlAddr'],
                    "state_code": item['trdStateGbn'],
                    "state": item['trdStateNm'],
                    "open_service_id": item['opnSvcId'],
                    "open_service": item['opnSvcNm'],
                    "detailed_classification": item['uptaeNm'],
                    "city_name": city_name,
                    "category_name": category_name,
                    "category_kor": category_kor,
                }

                print(cnt, "open", info)
                local_real_time_open_id = local_realtime_open.insert_one(info).inserted_id


if __name__ == "__main__":
    p1 = Process(target=close(yesterday, today))
    p2 = Process(target=today_open(yesterday))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
