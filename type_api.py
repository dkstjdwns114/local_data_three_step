from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']
theoremLocalDataLocationClose19 = client['theoremLocalDataLocationClose19']
theoremLocalDataLocationClose20 = client['theoremLocalDataLocationClose20']
theoremLocalDataLocationOpen19 = client['theoremLocalDataLocationOpen19']
theoremLocalDataLocationOpen20 = client['theoremLocalDataLocationOpen20']


def data():
    # 19년 업종별 close
    animal_close_19 = theoremLocalDataClose19['animal']
    culture_close_19 = theoremLocalDataClose19['culture']
    environment_close_19 = theoremLocalDataClose19['environment']
    food_close_19 = theoremLocalDataClose19['food']
    health_close_19 = theoremLocalDataClose19['health']
    life_close_19 = theoremLocalDataClose19['life']
    other_close_19 = theoremLocalDataClose19['other']

    animal_close_19_cnt = animal_close_19.count_documents({})
    culture_close_19_cnt = culture_close_19.count_documents({})
    environment_close_19_cnt = environment_close_19.count_documents({})
    food_close_19_cnt = food_close_19.count_documents({})
    health_close_19_cnt = health_close_19.count_documents({})
    life_close_19_cnt = life_close_19.count_documents({})
    other_close_19_cnt = other_close_19.count_documents({})

    print("--- 2019 업종별 Close ---")
    print("animal_close_19_cnt", animal_close_19_cnt)
    print("culture_close_19_cnt", culture_close_19_cnt)
    print("environment_close_19_cnt", environment_close_19_cnt)
    print("food_close_19_cnt", food_close_19_cnt)
    print("health_close_19_cnt", health_close_19_cnt)
    print("life_close_19_cnt", life_close_19_cnt)
    print("other_close_19_cnt", other_close_19_cnt)

    # -------------------------------------------------

    # 19년 업종별 open
    animal_open_19 = theoremLocalDataOpen19['animal']
    culture_open_19 = theoremLocalDataOpen19['culture']
    environment_open_19 = theoremLocalDataOpen19['environment']
    food_open_19 = theoremLocalDataOpen19['food']
    health_open_19 = theoremLocalDataOpen19['health']
    life_open_19 = theoremLocalDataOpen19['life']
    other_open_19 = theoremLocalDataOpen19['other']

    animal_open_19_cnt = animal_open_19.count_documents({})
    culture_open_19_cnt = culture_open_19.count_documents({})
    environment_open_19_cnt = environment_open_19.count_documents({})
    food_open_19_cnt = food_open_19.count_documents({})
    health_open_19_cnt = health_open_19.count_documents({})
    life_open_19_cnt = life_open_19.count_documents({})
    other_open_19_cnt = other_open_19.count_documents({})

    print("--- 2019 업종별 Open ---")
    print("animal_open_19_cnt", animal_open_19_cnt)
    print("culture_open_19_cnt", culture_open_19_cnt)
    print("environment_open_19_cnt", environment_open_19_cnt)
    print("food_open_19_cnt", food_open_19_cnt)
    print("health_open_19_cnt", health_open_19_cnt)
    print("life_open_19_cnt", life_open_19_cnt)
    print("other_open_19_cnt", other_open_19_cnt)

    # -------------------------------------------------

    # 20년 업종별 close
    animal_close_20 = theoremLocalDataClose20['animal']
    culture_close_20 = theoremLocalDataClose20['culture']
    environment_close_20 = theoremLocalDataClose20['environment']
    food_close_20 = theoremLocalDataClose20['food']
    health_close_20 = theoremLocalDataClose20['health']
    life_close_20 = theoremLocalDataClose20['life']
    other_close_20 = theoremLocalDataClose20['other']

    animal_close_20_cnt = animal_close_20.count_documents({})
    culture_close_20_cnt = culture_close_20.count_documents({})
    environment_close_20_cnt = environment_close_20.count_documents({})
    food_close_20_cnt = food_close_20.count_documents({})
    health_close_20_cnt = health_close_20.count_documents({})
    life_close_20_cnt = life_close_20.count_documents({})
    other_close_20_cnt = other_close_20.count_documents({})

    print("--- 2020 업종별 Close ---")
    print("animal_close_20_cnt", animal_close_20_cnt)
    print("culture_close_20_cnt", culture_close_20_cnt)
    print("environment_close_20_cnt", environment_close_20_cnt)
    print("food_close_20_cnt", food_close_20_cnt)
    print("health_close_20_cnt", health_close_20_cnt)
    print("life_close_20_cnt", life_close_20_cnt)
    print("other_close_20_cnt", other_close_20_cnt)

    # -------------------------------------------------

    # 20년 업종별 open
    animal_open_20 = theoremLocalDataOpen20['animal']
    culture_open_20 = theoremLocalDataOpen20['culture']
    environment_open_20 = theoremLocalDataOpen20['environment']
    food_open_20 = theoremLocalDataOpen20['food']
    health_open_20 = theoremLocalDataOpen20['health']
    life_open_20 = theoremLocalDataOpen20['life']
    other_open_20 = theoremLocalDataOpen20['other']

    animal_open_20_cnt = animal_open_20.count_documents({})
    culture_open_20_cnt = culture_open_20.count_documents({})
    environment_open_20_cnt = environment_open_20.count_documents({})
    food_open_20_cnt = food_open_20.count_documents({})
    health_open_20_cnt = health_open_20.count_documents({})
    life_open_20_cnt = life_open_20.count_documents({})
    other_open_20_cnt = other_open_20.count_documents({})

    print("--- 2020 업종별 Open ---")
    print("animal_open_20_cnt", animal_open_20_cnt)
    print("culture_open_20_cnt", culture_open_20_cnt)
    print("environment_open_20_cnt", environment_open_20_cnt)
    print("food_open_20_cnt", food_open_20_cnt)
    print("health_open_20_cnt", health_open_20_cnt)
    print("life_open_20_cnt", life_open_20_cnt)
    print("other_open_20_cnt", other_open_20_cnt)

    # -------------------------------------------------

    # 19년 시도별 close
    busan_close_19 = theoremLocalDataLocationClose19['busan']
    chungbuk_close_19 = theoremLocalDataLocationClose19['chungbuk']
    chungnam_close_19 = theoremLocalDataLocationClose19['chungnam']
    daegu_close_19 = theoremLocalDataLocationClose19['daegu']
    daejeon_close_19 = theoremLocalDataLocationClose19['daejeon']
    gangwon_close_19 = theoremLocalDataLocationClose19['gangwon']
    gwangju_close_19 = theoremLocalDataLocationClose19['gwangju']
    gyeonggi_close_19 = theoremLocalDataLocationClose19['gyeonggi']
    gyeongbuk_close_19 = theoremLocalDataLocationClose19['gyeongbuk']
    gyeongnam_close_19 = theoremLocalDataLocationClose19['gyeongnam']
    incheon_close_19 = theoremLocalDataLocationClose19['incheon']
    jeju_close_19 = theoremLocalDataLocationClose19['jeju']
    jeonbuk_close_19 = theoremLocalDataLocationClose19['jeonbuk']
    jeonnam_close_19 = theoremLocalDataLocationClose19['jeonnam']
    sejong_close_19 = theoremLocalDataLocationClose19['sejong']
    seoul_close_19 = theoremLocalDataLocationClose19['seoul']
    ulsan_close_19 = theoremLocalDataLocationClose19['ulsan']

    busan_close_19_cnt = busan_close_19.count_documents({})
    chungbuk_close_19_cnt = chungbuk_close_19.count_documents({})
    chungnam_close_19_cnt = chungnam_close_19.count_documents({})
    daegu_close_19_cnt = daegu_close_19.count_documents({})
    daejeon_close_19_cnt = daejeon_close_19.count_documents({})
    gangwon_close_19_cnt = gangwon_close_19.count_documents({})
    gwangju_close_19_cnt = gwangju_close_19.count_documents({})
    gyeonggi_close_19_cnt = gyeonggi_close_19.count_documents({})
    gyeongbuk_close_19_cnt = gyeongbuk_close_19.count_documents({})
    gyeongnam_close_19_cnt = gyeongnam_close_19.count_documents({})
    incheon_close_19_cnt = incheon_close_19.count_documents({})
    jeju_close_19_cnt = jeju_close_19.count_documents({})
    jeonbuk_close_19_cnt = jeonbuk_close_19.count_documents({})
    jeonnam_close_19_cnt = jeonnam_close_19.count_documents({})
    sejong_close_19_cnt = sejong_close_19.count_documents({})
    seoul_close_19_cnt = seoul_close_19.count_documents({})
    ulsan_close_19_cnt = ulsan_close_19.count_documents({})

    print("--- 2019 시도별 Open ---")
    print("부산", busan_close_19_cnt)
    print("충북", chungbuk_close_19_cnt)
    print("충남", chungnam_close_19_cnt)
    print("대구", daegu_close_19_cnt)
    print("대전", daejeon_close_19_cnt)
    print("강원", gangwon_close_19_cnt)
    print("광주", gwangju_close_19_cnt)
    print("경기", gyeonggi_close_19_cnt)
    print("경북", gyeongbuk_close_19_cnt)
    print("경남", gyeongnam_close_19_cnt)
    print("인천", incheon_close_19_cnt)
    print("제주", jeju_close_19_cnt)
    print("전북", jeonbuk_close_19_cnt)
    print("전남", jeonnam_close_19_cnt)
    print("세종", sejong_close_19_cnt)
    print("서울", seoul_close_19_cnt)
    print("울산", ulsan_close_19_cnt)

    # -------------------------------------------------

    # 19년 시도별 open
    busan_open_19 = theoremLocalDataLocationOpen19['busan']
    chungbuk_open_19 = theoremLocalDataLocationOpen19['chungbuk']
    chungnam_open_19 = theoremLocalDataLocationOpen19['chungnam']
    daegu_open_19 = theoremLocalDataLocationOpen19['daegu']
    daejeon_open_19 = theoremLocalDataLocationOpen19['daejeon']
    gangwon_open_19 = theoremLocalDataLocationOpen19['gangwon']
    gwangju_open_19 = theoremLocalDataLocationOpen19['gwangju']
    gyeonggi_open_19 = theoremLocalDataLocationOpen19['gyeonggi']
    gyeongbuk_open_19 = theoremLocalDataLocationOpen19['gyeongbuk']
    gyeongnam_open_19 = theoremLocalDataLocationOpen19['gyeongnam']
    incheon_open_19 = theoremLocalDataLocationOpen19['incheon']
    jeju_open_19 = theoremLocalDataLocationOpen19['jeju']
    jeonbuk_open_19 = theoremLocalDataLocationOpen19['jeonbuk']
    jeonnam_open_19 = theoremLocalDataLocationOpen19['jeonnam']
    sejong_open_19 = theoremLocalDataLocationOpen19['sejong']
    seoul_open_19 = theoremLocalDataLocationOpen19['seoul']
    ulsan_open_19 = theoremLocalDataLocationOpen19['ulsan']

    busan_open_19_cnt = busan_open_19.count_documents({})
    chungbuk_open_19_cnt = chungbuk_open_19.count_documents({})
    chungnam_open_19_cnt = chungnam_open_19.count_documents({})
    daegu_open_19_cnt = daegu_open_19.count_documents({})
    daejeon_open_19_cnt = daejeon_open_19.count_documents({})
    gangwon_open_19_cnt = gangwon_open_19.count_documents({})
    gwangju_open_19_cnt = gwangju_open_19.count_documents({})
    gyeonggi_open_19_cnt = gyeonggi_open_19.count_documents({})
    gyeongbuk_open_19_cnt = gyeongbuk_open_19.count_documents({})
    gyeongnam_open_19_cnt = gyeongnam_open_19.count_documents({})
    incheon_open_19_cnt = incheon_open_19.count_documents({})
    jeju_open_19_cnt = jeju_open_19.count_documents({})
    jeonbuk_open_19_cnt = jeonbuk_open_19.count_documents({})
    jeonnam_open_19_cnt = jeonnam_open_19.count_documents({})
    sejong_open_19_cnt = sejong_open_19.count_documents({})
    seoul_open_19_cnt = seoul_open_19.count_documents({})
    ulsan_open_19_cnt = ulsan_open_19.count_documents({})

    print("--- 2019 시도별 Open ---")
    print("부산", busan_open_19_cnt)
    print("충북", chungbuk_open_19_cnt)
    print("충남", chungnam_open_19_cnt)
    print("대구", daegu_open_19_cnt)
    print("대전", daejeon_open_19_cnt)
    print("강원", gangwon_open_19_cnt)
    print("광주", gwangju_open_19_cnt)
    print("경기", gyeonggi_open_19_cnt)
    print("경북", gyeongbuk_open_19_cnt)
    print("경남", gyeongnam_open_19_cnt)
    print("인천", incheon_open_19_cnt)
    print("제주", jeju_open_19_cnt)
    print("전북", jeonbuk_open_19_cnt)
    print("전남", jeonnam_open_19_cnt)
    print("세종", sejong_open_19_cnt)
    print("서울", seoul_open_19_cnt)
    print("울산", ulsan_open_19_cnt)

    # -------------------------------------------------

    # 20년 시도별 close
    busan_close_20 = theoremLocalDataLocationClose20['busan']
    chungbuk_close_20 = theoremLocalDataLocationClose20['chungbuk']
    chungnam_close_20 = theoremLocalDataLocationClose20['chungnam']
    daegu_close_20 = theoremLocalDataLocationClose20['daegu']
    daejeon_close_20 = theoremLocalDataLocationClose20['daejeon']
    gangwon_close_20 = theoremLocalDataLocationClose20['gangwon']
    gwangju_close_20 = theoremLocalDataLocationClose20['gwangju']
    gyeonggi_close_20 = theoremLocalDataLocationClose20['gyeonggi']
    gyeongbuk_close_20 = theoremLocalDataLocationClose20['gyeongbuk']
    gyeongnam_close_20 = theoremLocalDataLocationClose20['gyeongnam']
    incheon_close_20 = theoremLocalDataLocationClose20['incheon']
    jeju_close_20 = theoremLocalDataLocationClose20['jeju']
    jeonbuk_close_20 = theoremLocalDataLocationClose20['jeonbuk']
    jeonnam_close_20 = theoremLocalDataLocationClose20['jeonnam']
    sejong_close_20 = theoremLocalDataLocationClose20['sejong']
    seoul_close_20 = theoremLocalDataLocationClose20['seoul']
    ulsan_close_20 = theoremLocalDataLocationClose20['ulsan']

    busan_close_20_cnt = busan_close_20.count_documents({})
    chungbuk_close_20_cnt = chungbuk_close_20.count_documents({})
    chungnam_close_20_cnt = chungnam_close_20.count_documents({})
    daegu_close_20_cnt = daegu_close_20.count_documents({})
    daejeon_close_20_cnt = daejeon_close_20.count_documents({})
    gangwon_close_20_cnt = gangwon_close_20.count_documents({})
    gwangju_close_20_cnt = gwangju_close_20.count_documents({})
    gyeonggi_close_20_cnt = gyeonggi_close_20.count_documents({})
    gyeongbuk_close_20_cnt = gyeongbuk_close_20.count_documents({})
    gyeongnam_close_20_cnt = gyeongnam_close_20.count_documents({})
    incheon_close_20_cnt = incheon_close_20.count_documents({})
    jeju_close_20_cnt = jeju_close_20.count_documents({})
    jeonbuk_close_20_cnt = jeonbuk_close_20.count_documents({})
    jeonnam_close_20_cnt = jeonnam_close_20.count_documents({})
    sejong_close_20_cnt = sejong_close_20.count_documents({})
    seoul_close_20_cnt = seoul_close_20.count_documents({})
    ulsan_close_20_cnt = ulsan_close_20.count_documents({})

    print("--- 2020 시도별 Open ---")
    print("부산", busan_close_20_cnt)
    print("충북", chungbuk_close_20_cnt)
    print("충남", chungnam_close_20_cnt)
    print("대구", daegu_close_20_cnt)
    print("대전", daejeon_close_20_cnt)
    print("강원", gangwon_close_20_cnt)
    print("광주", gwangju_close_20_cnt)
    print("경기", gyeonggi_close_20_cnt)
    print("경북", gyeongbuk_close_20_cnt)
    print("경남", gyeongnam_close_20_cnt)
    print("인천", incheon_close_20_cnt)
    print("제주", jeju_close_20_cnt)
    print("전북", jeonbuk_close_20_cnt)
    print("전남", jeonnam_close_20_cnt)
    print("세종", sejong_close_20_cnt)
    print("서울", seoul_close_20_cnt)
    print("울산", ulsan_close_20_cnt)

    # -------------------------------------------------

    # 20년 시도별 open
    busan_open_20 = theoremLocalDataLocationOpen20['busan']
    chungbuk_open_20 = theoremLocalDataLocationOpen20['chungbuk']
    chungnam_open_20 = theoremLocalDataLocationOpen20['chungnam']
    daegu_open_20 = theoremLocalDataLocationOpen20['daegu']
    daejeon_open_20 = theoremLocalDataLocationOpen20['daejeon']
    gangwon_open_20 = theoremLocalDataLocationOpen20['gangwon']
    gwangju_open_20 = theoremLocalDataLocationOpen20['gwangju']
    gyeonggi_open_20 = theoremLocalDataLocationOpen20['gyeonggi']
    gyeongbuk_open_20 = theoremLocalDataLocationOpen20['gyeongbuk']
    gyeongnam_open_20 = theoremLocalDataLocationOpen20['gyeongnam']
    incheon_open_20 = theoremLocalDataLocationOpen20['incheon']
    jeju_open_20 = theoremLocalDataLocationOpen20['jeju']
    jeonbuk_open_20 = theoremLocalDataLocationOpen20['jeonbuk']
    jeonnam_open_20 = theoremLocalDataLocationOpen20['jeonnam']
    sejong_open_20 = theoremLocalDataLocationOpen20['sejong']
    seoul_open_20 = theoremLocalDataLocationOpen20['seoul']
    ulsan_open_20 = theoremLocalDataLocationOpen20['ulsan']

    busan_open_20_cnt = busan_open_20.count_documents({})
    chungbuk_open_20_cnt = chungbuk_open_20.count_documents({})
    chungnam_open_20_cnt = chungnam_open_20.count_documents({})
    daegu_open_20_cnt = daegu_open_20.count_documents({})
    daejeon_open_20_cnt = daejeon_open_20.count_documents({})
    gangwon_open_20_cnt = gangwon_open_20.count_documents({})
    gwangju_open_20_cnt = gwangju_open_20.count_documents({})
    gyeonggi_open_20_cnt = gyeonggi_open_20.count_documents({})
    gyeongbuk_open_20_cnt = gyeongbuk_open_20.count_documents({})
    gyeongnam_open_20_cnt = gyeongnam_open_20.count_documents({})
    incheon_open_20_cnt = incheon_open_20.count_documents({})
    jeju_open_20_cnt = jeju_open_20.count_documents({})
    jeonbuk_open_20_cnt = jeonbuk_open_20.count_documents({})
    jeonnam_open_20_cnt = jeonnam_open_20.count_documents({})
    sejong_open_20_cnt = sejong_open_20.count_documents({})
    seoul_open_20_cnt = seoul_open_20.count_documents({})
    ulsan_open_20_cnt = ulsan_open_20.count_documents({})

    print("--- 2020 시도별 Open ---")
    print("부산", busan_open_20_cnt)
    print("충북", chungbuk_open_20_cnt)
    print("충남", chungnam_open_20_cnt)
    print("대구", daegu_open_20_cnt)
    print("대전", daejeon_open_20_cnt)
    print("강원", gangwon_open_20_cnt)
    print("광주", gwangju_open_20_cnt)
    print("경기", gyeonggi_open_20_cnt)
    print("경북", gyeongbuk_open_20_cnt)
    print("경남", gyeongnam_open_20_cnt)
    print("인천", incheon_open_20_cnt)
    print("제주", jeju_open_20_cnt)
    print("전북", jeonbuk_open_20_cnt)
    print("전남", jeonnam_open_20_cnt)
    print("세종", sejong_open_20_cnt)
    print("서울", seoul_open_20_cnt)
    print("울산", ulsan_open_20_cnt)

    info = {
        "title": "Main Data",
        "type_close_19": [
            {
                "type": "동물",
                "count": animal_close_19_cnt
            },
            {
                "type": "문화",
                "count": culture_close_19_cnt
            },
            {
                "type": "자연환경",
                "count": environment_close_19_cnt
            },
            {
                "type": "식품",
                "count": food_close_19_cnt
            },
            {
                "type": "건강",
                "count": health_close_19_cnt
            },
            {
                "type": "생활",
                "count": life_close_19_cnt
            },
            {
                "type": "기타",
                "count": other_close_19_cnt
            }
        ],
        "type_open_19": [
            {
                "type": "동물",
                "count": animal_open_19_cnt
            },
            {
                "type": "문화",
                "count": culture_open_19_cnt
            },
            {
                "type": "자연환경",
                "count": environment_open_19_cnt
            },
            {
                "type": "식품",
                "count": food_open_19_cnt
            },
            {
                "type": "건강",
                "count": health_open_19_cnt
            },
            {
                "type": "생활",
                "count": life_open_19_cnt
            },
            {
                "type": "기타",
                "count": other_open_19_cnt
            }
        ],
        "type_close_20": [
            {
                "type": "동물",
                "count": animal_close_20_cnt
            },
            {
                "type": "문화",
                "count": culture_close_20_cnt
            },
            {
                "type": "자연환경",
                "count": environment_close_20_cnt
            },
            {
                "type": "식품",
                "count": food_close_20_cnt
            },
            {
                "type": "건강",
                "count": health_close_20_cnt
            },
            {
                "type": "생활",
                "count": life_close_20_cnt
            },
            {
                "type": "기타",
                "count": other_close_20_cnt
            }
        ],
        "type_open_20": [
            {
                "type": "동물",
                "count": animal_open_20_cnt
            },
            {
                "type": "문화",
                "count": culture_open_20_cnt
            },
            {
                "type": "자연환경",
                "count": environment_open_20_cnt
            },
            {
                "type": "식품",
                "count": food_open_20_cnt
            },
            {
                "type": "건강",
                "count": health_open_20_cnt
            },
            {
                "type": "생활",
                "count": life_open_20_cnt
            },
            {
                "type": "기타",
                "count": other_open_20_cnt
            }
        ],
        "city_close_19": [
            {
                "city": "busan",
                "count": busan_close_19_cnt
            },
            {
                "city": "chungbuk",
                "count": chungbuk_close_19_cnt
            },
            {
                "city": "chungnam",
                "count": chungnam_close_19_cnt
            },
            {
                "city": "daegu",
                "count": daegu_close_19_cnt
            },
            {
                "city": "daejeon",
                "count": daejeon_close_19_cnt
            },
            {
                "city": "gangwon",
                "count": gangwon_close_19_cnt
            },
            {
                "city": "gwangju",
                "count": gwangju_close_19_cnt
            },
            {
                "city": "gyeonggi",
                "count": gyeonggi_close_19_cnt
            },
            {
                "city": "gyeongbuk",
                "count": gyeongbuk_close_19_cnt
            },
            {
                "city": "gyeongnam",
                "count": gyeongnam_close_19_cnt
            },
            {
                "city": "incheon",
                "count": incheon_close_19_cnt
            },
            {
                "city": "jeju",
                "count": jeju_close_19_cnt
            },
            {
                "city": "jeonbuk",
                "count": jeonbuk_close_19_cnt
            },
            {
                "city": "jeonnam",
                "count": jeonnam_close_19_cnt
            },
            {
                "city": "sejong",
                "count": sejong_close_19_cnt
            },
            {
                "city": "seoul",
                "count": seoul_close_19_cnt
            },
            {
                "city": "ulsan",
                "count": ulsan_close_19_cnt
            }
        ],
        "city_open_19": [
            {
                "city": "busan",
                "count": busan_open_19_cnt
            },
            {
                "city": "chungbuk",
                "count": chungbuk_open_19_cnt
            },
            {
                "city": "chungnam",
                "count": chungnam_open_19_cnt
            },
            {
                "city": "daegu",
                "count": daegu_open_19_cnt
            },
            {
                "city": "daejeon",
                "count": daejeon_open_19_cnt
            },
            {
                "city": "gangwon",
                "count": gangwon_open_19_cnt
            },
            {
                "city": "gwangju",
                "count": gwangju_open_19_cnt
            },
            {
                "city": "gyeonggi",
                "count": gyeonggi_open_19_cnt
            },
            {
                "city": "gyeongbuk",
                "count": gyeongbuk_open_19_cnt
            },
            {
                "city": "gyeongnam",
                "count": gyeongnam_open_19_cnt
            },
            {
                "city": "incheon",
                "count": incheon_open_19_cnt
            },
            {
                "city": "jeju",
                "count": jeju_open_19_cnt
            },
            {
                "city": "jeonbuk",
                "count": jeonbuk_open_19_cnt
            },
            {
                "city": "jeonnam",
                "count": jeonnam_open_19_cnt
            },
            {
                "city": "sejong",
                "count": sejong_open_19_cnt
            },
            {
                "city": "seoul",
                "count": seoul_open_19_cnt
            },
            {
                "city": "ulsan",
                "count": ulsan_open_19_cnt
            }
        ],
        "city_close_20": [
            {
                "city": "busan",
                "count": busan_close_20_cnt
            },
            {
                "city": "chungbuk",
                "count": chungbuk_close_20_cnt
            },
            {
                "city": "chungnam",
                "count": chungnam_close_20_cnt
            },
            {
                "city": "daegu",
                "count": daegu_close_20_cnt
            },
            {
                "city": "daejeon",
                "count": daejeon_close_20_cnt
            },
            {
                "city": "gangwon",
                "count": gangwon_close_20_cnt
            },
            {
                "city": "gwangju",
                "count": gwangju_close_20_cnt
            },
            {
                "city": "gyeonggi",
                "count": gyeonggi_close_20_cnt
            },
            {
                "city": "gyeongbuk",
                "count": gyeongbuk_close_20_cnt
            },
            {
                "city": "gyeongnam",
                "count": gyeongnam_close_20_cnt
            },
            {
                "city": "incheon",
                "count": incheon_close_20_cnt
            },
            {
                "city": "jeju",
                "count": jeju_close_20_cnt
            },
            {
                "city": "jeonbuk",
                "count": jeonbuk_close_20_cnt
            },
            {
                "city": "jeonnam",
                "count": jeonnam_close_20_cnt
            },
            {
                "city": "sejong",
                "count": sejong_close_20_cnt
            },
            {
                "city": "seoul",
                "count": seoul_close_20_cnt
            },
            {
                "city": "ulsan",
                "count": ulsan_close_20_cnt
            }
        ],
        "city_open_20": [
            {
                "city": "busan",
                "count": busan_open_20_cnt
            },
            {
                "city": "chungbuk",
                "count": chungbuk_open_20_cnt
            },
            {
                "city": "chungnam",
                "count": chungnam_open_20_cnt
            },
            {
                "city": "daegu",
                "count": daegu_open_20_cnt
            },
            {
                "city": "daejeon",
                "count": daejeon_open_20_cnt
            },
            {
                "city": "gangwon",
                "count": gangwon_open_20_cnt
            },
            {
                "city": "gwangju",
                "count": gwangju_open_20_cnt
            },
            {
                "city": "gyeonggi",
                "count": gyeonggi_open_20_cnt
            },
            {
                "city": "gyeongbuk",
                "count": gyeongbuk_open_20_cnt
            },
            {
                "city": "gyeongnam",
                "count": gyeongnam_open_20_cnt
            },
            {
                "city": "incheon",
                "count": incheon_open_20_cnt
            },
            {
                "city": "jeju",
                "count": jeju_open_20_cnt
            },
            {
                "city": "jeonbuk",
                "count": jeonbuk_open_20_cnt
            },
            {
                "city": "jeonnam",
                "count": jeonnam_open_20_cnt
            },
            {
                "city": "sejong",
                "count": sejong_open_20_cnt
            },
            {
                "city": "seoul",
                "count": seoul_open_20_cnt
            },
            {
                "city": "ulsan",
                "count": ulsan_open_20_cnt
            }
        ]
    }

    local_main_api = db['local_data_api']

    print("info", info)

    info_id = local_main_api.insert_one(info).inserted_id
    print(info_id)


# data()
