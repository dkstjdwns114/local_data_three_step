from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient('localhost', 27017)

localSameAddress = client['localSameAddress']

same_address = localSameAddress['same_address_20']

nationwide_array = []
busan_array = []
chungbuk_array = []
chungnam_array = []
daegu_array = []
daejeon_array = []
gangwon_array = []
gwangju_array = []
gyeonggi_array = []
gyeongbuk_array = []
gyeongnam_array = []
incheon_array = []
jeju_array = []
jeonbuk_array = []
jeonnam_array = []
sejong_array = []
seoul_array = []
ulsan_array = []


def nationwide_top10():
    total_cnt = same_address.count_documents({})

    cnt = 0
    for location in same_address.find({}).batch_size(1):
        cnt += 1
        nationwide_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
        print(cnt, total_cnt, len(location['stores_info']))
        if location['address'].split(" ")[0] == "부산광역시":
            cnt += 1
            busan_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "충청북도":
            cnt += 1
            chungbuk_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "충청남도":
            cnt += 1
            chungnam_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "대구광역시":
            cnt += 1
            daegu_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "대전광역시":
            cnt += 1
            daejeon_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "강원도":
            cnt += 1
            gangwon_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "광주광역시":
            cnt += 1
            gwangju_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "경기도":
            cnt += 1
            gyeonggi_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "경상북도":
            cnt += 1
            gyeongbuk_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "경상남도":
            cnt += 1
            gyeongnam_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "인천광역시":
            cnt += 1
            incheon_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "제주특별자치도":
            cnt += 1
            jeju_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "전라북도":
            cnt += 1
            jeonbuk_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "전라남도":
            cnt += 1
            jeonnam_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "세종특별자치시":
            cnt += 1
            sejong_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "서울특별시":
            cnt += 1
            seoul_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))
        elif location['address'].split(" ")[0] == "울산광역시":
            cnt += 1
            ulsan_array.append({"address": location['address'], "stores_info": location['stores_info'], "count": len(location['stores_info'])})
            print(cnt, total_cnt, len(location['stores_info']))

    nationwide_sort_word = sorted(nationwide_array, key=lambda t : t["count"], reverse=True)[:10]
    busan_sort_word = sorted(busan_array, key=lambda t: t["count"], reverse=True)[:10]
    chungbuk_sort_word = sorted(chungbuk_array, key=lambda t: t["count"], reverse=True)[:10]
    chungnam_sort_word = sorted(chungnam_array, key=lambda t: t["count"], reverse=True)[:10]
    daegu_sort_word = sorted(daegu_array, key=lambda t: t["count"], reverse=True)[:10]
    daejeon_sort_word = sorted(daejeon_array, key=lambda t: t["count"], reverse=True)[:10]
    gangwon_sort_word = sorted(gangwon_array, key=lambda t: t["count"], reverse=True)[:10]
    gwangju_sort_word = sorted(gwangju_array, key=lambda t: t["count"], reverse=True)[:10]
    gyeonggi_sort_word = sorted(gyeonggi_array, key=lambda t: t["count"], reverse=True)[:10]
    gyeongbuk_sort_word = sorted(gyeongbuk_array, key=lambda t: t["count"], reverse=True)[:10]
    gyeongnam_sort_word = sorted(gyeongnam_array, key=lambda t: t["count"], reverse=True)[:10]
    incheon_sort_word = sorted(incheon_array, key=lambda t: t["count"], reverse=True)[:10]
    jeju_sort_word = sorted(jeju_array, key=lambda t: t["count"], reverse=True)[:10]
    jeonbuk_sort_word = sorted(jeonbuk_array, key=lambda t: t["count"], reverse=True)[:10]
    jeonnam_sort_word = sorted(jeonnam_array, key=lambda t: t["count"], reverse=True)[:10]
    sejong_sort_word = sorted(sejong_array, key=lambda t: t["count"], reverse=True)[:10]
    seoul_sort_word = sorted(seoul_array, key=lambda t: t["count"], reverse=True)[:10]
    ulsan_sort_word = sorted(ulsan_array, key=lambda t: t["count"], reverse=True)[:10]

    print("nationwide_sort_word", nationwide_sort_word)
    print("seoul_sort_word", busan_sort_word)
    print("chungbuk_sort_word", chungbuk_sort_word)
    print("chungnam_sort_word", chungnam_sort_word)
    print("daegu_sort_word", daegu_sort_word)
    print("daejeon_sort_word", daejeon_sort_word)
    print("gangwon_sort_word", gangwon_sort_word)
    print("gwangju_sort_word", gwangju_sort_word)
    print("gyeonggi_sort_word", gyeonggi_sort_word)
    print("gyeongbuk_sort_word", gyeongbuk_sort_word)
    print("gyeongnam_sort_word", gyeongnam_sort_word)
    print("incheon_sort_word", incheon_sort_word)
    print("jeju_sort_word", jeju_sort_word)
    print("jeonbuk_sort_word", jeonbuk_sort_word)
    print("jeonnam_sort_word", jeonnam_sort_word)
    print("sejong_sort_word", sejong_sort_word)
    print("seoul_sort_word", seoul_sort_word)
    print("ulsan_sort_word", ulsan_sort_word)

    tot_cnt = 10
    nationwide_result_cnt = 0
    for result in nationwide_sort_word:
        nationwide_result_cnt += 1
        print(nationwide_result_cnt, "/", tot_cnt, result)

    busan_array_result_cnt = 0
    for result in busan_sort_word:
        busan_array_result_cnt += 1
        print(busan_array_result_cnt, "/", tot_cnt, result)

    chungbuk_array_result_cnt = 0
    for result in chungbuk_sort_word:
        chungbuk_array_result_cnt += 1
        print(chungbuk_array_result_cnt, "/", tot_cnt, result)

    chungnam_array_result_cnt = 0
    for result in chungnam_sort_word:
        chungnam_array_result_cnt += 1
        print(chungnam_array_result_cnt, "/", tot_cnt, result)

    daegu_array_result_cnt = 0
    for result in daegu_sort_word:
        daegu_array_result_cnt += 1
        print(daegu_array_result_cnt, "/", tot_cnt, result)

    daejeon_array_result_cnt = 0
    for result in daejeon_sort_word:
        daejeon_array_result_cnt += 1
        print(daejeon_array_result_cnt, "/", tot_cnt, result)

    gangwon_array_result_cnt = 0
    for result in gangwon_sort_word:
        gangwon_array_result_cnt += 1
        print(gangwon_array_result_cnt, "/", tot_cnt, result)

    gwangju_array_result_cnt = 0
    for result in gwangju_sort_word:
        gwangju_array_result_cnt += 1
        print(gwangju_array_result_cnt, "/", tot_cnt, result)

    gyeonggi_array_result_cnt = 0
    for result in gyeonggi_sort_word:
        gyeonggi_array_result_cnt += 1
        print(gyeonggi_array_result_cnt, "/", tot_cnt, result)

    gyeongbuk_array_result_cnt = 0
    for result in gyeongbuk_sort_word:
        gyeongbuk_array_result_cnt += 1
        print(gyeongbuk_array_result_cnt, "/", tot_cnt, result)

    gyeongnam_array_result_cnt = 0
    for result in gyeongnam_sort_word:
        gyeongnam_array_result_cnt += 1
        print(gyeongnam_array_result_cnt, "/", tot_cnt, result)

    incheon_array_result_cnt = 0
    for result in incheon_sort_word:
        incheon_array_result_cnt += 1
        print(incheon_array_result_cnt, "/", tot_cnt, result)

    jeju_array_result_cnt = 0
    for result in jeju_sort_word:
        jeju_array_result_cnt += 1
        print(jeju_array_result_cnt, "/", tot_cnt, result)

    jeonbuk_array_result_cnt = 0
    for result in jeonbuk_sort_word:
        jeonbuk_array_result_cnt += 1
        print(jeonbuk_array_result_cnt, "/", tot_cnt, result)

    jeonnam_array_result_cnt = 0
    for result in jeonnam_sort_word:
        jeonnam_array_result_cnt += 1
        print(jeonnam_array_result_cnt, "/", tot_cnt, result)

    sejong_array_result_cnt = 0
    for result in sejong_sort_word:
        sejong_array_result_cnt += 1
        print(sejong_array_result_cnt, "/", tot_cnt, result)

    seoul_array_result_cnt = 0
    for result in seoul_sort_word:
        seoul_array_result_cnt += 1
        print(seoul_array_result_cnt, "/", tot_cnt, result)

    ulsan_array_result_cnt = 0
    for result in ulsan_sort_word:
        ulsan_array_result_cnt += 1
        print(ulsan_array_result_cnt, "/", tot_cnt, result)

    info = {
        "title": "2020 Same address location data",
        "nationwide": nationwide_sort_word,
        "busan": busan_sort_word,
        "chungbuk": chungbuk_sort_word,
        "chungnam": chungnam_sort_word,
        "daegu": daegu_sort_word,
        "daejeon": daejeon_sort_word,
        "gangwon": gangwon_sort_word,
        "gwangju": gwangju_sort_word,
        "gyeonggi": gyeonggi_sort_word,
        "gyeongbuk": gyeongbuk_sort_word,
        "gyeongnam": gyeongnam_sort_word,
        "incheon": incheon_sort_word,
        "jeju": jeju_sort_word,
        "jeonbuk": jeonbuk_sort_word,
        "jeonnam": jeonnam_sort_word,
        "sejong": sejong_sort_word,
        "seoul": seoul_sort_word,
        "ulsan": ulsan_sort_word
    }

    local_main_api = db['local_data_api']

    print("info", info)

    info_id = local_main_api.insert_one(info).inserted_id
    print(info_id)


nationwide_top10()
