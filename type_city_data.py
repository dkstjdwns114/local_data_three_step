from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']


def data():
    # 19년 업종별 폐업
    animal_close_19 = theoremLocalDataClose19['animal']
    culture_close_19 = theoremLocalDataClose19['culture']
    environment_close_19 = theoremLocalDataClose19['environment']
    food_close_19 = theoremLocalDataClose19['food']
    health_close_19 = theoremLocalDataClose19['health']
    life_close_19 = theoremLocalDataClose19['life']
    other_close_19 = theoremLocalDataClose19['other']

    # 19년 업종별 개업
    animal_open_19 = theoremLocalDataOpen19['animal']
    culture_open_19 = theoremLocalDataOpen19['culture']
    environment_open_19 = theoremLocalDataOpen19['environment']
    food_open_19 = theoremLocalDataOpen19['food']
    health_open_19 = theoremLocalDataOpen19['health']
    life_open_19 = theoremLocalDataOpen19['life']
    other_open_19 = theoremLocalDataOpen19['other']

    # 20년 업종별 폐업
    animal_close_20 = theoremLocalDataClose20['animal']
    culture_close_20 = theoremLocalDataClose20['culture']
    environment_close_20 = theoremLocalDataClose20['environment']
    food_close_20 = theoremLocalDataClose20['food']
    health_close_20 = theoremLocalDataClose20['health']
    life_close_20 = theoremLocalDataClose20['life']
    other_close_20 = theoremLocalDataClose20['other']

    # 20년 업종별 개업
    animal_open_20 = theoremLocalDataOpen20['animal']
    culture_open_20 = theoremLocalDataOpen20['culture']
    environment_open_20 = theoremLocalDataOpen20['environment']
    food_open_20 = theoremLocalDataOpen20['food']
    health_open_20 = theoremLocalDataOpen20['health']
    life_open_20 = theoremLocalDataOpen20['life']
    other_open_20 = theoremLocalDataOpen20['other']

    # 지역별 업종 close 19
    busan_animal_close_19_cnt = 0
    busan_culture_close_19_cnt = 0
    busan_environment_close_19_cnt = 0
    busan_food_close_19_cnt = 0
    busan_health_close_19_cnt = 0
    busan_life_close_19_cnt = 0
    busan_other_close_19_cnt = 0

    chungbuk_animal_close_19_cnt = 0
    chungbuk_culture_close_19_cnt = 0
    chungbuk_environment_close_19_cnt = 0
    chungbuk_food_close_19_cnt = 0
    chungbuk_health_close_19_cnt = 0
    chungbuk_life_close_19_cnt = 0
    chungbuk_other_close_19_cnt = 0

    chungnam_animal_close_19_cnt = 0
    chungnam_culture_close_19_cnt = 0
    chungnam_environment_close_19_cnt = 0
    chungnam_food_close_19_cnt = 0
    chungnam_health_close_19_cnt = 0
    chungnam_life_close_19_cnt = 0
    chungnam_other_close_19_cnt = 0

    daegu_animal_close_19_cnt = 0
    daegu_culture_close_19_cnt = 0
    daegu_environment_close_19_cnt = 0
    daegu_food_close_19_cnt = 0
    daegu_health_close_19_cnt = 0
    daegu_life_close_19_cnt = 0
    daegu_other_close_19_cnt = 0

    daejeon_animal_close_19_cnt = 0
    daejeon_culture_close_19_cnt = 0
    daejeon_environment_close_19_cnt = 0
    daejeon_food_close_19_cnt = 0
    daejeon_health_close_19_cnt = 0
    daejeon_life_close_19_cnt = 0
    daejeon_other_close_19_cnt = 0

    gangwon_animal_close_19_cnt = 0
    gangwon_culture_close_19_cnt = 0
    gangwon_environment_close_19_cnt = 0
    gangwon_food_close_19_cnt = 0
    gangwon_health_close_19_cnt = 0
    gangwon_life_close_19_cnt = 0
    gangwon_other_close_19_cnt = 0

    gwangju_animal_close_19_cnt = 0
    gwangju_culture_close_19_cnt = 0
    gwangju_environment_close_19_cnt = 0
    gwangju_food_close_19_cnt = 0
    gwangju_health_close_19_cnt = 0
    gwangju_life_close_19_cnt = 0
    gwangju_other_close_19_cnt = 0

    gyeonggi_animal_close_19_cnt = 0
    gyeonggi_culture_close_19_cnt = 0
    gyeonggi_environment_close_19_cnt = 0
    gyeonggi_food_close_19_cnt = 0
    gyeonggi_health_close_19_cnt = 0
    gyeonggi_life_close_19_cnt = 0
    gyeonggi_other_close_19_cnt = 0

    gyeongbuk_animal_close_19_cnt = 0
    gyeongbuk_culture_close_19_cnt = 0
    gyeongbuk_environment_close_19_cnt = 0
    gyeongbuk_food_close_19_cnt = 0
    gyeongbuk_health_close_19_cnt = 0
    gyeongbuk_life_close_19_cnt = 0
    gyeongbuk_other_close_19_cnt = 0

    gyeongnam_animal_close_19_cnt = 0
    gyeongnam_culture_close_19_cnt = 0
    gyeongnam_environment_close_19_cnt = 0
    gyeongnam_food_close_19_cnt = 0
    gyeongnam_health_close_19_cnt = 0
    gyeongnam_life_close_19_cnt = 0
    gyeongnam_other_close_19_cnt = 0

    incheon_animal_close_19_cnt = 0
    incheon_culture_close_19_cnt = 0
    incheon_environment_close_19_cnt = 0
    incheon_food_close_19_cnt = 0
    incheon_health_close_19_cnt = 0
    incheon_life_close_19_cnt = 0
    incheon_other_close_19_cnt = 0

    jeju_animal_close_19_cnt = 0
    jeju_culture_close_19_cnt = 0
    jeju_environment_close_19_cnt = 0
    jeju_food_close_19_cnt = 0
    jeju_health_close_19_cnt = 0
    jeju_life_close_19_cnt = 0
    jeju_other_close_19_cnt = 0

    jeonbuk_animal_close_19_cnt = 0
    jeonbuk_culture_close_19_cnt = 0
    jeonbuk_environment_close_19_cnt = 0
    jeonbuk_food_close_19_cnt = 0
    jeonbuk_health_close_19_cnt = 0
    jeonbuk_life_close_19_cnt = 0
    jeonbuk_other_close_19_cnt = 0

    jeonnam_animal_close_19_cnt = 0
    jeonnam_culture_close_19_cnt = 0
    jeonnam_environment_close_19_cnt = 0
    jeonnam_food_close_19_cnt = 0
    jeonnam_health_close_19_cnt = 0
    jeonnam_life_close_19_cnt = 0
    jeonnam_other_close_19_cnt = 0

    sejong_animal_close_19_cnt = 0
    sejong_culture_close_19_cnt = 0
    sejong_environment_close_19_cnt = 0
    sejong_food_close_19_cnt = 0
    sejong_health_close_19_cnt = 0
    sejong_life_close_19_cnt = 0
    sejong_other_close_19_cnt = 0

    seoul_animal_close_19_cnt = 0
    seoul_culture_close_19_cnt = 0
    seoul_environment_close_19_cnt = 0
    seoul_food_close_19_cnt = 0
    seoul_health_close_19_cnt = 0
    seoul_life_close_19_cnt = 0
    seoul_other_close_19_cnt = 0

    ulsan_animal_close_19_cnt = 0
    ulsan_culture_close_19_cnt = 0
    ulsan_environment_close_19_cnt = 0
    ulsan_food_close_19_cnt = 0
    ulsan_health_close_19_cnt = 0
    ulsan_life_close_19_cnt = 0
    ulsan_other_close_19_cnt = 0

    # 지역별 업종 close 20
    busan_animal_close_20_cnt = 0
    busan_culture_close_20_cnt = 0
    busan_environment_close_20_cnt = 0
    busan_food_close_20_cnt = 0
    busan_health_close_20_cnt = 0
    busan_life_close_20_cnt = 0
    busan_other_close_20_cnt = 0

    chungbuk_animal_close_20_cnt = 0
    chungbuk_culture_close_20_cnt = 0
    chungbuk_environment_close_20_cnt = 0
    chungbuk_food_close_20_cnt = 0
    chungbuk_health_close_20_cnt = 0
    chungbuk_life_close_20_cnt = 0
    chungbuk_other_close_20_cnt = 0

    chungnam_animal_close_20_cnt = 0
    chungnam_culture_close_20_cnt = 0
    chungnam_environment_close_20_cnt = 0
    chungnam_food_close_20_cnt = 0
    chungnam_health_close_20_cnt = 0
    chungnam_life_close_20_cnt = 0
    chungnam_other_close_20_cnt = 0

    daegu_animal_close_20_cnt = 0
    daegu_culture_close_20_cnt = 0
    daegu_environment_close_20_cnt = 0
    daegu_food_close_20_cnt = 0
    daegu_health_close_20_cnt = 0
    daegu_life_close_20_cnt = 0
    daegu_other_close_20_cnt = 0

    daejeon_animal_close_20_cnt = 0
    daejeon_culture_close_20_cnt = 0
    daejeon_environment_close_20_cnt = 0
    daejeon_food_close_20_cnt = 0
    daejeon_health_close_20_cnt = 0
    daejeon_life_close_20_cnt = 0
    daejeon_other_close_20_cnt = 0

    gangwon_animal_close_20_cnt = 0
    gangwon_culture_close_20_cnt = 0
    gangwon_environment_close_20_cnt = 0
    gangwon_food_close_20_cnt = 0
    gangwon_health_close_20_cnt = 0
    gangwon_life_close_20_cnt = 0
    gangwon_other_close_20_cnt = 0

    gwangju_animal_close_20_cnt = 0
    gwangju_culture_close_20_cnt = 0
    gwangju_environment_close_20_cnt = 0
    gwangju_food_close_20_cnt = 0
    gwangju_health_close_20_cnt = 0
    gwangju_life_close_20_cnt = 0
    gwangju_other_close_20_cnt = 0

    gyeonggi_animal_close_20_cnt = 0
    gyeonggi_culture_close_20_cnt = 0
    gyeonggi_environment_close_20_cnt = 0
    gyeonggi_food_close_20_cnt = 0
    gyeonggi_health_close_20_cnt = 0
    gyeonggi_life_close_20_cnt = 0
    gyeonggi_other_close_20_cnt = 0

    gyeongbuk_animal_close_20_cnt = 0
    gyeongbuk_culture_close_20_cnt = 0
    gyeongbuk_environment_close_20_cnt = 0
    gyeongbuk_food_close_20_cnt = 0
    gyeongbuk_health_close_20_cnt = 0
    gyeongbuk_life_close_20_cnt = 0
    gyeongbuk_other_close_20_cnt = 0

    gyeongnam_animal_close_20_cnt = 0
    gyeongnam_culture_close_20_cnt = 0
    gyeongnam_environment_close_20_cnt = 0
    gyeongnam_food_close_20_cnt = 0
    gyeongnam_health_close_20_cnt = 0
    gyeongnam_life_close_20_cnt = 0
    gyeongnam_other_close_20_cnt = 0

    incheon_animal_close_20_cnt = 0
    incheon_culture_close_20_cnt = 0
    incheon_environment_close_20_cnt = 0
    incheon_food_close_20_cnt = 0
    incheon_health_close_20_cnt = 0
    incheon_life_close_20_cnt = 0
    incheon_other_close_20_cnt = 0

    jeju_animal_close_20_cnt = 0
    jeju_culture_close_20_cnt = 0
    jeju_environment_close_20_cnt = 0
    jeju_food_close_20_cnt = 0
    jeju_health_close_20_cnt = 0
    jeju_life_close_20_cnt = 0
    jeju_other_close_20_cnt = 0

    jeonbuk_animal_close_20_cnt = 0
    jeonbuk_culture_close_20_cnt = 0
    jeonbuk_environment_close_20_cnt = 0
    jeonbuk_food_close_20_cnt = 0
    jeonbuk_health_close_20_cnt = 0
    jeonbuk_life_close_20_cnt = 0
    jeonbuk_other_close_20_cnt = 0

    jeonnam_animal_close_20_cnt = 0
    jeonnam_culture_close_20_cnt = 0
    jeonnam_environment_close_20_cnt = 0
    jeonnam_food_close_20_cnt = 0
    jeonnam_health_close_20_cnt = 0
    jeonnam_life_close_20_cnt = 0
    jeonnam_other_close_20_cnt = 0

    sejong_animal_close_20_cnt = 0
    sejong_culture_close_20_cnt = 0
    sejong_environment_close_20_cnt = 0
    sejong_food_close_20_cnt = 0
    sejong_health_close_20_cnt = 0
    sejong_life_close_20_cnt = 0
    sejong_other_close_20_cnt = 0

    seoul_animal_close_20_cnt = 0
    seoul_culture_close_20_cnt = 0
    seoul_environment_close_20_cnt = 0
    seoul_food_close_20_cnt = 0
    seoul_health_close_20_cnt = 0
    seoul_life_close_20_cnt = 0
    seoul_other_close_20_cnt = 0

    ulsan_animal_close_20_cnt = 0
    ulsan_culture_close_20_cnt = 0
    ulsan_environment_close_20_cnt = 0
    ulsan_food_close_20_cnt = 0
    ulsan_health_close_20_cnt = 0
    ulsan_life_close_20_cnt = 0
    ulsan_other_close_20_cnt = 0

    # 지역별 업종 open 19
    busan_animal_open_19_cnt = 0
    busan_culture_open_19_cnt = 0
    busan_environment_open_19_cnt = 0
    busan_food_open_19_cnt = 0
    busan_health_open_19_cnt = 0
    busan_life_open_19_cnt = 0
    busan_other_open_19_cnt = 0

    chungbuk_animal_open_19_cnt = 0
    chungbuk_culture_open_19_cnt = 0
    chungbuk_environment_open_19_cnt = 0
    chungbuk_food_open_19_cnt = 0
    chungbuk_health_open_19_cnt = 0
    chungbuk_life_open_19_cnt = 0
    chungbuk_other_open_19_cnt = 0

    chungnam_animal_open_19_cnt = 0
    chungnam_culture_open_19_cnt = 0
    chungnam_environment_open_19_cnt = 0
    chungnam_food_open_19_cnt = 0
    chungnam_health_open_19_cnt = 0
    chungnam_life_open_19_cnt = 0
    chungnam_other_open_19_cnt = 0

    daegu_animal_open_19_cnt = 0
    daegu_culture_open_19_cnt = 0
    daegu_environment_open_19_cnt = 0
    daegu_food_open_19_cnt = 0
    daegu_health_open_19_cnt = 0
    daegu_life_open_19_cnt = 0
    daegu_other_open_19_cnt = 0

    daejeon_animal_open_19_cnt = 0
    daejeon_culture_open_19_cnt = 0
    daejeon_environment_open_19_cnt = 0
    daejeon_food_open_19_cnt = 0
    daejeon_health_open_19_cnt = 0
    daejeon_life_open_19_cnt = 0
    daejeon_other_open_19_cnt = 0

    gangwon_animal_open_19_cnt = 0
    gangwon_culture_open_19_cnt = 0
    gangwon_environment_open_19_cnt = 0
    gangwon_food_open_19_cnt = 0
    gangwon_health_open_19_cnt = 0
    gangwon_life_open_19_cnt = 0
    gangwon_other_open_19_cnt = 0

    gwangju_animal_open_19_cnt = 0
    gwangju_culture_open_19_cnt = 0
    gwangju_environment_open_19_cnt = 0
    gwangju_food_open_19_cnt = 0
    gwangju_health_open_19_cnt = 0
    gwangju_life_open_19_cnt = 0
    gwangju_other_open_19_cnt = 0

    gyeonggi_animal_open_19_cnt = 0
    gyeonggi_culture_open_19_cnt = 0
    gyeonggi_environment_open_19_cnt = 0
    gyeonggi_food_open_19_cnt = 0
    gyeonggi_health_open_19_cnt = 0
    gyeonggi_life_open_19_cnt = 0
    gyeonggi_other_open_19_cnt = 0

    gyeongbuk_animal_open_19_cnt = 0
    gyeongbuk_culture_open_19_cnt = 0
    gyeongbuk_environment_open_19_cnt = 0
    gyeongbuk_food_open_19_cnt = 0
    gyeongbuk_health_open_19_cnt = 0
    gyeongbuk_life_open_19_cnt = 0
    gyeongbuk_other_open_19_cnt = 0

    gyeongnam_animal_open_19_cnt = 0
    gyeongnam_culture_open_19_cnt = 0
    gyeongnam_environment_open_19_cnt = 0
    gyeongnam_food_open_19_cnt = 0
    gyeongnam_health_open_19_cnt = 0
    gyeongnam_life_open_19_cnt = 0
    gyeongnam_other_open_19_cnt = 0

    incheon_animal_open_19_cnt = 0
    incheon_culture_open_19_cnt = 0
    incheon_environment_open_19_cnt = 0
    incheon_food_open_19_cnt = 0
    incheon_health_open_19_cnt = 0
    incheon_life_open_19_cnt = 0
    incheon_other_open_19_cnt = 0

    jeju_animal_open_19_cnt = 0
    jeju_culture_open_19_cnt = 0
    jeju_environment_open_19_cnt = 0
    jeju_food_open_19_cnt = 0
    jeju_health_open_19_cnt = 0
    jeju_life_open_19_cnt = 0
    jeju_other_open_19_cnt = 0

    jeonbuk_animal_open_19_cnt = 0
    jeonbuk_culture_open_19_cnt = 0
    jeonbuk_environment_open_19_cnt = 0
    jeonbuk_food_open_19_cnt = 0
    jeonbuk_health_open_19_cnt = 0
    jeonbuk_life_open_19_cnt = 0
    jeonbuk_other_open_19_cnt = 0

    jeonnam_animal_open_19_cnt = 0
    jeonnam_culture_open_19_cnt = 0
    jeonnam_environment_open_19_cnt = 0
    jeonnam_food_open_19_cnt = 0
    jeonnam_health_open_19_cnt = 0
    jeonnam_life_open_19_cnt = 0
    jeonnam_other_open_19_cnt = 0

    sejong_animal_open_19_cnt = 0
    sejong_culture_open_19_cnt = 0
    sejong_environment_open_19_cnt = 0
    sejong_food_open_19_cnt = 0
    sejong_health_open_19_cnt = 0
    sejong_life_open_19_cnt = 0
    sejong_other_open_19_cnt = 0

    seoul_animal_open_19_cnt = 0
    seoul_culture_open_19_cnt = 0
    seoul_environment_open_19_cnt = 0
    seoul_food_open_19_cnt = 0
    seoul_health_open_19_cnt = 0
    seoul_life_open_19_cnt = 0
    seoul_other_open_19_cnt = 0

    ulsan_animal_open_19_cnt = 0
    ulsan_culture_open_19_cnt = 0
    ulsan_environment_open_19_cnt = 0
    ulsan_food_open_19_cnt = 0
    ulsan_health_open_19_cnt = 0
    ulsan_life_open_19_cnt = 0
    ulsan_other_open_19_cnt = 0

    # 지역별 업종 open 20
    busan_animal_open_20_cnt = 0
    busan_culture_open_20_cnt = 0
    busan_environment_open_20_cnt = 0
    busan_food_open_20_cnt = 0
    busan_health_open_20_cnt = 0
    busan_life_open_20_cnt = 0
    busan_other_open_20_cnt = 0

    chungbuk_animal_open_20_cnt = 0
    chungbuk_culture_open_20_cnt = 0
    chungbuk_environment_open_20_cnt = 0
    chungbuk_food_open_20_cnt = 0
    chungbuk_health_open_20_cnt = 0
    chungbuk_life_open_20_cnt = 0
    chungbuk_other_open_20_cnt = 0

    chungnam_animal_open_20_cnt = 0
    chungnam_culture_open_20_cnt = 0
    chungnam_environment_open_20_cnt = 0
    chungnam_food_open_20_cnt = 0
    chungnam_health_open_20_cnt = 0
    chungnam_life_open_20_cnt = 0
    chungnam_other_open_20_cnt = 0

    daegu_animal_open_20_cnt = 0
    daegu_culture_open_20_cnt = 0
    daegu_environment_open_20_cnt = 0
    daegu_food_open_20_cnt = 0
    daegu_health_open_20_cnt = 0
    daegu_life_open_20_cnt = 0
    daegu_other_open_20_cnt = 0

    daejeon_animal_open_20_cnt = 0
    daejeon_culture_open_20_cnt = 0
    daejeon_environment_open_20_cnt = 0
    daejeon_food_open_20_cnt = 0
    daejeon_health_open_20_cnt = 0
    daejeon_life_open_20_cnt = 0
    daejeon_other_open_20_cnt = 0

    gangwon_animal_open_20_cnt = 0
    gangwon_culture_open_20_cnt = 0
    gangwon_environment_open_20_cnt = 0
    gangwon_food_open_20_cnt = 0
    gangwon_health_open_20_cnt = 0
    gangwon_life_open_20_cnt = 0
    gangwon_other_open_20_cnt = 0

    gwangju_animal_open_20_cnt = 0
    gwangju_culture_open_20_cnt = 0
    gwangju_environment_open_20_cnt = 0
    gwangju_food_open_20_cnt = 0
    gwangju_health_open_20_cnt = 0
    gwangju_life_open_20_cnt = 0
    gwangju_other_open_20_cnt = 0

    gyeonggi_animal_open_20_cnt = 0
    gyeonggi_culture_open_20_cnt = 0
    gyeonggi_environment_open_20_cnt = 0
    gyeonggi_food_open_20_cnt = 0
    gyeonggi_health_open_20_cnt = 0
    gyeonggi_life_open_20_cnt = 0
    gyeonggi_other_open_20_cnt = 0

    gyeongbuk_animal_open_20_cnt = 0
    gyeongbuk_culture_open_20_cnt = 0
    gyeongbuk_environment_open_20_cnt = 0
    gyeongbuk_food_open_20_cnt = 0
    gyeongbuk_health_open_20_cnt = 0
    gyeongbuk_life_open_20_cnt = 0
    gyeongbuk_other_open_20_cnt = 0

    gyeongnam_animal_open_20_cnt = 0
    gyeongnam_culture_open_20_cnt = 0
    gyeongnam_environment_open_20_cnt = 0
    gyeongnam_food_open_20_cnt = 0
    gyeongnam_health_open_20_cnt = 0
    gyeongnam_life_open_20_cnt = 0
    gyeongnam_other_open_20_cnt = 0

    incheon_animal_open_20_cnt = 0
    incheon_culture_open_20_cnt = 0
    incheon_environment_open_20_cnt = 0
    incheon_food_open_20_cnt = 0
    incheon_health_open_20_cnt = 0
    incheon_life_open_20_cnt = 0
    incheon_other_open_20_cnt = 0

    jeju_animal_open_20_cnt = 0
    jeju_culture_open_20_cnt = 0
    jeju_environment_open_20_cnt = 0
    jeju_food_open_20_cnt = 0
    jeju_health_open_20_cnt = 0
    jeju_life_open_20_cnt = 0
    jeju_other_open_20_cnt = 0

    jeonbuk_animal_open_20_cnt = 0
    jeonbuk_culture_open_20_cnt = 0
    jeonbuk_environment_open_20_cnt = 0
    jeonbuk_food_open_20_cnt = 0
    jeonbuk_health_open_20_cnt = 0
    jeonbuk_life_open_20_cnt = 0
    jeonbuk_other_open_20_cnt = 0

    jeonnam_animal_open_20_cnt = 0
    jeonnam_culture_open_20_cnt = 0
    jeonnam_environment_open_20_cnt = 0
    jeonnam_food_open_20_cnt = 0
    jeonnam_health_open_20_cnt = 0
    jeonnam_life_open_20_cnt = 0
    jeonnam_other_open_20_cnt = 0

    sejong_animal_open_20_cnt = 0
    sejong_culture_open_20_cnt = 0
    sejong_environment_open_20_cnt = 0
    sejong_food_open_20_cnt = 0
    sejong_health_open_20_cnt = 0
    sejong_life_open_20_cnt = 0
    sejong_other_open_20_cnt = 0

    seoul_animal_open_20_cnt = 0
    seoul_culture_open_20_cnt = 0
    seoul_environment_open_20_cnt = 0
    seoul_food_open_20_cnt = 0
    seoul_health_open_20_cnt = 0
    seoul_life_open_20_cnt = 0
    seoul_other_open_20_cnt = 0

    ulsan_animal_open_20_cnt = 0
    ulsan_culture_open_20_cnt = 0
    ulsan_environment_open_20_cnt = 0
    ulsan_food_open_20_cnt = 0
    ulsan_health_open_20_cnt = 0
    ulsan_life_open_20_cnt = 0
    ulsan_other_open_20_cnt = 0

    # 2019 업종별 폐업
    animal_close_19_cnt = 0
    animal_close_19_tot_cnt = animal_close_19.count_documents({})
    for store in animal_close_19.find({}).batch_size(1):
        animal_close_19_cnt += 1
        print(animal_close_19_cnt, "/", animal_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_animal_close_19_cnt += 1
            print("busan_animal_close_19_cnt", busan_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_animal_close_19_cnt += 1
            print("chungbuk_animal_close_19_cnt", chungbuk_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_animal_close_19_cnt += 1
            print("chungnam_animal_close_19_cnt", chungnam_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_animal_close_19_cnt += 1
            print("daegu_animal_close_19_cnt", daegu_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_animal_close_19_cnt += 1
            print("daejeon_animal_close_19_cnt", daejeon_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_animal_close_19_cnt += 1
            print("gangwon_animal_close_19_cnt", gangwon_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_animal_close_19_cnt += 1
            print("gwangju_animal_close_19_cnt", gwangju_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_animal_close_19_cnt += 1
            print("gyeonggi_animal_close_19_cnt", gyeonggi_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_animal_close_19_cnt += 1
            print("gyeongbuk_animal_close_19_cnt", gyeongbuk_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_animal_close_19_cnt += 1
            print("gyeongnam_animal_close_19_cnt", gyeongnam_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_animal_close_19_cnt += 1
            print("incheon_animal_close_19_cnt", incheon_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_animal_close_19_cnt += 1
            print("jeju_animal_close_19_cnt", jeju_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_animal_close_19_cnt += 1
            print("jeonbuk_animal_close_19_cnt", jeonbuk_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_animal_close_19_cnt += 1
            print("jeonnam_animal_close_19_cnt", jeonnam_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_animal_close_19_cnt += 1
            print("sejong_animal_close_19_cnt", sejong_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_animal_close_19_cnt += 1
            print("seoul_animal_close_19_cnt", seoul_animal_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_animal_close_19_cnt += 1
            print("ulsan_animal_close_19_cnt", ulsan_animal_close_19_cnt)

    culture_close_19_cnt = 0
    culture_close_19_tot_cnt = culture_close_19.count_documents({})
    for store in culture_close_19.find({}).batch_size(1):
        culture_close_19_cnt += 1
        print(culture_close_19_cnt, "/", culture_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_culture_close_19_cnt += 1
            print("busan_culture_close_19_cnt", busan_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_culture_close_19_cnt += 1
            print("chungbuk_culture_close_19_cnt", chungbuk_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_culture_close_19_cnt += 1
            print("chungnam_culture_close_19_cnt", chungnam_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_culture_close_19_cnt += 1
            print("daegu_culture_close_19_cnt", daegu_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_culture_close_19_cnt += 1
            print("daejeon_culture_close_19_cnt", daejeon_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_culture_close_19_cnt += 1
            print("gangwon_culture_close_19_cnt", gangwon_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_culture_close_19_cnt += 1
            print("gwangju_culture_close_19_cnt", gwangju_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_culture_close_19_cnt += 1
            print("gyeonggi_culture_close_19_cnt", gyeonggi_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_culture_close_19_cnt += 1
            print("gyeongbuk_culture_close_19_cnt", gyeongbuk_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_culture_close_19_cnt += 1
            print("gyeongnam_culture_close_19_cnt", gyeongnam_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_culture_close_19_cnt += 1
            print("incheon_culture_close_19_cnt", incheon_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_culture_close_19_cnt += 1
            print("jeju_culture_close_19_cnt", jeju_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_culture_close_19_cnt += 1
            print("jeonbuk_culture_close_19_cnt", jeonbuk_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_culture_close_19_cnt += 1
            print("jeonnam_culture_close_19_cnt", jeonnam_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_culture_close_19_cnt += 1
            print("sejong_culture_close_19_cnt", sejong_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_culture_close_19_cnt += 1
            print("seoul_culture_close_19_cnt", seoul_culture_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_culture_close_19_cnt += 1
            print("ulsan_culture_close_19_cnt", ulsan_culture_close_19_cnt)

    environment_close_19_cnt = 0
    environment_close_19_tot_cnt = environment_close_19.count_documents({})
    for store in environment_close_19.find({}).batch_size(1):
        environment_close_19_cnt += 1
        print(environment_close_19_cnt, "/", environment_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_environment_close_19_cnt += 1
            print("busan_environment_close_19_cnt", busan_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_environment_close_19_cnt += 1
            print("chungbuk_environment_close_19_cnt", chungbuk_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_environment_close_19_cnt += 1
            print("chungnam_environment_close_19_cnt", chungnam_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_environment_close_19_cnt += 1
            print("daegu_environment_close_19_cnt", daegu_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_environment_close_19_cnt += 1
            print("daejeon_environment_close_19_cnt", daejeon_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_environment_close_19_cnt += 1
            print("gangwon_environment_close_19_cnt", gangwon_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_environment_close_19_cnt += 1
            print("gwangju_environment_close_19_cnt", gwangju_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_environment_close_19_cnt += 1
            print("gyeonggi_environment_close_19_cnt", gyeonggi_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_environment_close_19_cnt += 1
            print("gyeongbuk_environment_close_19_cnt", gyeongbuk_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_environment_close_19_cnt += 1
            print("gyeongnam_environment_close_19_cnt", gyeongnam_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_environment_close_19_cnt += 1
            print("incheon_environment_close_19_cnt", incheon_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_environment_close_19_cnt += 1
            print("jeju_environment_close_19_cnt", jeju_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_environment_close_19_cnt += 1
            print("jeonbuk_environment_close_19_cnt", jeonbuk_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_environment_close_19_cnt += 1
            print("jeonnam_environment_close_19_cnt", jeonnam_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_environment_close_19_cnt += 1
            print("sejong_environment_close_19_cnt", sejong_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_environment_close_19_cnt += 1
            print("seoul_environment_close_19_cnt", seoul_environment_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_environment_close_19_cnt += 1
            print("ulsan_environment_close_19_cnt", ulsan_environment_close_19_cnt)

    food_close_19_cnt = 0
    food_close_19_tot_cnt = food_close_19.count_documents({})
    for store in food_close_19.find({}).batch_size(1):
        food_close_19_cnt += 1
        print(food_close_19_cnt, "/", food_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_food_close_19_cnt += 1
            print("busan_food_close_19_cnt", busan_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_food_close_19_cnt += 1
            print("chungbuk_food_close_19_cnt", chungbuk_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_food_close_19_cnt += 1
            print("chungnam_food_close_19_cnt", chungnam_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_food_close_19_cnt += 1
            print("daegu_food_close_19_cnt", daegu_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_food_close_19_cnt += 1
            print("daejeon_food_close_19_cnt", daejeon_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_food_close_19_cnt += 1
            print("gangwon_food_close_19_cnt", gangwon_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_food_close_19_cnt += 1
            print("gwangju_food_close_19_cnt", gwangju_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_food_close_19_cnt += 1
            print("gyeonggi_food_close_19_cnt", gyeonggi_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_food_close_19_cnt += 1
            print("gyeongbuk_food_close_19_cnt", gyeongbuk_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_food_close_19_cnt += 1
            print("gyeongnam_food_close_19_cnt", gyeongnam_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_food_close_19_cnt += 1
            print("incheon_food_close_19_cnt", incheon_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_food_close_19_cnt += 1
            print("jeju_food_close_19_cnt", jeju_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_food_close_19_cnt += 1
            print("jeonbuk_food_close_19_cnt", jeonbuk_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_food_close_19_cnt += 1
            print("jeonnam_food_close_19_cnt", jeonnam_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_food_close_19_cnt += 1
            print("sejong_food_close_19_cnt", sejong_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_food_close_19_cnt += 1
            print("seoul_food_close_19_cnt", seoul_food_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_food_close_19_cnt += 1
            print("ulsan_food_close_19_cnt", ulsan_food_close_19_cnt)

    health_close_19_cnt = 0
    health_close_19_tot_cnt = health_close_19.count_documents({})
    for store in health_close_19.find({}).batch_size(1):
        health_close_19_cnt += 1
        print(health_close_19_cnt, "/", health_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_health_close_19_cnt += 1
            print("busan_health_close_19_cnt", busan_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_health_close_19_cnt += 1
            print("chungbuk_health_close_19_cnt", chungbuk_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_health_close_19_cnt += 1
            print("chungnam_health_close_19_cnt", chungnam_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_health_close_19_cnt += 1
            print("daegu_health_close_19_cnt", daegu_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_health_close_19_cnt += 1
            print("daejeon_health_close_19_cnt", daejeon_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_health_close_19_cnt += 1
            print("gangwon_health_close_19_cnt", gangwon_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_health_close_19_cnt += 1
            print("gwangju_health_close_19_cnt", gwangju_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_health_close_19_cnt += 1
            print("gyeonggi_health_close_19_cnt", gyeonggi_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_health_close_19_cnt += 1
            print("gyeongbuk_health_close_19_cnt", gyeongbuk_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_health_close_19_cnt += 1
            print("gyeongnam_health_close_19_cnt", gyeongnam_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_health_close_19_cnt += 1
            print("incheon_health_close_19_cnt", incheon_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_health_close_19_cnt += 1
            print("jeju_health_close_19_cnt", jeju_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_health_close_19_cnt += 1
            print("jeonbuk_health_close_19_cnt", jeonbuk_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_health_close_19_cnt += 1
            print("jeonnam_health_close_19_cnt", jeonnam_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_health_close_19_cnt += 1
            print("sejong_health_close_19_cnt", sejong_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_health_close_19_cnt += 1
            print("seoul_health_close_19_cnt", seoul_health_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_health_close_19_cnt += 1
            print("ulsan_health_close_19_cnt", ulsan_health_close_19_cnt)

    life_close_19_cnt = 0
    life_close_19_tot_cnt = life_close_19.count_documents({})
    for store in life_close_19.find({}).batch_size(1):
        life_close_19_cnt += 1
        print(life_close_19_cnt, "/", life_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_life_close_19_cnt += 1
            print("busan_life_close_19_cnt", busan_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_life_close_19_cnt += 1
            print("chungbuk_life_close_19_cnt", chungbuk_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_life_close_19_cnt += 1
            print("chungnam_life_close_19_cnt", chungnam_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_life_close_19_cnt += 1
            print("daegu_life_close_19_cnt", daegu_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_life_close_19_cnt += 1
            print("daejeon_life_close_19_cnt", daejeon_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_life_close_19_cnt += 1
            print("gangwon_life_close_19_cnt", gangwon_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_life_close_19_cnt += 1
            print("gwangju_life_close_19_cnt", gwangju_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_life_close_19_cnt += 1
            print("gyeonggi_life_close_19_cnt", gyeonggi_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_life_close_19_cnt += 1
            print("gyeongbuk_life_close_19_cnt", gyeongbuk_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_life_close_19_cnt += 1
            print("gyeongnam_life_close_19_cnt", gyeongnam_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_life_close_19_cnt += 1
            print("incheon_life_close_19_cnt", incheon_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_life_close_19_cnt += 1
            print("jeju_life_close_19_cnt", jeju_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_life_close_19_cnt += 1
            print("jeonbuk_life_close_19_cnt", jeonbuk_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_life_close_19_cnt += 1
            print("jeonnam_life_close_19_cnt", jeonnam_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_life_close_19_cnt += 1
            print("sejong_life_close_19_cnt", sejong_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_life_close_19_cnt += 1
            print("seoul_life_close_19_cnt", seoul_life_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_life_close_19_cnt += 1
            print("ulsan_life_close_19_cnt", ulsan_life_close_19_cnt)

    other_close_19_cnt = 0
    other_close_19_tot_cnt = other_close_19.count_documents({})
    for store in other_close_19.find({}).batch_size(1):
        other_close_19_cnt += 1
        print(other_close_19_cnt, "/", other_close_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_other_close_19_cnt += 1
            print("busan_other_close_19_cnt", busan_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_other_close_19_cnt += 1
            print("chungbuk_other_close_19_cnt", chungbuk_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_other_close_19_cnt += 1
            print("chungnam_other_close_19_cnt", chungnam_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_other_close_19_cnt += 1
            print("daegu_other_close_19_cnt", daegu_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_other_close_19_cnt += 1
            print("daejeon_other_close_19_cnt", daejeon_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_other_close_19_cnt += 1
            print("gangwon_other_close_19_cnt", gangwon_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_other_close_19_cnt += 1
            print("gwangju_other_close_19_cnt", gwangju_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_other_close_19_cnt += 1
            print("gyeonggi_other_close_19_cnt", gyeonggi_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_other_close_19_cnt += 1
            print("gyeongbuk_other_close_19_cnt", gyeongbuk_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_other_close_19_cnt += 1
            print("gyeongnam_other_close_19_cnt", gyeongnam_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_other_close_19_cnt += 1
            print("incheon_other_close_19_cnt", incheon_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_other_close_19_cnt += 1
            print("jeju_other_close_19_cnt", jeju_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_other_close_19_cnt += 1
            print("jeonbuk_other_close_19_cnt", jeonbuk_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_other_close_19_cnt += 1
            print("jeonnam_other_close_19_cnt", jeonnam_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_other_close_19_cnt += 1
            print("sejong_other_close_19_cnt", sejong_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_other_close_19_cnt += 1
            print("seoul_other_close_19_cnt", seoul_other_close_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_other_close_19_cnt += 1
            print("ulsan_other_close_19_cnt", ulsan_other_close_19_cnt)

    # 2019 업종별 개업
    animal_open_19_cnt = 0
    animal_open_19_tot_cnt = animal_open_19.count_documents({})
    for store in animal_open_19.find({}).batch_size(1):
        animal_open_19_cnt += 1
        print(animal_open_19_cnt, "/", animal_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_animal_open_19_cnt += 1
            print("busan_animal_open_19_cnt", busan_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_animal_open_19_cnt += 1
            print("chungbuk_animal_open_19_cnt", chungbuk_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_animal_open_19_cnt += 1
            print("chungnam_animal_open_19_cnt", chungnam_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_animal_open_19_cnt += 1
            print("daegu_animal_open_19_cnt", daegu_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_animal_open_19_cnt += 1
            print("daejeon_animal_open_19_cnt", daejeon_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_animal_open_19_cnt += 1
            print("gangwon_animal_open_19_cnt", gangwon_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_animal_open_19_cnt += 1
            print("gwangju_animal_open_19_cnt", gwangju_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_animal_open_19_cnt += 1
            print("gyeonggi_animal_open_19_cnt", gyeonggi_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_animal_open_19_cnt += 1
            print("gyeongbuk_animal_open_19_cnt", gyeongbuk_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_animal_open_19_cnt += 1
            print("gyeongnam_animal_open_19_cnt", gyeongnam_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_animal_open_19_cnt += 1
            print("incheon_animal_open_19_cnt", incheon_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_animal_open_19_cnt += 1
            print("jeju_animal_open_19_cnt", jeju_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_animal_open_19_cnt += 1
            print("jeonbuk_animal_open_19_cnt", jeonbuk_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_animal_open_19_cnt += 1
            print("jeonnam_animal_open_19_cnt", jeonnam_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_animal_open_19_cnt += 1
            print("sejong_animal_open_19_cnt", sejong_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_animal_open_19_cnt += 1
            print("seoul_animal_open_19_cnt", seoul_animal_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_animal_open_19_cnt += 1
            print("ulsan_animal_open_19_cnt", ulsan_animal_open_19_cnt)

    culture_open_19_cnt = 0
    culture_open_19_tot_cnt = culture_open_19.count_documents({})
    for store in culture_open_19.find({}).batch_size(1):
        culture_open_19_cnt += 1
        print(culture_open_19_cnt, "/", culture_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_culture_open_19_cnt += 1
            print("busan_culture_open_19_cnt", busan_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_culture_open_19_cnt += 1
            print("chungbuk_culture_open_19_cnt", chungbuk_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_culture_open_19_cnt += 1
            print("chungnam_culture_open_19_cnt", chungnam_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_culture_open_19_cnt += 1
            print("daegu_culture_open_19_cnt", daegu_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_culture_open_19_cnt += 1
            print("daejeon_culture_open_19_cnt", daejeon_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_culture_open_19_cnt += 1
            print("gangwon_culture_open_19_cnt", gangwon_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_culture_open_19_cnt += 1
            print("gwangju_culture_open_19_cnt", gwangju_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_culture_open_19_cnt += 1
            print("gyeonggi_culture_open_19_cnt", gyeonggi_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_culture_open_19_cnt += 1
            print("gyeongbuk_culture_open_19_cnt", gyeongbuk_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_culture_open_19_cnt += 1
            print("gyeongnam_culture_open_19_cnt", gyeongnam_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_culture_open_19_cnt += 1
            print("incheon_culture_open_19_cnt", incheon_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_culture_open_19_cnt += 1
            print("jeju_culture_open_19_cnt", jeju_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_culture_open_19_cnt += 1
            print("jeonbuk_culture_open_19_cnt", jeonbuk_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_culture_open_19_cnt += 1
            print("jeonnam_culture_open_19_cnt", jeonnam_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_culture_open_19_cnt += 1
            print("sejong_culture_open_19_cnt", sejong_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_culture_open_19_cnt += 1
            print("seoul_culture_open_19_cnt", seoul_culture_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_culture_open_19_cnt += 1
            print("ulsan_culture_open_19_cnt", ulsan_culture_open_19_cnt)

    environment_open_19_cnt = 0
    environment_open_19_tot_cnt = environment_open_19.count_documents({})
    for store in environment_open_19.find({}).batch_size(1):
        environment_open_19_cnt += 1
        print(environment_open_19_cnt, "/", environment_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_environment_open_19_cnt += 1
            print("busan_environment_open_19_cnt", busan_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_environment_open_19_cnt += 1
            print("chungbuk_environment_open_19_cnt", chungbuk_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_environment_open_19_cnt += 1
            print("chungnam_environment_open_19_cnt", chungnam_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_environment_open_19_cnt += 1
            print("daegu_environment_open_19_cnt", daegu_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_environment_open_19_cnt += 1
            print("daejeon_environment_open_19_cnt", daejeon_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_environment_open_19_cnt += 1
            print("gangwon_environment_open_19_cnt", gangwon_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_environment_open_19_cnt += 1
            print("gwangju_environment_open_19_cnt", gwangju_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_environment_open_19_cnt += 1
            print("gyeonggi_environment_open_19_cnt", gyeonggi_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_environment_open_19_cnt += 1
            print("gyeongbuk_environment_open_19_cnt", gyeongbuk_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_environment_open_19_cnt += 1
            print("gyeongnam_environment_open_19_cnt", gyeongnam_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_environment_open_19_cnt += 1
            print("incheon_environment_open_19_cnt", incheon_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_environment_open_19_cnt += 1
            print("jeju_environment_open_19_cnt", jeju_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_environment_open_19_cnt += 1
            print("jeonbuk_environment_open_19_cnt", jeonbuk_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_environment_open_19_cnt += 1
            print("jeonnam_environment_open_19_cnt", jeonnam_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_environment_open_19_cnt += 1
            print("sejong_environment_open_19_cnt", sejong_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_environment_open_19_cnt += 1
            print("seoul_environment_open_19_cnt", seoul_environment_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_environment_open_19_cnt += 1
            print("ulsan_environment_open_19_cnt", ulsan_environment_open_19_cnt)

    food_open_19_cnt = 0
    food_open_19_tot_cnt = food_open_19.count_documents({})
    for store in food_open_19.find({}).batch_size(1):
        food_open_19_cnt += 1
        print(food_open_19_cnt, "/", food_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_food_open_19_cnt += 1
            print("busan_food_open_19_cnt", busan_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_food_open_19_cnt += 1
            print("chungbuk_food_open_19_cnt", chungbuk_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_food_open_19_cnt += 1
            print("chungnam_food_open_19_cnt", chungnam_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_food_open_19_cnt += 1
            print("daegu_food_open_19_cnt", daegu_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_food_open_19_cnt += 1
            print("daejeon_food_open_19_cnt", daejeon_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_food_open_19_cnt += 1
            print("gangwon_food_open_19_cnt", gangwon_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_food_open_19_cnt += 1
            print("gwangju_food_open_19_cnt", gwangju_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_food_open_19_cnt += 1
            print("gyeonggi_food_open_19_cnt", gyeonggi_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_food_open_19_cnt += 1
            print("gyeongbuk_food_open_19_cnt", gyeongbuk_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_food_open_19_cnt += 1
            print("gyeongnam_food_open_19_cnt", gyeongnam_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_food_open_19_cnt += 1
            print("incheon_food_open_19_cnt", incheon_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_food_open_19_cnt += 1
            print("jeju_food_open_19_cnt", jeju_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_food_open_19_cnt += 1
            print("jeonbuk_food_open_19_cnt", jeonbuk_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_food_open_19_cnt += 1
            print("jeonnam_food_open_19_cnt", jeonnam_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_food_open_19_cnt += 1
            print("sejong_food_open_19_cnt", sejong_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_food_open_19_cnt += 1
            print("seoul_food_open_19_cnt", seoul_food_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_food_open_19_cnt += 1
            print("ulsan_food_open_19_cnt", ulsan_food_open_19_cnt)

    health_open_19_cnt = 0
    health_open_19_tot_cnt = health_open_19.count_documents({})
    for store in health_open_19.find({}).batch_size(1):
        health_open_19_cnt += 1
        print(health_open_19_cnt, "/", health_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_health_open_19_cnt += 1
            print("busan_health_open_19_cnt", busan_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_health_open_19_cnt += 1
            print("chungbuk_health_open_19_cnt", chungbuk_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_health_open_19_cnt += 1
            print("chungnam_health_open_19_cnt", chungnam_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_health_open_19_cnt += 1
            print("daegu_health_open_19_cnt", daegu_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_health_open_19_cnt += 1
            print("daejeon_health_open_19_cnt", daejeon_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_health_open_19_cnt += 1
            print("gangwon_health_open_19_cnt", gangwon_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_health_open_19_cnt += 1
            print("gwangju_health_open_19_cnt", gwangju_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_health_open_19_cnt += 1
            print("gyeonggi_health_open_19_cnt", gyeonggi_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_health_open_19_cnt += 1
            print("gyeongbuk_health_open_19_cnt", gyeongbuk_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_health_open_19_cnt += 1
            print("gyeongnam_health_open_19_cnt", gyeongnam_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_health_open_19_cnt += 1
            print("incheon_health_open_19_cnt", incheon_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_health_open_19_cnt += 1
            print("jeju_health_open_19_cnt", jeju_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_health_open_19_cnt += 1
            print("jeonbuk_health_open_19_cnt", jeonbuk_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_health_open_19_cnt += 1
            print("jeonnam_health_open_19_cnt", jeonnam_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_health_open_19_cnt += 1
            print("sejong_health_open_19_cnt", sejong_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_health_open_19_cnt += 1
            print("seoul_health_open_19_cnt", seoul_health_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_health_open_19_cnt += 1
            print("ulsan_health_open_19_cnt", ulsan_health_open_19_cnt)

    life_open_19_cnt = 0
    life_open_19_tot_cnt = life_open_19.count_documents({})
    for store in life_open_19.find({}).batch_size(1):
        life_open_19_cnt += 1
        print(life_open_19_cnt, "/", life_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_life_open_19_cnt += 1
            print("busan_life_open_19_cnt", busan_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_life_open_19_cnt += 1
            print("chungbuk_life_open_19_cnt", chungbuk_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_life_open_19_cnt += 1
            print("chungnam_life_open_19_cnt", chungnam_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_life_open_19_cnt += 1
            print("daegu_life_open_19_cnt", daegu_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_life_open_19_cnt += 1
            print("daejeon_life_open_19_cnt", daejeon_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_life_open_19_cnt += 1
            print("gangwon_life_open_19_cnt", gangwon_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_life_open_19_cnt += 1
            print("gwangju_life_open_19_cnt", gwangju_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_life_open_19_cnt += 1
            print("gyeonggi_life_open_19_cnt", gyeonggi_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_life_open_19_cnt += 1
            print("gyeongbuk_life_open_19_cnt", gyeongbuk_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_life_open_19_cnt += 1
            print("gyeongnam_life_open_19_cnt", gyeongnam_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_life_open_19_cnt += 1
            print("incheon_life_open_19_cnt", incheon_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_life_open_19_cnt += 1
            print("jeju_life_open_19_cnt", jeju_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_life_open_19_cnt += 1
            print("jeonbuk_life_open_19_cnt", jeonbuk_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_life_open_19_cnt += 1
            print("jeonnam_life_open_19_cnt", jeonnam_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_life_open_19_cnt += 1
            print("sejong_life_open_19_cnt", sejong_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_life_open_19_cnt += 1
            print("seoul_life_open_19_cnt", seoul_life_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_life_open_19_cnt += 1
            print("ulsan_life_open_19_cnt", ulsan_life_open_19_cnt)

    other_open_19_cnt = 0
    other_open_19_tot_cnt = other_open_19.count_documents({})
    for store in other_open_19.find({}).batch_size(1):
        other_open_19_cnt += 1
        print(other_open_19_cnt, "/", other_open_19_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_other_open_19_cnt += 1
            print("busan_other_open_19_cnt", busan_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_other_open_19_cnt += 1
            print("chungbuk_other_open_19_cnt", chungbuk_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_other_open_19_cnt += 1
            print("chungnam_other_open_19_cnt", chungnam_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_other_open_19_cnt += 1
            print("daegu_other_open_19_cnt", daegu_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_other_open_19_cnt += 1
            print("daejeon_other_open_19_cnt", daejeon_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_other_open_19_cnt += 1
            print("gangwon_other_open_19_cnt", gangwon_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_other_open_19_cnt += 1
            print("gwangju_other_open_19_cnt", gwangju_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_other_open_19_cnt += 1
            print("gyeonggi_other_open_19_cnt", gyeonggi_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_other_open_19_cnt += 1
            print("gyeongbuk_other_open_19_cnt", gyeongbuk_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_other_open_19_cnt += 1
            print("gyeongnam_other_open_19_cnt", gyeongnam_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_other_open_19_cnt += 1
            print("incheon_other_open_19_cnt", incheon_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_other_open_19_cnt += 1
            print("jeju_other_open_19_cnt", jeju_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_other_open_19_cnt += 1
            print("jeonbuk_other_open_19_cnt", jeonbuk_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_other_open_19_cnt += 1
            print("jeonnam_other_open_19_cnt", jeonnam_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_other_open_19_cnt += 1
            print("sejong_other_open_19_cnt", sejong_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_other_open_19_cnt += 1
            print("seoul_other_open_19_cnt", seoul_other_open_19_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_other_open_19_cnt += 1
            print("ulsan_other_open_19_cnt", ulsan_other_open_19_cnt)

    # 2020 업종별 폐업
    animal_close_20_cnt = 0
    animal_close_20_tot_cnt = animal_close_20.count_documents({})
    for store in animal_close_20.find({}).batch_size(1):
        animal_close_20_cnt += 1
        print(animal_close_20_cnt, "/", animal_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_animal_close_20_cnt += 1
            print("busan_animal_close_20_cnt", busan_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_animal_close_20_cnt += 1
            print("chungbuk_animal_close_20_cnt", chungbuk_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_animal_close_20_cnt += 1
            print("chungnam_animal_close_20_cnt", chungnam_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_animal_close_20_cnt += 1
            print("daegu_animal_close_20_cnt", daegu_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_animal_close_20_cnt += 1
            print("daejeon_animal_close_20_cnt", daejeon_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_animal_close_20_cnt += 1
            print("gangwon_animal_close_20_cnt", gangwon_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_animal_close_20_cnt += 1
            print("gwangju_animal_close_20_cnt", gwangju_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_animal_close_20_cnt += 1
            print("gyeonggi_animal_close_20_cnt", gyeonggi_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_animal_close_20_cnt += 1
            print("gyeongbuk_animal_close_20_cnt", gyeongbuk_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_animal_close_20_cnt += 1
            print("gyeongnam_animal_close_20_cnt", gyeongnam_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_animal_close_20_cnt += 1
            print("incheon_animal_close_20_cnt", incheon_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_animal_close_20_cnt += 1
            print("jeju_animal_close_20_cnt", jeju_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_animal_close_20_cnt += 1
            print("jeonbuk_animal_close_20_cnt", jeonbuk_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_animal_close_20_cnt += 1
            print("jeonnam_animal_close_20_cnt", jeonnam_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_animal_close_20_cnt += 1
            print("sejong_animal_close_20_cnt", sejong_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_animal_close_20_cnt += 1
            print("seoul_animal_close_20_cnt", seoul_animal_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_animal_close_20_cnt += 1
            print("ulsan_animal_close_20_cnt", ulsan_animal_close_20_cnt)

    culture_close_20_cnt = 0
    culture_close_20_tot_cnt = culture_close_20.count_documents({})
    for store in culture_close_20.find({}).batch_size(1):
        culture_close_20_cnt += 1
        print(culture_close_20_cnt, "/", culture_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_culture_close_20_cnt += 1
            print("busan_culture_close_20_cnt", busan_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_culture_close_20_cnt += 1
            print("chungbuk_culture_close_20_cnt", chungbuk_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_culture_close_20_cnt += 1
            print("chungnam_culture_close_20_cnt", chungnam_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_culture_close_20_cnt += 1
            print("daegu_culture_close_20_cnt", daegu_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_culture_close_20_cnt += 1
            print("daejeon_culture_close_20_cnt", daejeon_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_culture_close_20_cnt += 1
            print("gangwon_culture_close_20_cnt", gangwon_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_culture_close_20_cnt += 1
            print("gwangju_culture_close_20_cnt", gwangju_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_culture_close_20_cnt += 1
            print("gyeonggi_culture_close_20_cnt", gyeonggi_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_culture_close_20_cnt += 1
            print("gyeongbuk_culture_close_20_cnt", gyeongbuk_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_culture_close_20_cnt += 1
            print("gyeongnam_culture_close_20_cnt", gyeongnam_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_culture_close_20_cnt += 1
            print("incheon_culture_close_20_cnt", incheon_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_culture_close_20_cnt += 1
            print("jeju_culture_close_20_cnt", jeju_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_culture_close_20_cnt += 1
            print("jeonbuk_culture_close_20_cnt", jeonbuk_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_culture_close_20_cnt += 1
            print("jeonnam_culture_close_20_cnt", jeonnam_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_culture_close_20_cnt += 1
            print("sejong_culture_close_20_cnt", sejong_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_culture_close_20_cnt += 1
            print("seoul_culture_close_20_cnt", seoul_culture_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_culture_close_20_cnt += 1
            print("ulsan_culture_close_20_cnt", ulsan_culture_close_20_cnt)

    environment_close_20_cnt = 0
    environment_close_20_tot_cnt = environment_close_20.count_documents({})
    for store in environment_close_20.find({}).batch_size(1):
        environment_close_20_cnt += 1
        print(environment_close_20_cnt, "/", environment_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_environment_close_20_cnt += 1
            print("busan_environment_close_20_cnt", busan_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_environment_close_20_cnt += 1
            print("chungbuk_environment_close_20_cnt", chungbuk_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_environment_close_20_cnt += 1
            print("chungnam_environment_close_20_cnt", chungnam_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_environment_close_20_cnt += 1
            print("daegu_environment_close_20_cnt", daegu_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_environment_close_20_cnt += 1
            print("daejeon_environment_close_20_cnt", daejeon_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_environment_close_20_cnt += 1
            print("gangwon_environment_close_20_cnt", gangwon_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_environment_close_20_cnt += 1
            print("gwangju_environment_close_20_cnt", gwangju_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_environment_close_20_cnt += 1
            print("gyeonggi_environment_close_20_cnt", gyeonggi_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_environment_close_20_cnt += 1
            print("gyeongbuk_environment_close_20_cnt", gyeongbuk_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_environment_close_20_cnt += 1
            print("gyeongnam_environment_close_20_cnt", gyeongnam_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_environment_close_20_cnt += 1
            print("incheon_environment_close_20_cnt", incheon_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_environment_close_20_cnt += 1
            print("jeju_environment_close_20_cnt", jeju_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_environment_close_20_cnt += 1
            print("jeonbuk_environment_close_20_cnt", jeonbuk_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_environment_close_20_cnt += 1
            print("jeonnam_environment_close_20_cnt", jeonnam_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_environment_close_20_cnt += 1
            print("sejong_environment_close_20_cnt", sejong_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_environment_close_20_cnt += 1
            print("seoul_environment_close_20_cnt", seoul_environment_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_environment_close_20_cnt += 1
            print("ulsan_environment_close_20_cnt", ulsan_environment_close_20_cnt)

    food_close_20_cnt = 0
    food_close_20_tot_cnt = food_close_20.count_documents({})
    for store in food_close_20.find({}).batch_size(1):
        food_close_20_cnt += 1
        print(food_close_20_cnt, "/", food_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_food_close_20_cnt += 1
            print("busan_food_close_20_cnt", busan_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_food_close_20_cnt += 1
            print("chungbuk_food_close_20_cnt", chungbuk_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_food_close_20_cnt += 1
            print("chungnam_food_close_20_cnt", chungnam_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_food_close_20_cnt += 1
            print("daegu_food_close_20_cnt", daegu_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_food_close_20_cnt += 1
            print("daejeon_food_close_20_cnt", daejeon_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_food_close_20_cnt += 1
            print("gangwon_food_close_20_cnt", gangwon_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_food_close_20_cnt += 1
            print("gwangju_food_close_20_cnt", gwangju_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_food_close_20_cnt += 1
            print("gyeonggi_food_close_20_cnt", gyeonggi_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_food_close_20_cnt += 1
            print("gyeongbuk_food_close_20_cnt", gyeongbuk_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_food_close_20_cnt += 1
            print("gyeongnam_food_close_20_cnt", gyeongnam_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_food_close_20_cnt += 1
            print("incheon_food_close_20_cnt", incheon_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_food_close_20_cnt += 1
            print("jeju_food_close_20_cnt", jeju_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_food_close_20_cnt += 1
            print("jeonbuk_food_close_20_cnt", jeonbuk_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_food_close_20_cnt += 1
            print("jeonnam_food_close_20_cnt", jeonnam_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_food_close_20_cnt += 1
            print("sejong_food_close_20_cnt", sejong_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_food_close_20_cnt += 1
            print("seoul_food_close_20_cnt", seoul_food_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_food_close_20_cnt += 1
            print("ulsan_food_close_20_cnt", ulsan_food_close_20_cnt)

    health_close_20_cnt = 0
    health_close_20_tot_cnt = health_close_20.count_documents({})
    for store in health_close_20.find({}).batch_size(1):
        health_close_20_cnt += 1
        print(health_close_20_cnt, "/", health_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_health_close_20_cnt += 1
            print("busan_health_close_20_cnt", busan_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_health_close_20_cnt += 1
            print("chungbuk_health_close_20_cnt", chungbuk_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_health_close_20_cnt += 1
            print("chungnam_health_close_20_cnt", chungnam_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_health_close_20_cnt += 1
            print("daegu_health_close_20_cnt", daegu_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_health_close_20_cnt += 1
            print("daejeon_health_close_20_cnt", daejeon_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_health_close_20_cnt += 1
            print("gangwon_health_close_20_cnt", gangwon_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_health_close_20_cnt += 1
            print("gwangju_health_close_20_cnt", gwangju_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_health_close_20_cnt += 1
            print("gyeonggi_health_close_20_cnt", gyeonggi_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_health_close_20_cnt += 1
            print("gyeongbuk_health_close_20_cnt", gyeongbuk_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_health_close_20_cnt += 1
            print("gyeongnam_health_close_20_cnt", gyeongnam_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_health_close_20_cnt += 1
            print("incheon_health_close_20_cnt", incheon_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_health_close_20_cnt += 1
            print("jeju_health_close_20_cnt", jeju_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_health_close_20_cnt += 1
            print("jeonbuk_health_close_20_cnt", jeonbuk_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_health_close_20_cnt += 1
            print("jeonnam_health_close_20_cnt", jeonnam_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_health_close_20_cnt += 1
            print("sejong_health_close_20_cnt", sejong_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_health_close_20_cnt += 1
            print("seoul_health_close_20_cnt", seoul_health_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_health_close_20_cnt += 1
            print("ulsan_health_close_20_cnt", ulsan_health_close_20_cnt)

    life_close_20_cnt = 0
    life_close_20_tot_cnt = life_close_20.count_documents({})
    for store in life_close_20.find({}).batch_size(1):
        life_close_20_cnt += 1
        print(life_close_20_cnt, "/", life_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_life_close_20_cnt += 1
            print("busan_life_close_20_cnt", busan_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_life_close_20_cnt += 1
            print("chungbuk_life_close_20_cnt", chungbuk_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_life_close_20_cnt += 1
            print("chungnam_life_close_20_cnt", chungnam_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_life_close_20_cnt += 1
            print("daegu_life_close_20_cnt", daegu_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_life_close_20_cnt += 1
            print("daejeon_life_close_20_cnt", daejeon_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_life_close_20_cnt += 1
            print("gangwon_life_close_20_cnt", gangwon_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_life_close_20_cnt += 1
            print("gwangju_life_close_20_cnt", gwangju_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_life_close_20_cnt += 1
            print("gyeonggi_life_close_20_cnt", gyeonggi_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_life_close_20_cnt += 1
            print("gyeongbuk_life_close_20_cnt", gyeongbuk_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_life_close_20_cnt += 1
            print("gyeongnam_life_close_20_cnt", gyeongnam_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_life_close_20_cnt += 1
            print("incheon_life_close_20_cnt", incheon_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_life_close_20_cnt += 1
            print("jeju_life_close_20_cnt", jeju_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_life_close_20_cnt += 1
            print("jeonbuk_life_close_20_cnt", jeonbuk_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_life_close_20_cnt += 1
            print("jeonnam_life_close_20_cnt", jeonnam_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_life_close_20_cnt += 1
            print("sejong_life_close_20_cnt", sejong_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_life_close_20_cnt += 1
            print("seoul_life_close_20_cnt", seoul_life_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_life_close_20_cnt += 1
            print("ulsan_life_close_20_cnt", ulsan_life_close_20_cnt)

    other_close_20_cnt = 0
    other_close_20_tot_cnt = other_close_20.count_documents({})
    for store in other_close_20.find({}).batch_size(1):
        other_close_20_cnt += 1
        print(other_close_20_cnt, "/", other_close_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_other_close_20_cnt += 1
            print("busan_other_close_20_cnt", busan_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_other_close_20_cnt += 1
            print("chungbuk_other_close_20_cnt", chungbuk_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_other_close_20_cnt += 1
            print("chungnam_other_close_20_cnt", chungnam_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_other_close_20_cnt += 1
            print("daegu_other_close_20_cnt", daegu_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_other_close_20_cnt += 1
            print("daejeon_other_close_20_cnt", daejeon_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_other_close_20_cnt += 1
            print("gangwon_other_close_20_cnt", gangwon_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_other_close_20_cnt += 1
            print("gwangju_other_close_20_cnt", gwangju_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_other_close_20_cnt += 1
            print("gyeonggi_other_close_20_cnt", gyeonggi_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_other_close_20_cnt += 1
            print("gyeongbuk_other_close_20_cnt", gyeongbuk_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_other_close_20_cnt += 1
            print("gyeongnam_other_close_20_cnt", gyeongnam_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_other_close_20_cnt += 1
            print("incheon_other_close_20_cnt", incheon_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_other_close_20_cnt += 1
            print("jeju_other_close_20_cnt", jeju_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_other_close_20_cnt += 1
            print("jeonbuk_other_close_20_cnt", jeonbuk_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_other_close_20_cnt += 1
            print("jeonnam_other_close_20_cnt", jeonnam_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_other_close_20_cnt += 1
            print("sejong_other_close_20_cnt", sejong_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_other_close_20_cnt += 1
            print("seoul_other_close_20_cnt", seoul_other_close_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_other_close_20_cnt += 1
            print("ulsan_other_close_20_cnt", ulsan_other_close_20_cnt)

    # 2020 업종별 개업
    animal_open_20_cnt = 0
    animal_open_20_tot_cnt = animal_open_20.count_documents({})
    for store in animal_open_20.find({}).batch_size(1):
        animal_open_20_cnt += 1
        print(animal_open_20_cnt, "/", animal_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_animal_open_20_cnt += 1
            print("busan_animal_open_20_cnt", busan_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_animal_open_20_cnt += 1
            print("chungbuk_animal_open_20_cnt", chungbuk_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_animal_open_20_cnt += 1
            print("chungnam_animal_open_20_cnt", chungnam_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_animal_open_20_cnt += 1
            print("daegu_animal_open_20_cnt", daegu_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_animal_open_20_cnt += 1
            print("daejeon_animal_open_20_cnt", daejeon_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_animal_open_20_cnt += 1
            print("gangwon_animal_open_20_cnt", gangwon_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_animal_open_20_cnt += 1
            print("gwangju_animal_open_20_cnt", gwangju_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_animal_open_20_cnt += 1
            print("gyeonggi_animal_open_20_cnt", gyeonggi_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_animal_open_20_cnt += 1
            print("gyeongbuk_animal_open_20_cnt", gyeongbuk_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_animal_open_20_cnt += 1
            print("gyeongnam_animal_open_20_cnt", gyeongnam_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_animal_open_20_cnt += 1
            print("incheon_animal_open_20_cnt", incheon_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_animal_open_20_cnt += 1
            print("jeju_animal_open_20_cnt", jeju_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_animal_open_20_cnt += 1
            print("jeonbuk_animal_open_20_cnt", jeonbuk_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_animal_open_20_cnt += 1
            print("jeonnam_animal_open_20_cnt", jeonnam_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_animal_open_20_cnt += 1
            print("sejong_animal_open_20_cnt", sejong_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_animal_open_20_cnt += 1
            print("seoul_animal_open_20_cnt", seoul_animal_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_animal_open_20_cnt += 1
            print("ulsan_animal_open_20_cnt", ulsan_animal_open_20_cnt)

    culture_open_20_cnt = 0
    culture_open_20_tot_cnt = culture_open_20.count_documents({})
    for store in culture_open_20.find({}).batch_size(1):
        culture_open_20_cnt += 1
        print(culture_open_20_cnt, "/", culture_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_culture_open_20_cnt += 1
            print("busan_culture_open_20_cnt", busan_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_culture_open_20_cnt += 1
            print("chungbuk_culture_open_20_cnt", chungbuk_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_culture_open_20_cnt += 1
            print("chungnam_culture_open_20_cnt", chungnam_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_culture_open_20_cnt += 1
            print("daegu_culture_open_20_cnt", daegu_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_culture_open_20_cnt += 1
            print("daejeon_culture_open_20_cnt", daejeon_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_culture_open_20_cnt += 1
            print("gangwon_culture_open_20_cnt", gangwon_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_culture_open_20_cnt += 1
            print("gwangju_culture_open_20_cnt", gwangju_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_culture_open_20_cnt += 1
            print("gyeonggi_culture_open_20_cnt", gyeonggi_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_culture_open_20_cnt += 1
            print("gyeongbuk_culture_open_20_cnt", gyeongbuk_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_culture_open_20_cnt += 1
            print("gyeongnam_culture_open_20_cnt", gyeongnam_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_culture_open_20_cnt += 1
            print("incheon_culture_open_20_cnt", incheon_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_culture_open_20_cnt += 1
            print("jeju_culture_open_20_cnt", jeju_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_culture_open_20_cnt += 1
            print("jeonbuk_culture_open_20_cnt", jeonbuk_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_culture_open_20_cnt += 1
            print("jeonnam_culture_open_20_cnt", jeonnam_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_culture_open_20_cnt += 1
            print("sejong_culture_open_20_cnt", sejong_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_culture_open_20_cnt += 1
            print("seoul_culture_open_20_cnt", seoul_culture_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_culture_open_20_cnt += 1
            print("ulsan_culture_open_20_cnt", ulsan_culture_open_20_cnt)

    environment_open_20_cnt = 0
    environment_open_20_tot_cnt = environment_open_20.count_documents({})
    for store in environment_open_20.find({}).batch_size(1):
        environment_open_20_cnt += 1
        print(environment_open_20_cnt, "/", environment_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_environment_open_20_cnt += 1
            print("busan_environment_open_20_cnt", busan_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_environment_open_20_cnt += 1
            print("chungbuk_environment_open_20_cnt", chungbuk_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_environment_open_20_cnt += 1
            print("chungnam_environment_open_20_cnt", chungnam_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_environment_open_20_cnt += 1
            print("daegu_environment_open_20_cnt", daegu_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_environment_open_20_cnt += 1
            print("daejeon_environment_open_20_cnt", daejeon_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_environment_open_20_cnt += 1
            print("gangwon_environment_open_20_cnt", gangwon_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_environment_open_20_cnt += 1
            print("gwangju_environment_open_20_cnt", gwangju_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_environment_open_20_cnt += 1
            print("gyeonggi_environment_open_20_cnt", gyeonggi_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_environment_open_20_cnt += 1
            print("gyeongbuk_environment_open_20_cnt", gyeongbuk_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_environment_open_20_cnt += 1
            print("gyeongnam_environment_open_20_cnt", gyeongnam_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_environment_open_20_cnt += 1
            print("incheon_environment_open_20_cnt", incheon_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_environment_open_20_cnt += 1
            print("jeju_environment_open_20_cnt", jeju_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_environment_open_20_cnt += 1
            print("jeonbuk_environment_open_20_cnt", jeonbuk_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_environment_open_20_cnt += 1
            print("jeonnam_environment_open_20_cnt", jeonnam_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_environment_open_20_cnt += 1
            print("sejong_environment_open_20_cnt", sejong_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_environment_open_20_cnt += 1
            print("seoul_environment_open_20_cnt", seoul_environment_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_environment_open_20_cnt += 1
            print("ulsan_environment_open_20_cnt", ulsan_environment_open_20_cnt)

    food_open_20_cnt = 0
    food_open_20_tot_cnt = food_open_20.count_documents({})
    for store in food_open_20.find({}).batch_size(1):
        food_open_20_cnt += 1
        print(food_open_20_cnt, "/", food_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_food_open_20_cnt += 1
            print("busan_food_open_20_cnt", busan_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_food_open_20_cnt += 1
            print("chungbuk_food_open_20_cnt", chungbuk_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_food_open_20_cnt += 1
            print("chungnam_food_open_20_cnt", chungnam_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_food_open_20_cnt += 1
            print("daegu_food_open_20_cnt", daegu_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_food_open_20_cnt += 1
            print("daejeon_food_open_20_cnt", daejeon_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_food_open_20_cnt += 1
            print("gangwon_food_open_20_cnt", gangwon_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_food_open_20_cnt += 1
            print("gwangju_food_open_20_cnt", gwangju_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_food_open_20_cnt += 1
            print("gyeonggi_food_open_20_cnt", gyeonggi_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_food_open_20_cnt += 1
            print("gyeongbuk_food_open_20_cnt", gyeongbuk_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_food_open_20_cnt += 1
            print("gyeongnam_food_open_20_cnt", gyeongnam_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_food_open_20_cnt += 1
            print("incheon_food_open_20_cnt", incheon_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_food_open_20_cnt += 1
            print("jeju_food_open_20_cnt", jeju_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_food_open_20_cnt += 1
            print("jeonbuk_food_open_20_cnt", jeonbuk_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_food_open_20_cnt += 1
            print("jeonnam_food_open_20_cnt", jeonnam_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_food_open_20_cnt += 1
            print("sejong_food_open_20_cnt", sejong_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_food_open_20_cnt += 1
            print("seoul_food_open_20_cnt", seoul_food_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_food_open_20_cnt += 1
            print("ulsan_food_open_20_cnt", ulsan_food_open_20_cnt)

    health_open_20_cnt = 0
    health_open_20_tot_cnt = health_open_20.count_documents({})
    for store in health_open_20.find({}).batch_size(1):
        health_open_20_cnt += 1
        print(health_open_20_cnt, "/", health_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_health_open_20_cnt += 1
            print("busan_health_open_20_cnt", busan_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_health_open_20_cnt += 1
            print("chungbuk_health_open_20_cnt", chungbuk_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_health_open_20_cnt += 1
            print("chungnam_health_open_20_cnt", chungnam_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_health_open_20_cnt += 1
            print("daegu_health_open_20_cnt", daegu_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_health_open_20_cnt += 1
            print("daejeon_health_open_20_cnt", daejeon_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_health_open_20_cnt += 1
            print("gangwon_health_open_20_cnt", gangwon_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_health_open_20_cnt += 1
            print("gwangju_health_open_20_cnt", gwangju_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_health_open_20_cnt += 1
            print("gyeonggi_health_open_20_cnt", gyeonggi_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_health_open_20_cnt += 1
            print("gyeongbuk_health_open_20_cnt", gyeongbuk_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_health_open_20_cnt += 1
            print("gyeongnam_health_open_20_cnt", gyeongnam_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_health_open_20_cnt += 1
            print("incheon_health_open_20_cnt", incheon_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_health_open_20_cnt += 1
            print("jeju_health_open_20_cnt", jeju_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_health_open_20_cnt += 1
            print("jeonbuk_health_open_20_cnt", jeonbuk_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_health_open_20_cnt += 1
            print("jeonnam_health_open_20_cnt", jeonnam_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_health_open_20_cnt += 1
            print("sejong_health_open_20_cnt", sejong_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_health_open_20_cnt += 1
            print("seoul_health_open_20_cnt", seoul_health_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_health_open_20_cnt += 1
            print("ulsan_health_open_20_cnt", ulsan_health_open_20_cnt)

    life_open_20_cnt = 0
    life_open_20_tot_cnt = life_open_20.count_documents({})
    for store in life_open_20.find({}).batch_size(1):
        life_open_20_cnt += 1
        print(life_open_20_cnt, "/", life_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_life_open_20_cnt += 1
            print("busan_life_open_20_cnt", busan_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_life_open_20_cnt += 1
            print("chungbuk_life_open_20_cnt", chungbuk_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_life_open_20_cnt += 1
            print("chungnam_life_open_20_cnt", chungnam_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_life_open_20_cnt += 1
            print("daegu_life_open_20_cnt", daegu_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_life_open_20_cnt += 1
            print("daejeon_life_open_20_cnt", daejeon_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_life_open_20_cnt += 1
            print("gangwon_life_open_20_cnt", gangwon_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_life_open_20_cnt += 1
            print("gwangju_life_open_20_cnt", gwangju_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_life_open_20_cnt += 1
            print("gyeonggi_life_open_20_cnt", gyeonggi_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_life_open_20_cnt += 1
            print("gyeongbuk_life_open_20_cnt", gyeongbuk_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_life_open_20_cnt += 1
            print("gyeongnam_life_open_20_cnt", gyeongnam_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_life_open_20_cnt += 1
            print("incheon_life_open_20_cnt", incheon_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_life_open_20_cnt += 1
            print("jeju_life_open_20_cnt", jeju_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_life_open_20_cnt += 1
            print("jeonbuk_life_open_20_cnt", jeonbuk_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_life_open_20_cnt += 1
            print("jeonnam_life_open_20_cnt", jeonnam_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_life_open_20_cnt += 1
            print("sejong_life_open_20_cnt", sejong_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_life_open_20_cnt += 1
            print("seoul_life_open_20_cnt", seoul_life_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_life_open_20_cnt += 1
            print("ulsan_life_open_20_cnt", ulsan_life_open_20_cnt)

    other_open_20_cnt = 0
    other_open_20_tot_cnt = other_open_20.count_documents({})
    for store in other_open_20.find({}).batch_size(1):
        other_open_20_cnt += 1
        print(other_open_20_cnt, "/", other_open_20_tot_cnt)

        if store['address'].split(' ')[0] == "부산광역시":
            busan_other_open_20_cnt += 1
            print("busan_other_open_20_cnt", busan_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청북도":
            chungbuk_other_open_20_cnt += 1
            print("chungbuk_other_open_20_cnt", chungbuk_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "충청남도":
            chungnam_other_open_20_cnt += 1
            print("chungnam_other_open_20_cnt", chungnam_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "대구광역시":
            daegu_other_open_20_cnt += 1
            print("daegu_other_open_20_cnt", daegu_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "대전광역시":
            daejeon_other_open_20_cnt += 1
            print("daejeon_other_open_20_cnt", daejeon_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "강원도":
            gangwon_other_open_20_cnt += 1
            print("gangwon_other_open_20_cnt", gangwon_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "광주광역시":
            gwangju_other_open_20_cnt += 1
            print("gwangju_other_open_20_cnt", gwangju_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "경기도":
            gyeonggi_other_open_20_cnt += 1
            print("gyeonggi_other_open_20_cnt", gyeonggi_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상북도":
            gyeongbuk_other_open_20_cnt += 1
            print("gyeongbuk_other_open_20_cnt", gyeongbuk_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "경상남도":
            gyeongnam_other_open_20_cnt += 1
            print("gyeongnam_other_open_20_cnt", gyeongnam_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "인천광역시":
            incheon_other_open_20_cnt += 1
            print("incheon_other_open_20_cnt", incheon_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            jeju_other_open_20_cnt += 1
            print("jeju_other_open_20_cnt", jeju_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라북도":
            jeonbuk_other_open_20_cnt += 1
            print("jeonbuk_other_open_20_cnt", jeonbuk_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "전라남도":
            jeonnam_other_open_20_cnt += 1
            print("jeonnam_other_open_20_cnt", jeonnam_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            sejong_other_open_20_cnt += 1
            print("sejong_other_open_20_cnt", sejong_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "서울특별시":
            seoul_other_open_20_cnt += 1
            print("seoul_other_open_20_cnt", seoul_other_open_20_cnt)
        elif store['address'].split(' ')[0] == "울산광역시":
            ulsan_other_open_20_cnt += 1
            print("ulsan_other_open_20_cnt", ulsan_other_open_20_cnt)

    my_api = {
        "title": "Location type data",
        "busan": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": busan_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": busan_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": busan_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": busan_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": busan_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": busan_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": busan_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": busan_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": busan_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": busan_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": busan_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": busan_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": busan_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": busan_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": busan_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": busan_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": busan_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": busan_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": busan_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": busan_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": busan_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": busan_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": busan_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": busan_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": busan_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": busan_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": busan_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": busan_other_open_20_cnt
                }
            ],
        },
        "chungbuk": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": chungbuk_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": chungbuk_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": chungbuk_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": chungbuk_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": chungbuk_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": chungbuk_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": chungbuk_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": chungbuk_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": chungbuk_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": chungbuk_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": chungbuk_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": chungbuk_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": chungbuk_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": chungbuk_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": chungbuk_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": chungbuk_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": chungbuk_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": chungbuk_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": chungbuk_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": chungbuk_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": chungbuk_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": chungbuk_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": chungbuk_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": chungbuk_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": chungbuk_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": chungbuk_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": chungbuk_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": chungbuk_other_open_20_cnt
                }
            ],
        },
        "chungnam": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": chungnam_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": chungnam_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": chungnam_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": chungnam_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": chungnam_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": chungnam_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": chungnam_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": chungnam_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": chungnam_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": chungnam_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": chungnam_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": chungnam_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": chungnam_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": chungnam_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": chungnam_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": chungnam_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": chungnam_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": chungnam_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": chungnam_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": chungnam_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": chungnam_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": chungnam_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": chungnam_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": chungnam_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": chungnam_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": chungnam_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": chungnam_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": chungnam_other_open_20_cnt
                }
            ],
        },
        "daegu": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": daegu_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": daegu_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": daegu_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": daegu_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": daegu_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": daegu_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": daegu_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": daegu_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": daegu_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": daegu_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": daegu_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": daegu_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": daegu_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": daegu_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": daegu_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": daegu_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": daegu_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": daegu_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": daegu_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": daegu_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": daegu_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": daegu_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": daegu_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": daegu_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": daegu_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": daegu_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": daegu_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": daegu_other_open_20_cnt
                }
            ],
        },
        "daejeon": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": daejeon_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": daejeon_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": daejeon_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": daejeon_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": daejeon_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": daejeon_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": daejeon_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": daejeon_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": daejeon_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": daejeon_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": daejeon_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": daejeon_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": daejeon_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": daejeon_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": daejeon_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": daejeon_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": daejeon_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": daejeon_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": daejeon_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": daejeon_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": daejeon_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": daejeon_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": daejeon_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": daejeon_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": daejeon_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": daejeon_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": daejeon_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": daejeon_other_open_20_cnt
                }
            ],
        },
        "gangwon": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": gangwon_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": gangwon_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": gangwon_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": gangwon_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": gangwon_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": gangwon_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": gangwon_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": gangwon_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": gangwon_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": gangwon_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": gangwon_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": gangwon_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": gangwon_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": gangwon_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": gangwon_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": gangwon_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": gangwon_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": gangwon_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": gangwon_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": gangwon_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": gangwon_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": gangwon_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": gangwon_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": gangwon_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": gangwon_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": gangwon_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": gangwon_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": gangwon_other_open_20_cnt
                }
            ],
        },
        "gwangju": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": gwangju_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": gwangju_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": gwangju_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": gwangju_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": gwangju_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": gwangju_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": gwangju_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": gwangju_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": gwangju_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": gwangju_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": gwangju_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": gwangju_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": gwangju_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": gwangju_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": gwangju_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": gwangju_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": gwangju_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": gwangju_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": gwangju_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": gwangju_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": gwangju_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": gwangju_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": gwangju_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": gwangju_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": gwangju_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": gwangju_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": gwangju_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": gwangju_other_open_20_cnt
                }
            ],
        },
        "gyeonggi": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": gyeonggi_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeonggi_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeonggi_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeonggi_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeonggi_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeonggi_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeonggi_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": gyeonggi_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeonggi_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeonggi_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeonggi_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeonggi_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeonggi_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeonggi_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": gyeonggi_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeonggi_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeonggi_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeonggi_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeonggi_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeonggi_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeonggi_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": gyeonggi_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeonggi_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeonggi_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeonggi_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeonggi_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeonggi_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeonggi_other_open_20_cnt
                }
            ],
        },
        "gyeongbuk": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": gyeongbuk_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongbuk_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongbuk_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongbuk_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongbuk_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongbuk_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongbuk_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": gyeongbuk_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongbuk_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongbuk_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongbuk_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongbuk_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongbuk_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongbuk_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": gyeongbuk_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongbuk_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongbuk_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongbuk_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongbuk_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongbuk_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongbuk_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": gyeongbuk_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongbuk_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongbuk_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongbuk_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongbuk_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongbuk_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongbuk_other_open_20_cnt
                }
            ],
        },
        "gyeongnam": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": gyeongnam_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongnam_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongnam_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongnam_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongnam_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongnam_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongnam_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": gyeongnam_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongnam_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongnam_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongnam_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongnam_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongnam_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongnam_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": gyeongnam_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongnam_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongnam_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongnam_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongnam_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongnam_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongnam_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": gyeongnam_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": gyeongnam_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": gyeongnam_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": gyeongnam_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": gyeongnam_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": gyeongnam_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": gyeongnam_other_open_20_cnt
                }
            ],
        },
        "incheon": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": incheon_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": incheon_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": incheon_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": incheon_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": incheon_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": incheon_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": incheon_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": incheon_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": incheon_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": incheon_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": incheon_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": incheon_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": incheon_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": incheon_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": incheon_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": incheon_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": incheon_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": incheon_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": incheon_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": incheon_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": incheon_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": incheon_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": incheon_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": incheon_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": incheon_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": incheon_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": incheon_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": incheon_other_open_20_cnt
                }
            ],
        },
        "jeju": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": jeju_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeju_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeju_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeju_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeju_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeju_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeju_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": jeju_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeju_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeju_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeju_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeju_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeju_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeju_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": jeju_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeju_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeju_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeju_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeju_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeju_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeju_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": jeju_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeju_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeju_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeju_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeju_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeju_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeju_other_open_20_cnt
                }
            ],
        },
        "jeonbuk": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": jeonbuk_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeonbuk_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeonbuk_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeonbuk_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeonbuk_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeonbuk_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeonbuk_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": jeonbuk_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeonbuk_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeonbuk_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeonbuk_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeonbuk_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeonbuk_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeonbuk_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": jeonbuk_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeonbuk_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeonbuk_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeonbuk_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeonbuk_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeonbuk_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeonbuk_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": jeonbuk_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeonbuk_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeonbuk_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeonbuk_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeonbuk_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeonbuk_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeonbuk_other_open_20_cnt
                }
            ],
        },
        "jeonnam": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": jeonnam_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeonnam_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeonnam_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeonnam_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeonnam_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeonnam_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeonnam_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": jeonnam_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeonnam_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeonnam_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeonnam_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeonnam_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeonnam_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeonnam_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": jeonnam_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": jeonnam_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": jeonnam_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": jeonnam_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": jeonnam_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": jeonnam_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": jeonnam_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": jeonnam_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": jeonnam_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": jeonnam_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": jeonnam_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": jeonnam_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": jeonnam_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": jeonnam_other_open_20_cnt
                }
            ],
        },
        "sejong": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": sejong_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": sejong_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": sejong_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": sejong_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": sejong_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": sejong_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": sejong_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": sejong_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": sejong_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": sejong_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": sejong_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": sejong_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": sejong_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": sejong_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": sejong_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": sejong_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": sejong_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": sejong_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": sejong_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": sejong_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": sejong_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": sejong_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": sejong_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": sejong_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": sejong_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": sejong_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": sejong_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": sejong_other_open_20_cnt
                }
            ],
        },
        "seoul": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": seoul_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": seoul_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": seoul_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": seoul_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": seoul_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": seoul_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": seoul_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": seoul_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": seoul_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": seoul_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": seoul_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": seoul_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": seoul_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": seoul_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": seoul_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": seoul_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": seoul_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": seoul_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": seoul_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": seoul_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": seoul_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": seoul_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": seoul_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": seoul_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": seoul_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": seoul_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": seoul_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": seoul_other_open_20_cnt
                }
            ],
        },
        "ulsan": {
            "type_close_19": [
                {
                    "type": "동물",
                    "count": ulsan_animal_close_19_cnt
                },
                {
                    "type": "문화",
                    "count": ulsan_culture_close_19_cnt
                },
                {
                    "type": "환경",
                    "count": ulsan_environment_close_19_cnt
                },
                {
                    "type": "식품",
                    "count": ulsan_food_close_19_cnt
                },
                {
                    "type": "건강",
                    "count": ulsan_health_close_19_cnt
                },
                {
                    "type": "생활",
                    "count": ulsan_life_close_19_cnt
                },
                {
                    "type": "기타",
                    "count": ulsan_other_close_19_cnt
                }
            ],
            "type_close_20": [
                {
                    "type": "동물",
                    "count": ulsan_animal_close_20_cnt
                },
                {
                    "type": "문화",
                    "count": ulsan_culture_close_20_cnt
                },
                {
                    "type": "환경",
                    "count": ulsan_environment_close_20_cnt
                },
                {
                    "type": "식품",
                    "count": ulsan_food_close_20_cnt
                },
                {
                    "type": "건강",
                    "count": ulsan_health_close_20_cnt
                },
                {
                    "type": "생활",
                    "count": ulsan_life_close_20_cnt
                },
                {
                    "type": "기타",
                    "count": ulsan_other_close_20_cnt
                }
            ],
            "type_open_19": [
                {
                    "type": "동물",
                    "count": ulsan_animal_open_19_cnt
                },
                {
                    "type": "문화",
                    "count": ulsan_culture_open_19_cnt
                },
                {
                    "type": "환경",
                    "count": ulsan_environment_open_19_cnt
                },
                {
                    "type": "식품",
                    "count": ulsan_food_open_19_cnt
                },
                {
                    "type": "건강",
                    "count": ulsan_health_open_19_cnt
                },
                {
                    "type": "생활",
                    "count": ulsan_life_open_19_cnt
                },
                {
                    "type": "기타",
                    "count": ulsan_other_open_19_cnt
                }
            ],
            "type_open_20": [
                {
                    "type": "동물",
                    "count": ulsan_animal_open_20_cnt
                },
                {
                    "type": "문화",
                    "count": ulsan_culture_open_20_cnt
                },
                {
                    "type": "환경",
                    "count": ulsan_environment_open_20_cnt
                },
                {
                    "type": "식품",
                    "count": ulsan_food_open_20_cnt
                },
                {
                    "type": "건강",
                    "count": ulsan_health_open_20_cnt
                },
                {
                    "type": "생활",
                    "count": ulsan_life_open_20_cnt
                },
                {
                    "type": "기타",
                    "count": ulsan_other_open_20_cnt
                }
            ],
        },
    }

    local_main_api = db['local_data_api']
    print("my_api", my_api)

    my_api_id = local_main_api.insert_one(my_api).inserted_id
    print(my_api_id)


data()