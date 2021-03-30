import csv
import geocoder
import time

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

localSameAddress = client['localSameAddress']
current_three_step = client['my_test']


def write_csv():
    same_address = localSameAddress['same_address']
    f = open("address.csv", 'a', newline='')
    wr = csv.writer(f)

    for addr in same_address.find({"lon": {"$exists": False}}):
        split1 = addr['address'].split(',')[0]
        split2 = split1.split("(")[0]
        wr.writerow([split2])
    f.close()


def convert_place():
    busan = current_three_step['busan']
    chungbuk = current_three_step['chungbuk']
    chungnam = current_three_step['chungnam']
    daegu = current_three_step['daegu']
    daejeon = current_three_step['daejeon']
    gangwon = current_three_step['gwangwon']
    gwangju = current_three_step['gwangju']
    gyeonggi = current_three_step['gyeonggi']
    gyeongbuk = current_three_step['gyeongbuk']
    gyeongnam = current_three_step['gyeongnam']
    incheon = current_three_step['incheon']
    jeju = current_three_step['jeju']
    jeonbuk = current_three_step['jeonbuk']
    jeonnam = current_three_step['jeonnam']
    sejong = current_three_step['sejong']
    seoul = current_three_step['seoul']
    ulsan = current_three_step['ulsan']

    # 데이터 가져오기
    rowCount = 1
    f = open("address.csv", 'r')
    rdr = csv.reader(f)

    lines = []
    for line in rdr:
        busan_data = None
        chungbuk_data = None
        chungnam_data = None
        daegu_data = None
        daejeon_data = None
        gangwon_data = None
        gwangju_data = None
        gyeonggi_data = None
        gyeongbuk_data = None
        gyeongnam_data = None
        incheon_data = None
        jeju_data = None
        jeonbuk_data = None
        jeonnam_data = None
        sejong_data = None
        seoul_data = None
        ulsan_data = None

        print(line[0])
        current_list = []
        if line[0].split(" ")[0] == "부산광역시":
            busan_data = busan.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "충청북도":
            chungbuk_data = chungbuk.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "충청남도":
            chungnam_data = chungnam.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "대구광역시":
            daegu_data = daegu.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "대전광역시":
            daejeon_data = daejeon.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "강원도":
            gangwon_data = gangwon.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "광주광역시":
            gwangju_data = gwangju.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "경기도":
            gyeonggi_data = gyeonggi.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "경상북도":
            gyeongbuk_data = gyeongbuk.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "경상남도":
            gyeongnam_data = gyeongnam.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "인천광역시":
            incheon_data = incheon.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "제주특별자치도":
            jeju_data = jeju.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "전라북도":
            jeonbuk_data = jeonbuk.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "전라남도":
            jeonnam_data = jeonnam.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "세종특별자치시":
            sejong_data = sejong.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "서울특별시":
            seoul_data = seoul.find_one({"rdnmAdr": line[0]})
        if line[0].split(" ")[0] == "울산광역시":
            ulsan_data = ulsan.find_one({"rdnmAdr": line[0]})

        if busan_data:
            current_list.append(line[0])
            current_list.append(busan_data['lon'])
            current_list.append(busan_data['lat'])
            print(current_list)
        elif chungbuk_data:
            current_list.append(line[0])
            current_list.append(chungbuk_data['lon'])
            current_list.append(chungbuk_data['lat'])
            print(current_list)
        elif chungnam_data:
            current_list.append(line[0])
            current_list.append(chungnam_data['lon'])
            current_list.append(chungnam_data['lat'])
            print(current_list)
        elif daegu_data:
            current_list.append(line[0])
            current_list.append(daegu_data['lon'])
            current_list.append(daegu_data['lat'])
            print(current_list)
        elif daejeon_data:
            current_list.append(line[0])
            current_list.append(daejeon_data['lon'])
            current_list.append(daejeon_data['lat'])
            print(current_list)
        elif gangwon_data:
            current_list.append(line[0])
            current_list.append(gangwon_data['lon'])
            current_list.append(gangwon_data['lat'])
            print(current_list)
        elif gwangju_data:
            current_list.append(line[0])
            current_list.append(gwangju_data['lon'])
            current_list.append(gwangju_data['lat'])
            print(current_list)
        elif gyeonggi_data:
            current_list.append(line[0])
            current_list.append(gyeonggi_data['lon'])
            current_list.append(gyeonggi_data['lat'])
            print(current_list)
        elif gyeongbuk_data:
            current_list.append(line[0])
            current_list.append(gyeongbuk_data['lon'])
            current_list.append(gyeongbuk_data['lat'])
            print(current_list)
        elif gyeongnam_data:
            current_list.append(line[0])
            current_list.append(gyeongnam_data['lon'])
            current_list.append(gyeongnam_data['lat'])
            print(current_list)
        elif incheon_data:
            current_list.append(line[0])
            current_list.append(incheon_data['lon'])
            current_list.append(incheon_data['lat'])
            print(current_list)
        elif jeju_data:
            current_list.append(line[0])
            current_list.append(jeju_data['lon'])
            current_list.append(jeju_data['lat'])
            print(current_list)
        elif jeonbuk_data:
            current_list.append(line[0])
            current_list.append(jeonbuk_data['lon'])
            current_list.append(jeonbuk_data['lat'])
            print(current_list)
        elif jeonnam_data:
            current_list.append(line[0])
            current_list.append(jeonnam_data['lon'])
            current_list.append(jeonnam_data['lat'])
            print(current_list)
        elif sejong_data:
            current_list.append(line[0])
            current_list.append(sejong_data['lon'])
            current_list.append(sejong_data['lat'])
            print(current_list)
        elif seoul_data:
            current_list.append(line[0])
            current_list.append(seoul_data['lon'])
            current_list.append(seoul_data['lat'])
            print(current_list)
        elif ulsan_data:
            current_list.append(line[0])
            current_list.append(ulsan_data['lon'])
            current_list.append(ulsan_data['lat'])
            print(current_list)

        rowCount = rowCount + 1
        print(rowCount)
        if len(current_list) != 0:
            lines.append(current_list)

    f = open("example.csv", "w", newline='')
    wr = csv.writer(f)
    wr.writerows(lines)


def update_db():
    same_address = localSameAddress['same_address']
    f = open('example.csv', 'r', encoding='cp949')
    rdr = csv.reader(f)

    cnt = 0
    for line in rdr:
        for local in same_address.find({"address": {"$regex": line[0]}}):
            same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lon": line[1]}})
            same_address.update_one({"_id": ObjectId(local['_id'])}, {"$set": {"lat": line[2]}})
            cnt += 1
            print(cnt, line, local)


# write_csv()
# convert_place()
update_db()
