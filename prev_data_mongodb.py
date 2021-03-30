import csv
from multiprocessing import Process

from pymongo import MongoClient

client = MongoClient("localhost", 27017)

my_test = client['my_test']


def first():
    busan = my_test['busan']
    seoul = my_test['seoul']
    f = open('./prev_csv_data/상가업소정보_202012_1.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        ctprvnNm = line[12]
        lon = line[37]
        lat = line[38]

        store = {
            "address": rdnmAdr,
            "lon": lon,
            "lat": lat
        }
        print(store)
        if ctprvnNm == "부산광역시":
            busan_id = busan.insert_one(store).inserted_id
        elif ctprvnNm == "서울특별시":
            seoul_id = seoul.insert_one(store).inserted_id


def second():
    daegu = my_test['daegu']
    incheon = my_test['incheon']
    gwangju = my_test['gwangju']
    daejeon = my_test['daejeon']
    ulsan = my_test['ulsan']
    sejong = my_test['sejong']
    f = open('./prev_csv_data/상가업소정보_202012_2.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        ctprvnNm = line[12]
        lon = line[37]
        lat = line[38]

        store = {
            "address": rdnmAdr,
            "lon": lon,
            "lat": lat
        }
        print(store)
        if ctprvnNm == "대구광역시":
            daegu_id = daegu.insert_one(store).inserted_id
        elif ctprvnNm == "인천광역시":
            incheon_id = incheon.insert_one(store).inserted_id
        elif ctprvnNm == "광주광역시":
            gwangju_id = gwangju.insert_one(store).inserted_id
        elif ctprvnNm == "대전광역시":
            daejeon_id = daejeon.insert_one(store).inserted_id
        elif ctprvnNm == "울산광역시":
            ulsan_id = ulsan.insert_one(store).inserted_id
        elif ctprvnNm == "세종특별자치시":
            sejong_id = sejong.insert_one(store).inserted_id


def third():
    gyeonggi = my_test['gyeonggi']
    gwangwon = my_test['gwangwon']
    chungbuk = my_test['chungbuk']

    f = open('./prev_csv_data/상가업소정보_202012_3.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        ctprvnNm = line[12]
        lon = line[37]
        lat = line[38]

        store = {
            "address": rdnmAdr,
            "lon": lon,
            "lat": lat
        }
        print(store)
        if ctprvnNm == "경기도":
            gyeonggi_id = gyeonggi.insert_one(store).inserted_id
        elif ctprvnNm == "강원도":
            gwangwon_id = gwangwon.insert_one(store).inserted_id
        elif ctprvnNm == "충청북도":
            chungbuk_id = chungbuk.insert_one(store).inserted_id


def four():
    chungnam = my_test['chungnam']
    jeonbuk = my_test['jeonbuk']
    jeonnam = my_test['jeonnam']
    gyeongbuk = my_test['gyeongbuk']
    gyeongnam = my_test['gyeongnam']
    jeju = my_test['jeju']
    f = open('./prev_csv_data/상가업소정보_202012_4.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    current_count = 0
    for line in rdr:
        current_count += 1
        print(current_count)
        rdnmAdr = line[31]
        ctprvnNm = line[12]
        lon = line[37]
        lat = line[38]

        store = {
            "address": rdnmAdr,
            "lon": lon,
            "lat": lat
        }
        print(store)
        if ctprvnNm == "충청남도":
            daegu_id = chungnam.insert_one(store).inserted_id
        elif ctprvnNm == "전라북도":
            incheon_id = jeonbuk.insert_one(store).inserted_id
        elif ctprvnNm == "전라남도":
            gwangju_id = jeonnam.insert_one(store).inserted_id
        elif ctprvnNm == "경상북도":
            daejeon_id = gyeongbuk.insert_one(store).inserted_id
        elif ctprvnNm == "경상남도":
            ulsan_id = gyeongnam.insert_one(store).inserted_id
        elif ctprvnNm == "제주특별자치도":
            sejong_id = jeju.insert_one(store).inserted_id


if __name__ == "__main__":
    p1 = Process(target=second)
    p2 = Process(target=third)
    p3 = Process(target=four)
    p4 = Process(target=first)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()