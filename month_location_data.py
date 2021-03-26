from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

theoremLocalDataLocationClose19 = client['theoremLocalDataLocationClose19']
theoremLocalDataLocationClose20 = client['theoremLocalDataLocationClose20']
theoremLocalDataLocationOpen19 = client['theoremLocalDataLocationOpen19']
theoremLocalDataLocationOpen20 = client['theoremLocalDataLocationOpen20']


def data():
    # 19년 지역별 close
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

    # 19년 지역별 open
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

    # 20년 지역별 close
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

    # 20년 지역별 open
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

    # ------------------------
    # 부산 close 19 cnt
    busan_jan_close_cnt_19 = 0
    busan_feb_close_cnt_19 = 0
    busan_mar_close_cnt_19 = 0
    busan_apr_close_cnt_19 = 0
    busan_may_close_cnt_19 = 0
    busan_jun_close_cnt_19 = 0
    busan_jul_close_cnt_19 = 0
    busan_aug_close_cnt_19 = 0
    busan_sep_close_cnt_19 = 0
    busan_oct_close_cnt_19 = 0
    busan_nov_close_cnt_19 = 0
    busan_dec_close_cnt_19 = 0

    # 충북 close 19 cnt
    chungbuk_jan_close_cnt_19 = 0
    chungbuk_feb_close_cnt_19 = 0
    chungbuk_mar_close_cnt_19 = 0
    chungbuk_apr_close_cnt_19 = 0
    chungbuk_may_close_cnt_19 = 0
    chungbuk_jun_close_cnt_19 = 0
    chungbuk_jul_close_cnt_19 = 0
    chungbuk_aug_close_cnt_19 = 0
    chungbuk_sep_close_cnt_19 = 0
    chungbuk_oct_close_cnt_19 = 0
    chungbuk_nov_close_cnt_19 = 0
    chungbuk_dec_close_cnt_19 = 0

    # 충남 close 19 cnt
    chungnam_jan_close_cnt_19 = 0
    chungnam_feb_close_cnt_19 = 0
    chungnam_mar_close_cnt_19 = 0
    chungnam_apr_close_cnt_19 = 0
    chungnam_may_close_cnt_19 = 0
    chungnam_jun_close_cnt_19 = 0
    chungnam_jul_close_cnt_19 = 0
    chungnam_aug_close_cnt_19 = 0
    chungnam_sep_close_cnt_19 = 0
    chungnam_oct_close_cnt_19 = 0
    chungnam_nov_close_cnt_19 = 0
    chungnam_dec_close_cnt_19 = 0

    # 대구 close 19 cnt
    daegu_jan_close_cnt_19 = 0
    daegu_feb_close_cnt_19 = 0
    daegu_mar_close_cnt_19 = 0
    daegu_apr_close_cnt_19 = 0
    daegu_may_close_cnt_19 = 0
    daegu_jun_close_cnt_19 = 0
    daegu_jul_close_cnt_19 = 0
    daegu_aug_close_cnt_19 = 0
    daegu_sep_close_cnt_19 = 0
    daegu_oct_close_cnt_19 = 0
    daegu_nov_close_cnt_19 = 0
    daegu_dec_close_cnt_19 = 0

    # 대전 close 19 cnt
    daejeon_jan_close_cnt_19 = 0
    daejeon_feb_close_cnt_19 = 0
    daejeon_mar_close_cnt_19 = 0
    daejeon_apr_close_cnt_19 = 0
    daejeon_may_close_cnt_19 = 0
    daejeon_jun_close_cnt_19 = 0
    daejeon_jul_close_cnt_19 = 0
    daejeon_aug_close_cnt_19 = 0
    daejeon_sep_close_cnt_19 = 0
    daejeon_oct_close_cnt_19 = 0
    daejeon_nov_close_cnt_19 = 0
    daejeon_dec_close_cnt_19 = 0

    # 강원 close 19 cnt
    gangwon_jan_close_cnt_19 = 0
    gangwon_feb_close_cnt_19 = 0
    gangwon_mar_close_cnt_19 = 0
    gangwon_apr_close_cnt_19 = 0
    gangwon_may_close_cnt_19 = 0
    gangwon_jun_close_cnt_19 = 0
    gangwon_jul_close_cnt_19 = 0
    gangwon_aug_close_cnt_19 = 0
    gangwon_sep_close_cnt_19 = 0
    gangwon_oct_close_cnt_19 = 0
    gangwon_nov_close_cnt_19 = 0
    gangwon_dec_close_cnt_19 = 0

    # 광주 close 19 cnt
    gwangju_jan_close_cnt_19 = 0
    gwangju_feb_close_cnt_19 = 0
    gwangju_mar_close_cnt_19 = 0
    gwangju_apr_close_cnt_19 = 0
    gwangju_may_close_cnt_19 = 0
    gwangju_jun_close_cnt_19 = 0
    gwangju_jul_close_cnt_19 = 0
    gwangju_aug_close_cnt_19 = 0
    gwangju_sep_close_cnt_19 = 0
    gwangju_oct_close_cnt_19 = 0
    gwangju_nov_close_cnt_19 = 0
    gwangju_dec_close_cnt_19 = 0

    # 경기 close 19 cnt
    gyeonggi_jan_close_cnt_19 = 0
    gyeonggi_feb_close_cnt_19 = 0
    gyeonggi_mar_close_cnt_19 = 0
    gyeonggi_apr_close_cnt_19 = 0
    gyeonggi_may_close_cnt_19 = 0
    gyeonggi_jun_close_cnt_19 = 0
    gyeonggi_jul_close_cnt_19 = 0
    gyeonggi_aug_close_cnt_19 = 0
    gyeonggi_sep_close_cnt_19 = 0
    gyeonggi_oct_close_cnt_19 = 0
    gyeonggi_nov_close_cnt_19 = 0
    gyeonggi_dec_close_cnt_19 = 0

    # 경북 close 19 cnt
    gyeongbuk_jan_close_cnt_19 = 0
    gyeongbuk_feb_close_cnt_19 = 0
    gyeongbuk_mar_close_cnt_19 = 0
    gyeongbuk_apr_close_cnt_19 = 0
    gyeongbuk_may_close_cnt_19 = 0
    gyeongbuk_jun_close_cnt_19 = 0
    gyeongbuk_jul_close_cnt_19 = 0
    gyeongbuk_aug_close_cnt_19 = 0
    gyeongbuk_sep_close_cnt_19 = 0
    gyeongbuk_oct_close_cnt_19 = 0
    gyeongbuk_nov_close_cnt_19 = 0
    gyeongbuk_dec_close_cnt_19 = 0

    # 경남 close 19 cnt
    gyeongnam_jan_close_cnt_19 = 0
    gyeongnam_feb_close_cnt_19 = 0
    gyeongnam_mar_close_cnt_19 = 0
    gyeongnam_apr_close_cnt_19 = 0
    gyeongnam_may_close_cnt_19 = 0
    gyeongnam_jun_close_cnt_19 = 0
    gyeongnam_jul_close_cnt_19 = 0
    gyeongnam_aug_close_cnt_19 = 0
    gyeongnam_sep_close_cnt_19 = 0
    gyeongnam_oct_close_cnt_19 = 0
    gyeongnam_nov_close_cnt_19 = 0
    gyeongnam_dec_close_cnt_19 = 0

    # 인천 close 19 cnt
    incheon_jan_close_cnt_19 = 0
    incheon_feb_close_cnt_19 = 0
    incheon_mar_close_cnt_19 = 0
    incheon_apr_close_cnt_19 = 0
    incheon_may_close_cnt_19 = 0
    incheon_jun_close_cnt_19 = 0
    incheon_jul_close_cnt_19 = 0
    incheon_aug_close_cnt_19 = 0
    incheon_sep_close_cnt_19 = 0
    incheon_oct_close_cnt_19 = 0
    incheon_nov_close_cnt_19 = 0
    incheon_dec_close_cnt_19 = 0

    # 제주 close 19 cnt
    jeju_jan_close_cnt_19 = 0
    jeju_feb_close_cnt_19 = 0
    jeju_mar_close_cnt_19 = 0
    jeju_apr_close_cnt_19 = 0
    jeju_may_close_cnt_19 = 0
    jeju_jun_close_cnt_19 = 0
    jeju_jul_close_cnt_19 = 0
    jeju_aug_close_cnt_19 = 0
    jeju_sep_close_cnt_19 = 0
    jeju_oct_close_cnt_19 = 0
    jeju_nov_close_cnt_19 = 0
    jeju_dec_close_cnt_19 = 0

    # 전북 close 19 cnt
    jeonbuk_jan_close_cnt_19 = 0
    jeonbuk_feb_close_cnt_19 = 0
    jeonbuk_mar_close_cnt_19 = 0
    jeonbuk_apr_close_cnt_19 = 0
    jeonbuk_may_close_cnt_19 = 0
    jeonbuk_jun_close_cnt_19 = 0
    jeonbuk_jul_close_cnt_19 = 0
    jeonbuk_aug_close_cnt_19 = 0
    jeonbuk_sep_close_cnt_19 = 0
    jeonbuk_oct_close_cnt_19 = 0
    jeonbuk_nov_close_cnt_19 = 0
    jeonbuk_dec_close_cnt_19 = 0

    # 전남 close 19 cnt
    jeonnam_jan_close_cnt_19 = 0
    jeonnam_feb_close_cnt_19 = 0
    jeonnam_mar_close_cnt_19 = 0
    jeonnam_apr_close_cnt_19 = 0
    jeonnam_may_close_cnt_19 = 0
    jeonnam_jun_close_cnt_19 = 0
    jeonnam_jul_close_cnt_19 = 0
    jeonnam_aug_close_cnt_19 = 0
    jeonnam_sep_close_cnt_19 = 0
    jeonnam_oct_close_cnt_19 = 0
    jeonnam_nov_close_cnt_19 = 0
    jeonnam_dec_close_cnt_19 = 0

    # 세종 close 19 cnt
    sejong_jan_close_cnt_19 = 0
    sejong_feb_close_cnt_19 = 0
    sejong_mar_close_cnt_19 = 0
    sejong_apr_close_cnt_19 = 0
    sejong_may_close_cnt_19 = 0
    sejong_jun_close_cnt_19 = 0
    sejong_jul_close_cnt_19 = 0
    sejong_aug_close_cnt_19 = 0
    sejong_sep_close_cnt_19 = 0
    sejong_oct_close_cnt_19 = 0
    sejong_nov_close_cnt_19 = 0
    sejong_dec_close_cnt_19 = 0

    # 서울 close 19 cnt
    seoul_jan_close_cnt_19 = 0
    seoul_feb_close_cnt_19 = 0
    seoul_mar_close_cnt_19 = 0
    seoul_apr_close_cnt_19 = 0
    seoul_may_close_cnt_19 = 0
    seoul_jun_close_cnt_19 = 0
    seoul_jul_close_cnt_19 = 0
    seoul_aug_close_cnt_19 = 0
    seoul_sep_close_cnt_19 = 0
    seoul_oct_close_cnt_19 = 0
    seoul_nov_close_cnt_19 = 0
    seoul_dec_close_cnt_19 = 0

    # 울산 close 19 cnt
    ulsan_jan_close_cnt_19 = 0
    ulsan_feb_close_cnt_19 = 0
    ulsan_mar_close_cnt_19 = 0
    ulsan_apr_close_cnt_19 = 0
    ulsan_may_close_cnt_19 = 0
    ulsan_jun_close_cnt_19 = 0
    ulsan_jul_close_cnt_19 = 0
    ulsan_aug_close_cnt_19 = 0
    ulsan_sep_close_cnt_19 = 0
    ulsan_oct_close_cnt_19 = 0
    ulsan_nov_close_cnt_19 = 0
    ulsan_dec_close_cnt_19 = 0

    # ------------------------
    # 부산 close 20 cnt
    busan_jan_close_cnt_20 = 0
    busan_feb_close_cnt_20 = 0
    busan_mar_close_cnt_20 = 0
    busan_apr_close_cnt_20 = 0
    busan_may_close_cnt_20 = 0
    busan_jun_close_cnt_20 = 0
    busan_jul_close_cnt_20 = 0
    busan_aug_close_cnt_20 = 0
    busan_sep_close_cnt_20 = 0
    busan_oct_close_cnt_20 = 0
    busan_nov_close_cnt_20 = 0
    busan_dec_close_cnt_20 = 0

    # 충북 close 20 cnt
    chungbuk_jan_close_cnt_20 = 0
    chungbuk_feb_close_cnt_20 = 0
    chungbuk_mar_close_cnt_20 = 0
    chungbuk_apr_close_cnt_20 = 0
    chungbuk_may_close_cnt_20 = 0
    chungbuk_jun_close_cnt_20 = 0
    chungbuk_jul_close_cnt_20 = 0
    chungbuk_aug_close_cnt_20 = 0
    chungbuk_sep_close_cnt_20 = 0
    chungbuk_oct_close_cnt_20 = 0
    chungbuk_nov_close_cnt_20 = 0
    chungbuk_dec_close_cnt_20 = 0

    # 충남 close 20 cnt
    chungnam_jan_close_cnt_20 = 0
    chungnam_feb_close_cnt_20 = 0
    chungnam_mar_close_cnt_20 = 0
    chungnam_apr_close_cnt_20 = 0
    chungnam_may_close_cnt_20 = 0
    chungnam_jun_close_cnt_20 = 0
    chungnam_jul_close_cnt_20 = 0
    chungnam_aug_close_cnt_20 = 0
    chungnam_sep_close_cnt_20 = 0
    chungnam_oct_close_cnt_20 = 0
    chungnam_nov_close_cnt_20 = 0
    chungnam_dec_close_cnt_20 = 0

    # 대구 close 20 cnt
    daegu_jan_close_cnt_20 = 0
    daegu_feb_close_cnt_20 = 0
    daegu_mar_close_cnt_20 = 0
    daegu_apr_close_cnt_20 = 0
    daegu_may_close_cnt_20 = 0
    daegu_jun_close_cnt_20 = 0
    daegu_jul_close_cnt_20 = 0
    daegu_aug_close_cnt_20 = 0
    daegu_sep_close_cnt_20 = 0
    daegu_oct_close_cnt_20 = 0
    daegu_nov_close_cnt_20 = 0
    daegu_dec_close_cnt_20 = 0

    # 대전 close 20 cnt
    daejeon_jan_close_cnt_20 = 0
    daejeon_feb_close_cnt_20 = 0
    daejeon_mar_close_cnt_20 = 0
    daejeon_apr_close_cnt_20 = 0
    daejeon_may_close_cnt_20 = 0
    daejeon_jun_close_cnt_20 = 0
    daejeon_jul_close_cnt_20 = 0
    daejeon_aug_close_cnt_20 = 0
    daejeon_sep_close_cnt_20 = 0
    daejeon_oct_close_cnt_20 = 0
    daejeon_nov_close_cnt_20 = 0
    daejeon_dec_close_cnt_20 = 0

    # 강원 close 20 cnt
    gangwon_jan_close_cnt_20 = 0
    gangwon_feb_close_cnt_20 = 0
    gangwon_mar_close_cnt_20 = 0
    gangwon_apr_close_cnt_20 = 0
    gangwon_may_close_cnt_20 = 0
    gangwon_jun_close_cnt_20 = 0
    gangwon_jul_close_cnt_20 = 0
    gangwon_aug_close_cnt_20 = 0
    gangwon_sep_close_cnt_20 = 0
    gangwon_oct_close_cnt_20 = 0
    gangwon_nov_close_cnt_20 = 0
    gangwon_dec_close_cnt_20 = 0

    # 광주 close 20 cnt
    gwangju_jan_close_cnt_20 = 0
    gwangju_feb_close_cnt_20 = 0
    gwangju_mar_close_cnt_20 = 0
    gwangju_apr_close_cnt_20 = 0
    gwangju_may_close_cnt_20 = 0
    gwangju_jun_close_cnt_20 = 0
    gwangju_jul_close_cnt_20 = 0
    gwangju_aug_close_cnt_20 = 0
    gwangju_sep_close_cnt_20 = 0
    gwangju_oct_close_cnt_20 = 0
    gwangju_nov_close_cnt_20 = 0
    gwangju_dec_close_cnt_20 = 0

    # 경기 close 20 cnt
    gyeonggi_jan_close_cnt_20 = 0
    gyeonggi_feb_close_cnt_20 = 0
    gyeonggi_mar_close_cnt_20 = 0
    gyeonggi_apr_close_cnt_20 = 0
    gyeonggi_may_close_cnt_20 = 0
    gyeonggi_jun_close_cnt_20 = 0
    gyeonggi_jul_close_cnt_20 = 0
    gyeonggi_aug_close_cnt_20 = 0
    gyeonggi_sep_close_cnt_20 = 0
    gyeonggi_oct_close_cnt_20 = 0
    gyeonggi_nov_close_cnt_20 = 0
    gyeonggi_dec_close_cnt_20 = 0

    # 경북 close 20 cnt
    gyeongbuk_jan_close_cnt_20 = 0
    gyeongbuk_feb_close_cnt_20 = 0
    gyeongbuk_mar_close_cnt_20 = 0
    gyeongbuk_apr_close_cnt_20 = 0
    gyeongbuk_may_close_cnt_20 = 0
    gyeongbuk_jun_close_cnt_20 = 0
    gyeongbuk_jul_close_cnt_20 = 0
    gyeongbuk_aug_close_cnt_20 = 0
    gyeongbuk_sep_close_cnt_20 = 0
    gyeongbuk_oct_close_cnt_20 = 0
    gyeongbuk_nov_close_cnt_20 = 0
    gyeongbuk_dec_close_cnt_20 = 0

    # 경남 close 20 cnt
    gyeongnam_jan_close_cnt_20 = 0
    gyeongnam_feb_close_cnt_20 = 0
    gyeongnam_mar_close_cnt_20 = 0
    gyeongnam_apr_close_cnt_20 = 0
    gyeongnam_may_close_cnt_20 = 0
    gyeongnam_jun_close_cnt_20 = 0
    gyeongnam_jul_close_cnt_20 = 0
    gyeongnam_aug_close_cnt_20 = 0
    gyeongnam_sep_close_cnt_20 = 0
    gyeongnam_oct_close_cnt_20 = 0
    gyeongnam_nov_close_cnt_20 = 0
    gyeongnam_dec_close_cnt_20 = 0

    # 인천 close 20 cnt
    incheon_jan_close_cnt_20 = 0
    incheon_feb_close_cnt_20 = 0
    incheon_mar_close_cnt_20 = 0
    incheon_apr_close_cnt_20 = 0
    incheon_may_close_cnt_20 = 0
    incheon_jun_close_cnt_20 = 0
    incheon_jul_close_cnt_20 = 0
    incheon_aug_close_cnt_20 = 0
    incheon_sep_close_cnt_20 = 0
    incheon_oct_close_cnt_20 = 0
    incheon_nov_close_cnt_20 = 0
    incheon_dec_close_cnt_20 = 0

    # 제주 close 20 cnt
    jeju_jan_close_cnt_20 = 0
    jeju_feb_close_cnt_20 = 0
    jeju_mar_close_cnt_20 = 0
    jeju_apr_close_cnt_20 = 0
    jeju_may_close_cnt_20 = 0
    jeju_jun_close_cnt_20 = 0
    jeju_jul_close_cnt_20 = 0
    jeju_aug_close_cnt_20 = 0
    jeju_sep_close_cnt_20 = 0
    jeju_oct_close_cnt_20 = 0
    jeju_nov_close_cnt_20 = 0
    jeju_dec_close_cnt_20 = 0

    # 전북 close 20 cnt
    jeonbuk_jan_close_cnt_20 = 0
    jeonbuk_feb_close_cnt_20 = 0
    jeonbuk_mar_close_cnt_20 = 0
    jeonbuk_apr_close_cnt_20 = 0
    jeonbuk_may_close_cnt_20 = 0
    jeonbuk_jun_close_cnt_20 = 0
    jeonbuk_jul_close_cnt_20 = 0
    jeonbuk_aug_close_cnt_20 = 0
    jeonbuk_sep_close_cnt_20 = 0
    jeonbuk_oct_close_cnt_20 = 0
    jeonbuk_nov_close_cnt_20 = 0
    jeonbuk_dec_close_cnt_20 = 0

    # 전남 close 20 cnt
    jeonnam_jan_close_cnt_20 = 0
    jeonnam_feb_close_cnt_20 = 0
    jeonnam_mar_close_cnt_20 = 0
    jeonnam_apr_close_cnt_20 = 0
    jeonnam_may_close_cnt_20 = 0
    jeonnam_jun_close_cnt_20 = 0
    jeonnam_jul_close_cnt_20 = 0
    jeonnam_aug_close_cnt_20 = 0
    jeonnam_sep_close_cnt_20 = 0
    jeonnam_oct_close_cnt_20 = 0
    jeonnam_nov_close_cnt_20 = 0
    jeonnam_dec_close_cnt_20 = 0

    # 세종 close 20 cnt
    sejong_jan_close_cnt_20 = 0
    sejong_feb_close_cnt_20 = 0
    sejong_mar_close_cnt_20 = 0
    sejong_apr_close_cnt_20 = 0
    sejong_may_close_cnt_20 = 0
    sejong_jun_close_cnt_20 = 0
    sejong_jul_close_cnt_20 = 0
    sejong_aug_close_cnt_20 = 0
    sejong_sep_close_cnt_20 = 0
    sejong_oct_close_cnt_20 = 0
    sejong_nov_close_cnt_20 = 0
    sejong_dec_close_cnt_20 = 0

    # 서울 close 20 cnt
    seoul_jan_close_cnt_20 = 0
    seoul_feb_close_cnt_20 = 0
    seoul_mar_close_cnt_20 = 0
    seoul_apr_close_cnt_20 = 0
    seoul_may_close_cnt_20 = 0
    seoul_jun_close_cnt_20 = 0
    seoul_jul_close_cnt_20 = 0
    seoul_aug_close_cnt_20 = 0
    seoul_sep_close_cnt_20 = 0
    seoul_oct_close_cnt_20 = 0
    seoul_nov_close_cnt_20 = 0
    seoul_dec_close_cnt_20 = 0

    # 울산 close 20 cnt
    ulsan_jan_close_cnt_20 = 0
    ulsan_feb_close_cnt_20 = 0
    ulsan_mar_close_cnt_20 = 0
    ulsan_apr_close_cnt_20 = 0
    ulsan_may_close_cnt_20 = 0
    ulsan_jun_close_cnt_20 = 0
    ulsan_jul_close_cnt_20 = 0
    ulsan_aug_close_cnt_20 = 0
    ulsan_sep_close_cnt_20 = 0
    ulsan_oct_close_cnt_20 = 0
    ulsan_nov_close_cnt_20 = 0
    ulsan_dec_close_cnt_20 = 0

    # ------------------------
    # 부산 open 19 cnt
    busan_jan_open_cnt_19 = 0
    busan_feb_open_cnt_19 = 0
    busan_mar_open_cnt_19 = 0
    busan_apr_open_cnt_19 = 0
    busan_may_open_cnt_19 = 0
    busan_jun_open_cnt_19 = 0
    busan_jul_open_cnt_19 = 0
    busan_aug_open_cnt_19 = 0
    busan_sep_open_cnt_19 = 0
    busan_oct_open_cnt_19 = 0
    busan_nov_open_cnt_19 = 0
    busan_dec_open_cnt_19 = 0

    # 충북 open 19 cnt
    chungbuk_jan_open_cnt_19 = 0
    chungbuk_feb_open_cnt_19 = 0
    chungbuk_mar_open_cnt_19 = 0
    chungbuk_apr_open_cnt_19 = 0
    chungbuk_may_open_cnt_19 = 0
    chungbuk_jun_open_cnt_19 = 0
    chungbuk_jul_open_cnt_19 = 0
    chungbuk_aug_open_cnt_19 = 0
    chungbuk_sep_open_cnt_19 = 0
    chungbuk_oct_open_cnt_19 = 0
    chungbuk_nov_open_cnt_19 = 0
    chungbuk_dec_open_cnt_19 = 0

    # 충남 open 19 cnt
    chungnam_jan_open_cnt_19 = 0
    chungnam_feb_open_cnt_19 = 0
    chungnam_mar_open_cnt_19 = 0
    chungnam_apr_open_cnt_19 = 0
    chungnam_may_open_cnt_19 = 0
    chungnam_jun_open_cnt_19 = 0
    chungnam_jul_open_cnt_19 = 0
    chungnam_aug_open_cnt_19 = 0
    chungnam_sep_open_cnt_19 = 0
    chungnam_oct_open_cnt_19 = 0
    chungnam_nov_open_cnt_19 = 0
    chungnam_dec_open_cnt_19 = 0

    # 대구 open 19 cnt
    daegu_jan_open_cnt_19 = 0
    daegu_feb_open_cnt_19 = 0
    daegu_mar_open_cnt_19 = 0
    daegu_apr_open_cnt_19 = 0
    daegu_may_open_cnt_19 = 0
    daegu_jun_open_cnt_19 = 0
    daegu_jul_open_cnt_19 = 0
    daegu_aug_open_cnt_19 = 0
    daegu_sep_open_cnt_19 = 0
    daegu_oct_open_cnt_19 = 0
    daegu_nov_open_cnt_19 = 0
    daegu_dec_open_cnt_19 = 0

    # 대전 open 19 cnt
    daejeon_jan_open_cnt_19 = 0
    daejeon_feb_open_cnt_19 = 0
    daejeon_mar_open_cnt_19 = 0
    daejeon_apr_open_cnt_19 = 0
    daejeon_may_open_cnt_19 = 0
    daejeon_jun_open_cnt_19 = 0
    daejeon_jul_open_cnt_19 = 0
    daejeon_aug_open_cnt_19 = 0
    daejeon_sep_open_cnt_19 = 0
    daejeon_oct_open_cnt_19 = 0
    daejeon_nov_open_cnt_19 = 0
    daejeon_dec_open_cnt_19 = 0

    # 강원 open 19 cnt
    gangwon_jan_open_cnt_19 = 0
    gangwon_feb_open_cnt_19 = 0
    gangwon_mar_open_cnt_19 = 0
    gangwon_apr_open_cnt_19 = 0
    gangwon_may_open_cnt_19 = 0
    gangwon_jun_open_cnt_19 = 0
    gangwon_jul_open_cnt_19 = 0
    gangwon_aug_open_cnt_19 = 0
    gangwon_sep_open_cnt_19 = 0
    gangwon_oct_open_cnt_19 = 0
    gangwon_nov_open_cnt_19 = 0
    gangwon_dec_open_cnt_19 = 0

    # 광주 open 19 cnt
    gwangju_jan_open_cnt_19 = 0
    gwangju_feb_open_cnt_19 = 0
    gwangju_mar_open_cnt_19 = 0
    gwangju_apr_open_cnt_19 = 0
    gwangju_may_open_cnt_19 = 0
    gwangju_jun_open_cnt_19 = 0
    gwangju_jul_open_cnt_19 = 0
    gwangju_aug_open_cnt_19 = 0
    gwangju_sep_open_cnt_19 = 0
    gwangju_oct_open_cnt_19 = 0
    gwangju_nov_open_cnt_19 = 0
    gwangju_dec_open_cnt_19 = 0

    # 경기 open 19 cnt
    gyeonggi_jan_open_cnt_19 = 0
    gyeonggi_feb_open_cnt_19 = 0
    gyeonggi_mar_open_cnt_19 = 0
    gyeonggi_apr_open_cnt_19 = 0
    gyeonggi_may_open_cnt_19 = 0
    gyeonggi_jun_open_cnt_19 = 0
    gyeonggi_jul_open_cnt_19 = 0
    gyeonggi_aug_open_cnt_19 = 0
    gyeonggi_sep_open_cnt_19 = 0
    gyeonggi_oct_open_cnt_19 = 0
    gyeonggi_nov_open_cnt_19 = 0
    gyeonggi_dec_open_cnt_19 = 0

    # 경북 open 19 cnt
    gyeongbuk_jan_open_cnt_19 = 0
    gyeongbuk_feb_open_cnt_19 = 0
    gyeongbuk_mar_open_cnt_19 = 0
    gyeongbuk_apr_open_cnt_19 = 0
    gyeongbuk_may_open_cnt_19 = 0
    gyeongbuk_jun_open_cnt_19 = 0
    gyeongbuk_jul_open_cnt_19 = 0
    gyeongbuk_aug_open_cnt_19 = 0
    gyeongbuk_sep_open_cnt_19 = 0
    gyeongbuk_oct_open_cnt_19 = 0
    gyeongbuk_nov_open_cnt_19 = 0
    gyeongbuk_dec_open_cnt_19 = 0

    # 경남 open 19 cnt
    gyeongnam_jan_open_cnt_19 = 0
    gyeongnam_feb_open_cnt_19 = 0
    gyeongnam_mar_open_cnt_19 = 0
    gyeongnam_apr_open_cnt_19 = 0
    gyeongnam_may_open_cnt_19 = 0
    gyeongnam_jun_open_cnt_19 = 0
    gyeongnam_jul_open_cnt_19 = 0
    gyeongnam_aug_open_cnt_19 = 0
    gyeongnam_sep_open_cnt_19 = 0
    gyeongnam_oct_open_cnt_19 = 0
    gyeongnam_nov_open_cnt_19 = 0
    gyeongnam_dec_open_cnt_19 = 0

    # 인천 open 19 cnt
    incheon_jan_open_cnt_19 = 0
    incheon_feb_open_cnt_19 = 0
    incheon_mar_open_cnt_19 = 0
    incheon_apr_open_cnt_19 = 0
    incheon_may_open_cnt_19 = 0
    incheon_jun_open_cnt_19 = 0
    incheon_jul_open_cnt_19 = 0
    incheon_aug_open_cnt_19 = 0
    incheon_sep_open_cnt_19 = 0
    incheon_oct_open_cnt_19 = 0
    incheon_nov_open_cnt_19 = 0
    incheon_dec_open_cnt_19 = 0

    # 제주 open 19 cnt
    jeju_jan_open_cnt_19 = 0
    jeju_feb_open_cnt_19 = 0
    jeju_mar_open_cnt_19 = 0
    jeju_apr_open_cnt_19 = 0
    jeju_may_open_cnt_19 = 0
    jeju_jun_open_cnt_19 = 0
    jeju_jul_open_cnt_19 = 0
    jeju_aug_open_cnt_19 = 0
    jeju_sep_open_cnt_19 = 0
    jeju_oct_open_cnt_19 = 0
    jeju_nov_open_cnt_19 = 0
    jeju_dec_open_cnt_19 = 0

    # 전북 open 19 cnt
    jeonbuk_jan_open_cnt_19 = 0
    jeonbuk_feb_open_cnt_19 = 0
    jeonbuk_mar_open_cnt_19 = 0
    jeonbuk_apr_open_cnt_19 = 0
    jeonbuk_may_open_cnt_19 = 0
    jeonbuk_jun_open_cnt_19 = 0
    jeonbuk_jul_open_cnt_19 = 0
    jeonbuk_aug_open_cnt_19 = 0
    jeonbuk_sep_open_cnt_19 = 0
    jeonbuk_oct_open_cnt_19 = 0
    jeonbuk_nov_open_cnt_19 = 0
    jeonbuk_dec_open_cnt_19 = 0

    # 전남 open 19 cnt
    jeonnam_jan_open_cnt_19 = 0
    jeonnam_feb_open_cnt_19 = 0
    jeonnam_mar_open_cnt_19 = 0
    jeonnam_apr_open_cnt_19 = 0
    jeonnam_may_open_cnt_19 = 0
    jeonnam_jun_open_cnt_19 = 0
    jeonnam_jul_open_cnt_19 = 0
    jeonnam_aug_open_cnt_19 = 0
    jeonnam_sep_open_cnt_19 = 0
    jeonnam_oct_open_cnt_19 = 0
    jeonnam_nov_open_cnt_19 = 0
    jeonnam_dec_open_cnt_19 = 0

    # 세종 open 19 cnt
    sejong_jan_open_cnt_19 = 0
    sejong_feb_open_cnt_19 = 0
    sejong_mar_open_cnt_19 = 0
    sejong_apr_open_cnt_19 = 0
    sejong_may_open_cnt_19 = 0
    sejong_jun_open_cnt_19 = 0
    sejong_jul_open_cnt_19 = 0
    sejong_aug_open_cnt_19 = 0
    sejong_sep_open_cnt_19 = 0
    sejong_oct_open_cnt_19 = 0
    sejong_nov_open_cnt_19 = 0
    sejong_dec_open_cnt_19 = 0

    # 서울 open 19 cnt
    seoul_jan_open_cnt_19 = 0
    seoul_feb_open_cnt_19 = 0
    seoul_mar_open_cnt_19 = 0
    seoul_apr_open_cnt_19 = 0
    seoul_may_open_cnt_19 = 0
    seoul_jun_open_cnt_19 = 0
    seoul_jul_open_cnt_19 = 0
    seoul_aug_open_cnt_19 = 0
    seoul_sep_open_cnt_19 = 0
    seoul_oct_open_cnt_19 = 0
    seoul_nov_open_cnt_19 = 0
    seoul_dec_open_cnt_19 = 0

    # 울산 open 19 cnt
    ulsan_jan_open_cnt_19 = 0
    ulsan_feb_open_cnt_19 = 0
    ulsan_mar_open_cnt_19 = 0
    ulsan_apr_open_cnt_19 = 0
    ulsan_may_open_cnt_19 = 0
    ulsan_jun_open_cnt_19 = 0
    ulsan_jul_open_cnt_19 = 0
    ulsan_aug_open_cnt_19 = 0
    ulsan_sep_open_cnt_19 = 0
    ulsan_oct_open_cnt_19 = 0
    ulsan_nov_open_cnt_19 = 0
    ulsan_dec_open_cnt_19 = 0

    # ------------------------
    # 부산 open 20 cnt
    busan_jan_open_cnt_20 = 0
    busan_feb_open_cnt_20 = 0
    busan_mar_open_cnt_20 = 0
    busan_apr_open_cnt_20 = 0
    busan_may_open_cnt_20 = 0
    busan_jun_open_cnt_20 = 0
    busan_jul_open_cnt_20 = 0
    busan_aug_open_cnt_20 = 0
    busan_sep_open_cnt_20 = 0
    busan_oct_open_cnt_20 = 0
    busan_nov_open_cnt_20 = 0
    busan_dec_open_cnt_20 = 0

    # 충북 open 20 cnt
    chungbuk_jan_open_cnt_20 = 0
    chungbuk_feb_open_cnt_20 = 0
    chungbuk_mar_open_cnt_20 = 0
    chungbuk_apr_open_cnt_20 = 0
    chungbuk_may_open_cnt_20 = 0
    chungbuk_jun_open_cnt_20 = 0
    chungbuk_jul_open_cnt_20 = 0
    chungbuk_aug_open_cnt_20 = 0
    chungbuk_sep_open_cnt_20 = 0
    chungbuk_oct_open_cnt_20 = 0
    chungbuk_nov_open_cnt_20 = 0
    chungbuk_dec_open_cnt_20 = 0

    # 충남 open 20 cnt
    chungnam_jan_open_cnt_20 = 0
    chungnam_feb_open_cnt_20 = 0
    chungnam_mar_open_cnt_20 = 0
    chungnam_apr_open_cnt_20 = 0
    chungnam_may_open_cnt_20 = 0
    chungnam_jun_open_cnt_20 = 0
    chungnam_jul_open_cnt_20 = 0
    chungnam_aug_open_cnt_20 = 0
    chungnam_sep_open_cnt_20 = 0
    chungnam_oct_open_cnt_20 = 0
    chungnam_nov_open_cnt_20 = 0
    chungnam_dec_open_cnt_20 = 0

    # 대구 open 20 cnt
    daegu_jan_open_cnt_20 = 0
    daegu_feb_open_cnt_20 = 0
    daegu_mar_open_cnt_20 = 0
    daegu_apr_open_cnt_20 = 0
    daegu_may_open_cnt_20 = 0
    daegu_jun_open_cnt_20 = 0
    daegu_jul_open_cnt_20 = 0
    daegu_aug_open_cnt_20 = 0
    daegu_sep_open_cnt_20 = 0
    daegu_oct_open_cnt_20 = 0
    daegu_nov_open_cnt_20 = 0
    daegu_dec_open_cnt_20 = 0

    # 대전 open 20 cnt
    daejeon_jan_open_cnt_20 = 0
    daejeon_feb_open_cnt_20 = 0
    daejeon_mar_open_cnt_20 = 0
    daejeon_apr_open_cnt_20 = 0
    daejeon_may_open_cnt_20 = 0
    daejeon_jun_open_cnt_20 = 0
    daejeon_jul_open_cnt_20 = 0
    daejeon_aug_open_cnt_20 = 0
    daejeon_sep_open_cnt_20 = 0
    daejeon_oct_open_cnt_20 = 0
    daejeon_nov_open_cnt_20 = 0
    daejeon_dec_open_cnt_20 = 0

    # 강원 open 20 cnt
    gangwon_jan_open_cnt_20 = 0
    gangwon_feb_open_cnt_20 = 0
    gangwon_mar_open_cnt_20 = 0
    gangwon_apr_open_cnt_20 = 0
    gangwon_may_open_cnt_20 = 0
    gangwon_jun_open_cnt_20 = 0
    gangwon_jul_open_cnt_20 = 0
    gangwon_aug_open_cnt_20 = 0
    gangwon_sep_open_cnt_20 = 0
    gangwon_oct_open_cnt_20 = 0
    gangwon_nov_open_cnt_20 = 0
    gangwon_dec_open_cnt_20 = 0

    # 광주 open 20 cnt
    gwangju_jan_open_cnt_20 = 0
    gwangju_feb_open_cnt_20 = 0
    gwangju_mar_open_cnt_20 = 0
    gwangju_apr_open_cnt_20 = 0
    gwangju_may_open_cnt_20 = 0
    gwangju_jun_open_cnt_20 = 0
    gwangju_jul_open_cnt_20 = 0
    gwangju_aug_open_cnt_20 = 0
    gwangju_sep_open_cnt_20 = 0
    gwangju_oct_open_cnt_20 = 0
    gwangju_nov_open_cnt_20 = 0
    gwangju_dec_open_cnt_20 = 0

    # 경기 open 20 cnt
    gyeonggi_jan_open_cnt_20 = 0
    gyeonggi_feb_open_cnt_20 = 0
    gyeonggi_mar_open_cnt_20 = 0
    gyeonggi_apr_open_cnt_20 = 0
    gyeonggi_may_open_cnt_20 = 0
    gyeonggi_jun_open_cnt_20 = 0
    gyeonggi_jul_open_cnt_20 = 0
    gyeonggi_aug_open_cnt_20 = 0
    gyeonggi_sep_open_cnt_20 = 0
    gyeonggi_oct_open_cnt_20 = 0
    gyeonggi_nov_open_cnt_20 = 0
    gyeonggi_dec_open_cnt_20 = 0

    # 경북 open 20 cnt
    gyeongbuk_jan_open_cnt_20 = 0
    gyeongbuk_feb_open_cnt_20 = 0
    gyeongbuk_mar_open_cnt_20 = 0
    gyeongbuk_apr_open_cnt_20 = 0
    gyeongbuk_may_open_cnt_20 = 0
    gyeongbuk_jun_open_cnt_20 = 0
    gyeongbuk_jul_open_cnt_20 = 0
    gyeongbuk_aug_open_cnt_20 = 0
    gyeongbuk_sep_open_cnt_20 = 0
    gyeongbuk_oct_open_cnt_20 = 0
    gyeongbuk_nov_open_cnt_20 = 0
    gyeongbuk_dec_open_cnt_20 = 0

    # 경남 open 20 cnt
    gyeongnam_jan_open_cnt_20 = 0
    gyeongnam_feb_open_cnt_20 = 0
    gyeongnam_mar_open_cnt_20 = 0
    gyeongnam_apr_open_cnt_20 = 0
    gyeongnam_may_open_cnt_20 = 0
    gyeongnam_jun_open_cnt_20 = 0
    gyeongnam_jul_open_cnt_20 = 0
    gyeongnam_aug_open_cnt_20 = 0
    gyeongnam_sep_open_cnt_20 = 0
    gyeongnam_oct_open_cnt_20 = 0
    gyeongnam_nov_open_cnt_20 = 0
    gyeongnam_dec_open_cnt_20 = 0

    # 인천 open 20 cnt
    incheon_jan_open_cnt_20 = 0
    incheon_feb_open_cnt_20 = 0
    incheon_mar_open_cnt_20 = 0
    incheon_apr_open_cnt_20 = 0
    incheon_may_open_cnt_20 = 0
    incheon_jun_open_cnt_20 = 0
    incheon_jul_open_cnt_20 = 0
    incheon_aug_open_cnt_20 = 0
    incheon_sep_open_cnt_20 = 0
    incheon_oct_open_cnt_20 = 0
    incheon_nov_open_cnt_20 = 0
    incheon_dec_open_cnt_20 = 0

    # 제주 open 20 cnt
    jeju_jan_open_cnt_20 = 0
    jeju_feb_open_cnt_20 = 0
    jeju_mar_open_cnt_20 = 0
    jeju_apr_open_cnt_20 = 0
    jeju_may_open_cnt_20 = 0
    jeju_jun_open_cnt_20 = 0
    jeju_jul_open_cnt_20 = 0
    jeju_aug_open_cnt_20 = 0
    jeju_sep_open_cnt_20 = 0
    jeju_oct_open_cnt_20 = 0
    jeju_nov_open_cnt_20 = 0
    jeju_dec_open_cnt_20 = 0

    # 전북 open 20 cnt
    jeonbuk_jan_open_cnt_20 = 0
    jeonbuk_feb_open_cnt_20 = 0
    jeonbuk_mar_open_cnt_20 = 0
    jeonbuk_apr_open_cnt_20 = 0
    jeonbuk_may_open_cnt_20 = 0
    jeonbuk_jun_open_cnt_20 = 0
    jeonbuk_jul_open_cnt_20 = 0
    jeonbuk_aug_open_cnt_20 = 0
    jeonbuk_sep_open_cnt_20 = 0
    jeonbuk_oct_open_cnt_20 = 0
    jeonbuk_nov_open_cnt_20 = 0
    jeonbuk_dec_open_cnt_20 = 0

    # 전남 open 20 cnt
    jeonnam_jan_open_cnt_20 = 0
    jeonnam_feb_open_cnt_20 = 0
    jeonnam_mar_open_cnt_20 = 0
    jeonnam_apr_open_cnt_20 = 0
    jeonnam_may_open_cnt_20 = 0
    jeonnam_jun_open_cnt_20 = 0
    jeonnam_jul_open_cnt_20 = 0
    jeonnam_aug_open_cnt_20 = 0
    jeonnam_sep_open_cnt_20 = 0
    jeonnam_oct_open_cnt_20 = 0
    jeonnam_nov_open_cnt_20 = 0
    jeonnam_dec_open_cnt_20 = 0

    # 세종 open 20 cnt
    sejong_jan_open_cnt_20 = 0
    sejong_feb_open_cnt_20 = 0
    sejong_mar_open_cnt_20 = 0
    sejong_apr_open_cnt_20 = 0
    sejong_may_open_cnt_20 = 0
    sejong_jun_open_cnt_20 = 0
    sejong_jul_open_cnt_20 = 0
    sejong_aug_open_cnt_20 = 0
    sejong_sep_open_cnt_20 = 0
    sejong_oct_open_cnt_20 = 0
    sejong_nov_open_cnt_20 = 0
    sejong_dec_open_cnt_20 = 0

    # 서울 open 20 cnt
    seoul_jan_open_cnt_20 = 0
    seoul_feb_open_cnt_20 = 0
    seoul_mar_open_cnt_20 = 0
    seoul_apr_open_cnt_20 = 0
    seoul_may_open_cnt_20 = 0
    seoul_jun_open_cnt_20 = 0
    seoul_jul_open_cnt_20 = 0
    seoul_aug_open_cnt_20 = 0
    seoul_sep_open_cnt_20 = 0
    seoul_oct_open_cnt_20 = 0
    seoul_nov_open_cnt_20 = 0
    seoul_dec_open_cnt_20 = 0

    # 울산 open 20 cnt
    ulsan_jan_open_cnt_20 = 0
    ulsan_feb_open_cnt_20 = 0
    ulsan_mar_open_cnt_20 = 0
    ulsan_apr_open_cnt_20 = 0
    ulsan_may_open_cnt_20 = 0
    ulsan_jun_open_cnt_20 = 0
    ulsan_jul_open_cnt_20 = 0
    ulsan_aug_open_cnt_20 = 0
    ulsan_sep_open_cnt_20 = 0
    ulsan_oct_open_cnt_20 = 0
    ulsan_nov_open_cnt_20 = 0
    ulsan_dec_open_cnt_20 = 0

    # 시도별 19년 close
    for info in busan_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            busan_jan_close_cnt_19 += 1
            print("busan_jan_close_cnt_19", busan_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            busan_feb_close_cnt_19 += 1
            print("busan_feb_close_cnt_19", busan_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            busan_mar_close_cnt_19 += 1
            print("busan_mar_close_cnt_19", busan_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            busan_apr_close_cnt_19 += 1
            print("busan_apr_close_cnt_19", busan_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            busan_may_close_cnt_19 += 1
            print("busan_may_close_cnt_19", busan_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            busan_jun_close_cnt_19 += 1
            print("busan_jun_close_cnt_19", busan_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            busan_jul_close_cnt_19 += 1
            print("busan_jul_close_cnt_19", busan_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            busan_aug_close_cnt_19 += 1
            print("busan_aug_close_cnt_19", busan_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            busan_sep_close_cnt_19 += 1
            print("busan_sep_close_cnt_19", busan_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            busan_oct_close_cnt_19 += 1
            print("busan_oct_close_cnt_19", busan_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            busan_nov_close_cnt_19 += 1
            print("busan_nov_close_cnt_19", busan_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            busan_dec_close_cnt_19 += 1
            print("busan_dec_close_cnt_19", busan_dec_close_cnt_19)
    for info in chungbuk_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            chungbuk_jan_close_cnt_19 += 1
            print("chungbuk_jan_close_cnt_19", chungbuk_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            chungbuk_feb_close_cnt_19 += 1
            print("chungbuk_feb_close_cnt_19", chungbuk_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            chungbuk_mar_close_cnt_19 += 1
            print("chungbuk_mar_close_cnt_19", chungbuk_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            chungbuk_apr_close_cnt_19 += 1
            print("chungbuk_apr_close_cnt_19", chungbuk_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            chungbuk_may_close_cnt_19 += 1
            print("chungbuk_may_close_cnt_19", chungbuk_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            chungbuk_jun_close_cnt_19 += 1
            print("chungbuk_jun_close_cnt_19", chungbuk_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            chungbuk_jul_close_cnt_19 += 1
            print("chungbuk_jul_close_cnt_19", chungbuk_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            chungbuk_aug_close_cnt_19 += 1
            print("chungbuk_aug_close_cnt_19", chungbuk_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            chungbuk_sep_close_cnt_19 += 1
            print("chungbuk_sep_close_cnt_19", chungbuk_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            chungbuk_oct_close_cnt_19 += 1
            print("chungbuk_oct_close_cnt_19", chungbuk_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            chungbuk_nov_close_cnt_19 += 1
            print("chungbuk_nov_close_cnt_19", chungbuk_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            chungbuk_dec_close_cnt_19 += 1
            print("chungbuk_dec_close_cnt_19", chungbuk_dec_close_cnt_19)
    for info in chungnam_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            chungnam_jan_close_cnt_19 += 1
            print("chungnam_jan_close_cnt_19", chungnam_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            chungnam_feb_close_cnt_19 += 1
            print("chungnam_feb_close_cnt_19", chungnam_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            chungnam_mar_close_cnt_19 += 1
            print("chungnam_mar_close_cnt_19", chungnam_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            chungnam_apr_close_cnt_19 += 1
            print("chungnam_apr_close_cnt_19", chungnam_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            chungnam_may_close_cnt_19 += 1
            print("chungnam_may_close_cnt_19", chungnam_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            chungnam_jun_close_cnt_19 += 1
            print("chungnam_jun_close_cnt_19", chungnam_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            chungnam_jul_close_cnt_19 += 1
            print("chungnam_jul_close_cnt_19", chungnam_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            chungnam_aug_close_cnt_19 += 1
            print("chungnam_aug_close_cnt_19", chungnam_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            chungnam_sep_close_cnt_19 += 1
            print("chungnam_sep_close_cnt_19", chungnam_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            chungnam_oct_close_cnt_19 += 1
            print("chungnam_oct_close_cnt_19", chungnam_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            chungnam_nov_close_cnt_19 += 1
            print("chungnam_nov_close_cnt_19", chungnam_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            chungnam_dec_close_cnt_19 += 1
            print("chungnam_dec_close_cnt_19", chungnam_dec_close_cnt_19)
    for info in daegu_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            daegu_jan_close_cnt_19 += 1
            print("daegu_jan_close_cnt_19", daegu_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            daegu_feb_close_cnt_19 += 1
            print("daegu_feb_close_cnt_19", daegu_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            daegu_mar_close_cnt_19 += 1
            print("daegu_mar_close_cnt_19", daegu_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            daegu_apr_close_cnt_19 += 1
            print("daegu_apr_close_cnt_19", daegu_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            daegu_may_close_cnt_19 += 1
            print("daegu_may_close_cnt_19", daegu_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            daegu_jun_close_cnt_19 += 1
            print("daegu_jun_close_cnt_19", daegu_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            daegu_jul_close_cnt_19 += 1
            print("daegu_jul_close_cnt_19", daegu_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            daegu_aug_close_cnt_19 += 1
            print("daegu_aug_close_cnt_19", daegu_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            daegu_sep_close_cnt_19 += 1
            print("daegu_sep_close_cnt_19", daegu_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            daegu_oct_close_cnt_19 += 1
            print("daegu_oct_close_cnt_19", daegu_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            daegu_nov_close_cnt_19 += 1
            print("daegu_nov_close_cnt_19", daegu_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            daegu_dec_close_cnt_19 += 1
            print("daegu_dec_close_cnt_19", daegu_dec_close_cnt_19)
    for info in daejeon_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            daejeon_jan_close_cnt_19 += 1
            print("daejeon_jan_close_cnt_19", daejeon_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            daejeon_feb_close_cnt_19 += 1
            print("daejeon_feb_close_cnt_19", daejeon_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            daejeon_mar_close_cnt_19 += 1
            print("daejeon_mar_close_cnt_19", daejeon_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            daejeon_apr_close_cnt_19 += 1
            print("daejeon_apr_close_cnt_19", daejeon_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            daejeon_may_close_cnt_19 += 1
            print("daejeon_may_close_cnt_19", daejeon_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            daejeon_jun_close_cnt_19 += 1
            print("daejeon_jun_close_cnt_19", daejeon_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            daejeon_jul_close_cnt_19 += 1
            print("daejeon_jul_close_cnt_19", daejeon_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            daejeon_aug_close_cnt_19 += 1
            print("daejeon_aug_close_cnt_19", daejeon_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            daejeon_sep_close_cnt_19 += 1
            print("daejeon_sep_close_cnt_19", daejeon_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            daejeon_oct_close_cnt_19 += 1
            print("daejeon_oct_close_cnt_19", daejeon_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            daejeon_nov_close_cnt_19 += 1
            print("daejeon_nov_close_cnt_19", daejeon_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            daejeon_dec_close_cnt_19 += 1
            print("daejeon_dec_close_cnt_19", daejeon_dec_close_cnt_19)
    for info in gangwon_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gangwon_jan_close_cnt_19 += 1
            print("gangwon_jan_close_cnt_19", gangwon_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            gangwon_feb_close_cnt_19 += 1
            print("gangwon_feb_close_cnt_19", gangwon_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            gangwon_mar_close_cnt_19 += 1
            print("gangwon_mar_close_cnt_19", gangwon_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            gangwon_apr_close_cnt_19 += 1
            print("gangwon_apr_close_cnt_19", gangwon_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            gangwon_may_close_cnt_19 += 1
            print("gangwon_may_close_cnt_19", gangwon_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            gangwon_jun_close_cnt_19 += 1
            print("gangwon_jun_close_cnt_19", gangwon_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            gangwon_jul_close_cnt_19 += 1
            print("gangwon_jul_close_cnt_19", gangwon_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            gangwon_aug_close_cnt_19 += 1
            print("gangwon_aug_close_cnt_19", gangwon_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            gangwon_sep_close_cnt_19 += 1
            print("gangwon_sep_close_cnt_19", gangwon_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            gangwon_oct_close_cnt_19 += 1
            print("gangwon_oct_close_cnt_19", gangwon_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            gangwon_nov_close_cnt_19 += 1
            print("gangwon_nov_close_cnt_19", gangwon_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            gangwon_dec_close_cnt_19 += 1
            print("gangwon_dec_close_cnt_19", gangwon_dec_close_cnt_19)
    for info in gwangju_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gwangju_jan_close_cnt_19 += 1
            print("gwangju_jan_close_cnt_19", gwangju_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            gwangju_feb_close_cnt_19 += 1
            print("gwangju_feb_close_cnt_19", gwangju_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            gwangju_mar_close_cnt_19 += 1
            print("gwangju_mar_close_cnt_19", gwangju_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            gwangju_apr_close_cnt_19 += 1
            print("gwangju_apr_close_cnt_19", gwangju_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            gwangju_may_close_cnt_19 += 1
            print("gwangju_may_close_cnt_19", gwangju_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            gwangju_jun_close_cnt_19 += 1
            print("gwangju_jun_close_cnt_19", gwangju_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            gwangju_jul_close_cnt_19 += 1
            print("gwangju_jul_close_cnt_19", gwangju_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            gwangju_aug_close_cnt_19 += 1
            print("gwangju_aug_close_cnt_19", gwangju_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            gwangju_sep_close_cnt_19 += 1
            print("gwangju_sep_close_cnt_19", gwangju_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            gwangju_oct_close_cnt_19 += 1
            print("gwangju_oct_close_cnt_19", gwangju_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            gwangju_nov_close_cnt_19 += 1
            print("gwangju_nov_close_cnt_19", gwangju_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            gwangju_dec_close_cnt_19 += 1
            print("gwangju_dec_close_cnt_19", gwangju_dec_close_cnt_19)
    for info in gyeonggi_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeonggi_jan_close_cnt_19 += 1
            print("gyeonggi_jan_close_cnt_19", gyeonggi_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            gyeonggi_feb_close_cnt_19 += 1
            print("gyeonggi_feb_close_cnt_19", gyeonggi_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            gyeonggi_mar_close_cnt_19 += 1
            print("gyeonggi_mar_close_cnt_19", gyeonggi_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            gyeonggi_apr_close_cnt_19 += 1
            print("gyeonggi_apr_close_cnt_19", gyeonggi_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            gyeonggi_may_close_cnt_19 += 1
            print("gyeonggi_may_close_cnt_19", gyeonggi_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            gyeonggi_jun_close_cnt_19 += 1
            print("gyeonggi_jun_close_cnt_19", gyeonggi_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            gyeonggi_jul_close_cnt_19 += 1
            print("gyeonggi_jul_close_cnt_19", gyeonggi_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            gyeonggi_aug_close_cnt_19 += 1
            print("gyeonggi_aug_close_cnt_19", gyeonggi_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            gyeonggi_sep_close_cnt_19 += 1
            print("gyeonggi_sep_close_cnt_19", gyeonggi_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            gyeonggi_oct_close_cnt_19 += 1
            print("gyeonggi_oct_close_cnt_19", gyeonggi_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            gyeonggi_nov_close_cnt_19 += 1
            print("gyeonggi_nov_close_cnt_19", gyeonggi_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            gyeonggi_dec_close_cnt_19 += 1
            print("gyeonggi_dec_close_cnt_19", gyeonggi_dec_close_cnt_19)
    for info in gyeongbuk_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeongbuk_jan_close_cnt_19 += 1
            print("gyeongbuk_jan_close_cnt_19", gyeongbuk_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            gyeongbuk_feb_close_cnt_19 += 1
            print("gyeongbuk_feb_close_cnt_19", gyeongbuk_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            gyeongbuk_mar_close_cnt_19 += 1
            print("gyeongbuk_mar_close_cnt_19", gyeongbuk_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            gyeongbuk_apr_close_cnt_19 += 1
            print("gyeongbuk_apr_close_cnt_19", gyeongbuk_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            gyeongbuk_may_close_cnt_19 += 1
            print("gyeongbuk_may_close_cnt_19", gyeongbuk_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            gyeongbuk_jun_close_cnt_19 += 1
            print("gyeongbuk_jun_close_cnt_19", gyeongbuk_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            gyeongbuk_jul_close_cnt_19 += 1
            print("gyeongbuk_jul_close_cnt_19", gyeongbuk_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            gyeongbuk_aug_close_cnt_19 += 1
            print("gyeongbuk_aug_close_cnt_19", gyeongbuk_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            gyeongbuk_sep_close_cnt_19 += 1
            print("gyeongbuk_sep_close_cnt_19", gyeongbuk_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            gyeongbuk_oct_close_cnt_19 += 1
            print("gyeongbuk_oct_close_cnt_19", gyeongbuk_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            gyeongbuk_nov_close_cnt_19 += 1
            print("gyeongbuk_nov_close_cnt_19", gyeongbuk_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            gyeongbuk_dec_close_cnt_19 += 1
            print("gyeongbuk_dec_close_cnt_19", gyeongbuk_dec_close_cnt_19)
    for info in gyeongnam_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeongnam_jan_close_cnt_19 += 1
            print("gyeongnam_jan_close_cnt_19", gyeongnam_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            gyeongnam_feb_close_cnt_19 += 1
            print("gyeongnam_feb_close_cnt_19", gyeongnam_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            gyeongnam_mar_close_cnt_19 += 1
            print("gyeongnam_mar_close_cnt_19", gyeongnam_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            gyeongnam_apr_close_cnt_19 += 1
            print("gyeongnam_apr_close_cnt_19", gyeongnam_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            gyeongnam_may_close_cnt_19 += 1
            print("gyeongnam_may_close_cnt_19", gyeongnam_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            gyeongnam_jun_close_cnt_19 += 1
            print("gyeongnam_jun_close_cnt_19", gyeongnam_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            gyeongnam_jul_close_cnt_19 += 1
            print("gyeongnam_jul_close_cnt_19", gyeongnam_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            gyeongnam_aug_close_cnt_19 += 1
            print("gyeongnam_aug_close_cnt_19", gyeongnam_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            gyeongnam_sep_close_cnt_19 += 1
            print("gyeongnam_sep_close_cnt_19", gyeongnam_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            gyeongnam_oct_close_cnt_19 += 1
            print("gyeongnam_oct_close_cnt_19", gyeongnam_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            gyeongnam_nov_close_cnt_19 += 1
            print("gyeongnam_nov_close_cnt_19", gyeongnam_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            gyeongnam_dec_close_cnt_19 += 1
            print("gyeongnam_dec_close_cnt_19", gyeongnam_dec_close_cnt_19)
    for info in incheon_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            incheon_jan_close_cnt_19 += 1
            print("incheon_jan_close_cnt_19", incheon_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            incheon_feb_close_cnt_19 += 1
            print("incheon_feb_close_cnt_19", incheon_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            incheon_mar_close_cnt_19 += 1
            print("incheon_mar_close_cnt_19", incheon_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            incheon_apr_close_cnt_19 += 1
            print("incheon_apr_close_cnt_19", incheon_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            incheon_may_close_cnt_19 += 1
            print("incheon_may_close_cnt_19", incheon_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            incheon_jun_close_cnt_19 += 1
            print("incheon_jun_close_cnt_19", incheon_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            incheon_jul_close_cnt_19 += 1
            print("incheon_jul_close_cnt_19", incheon_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            incheon_aug_close_cnt_19 += 1
            print("incheon_aug_close_cnt_19", incheon_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            incheon_sep_close_cnt_19 += 1
            print("incheon_sep_close_cnt_19", incheon_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            incheon_oct_close_cnt_19 += 1
            print("incheon_oct_close_cnt_19", incheon_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            incheon_nov_close_cnt_19 += 1
            print("incheon_nov_close_cnt_19", incheon_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            incheon_dec_close_cnt_19 += 1
            print("incheon_dec_close_cnt_19", incheon_dec_close_cnt_19)
    for info in jeju_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeju_jan_close_cnt_19 += 1
            print("jeju_jan_close_cnt_19", jeju_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            jeju_feb_close_cnt_19 += 1
            print("jeju_feb_close_cnt_19", jeju_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            jeju_mar_close_cnt_19 += 1
            print("jeju_mar_close_cnt_19", jeju_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            jeju_apr_close_cnt_19 += 1
            print("jeju_apr_close_cnt_19", jeju_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            jeju_may_close_cnt_19 += 1
            print("jeju_may_close_cnt_19", jeju_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jeju_jun_close_cnt_19 += 1
            print("jeju_jun_close_cnt_19", jeju_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jeju_jul_close_cnt_19 += 1
            print("jeju_jul_close_cnt_19", jeju_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            jeju_aug_close_cnt_19 += 1
            print("jeju_aug_close_cnt_19", jeju_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            jeju_sep_close_cnt_19 += 1
            print("jeju_sep_close_cnt_19", jeju_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            jeju_oct_close_cnt_19 += 1
            print("jeju_oct_close_cnt_19", jeju_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            jeju_nov_close_cnt_19 += 1
            print("jeju_nov_close_cnt_19", jeju_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            jeju_dec_close_cnt_19 += 1
            print("jeju_dec_close_cnt_19", jeju_dec_close_cnt_19)
    for info in jeonbuk_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeonbuk_jan_close_cnt_19 += 1
            print("jeonbuk_jan_close_cnt_19", jeonbuk_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            jeonbuk_feb_close_cnt_19 += 1
            print("jeonbuk_feb_close_cnt_19", jeonbuk_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            jeonbuk_mar_close_cnt_19 += 1
            print("jeonbuk_mar_close_cnt_19", jeonbuk_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            jeonbuk_apr_close_cnt_19 += 1
            print("jeonbuk_apr_close_cnt_19", jeonbuk_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            jeonbuk_may_close_cnt_19 += 1
            print("jeonbuk_may_close_cnt_19", jeonbuk_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jeonbuk_jun_close_cnt_19 += 1
            print("jeonbuk_jun_close_cnt_19", jeonbuk_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jeonbuk_jul_close_cnt_19 += 1
            print("jeonbuk_jul_close_cnt_19", jeonbuk_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            jeonbuk_aug_close_cnt_19 += 1
            print("jeonbuk_aug_close_cnt_19", jeonbuk_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            jeonbuk_sep_close_cnt_19 += 1
            print("jeonbuk_sep_close_cnt_19", jeonbuk_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            jeonbuk_oct_close_cnt_19 += 1
            print("jeonbuk_oct_close_cnt_19", jeonbuk_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            jeonbuk_nov_close_cnt_19 += 1
            print("jeonbuk_nov_close_cnt_19", jeonbuk_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            jeonbuk_dec_close_cnt_19 += 1
            print("jeonbuk_dec_close_cnt_19", jeonbuk_dec_close_cnt_19)
    for info in jeonnam_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeonnam_jan_close_cnt_19 += 1
            print("jeonnam_jan_close_cnt_19", jeonnam_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            jeonnam_feb_close_cnt_19 += 1
            print("jeonnam_feb_close_cnt_19", jeonnam_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            jeonnam_mar_close_cnt_19 += 1
            print("jeonnam_mar_close_cnt_19", jeonnam_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            jeonnam_apr_close_cnt_19 += 1
            print("jeonnam_apr_close_cnt_19", jeonnam_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            jeonnam_may_close_cnt_19 += 1
            print("jeonnam_may_close_cnt_19", jeonnam_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jeonnam_jun_close_cnt_19 += 1
            print("jeonnam_jun_close_cnt_19", jeonnam_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jeonnam_jul_close_cnt_19 += 1
            print("jeonnam_jul_close_cnt_19", jeonnam_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            jeonnam_aug_close_cnt_19 += 1
            print("jeonnam_aug_close_cnt_19", jeonnam_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            jeonnam_sep_close_cnt_19 += 1
            print("jeonnam_sep_close_cnt_19", jeonnam_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            jeonnam_oct_close_cnt_19 += 1
            print("jeonnam_oct_close_cnt_19", jeonnam_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            jeonnam_nov_close_cnt_19 += 1
            print("jeonnam_nov_close_cnt_19", jeonnam_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            jeonnam_dec_close_cnt_19 += 1
            print("jeonnam_dec_close_cnt_19", jeonnam_dec_close_cnt_19)
    for info in sejong_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            sejong_jan_close_cnt_19 += 1
            print("sejong_jan_close_cnt_19", sejong_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            sejong_feb_close_cnt_19 += 1
            print("sejong_feb_close_cnt_19", sejong_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            sejong_mar_close_cnt_19 += 1
            print("sejong_mar_close_cnt_19", sejong_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            sejong_apr_close_cnt_19 += 1
            print("sejong_apr_close_cnt_19", sejong_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            sejong_may_close_cnt_19 += 1
            print("sejong_may_close_cnt_19", sejong_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            sejong_jun_close_cnt_19 += 1
            print("sejong_jun_close_cnt_19", sejong_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            sejong_jul_close_cnt_19 += 1
            print("sejong_jul_close_cnt_19", sejong_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            sejong_aug_close_cnt_19 += 1
            print("sejong_aug_close_cnt_19", sejong_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sejong_sep_close_cnt_19 += 1
            print("sejong_sep_close_cnt_19", sejong_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            sejong_oct_close_cnt_19 += 1
            print("sejong_oct_close_cnt_19", sejong_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            sejong_nov_close_cnt_19 += 1
            print("sejong_nov_close_cnt_19", sejong_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            sejong_dec_close_cnt_19 += 1
            print("sejong_dec_close_cnt_19", sejong_dec_close_cnt_19)
    for info in seoul_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            seoul_jan_close_cnt_19 += 1
            print("seoul_jan_close_cnt_19", seoul_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            seoul_feb_close_cnt_19 += 1
            print("seoul_feb_close_cnt_19", seoul_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            seoul_mar_close_cnt_19 += 1
            print("seoul_mar_close_cnt_19", seoul_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            seoul_apr_close_cnt_19 += 1
            print("seoul_apr_close_cnt_19", seoul_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            seoul_may_close_cnt_19 += 1
            print("seoul_may_close_cnt_19", seoul_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            seoul_jun_close_cnt_19 += 1
            print("seoul_jun_close_cnt_19", seoul_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            seoul_jul_close_cnt_19 += 1
            print("seoul_jul_close_cnt_19", seoul_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            seoul_aug_close_cnt_19 += 1
            print("seoul_aug_close_cnt_19", seoul_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            seoul_sep_close_cnt_19 += 1
            print("seoul_sep_close_cnt_19", seoul_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            seoul_oct_close_cnt_19 += 1
            print("seoul_oct_close_cnt_19", seoul_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            seoul_nov_close_cnt_19 += 1
            print("seoul_nov_close_cnt_19", seoul_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            seoul_dec_close_cnt_19 += 1
            print("seoul_dec_close_cnt_19", seoul_dec_close_cnt_19)
    for info in ulsan_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            ulsan_jan_close_cnt_19 += 1
            print("ulsan_jan_close_cnt_19", ulsan_jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            ulsan_feb_close_cnt_19 += 1
            print("ulsan_feb_close_cnt_19", ulsan_feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            ulsan_mar_close_cnt_19 += 1
            print("ulsan_mar_close_cnt_19", ulsan_mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            ulsan_apr_close_cnt_19 += 1
            print("ulsan_apr_close_cnt_19", ulsan_apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            ulsan_may_close_cnt_19 += 1
            print("ulsan_may_close_cnt_19", ulsan_may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            ulsan_jun_close_cnt_19 += 1
            print("ulsan_jun_close_cnt_19", ulsan_jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            ulsan_jul_close_cnt_19 += 1
            print("ulsan_jul_close_cnt_19", ulsan_jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            ulsan_aug_close_cnt_19 += 1
            print("ulsan_aug_close_cnt_19", ulsan_aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            ulsan_sep_close_cnt_19 += 1
            print("ulsan_sep_close_cnt_19", ulsan_sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            ulsan_oct_close_cnt_19 += 1
            print("ulsan_oct_close_cnt_19", ulsan_oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            ulsan_nov_close_cnt_19 += 1
            print("ulsan_nov_close_cnt_19", ulsan_nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            ulsan_dec_close_cnt_19 += 1
            print("ulsan_dec_close_cnt_19", ulsan_dec_close_cnt_19)

    # 시도별 19년 open
    for info in busan_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            busan_jan_open_cnt_19 += 1
            print("busan_jan_open_cnt_19", busan_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            busan_feb_open_cnt_19 += 1
            print("busan_feb_open_cnt_19", busan_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            busan_mar_open_cnt_19 += 1
            print("busan_mar_open_cnt_19", busan_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            busan_apr_open_cnt_19 += 1
            print("busan_apr_open_cnt_19", busan_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            busan_may_open_cnt_19 += 1
            print("busan_may_open_cnt_19", busan_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            busan_jun_open_cnt_19 += 1
            print("busan_jun_open_cnt_19", busan_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            busan_jul_open_cnt_19 += 1
            print("busan_jul_open_cnt_19", busan_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            busan_aug_open_cnt_19 += 1
            print("busan_aug_open_cnt_19", busan_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            busan_sep_open_cnt_19 += 1
            print("busan_sep_open_cnt_19", busan_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            busan_oct_open_cnt_19 += 1
            print("busan_oct_open_cnt_19", busan_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            busan_nov_open_cnt_19 += 1
            print("busan_nov_open_cnt_19", busan_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            busan_dec_open_cnt_19 += 1
            print("busan_dec_open_cnt_19", busan_dec_open_cnt_19)
    for info in chungbuk_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            chungbuk_jan_open_cnt_19 += 1
            print("chungbuk_jan_open_cnt_19", chungbuk_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            chungbuk_feb_open_cnt_19 += 1
            print("chungbuk_feb_open_cnt_19", chungbuk_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            chungbuk_mar_open_cnt_19 += 1
            print("chungbuk_mar_open_cnt_19", chungbuk_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            chungbuk_apr_open_cnt_19 += 1
            print("chungbuk_apr_open_cnt_19", chungbuk_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            chungbuk_may_open_cnt_19 += 1
            print("chungbuk_may_open_cnt_19", chungbuk_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            chungbuk_jun_open_cnt_19 += 1
            print("chungbuk_jun_open_cnt_19", chungbuk_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            chungbuk_jul_open_cnt_19 += 1
            print("chungbuk_jul_open_cnt_19", chungbuk_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            chungbuk_aug_open_cnt_19 += 1
            print("chungbuk_aug_open_cnt_19", chungbuk_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            chungbuk_sep_open_cnt_19 += 1
            print("chungbuk_sep_open_cnt_19", chungbuk_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            chungbuk_oct_open_cnt_19 += 1
            print("chungbuk_oct_open_cnt_19", chungbuk_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            chungbuk_nov_open_cnt_19 += 1
            print("chungbuk_nov_open_cnt_19", chungbuk_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            chungbuk_dec_open_cnt_19 += 1
            print("chungbuk_dec_open_cnt_19", chungbuk_dec_open_cnt_19)
    for info in chungnam_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            chungnam_jan_open_cnt_19 += 1
            print("chungnam_jan_open_cnt_19", chungnam_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            chungnam_feb_open_cnt_19 += 1
            print("chungnam_feb_open_cnt_19", chungnam_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            chungnam_mar_open_cnt_19 += 1
            print("chungnam_mar_open_cnt_19", chungnam_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            chungnam_apr_open_cnt_19 += 1
            print("chungnam_apr_open_cnt_19", chungnam_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            chungnam_may_open_cnt_19 += 1
            print("chungnam_may_open_cnt_19", chungnam_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            chungnam_jun_open_cnt_19 += 1
            print("chungnam_jun_open_cnt_19", chungnam_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            chungnam_jul_open_cnt_19 += 1
            print("chungnam_jul_open_cnt_19", chungnam_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            chungnam_aug_open_cnt_19 += 1
            print("chungnam_aug_open_cnt_19", chungnam_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            chungnam_sep_open_cnt_19 += 1
            print("chungnam_sep_open_cnt_19", chungnam_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            chungnam_oct_open_cnt_19 += 1
            print("chungnam_oct_open_cnt_19", chungnam_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            chungnam_nov_open_cnt_19 += 1
            print("chungnam_nov_open_cnt_19", chungnam_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            chungnam_dec_open_cnt_19 += 1
            print("chungnam_dec_open_cnt_19", chungnam_dec_open_cnt_19)
    for info in daegu_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            daegu_jan_open_cnt_19 += 1
            print("daegu_jan_open_cnt_19", daegu_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            daegu_feb_open_cnt_19 += 1
            print("daegu_feb_open_cnt_19", daegu_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            daegu_mar_open_cnt_19 += 1
            print("daegu_mar_open_cnt_19", daegu_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            daegu_apr_open_cnt_19 += 1
            print("daegu_apr_open_cnt_19", daegu_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            daegu_may_open_cnt_19 += 1
            print("daegu_may_open_cnt_19", daegu_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            daegu_jun_open_cnt_19 += 1
            print("daegu_jun_open_cnt_19", daegu_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            daegu_jul_open_cnt_19 += 1
            print("daegu_jul_open_cnt_19", daegu_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            daegu_aug_open_cnt_19 += 1
            print("daegu_aug_open_cnt_19", daegu_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            daegu_sep_open_cnt_19 += 1
            print("daegu_sep_open_cnt_19", daegu_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            daegu_oct_open_cnt_19 += 1
            print("daegu_oct_open_cnt_19", daegu_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            daegu_nov_open_cnt_19 += 1
            print("daegu_nov_open_cnt_19", daegu_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            daegu_dec_open_cnt_19 += 1
            print("daegu_dec_open_cnt_19", daegu_dec_open_cnt_19)
    for info in daejeon_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            daejeon_jan_open_cnt_19 += 1
            print("daejeon_jan_open_cnt_19", daejeon_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            daejeon_feb_open_cnt_19 += 1
            print("daejeon_feb_open_cnt_19", daejeon_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            daejeon_mar_open_cnt_19 += 1
            print("daejeon_mar_open_cnt_19", daejeon_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            daejeon_apr_open_cnt_19 += 1
            print("daejeon_apr_open_cnt_19", daejeon_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            daejeon_may_open_cnt_19 += 1
            print("daejeon_may_open_cnt_19", daejeon_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            daejeon_jun_open_cnt_19 += 1
            print("daejeon_jun_open_cnt_19", daejeon_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            daejeon_jul_open_cnt_19 += 1
            print("daejeon_jul_open_cnt_19", daejeon_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            daejeon_aug_open_cnt_19 += 1
            print("daejeon_aug_open_cnt_19", daejeon_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            daejeon_sep_open_cnt_19 += 1
            print("daejeon_sep_open_cnt_19", daejeon_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            daejeon_oct_open_cnt_19 += 1
            print("daejeon_oct_open_cnt_19", daejeon_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            daejeon_nov_open_cnt_19 += 1
            print("daejeon_nov_open_cnt_19", daejeon_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            daejeon_dec_open_cnt_19 += 1
            print("daejeon_dec_open_cnt_19", daejeon_dec_open_cnt_19)
    for info in gangwon_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gangwon_jan_open_cnt_19 += 1
            print("gangwon_jan_open_cnt_19", gangwon_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            gangwon_feb_open_cnt_19 += 1
            print("gangwon_feb_open_cnt_19", gangwon_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            gangwon_mar_open_cnt_19 += 1
            print("gangwon_mar_open_cnt_19", gangwon_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            gangwon_apr_open_cnt_19 += 1
            print("gangwon_apr_open_cnt_19", gangwon_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            gangwon_may_open_cnt_19 += 1
            print("gangwon_may_open_cnt_19", gangwon_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            gangwon_jun_open_cnt_19 += 1
            print("gangwon_jun_open_cnt_19", gangwon_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            gangwon_jul_open_cnt_19 += 1
            print("gangwon_jul_open_cnt_19", gangwon_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            gangwon_aug_open_cnt_19 += 1
            print("gangwon_aug_open_cnt_19", gangwon_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            gangwon_sep_open_cnt_19 += 1
            print("gangwon_sep_open_cnt_19", gangwon_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            gangwon_oct_open_cnt_19 += 1
            print("gangwon_oct_open_cnt_19", gangwon_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            gangwon_nov_open_cnt_19 += 1
            print("gangwon_nov_open_cnt_19", gangwon_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            gangwon_dec_open_cnt_19 += 1
            print("gangwon_dec_open_cnt_19", gangwon_dec_open_cnt_19)
    for info in gwangju_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gwangju_jan_open_cnt_19 += 1
            print("gwangju_jan_open_cnt_19", gwangju_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            gwangju_feb_open_cnt_19 += 1
            print("gwangju_feb_open_cnt_19", gwangju_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            gwangju_mar_open_cnt_19 += 1
            print("gwangju_mar_open_cnt_19", gwangju_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            gwangju_apr_open_cnt_19 += 1
            print("gwangju_apr_open_cnt_19", gwangju_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            gwangju_may_open_cnt_19 += 1
            print("gwangju_may_open_cnt_19", gwangju_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            gwangju_jun_open_cnt_19 += 1
            print("gwangju_jun_open_cnt_19", gwangju_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            gwangju_jul_open_cnt_19 += 1
            print("gwangju_jul_open_cnt_19", gwangju_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            gwangju_aug_open_cnt_19 += 1
            print("gwangju_aug_open_cnt_19", gwangju_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            gwangju_sep_open_cnt_19 += 1
            print("gwangju_sep_open_cnt_19", gwangju_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            gwangju_oct_open_cnt_19 += 1
            print("gwangju_oct_open_cnt_19", gwangju_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            gwangju_nov_open_cnt_19 += 1
            print("gwangju_nov_open_cnt_19", gwangju_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            gwangju_dec_open_cnt_19 += 1
            print("gwangju_dec_open_cnt_19", gwangju_dec_open_cnt_19)
    for info in gyeonggi_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeonggi_jan_open_cnt_19 += 1
            print("gyeonggi_jan_open_cnt_19", gyeonggi_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            gyeonggi_feb_open_cnt_19 += 1
            print("gyeonggi_feb_open_cnt_19", gyeonggi_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            gyeonggi_mar_open_cnt_19 += 1
            print("gyeonggi_mar_open_cnt_19", gyeonggi_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            gyeonggi_apr_open_cnt_19 += 1
            print("gyeonggi_apr_open_cnt_19", gyeonggi_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            gyeonggi_may_open_cnt_19 += 1
            print("gyeonggi_may_open_cnt_19", gyeonggi_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            gyeonggi_jun_open_cnt_19 += 1
            print("gyeonggi_jun_open_cnt_19", gyeonggi_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            gyeonggi_jul_open_cnt_19 += 1
            print("gyeonggi_jul_open_cnt_19", gyeonggi_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            gyeonggi_aug_open_cnt_19 += 1
            print("gyeonggi_aug_open_cnt_19", gyeonggi_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            gyeonggi_sep_open_cnt_19 += 1
            print("gyeonggi_sep_open_cnt_19", gyeonggi_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            gyeonggi_oct_open_cnt_19 += 1
            print("gyeonggi_oct_open_cnt_19", gyeonggi_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            gyeonggi_nov_open_cnt_19 += 1
            print("gyeonggi_nov_open_cnt_19", gyeonggi_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            gyeonggi_dec_open_cnt_19 += 1
            print("gyeonggi_dec_open_cnt_19", gyeonggi_dec_open_cnt_19)
    for info in gyeongbuk_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeongbuk_jan_open_cnt_19 += 1
            print("gyeongbuk_jan_open_cnt_19", gyeongbuk_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            gyeongbuk_feb_open_cnt_19 += 1
            print("gyeongbuk_feb_open_cnt_19", gyeongbuk_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            gyeongbuk_mar_open_cnt_19 += 1
            print("gyeongbuk_mar_open_cnt_19", gyeongbuk_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            gyeongbuk_apr_open_cnt_19 += 1
            print("gyeongbuk_apr_open_cnt_19", gyeongbuk_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            gyeongbuk_may_open_cnt_19 += 1
            print("gyeongbuk_may_open_cnt_19", gyeongbuk_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            gyeongbuk_jun_open_cnt_19 += 1
            print("gyeongbuk_jun_open_cnt_19", gyeongbuk_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            gyeongbuk_jul_open_cnt_19 += 1
            print("gyeongbuk_jul_open_cnt_19", gyeongbuk_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            gyeongbuk_aug_open_cnt_19 += 1
            print("gyeongbuk_aug_open_cnt_19", gyeongbuk_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            gyeongbuk_sep_open_cnt_19 += 1
            print("gyeongbuk_sep_open_cnt_19", gyeongbuk_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            gyeongbuk_oct_open_cnt_19 += 1
            print("gyeongbuk_oct_open_cnt_19", gyeongbuk_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            gyeongbuk_nov_open_cnt_19 += 1
            print("gyeongbuk_nov_open_cnt_19", gyeongbuk_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            gyeongbuk_dec_open_cnt_19 += 1
            print("gyeongbuk_dec_open_cnt_19", gyeongbuk_dec_open_cnt_19)
    for info in gyeongnam_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeongnam_jan_open_cnt_19 += 1
            print("gyeongnam_jan_open_cnt_19", gyeongnam_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            gyeongnam_feb_open_cnt_19 += 1
            print("gyeongnam_feb_open_cnt_19", gyeongnam_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            gyeongnam_mar_open_cnt_19 += 1
            print("gyeongnam_mar_open_cnt_19", gyeongnam_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            gyeongnam_apr_open_cnt_19 += 1
            print("gyeongnam_apr_open_cnt_19", gyeongnam_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            gyeongnam_may_open_cnt_19 += 1
            print("gyeongnam_may_open_cnt_19", gyeongnam_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            gyeongnam_jun_open_cnt_19 += 1
            print("gyeongnam_jun_open_cnt_19", gyeongnam_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            gyeongnam_jul_open_cnt_19 += 1
            print("gyeongnam_jul_open_cnt_19", gyeongnam_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            gyeongnam_aug_open_cnt_19 += 1
            print("gyeongnam_aug_open_cnt_19", gyeongnam_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            gyeongnam_sep_open_cnt_19 += 1
            print("gyeongnam_sep_open_cnt_19", gyeongnam_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            gyeongnam_oct_open_cnt_19 += 1
            print("gyeongnam_oct_open_cnt_19", gyeongnam_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            gyeongnam_nov_open_cnt_19 += 1
            print("gyeongnam_nov_open_cnt_19", gyeongnam_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            gyeongnam_dec_open_cnt_19 += 1
            print("gyeongnam_dec_open_cnt_19", gyeongnam_dec_open_cnt_19)
    for info in incheon_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            incheon_jan_open_cnt_19 += 1
            print("incheon_jan_open_cnt_19", incheon_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            incheon_feb_open_cnt_19 += 1
            print("incheon_feb_open_cnt_19", incheon_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            incheon_mar_open_cnt_19 += 1
            print("incheon_mar_open_cnt_19", incheon_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            incheon_apr_open_cnt_19 += 1
            print("incheon_apr_open_cnt_19", incheon_apr_close_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            incheon_may_open_cnt_19 += 1
            print("incheon_may_open_cnt_19", incheon_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            incheon_jun_open_cnt_19 += 1
            print("incheon_jun_open_cnt_19", incheon_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            incheon_jul_open_cnt_19 += 1
            print("incheon_jul_open_cnt_19", incheon_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            incheon_aug_open_cnt_19 += 1
            print("incheon_aug_open_cnt_19", incheon_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            incheon_sep_open_cnt_19 += 1
            print("incheon_sep_open_cnt_19", incheon_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            incheon_oct_open_cnt_19 += 1
            print("incheon_oct_open_cnt_19", incheon_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            incheon_nov_open_cnt_19 += 1
            print("incheon_nov_open_cnt_19", incheon_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            incheon_dec_open_cnt_19 += 1
            print("incheon_dec_open_cnt_19", incheon_dec_open_cnt_19)
    for info in jeju_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeju_jan_open_cnt_19 += 1
            print("jeju_jan_open_cnt_19", jeju_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            jeju_feb_open_cnt_19 += 1
            print("jeju_feb_open_cnt_19", jeju_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            jeju_mar_open_cnt_19 += 1
            print("jeju_mar_open_cnt_19", jeju_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            jeju_apr_open_cnt_19 += 1
            print("jeju_apr_open_cnt_19", jeju_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            jeju_may_open_cnt_19 += 1
            print("jeju_may_open_cnt_19", jeju_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jeju_jun_open_cnt_19 += 1
            print("jeju_jun_open_cnt_19", jeju_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jeju_jul_open_cnt_19 += 1
            print("jeju_jul_open_cnt_19", jeju_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            jeju_aug_open_cnt_19 += 1
            print("jeju_aug_open_cnt_19", jeju_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            jeju_sep_open_cnt_19 += 1
            print("jeju_sep_open_cnt_19", jeju_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            jeju_oct_open_cnt_19 += 1
            print("jeju_oct_open_cnt_19", jeju_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            jeju_nov_open_cnt_19 += 1
            print("jeju_nov_open_cnt_19", jeju_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            jeju_dec_open_cnt_19 += 1
            print("jeju_dec_open_cnt_19", jeju_dec_open_cnt_19)
    for info in jeonbuk_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeonbuk_jan_open_cnt_19 += 1
            print("jeonbuk_jan_open_cnt_19", jeonbuk_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            jeonbuk_feb_open_cnt_19 += 1
            print("jeonbuk_feb_open_cnt_19", jeonbuk_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            jeonbuk_mar_open_cnt_19 += 1
            print("jeonbuk_mar_open_cnt_19", jeonbuk_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            jeonbuk_apr_open_cnt_19 += 1
            print("jeonbuk_apr_open_cnt_19", jeonbuk_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            jeonbuk_may_open_cnt_19 += 1
            print("jeonbuk_may_open_cnt_19", jeonbuk_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jeonbuk_jun_open_cnt_19 += 1
            print("jeonbuk_jun_open_cnt_19", jeonbuk_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jeonbuk_jul_open_cnt_19 += 1
            print("jeonbuk_jul_open_cnt_19", jeonbuk_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            jeonbuk_aug_open_cnt_19 += 1
            print("jeonbuk_aug_open_cnt_19", jeonbuk_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            jeonbuk_sep_open_cnt_19 += 1
            print("jeonbuk_sep_open_cnt_19", jeonbuk_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            jeonbuk_oct_open_cnt_19 += 1
            print("jeonbuk_oct_open_cnt_19", jeonbuk_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            jeonbuk_nov_open_cnt_19 += 1
            print("jeonbuk_nov_open_cnt_19", jeonbuk_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            jeonbuk_dec_open_cnt_19 += 1
            print("jeonbuk_dec_open_cnt_19", jeonbuk_dec_open_cnt_19)
    for info in jeonnam_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeonnam_jan_open_cnt_19 += 1
            print("jeonnam_jan_open_cnt_19", jeonnam_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            jeonnam_feb_open_cnt_19 += 1
            print("jeonnam_feb_open_cnt_19", jeonnam_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            jeonnam_mar_open_cnt_19 += 1
            print("jeonnam_mar_open_cnt_19", jeonnam_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            jeonnam_apr_open_cnt_19 += 1
            print("jeonnam_apr_open_cnt_19", jeonnam_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            jeonnam_may_open_cnt_19 += 1
            print("jeonnam_may_open_cnt_19", jeonnam_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jeonnam_jun_open_cnt_19 += 1
            print("jeonnam_jun_open_cnt_19", jeonnam_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jeonnam_jul_open_cnt_19 += 1
            print("jeonnam_jul_open_cnt_19", jeonnam_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            jeonnam_aug_open_cnt_19 += 1
            print("jeonnam_aug_open_cnt_19", jeonnam_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            jeonnam_sep_open_cnt_19 += 1
            print("jeonnam_sep_open_cnt_19", jeonnam_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            jeonnam_oct_open_cnt_19 += 1
            print("jeonnam_oct_open_cnt_19", jeonnam_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            jeonnam_nov_open_cnt_19 += 1
            print("jeonnam_nov_open_cnt_19", jeonnam_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            jeonnam_dec_open_cnt_19 += 1
            print("jeonnam_dec_open_cnt_19", jeonnam_dec_open_cnt_19)
    for info in sejong_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            sejong_jan_open_cnt_19 += 1
            print("sejong_jan_open_cnt_19", sejong_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            sejong_feb_open_cnt_19 += 1
            print("sejong_feb_open_cnt_19", sejong_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            sejong_mar_open_cnt_19 += 1
            print("sejong_mar_open_cnt_19", sejong_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            sejong_apr_open_cnt_19 += 1
            print("sejong_apr_open_cnt_19", sejong_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            sejong_may_open_cnt_19 += 1
            print("sejong_may_open_cnt_19", sejong_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            sejong_jun_open_cnt_19 += 1
            print("sejong_jun_open_cnt_19", sejong_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            sejong_jul_open_cnt_19 += 1
            print("sejong_jul_open_cnt_19", sejong_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            sejong_aug_open_cnt_19 += 1
            print("sejong_aug_open_cnt_19", sejong_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sejong_sep_open_cnt_19 += 1
            print("sejong_sep_open_cnt_19", sejong_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            sejong_oct_open_cnt_19 += 1
            print("sejong_oct_open_cnt_19", sejong_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            sejong_nov_open_cnt_19 += 1
            print("sejong_nov_open_cnt_19", sejong_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            sejong_dec_open_cnt_19 += 1
            print("sejong_dec_open_cnt_19", sejong_dec_open_cnt_19)
    for info in seoul_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            seoul_jan_open_cnt_19 += 1
            print("seoul_jan_open_cnt_19", seoul_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            seoul_feb_open_cnt_19 += 1
            print("seoul_feb_open_cnt_19", seoul_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            seoul_mar_open_cnt_19 += 1
            print("seoul_mar_open_cnt_19", seoul_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            seoul_apr_open_cnt_19 += 1
            print("seoul_apr_open_cnt_19", seoul_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            seoul_may_open_cnt_19 += 1
            print("seoul_may_open_cnt_19", seoul_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            seoul_jun_open_cnt_19 += 1
            print("seoul_jun_open_cnt_19", seoul_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            seoul_jul_open_cnt_19 += 1
            print("seoul_jul_open_cnt_19", seoul_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            seoul_aug_open_cnt_19 += 1
            print("seoul_aug_open_cnt_19", seoul_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            seoul_sep_open_cnt_19 += 1
            print("seoul_sep_open_cnt_19", seoul_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            seoul_oct_open_cnt_19 += 1
            print("seoul_oct_open_cnt_19", seoul_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            seoul_nov_open_cnt_19 += 1
            print("seoul_nov_open_cnt_19", seoul_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            seoul_dec_open_cnt_19 += 1
            print("seoul_dec_open_cnt_19", seoul_dec_open_cnt_19)
    for info in ulsan_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            ulsan_jan_open_cnt_19 += 1
            print("ulsan_jan_open_cnt_19", ulsan_jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            ulsan_feb_open_cnt_19 += 1
            print("ulsan_feb_open_cnt_19", ulsan_feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            ulsan_mar_open_cnt_19 += 1
            print("ulsan_mar_open_cnt_19", ulsan_mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            ulsan_apr_open_cnt_19 += 1
            print("ulsan_apr_open_cnt_19", ulsan_apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            ulsan_may_open_cnt_19 += 1
            print("ulsan_may_open_cnt_19", ulsan_may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            ulsan_jun_open_cnt_19 += 1
            print("ulsan_jun_open_cnt_19", ulsan_jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            ulsan_jul_open_cnt_19 += 1
            print("ulsan_jul_open_cnt_19", ulsan_jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            ulsan_aug_open_cnt_19 += 1
            print("ulsan_aug_open_cnt_19", ulsan_aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            ulsan_sep_open_cnt_19 += 1
            print("ulsan_sep_open_cnt_19", ulsan_sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            ulsan_oct_open_cnt_19 += 1
            print("ulsan_oct_open_cnt_19", ulsan_oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            ulsan_nov_open_cnt_19 += 1
            print("ulsan_nov_open_cnt_19", ulsan_nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            ulsan_dec_open_cnt_19 += 1
            print("ulsan_dec_open_cnt_19", ulsan_dec_open_cnt_19)

    # 시도별 20년 close
    for info in busan_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            busan_jan_close_cnt_20 += 1
            print("busan_jan_close_cnt_20", busan_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            busan_feb_close_cnt_20 += 1
            print("busan_feb_close_cnt_20", busan_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            busan_mar_close_cnt_20 += 1
            print("busan_mar_close_cnt_20", busan_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            busan_apr_close_cnt_20 += 1
            print("busan_apr_close_cnt_20", busan_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            busan_may_close_cnt_20 += 1
            print("busan_may_close_cnt_20", busan_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            busan_jun_close_cnt_20 += 1
            print("busan_jun_close_cnt_20", busan_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            busan_jul_close_cnt_20 += 1
            print("busan_jul_close_cnt_20", busan_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            busan_aug_close_cnt_20 += 1
            print("busan_aug_close_cnt_20", busan_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            busan_sep_close_cnt_20 += 1
            print("busan_sep_close_cnt_20", busan_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            busan_oct_close_cnt_20 += 1
            print("busan_oct_close_cnt_20", busan_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            busan_nov_close_cnt_20 += 1
            print("busan_nov_close_cnt_20", busan_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            busan_dec_close_cnt_20 += 1
            print("busan_dec_close_cnt_20", busan_dec_close_cnt_20)
    for info in chungbuk_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            chungbuk_jan_close_cnt_20 += 1
            print("chungbuk_jan_close_cnt_20", chungbuk_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            chungbuk_feb_close_cnt_20 += 1
            print("chungbuk_feb_close_cnt_20", chungbuk_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            chungbuk_mar_close_cnt_20 += 1
            print("chungbuk_mar_close_cnt_20", chungbuk_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            chungbuk_apr_close_cnt_20 += 1
            print("chungbuk_apr_close_cnt_20", chungbuk_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            chungbuk_may_close_cnt_20 += 1
            print("chungbuk_may_close_cnt_20", chungbuk_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            chungbuk_jun_close_cnt_20 += 1
            print("chungbuk_jun_close_cnt_20", chungbuk_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            chungbuk_jul_close_cnt_20 += 1
            print("chungbuk_jul_close_cnt_20", chungbuk_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            chungbuk_aug_close_cnt_20 += 1
            print("chungbuk_aug_close_cnt_20", chungbuk_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            chungbuk_sep_close_cnt_20 += 1
            print("chungbuk_sep_close_cnt_20", chungbuk_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            chungbuk_oct_close_cnt_20 += 1
            print("chungbuk_oct_close_cnt_20", chungbuk_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            chungbuk_nov_close_cnt_20 += 1
            print("chungbuk_nov_close_cnt_20", chungbuk_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            chungbuk_dec_close_cnt_20 += 1
            print("chungbuk_dec_close_cnt_20", chungbuk_dec_close_cnt_20)
    for info in chungnam_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            chungnam_jan_close_cnt_20 += 1
            print("chungnam_jan_close_cnt_20", chungnam_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            chungnam_feb_close_cnt_20 += 1
            print("chungnam_feb_close_cnt_20", chungnam_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            chungnam_mar_close_cnt_20 += 1
            print("chungnam_mar_close_cnt_20", chungnam_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            chungnam_apr_close_cnt_20 += 1
            print("chungnam_apr_close_cnt_20", chungnam_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            chungnam_may_close_cnt_20 += 1
            print("chungnam_may_close_cnt_20", chungnam_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            chungnam_jun_close_cnt_20 += 1
            print("chungnam_jun_close_cnt_20", chungnam_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            chungnam_jul_close_cnt_20 += 1
            print("chungnam_jul_close_cnt_20", chungnam_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            chungnam_aug_close_cnt_20 += 1
            print("chungnam_aug_close_cnt_20", chungnam_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            chungnam_sep_close_cnt_20 += 1
            print("chungnam_sep_close_cnt_20", chungnam_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            chungnam_oct_close_cnt_20 += 1
            print("chungnam_oct_close_cnt_20", chungnam_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            chungnam_nov_close_cnt_20 += 1
            print("chungnam_nov_close_cnt_20", chungnam_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            chungnam_dec_close_cnt_20 += 1
            print("chungnam_dec_close_cnt_20", chungnam_dec_close_cnt_20)
    for info in daegu_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            daegu_jan_close_cnt_20 += 1
            print("daegu_jan_close_cnt_20", daegu_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            daegu_feb_close_cnt_20 += 1
            print("daegu_feb_close_cnt_20", daegu_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            daegu_mar_close_cnt_20 += 1
            print("daegu_mar_close_cnt_20", daegu_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            daegu_apr_close_cnt_20 += 1
            print("daegu_apr_close_cnt_20", daegu_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            daegu_may_close_cnt_20 += 1
            print("daegu_may_close_cnt_20", daegu_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            daegu_jun_close_cnt_20 += 1
            print("daegu_jun_close_cnt_20", daegu_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            daegu_jul_close_cnt_20 += 1
            print("daegu_jul_close_cnt_20", daegu_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            daegu_aug_close_cnt_20 += 1
            print("daegu_aug_close_cnt_20", daegu_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            daegu_sep_close_cnt_20 += 1
            print("daegu_sep_close_cnt_20", daegu_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            daegu_oct_close_cnt_20 += 1
            print("daegu_oct_close_cnt_20", daegu_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            daegu_nov_close_cnt_20 += 1
            print("daegu_nov_close_cnt_20", daegu_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            daegu_dec_close_cnt_20 += 1
            print("daegu_dec_close_cnt_20", daegu_dec_close_cnt_20)
    for info in daejeon_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            daejeon_jan_close_cnt_20 += 1
            print("daejeon_jan_close_cnt_20", daejeon_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            daejeon_feb_close_cnt_20 += 1
            print("daejeon_feb_close_cnt_20", daejeon_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            daejeon_mar_close_cnt_20 += 1
            print("daejeon_mar_close_cnt_20", daejeon_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            daejeon_apr_close_cnt_20 += 1
            print("daejeon_apr_close_cnt_20", daejeon_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            daejeon_may_close_cnt_20 += 1
            print("daejeon_may_close_cnt_20", daejeon_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            daejeon_jun_close_cnt_20 += 1
            print("daejeon_jun_close_cnt_20", daejeon_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            daejeon_jul_close_cnt_20 += 1
            print("daejeon_jul_close_cnt_20", daejeon_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            daejeon_aug_close_cnt_20 += 1
            print("daejeon_aug_close_cnt_20", daejeon_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            daejeon_sep_close_cnt_20 += 1
            print("daejeon_sep_close_cnt_20", daejeon_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            daejeon_oct_close_cnt_20 += 1
            print("daejeon_oct_close_cnt_20", daejeon_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            daejeon_nov_close_cnt_20 += 1
            print("daejeon_nov_close_cnt_20", daejeon_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            daejeon_dec_close_cnt_20 += 1
            print("daejeon_dec_close_cnt_20", daejeon_dec_close_cnt_20)
    for info in gangwon_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gangwon_jan_close_cnt_20 += 1
            print("gangwon_jan_close_cnt_20", gangwon_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            gangwon_feb_close_cnt_20 += 1
            print("gangwon_feb_close_cnt_20", gangwon_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            gangwon_mar_close_cnt_20 += 1
            print("gangwon_mar_close_cnt_20", gangwon_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            gangwon_apr_close_cnt_20 += 1
            print("gangwon_apr_close_cnt_20", gangwon_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            gangwon_may_close_cnt_20 += 1
            print("gangwon_may_close_cnt_20", gangwon_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            gangwon_jun_close_cnt_20 += 1
            print("gangwon_jun_close_cnt_20", gangwon_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            gangwon_jul_close_cnt_20 += 1
            print("gangwon_jul_close_cnt_20", gangwon_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            gangwon_aug_close_cnt_20 += 1
            print("gangwon_aug_close_cnt_20", gangwon_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            gangwon_sep_close_cnt_20 += 1
            print("gangwon_sep_close_cnt_20", gangwon_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            gangwon_oct_close_cnt_20 += 1
            print("gangwon_oct_close_cnt_20", gangwon_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            gangwon_nov_close_cnt_20 += 1
            print("gangwon_nov_close_cnt_20", gangwon_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            gangwon_dec_close_cnt_20 += 1
            print("gangwon_dec_close_cnt_20", gangwon_dec_close_cnt_20)
    for info in gwangju_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gwangju_jan_close_cnt_20 += 1
            print("gwangju_jan_close_cnt_20", gwangju_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            gwangju_feb_close_cnt_20 += 1
            print("gwangju_feb_close_cnt_20", gwangju_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            gwangju_mar_close_cnt_20 += 1
            print("gwangju_mar_close_cnt_20", gwangju_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            gwangju_apr_close_cnt_20 += 1
            print("gwangju_apr_close_cnt_20", gwangju_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            gwangju_may_close_cnt_20 += 1
            print("gwangju_may_close_cnt_20", gwangju_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            gwangju_jun_close_cnt_20 += 1
            print("gwangju_jun_close_cnt_20", gwangju_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            gwangju_jul_close_cnt_20 += 1
            print("gwangju_jul_close_cnt_20", gwangju_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            gwangju_aug_close_cnt_20 += 1
            print("gwangju_aug_close_cnt_20", gwangju_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            gwangju_sep_close_cnt_20 += 1
            print("gwangju_sep_close_cnt_20", gwangju_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            gwangju_oct_close_cnt_20 += 1
            print("gwangju_oct_close_cnt_20", gwangju_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            gwangju_nov_close_cnt_20 += 1
            print("gwangju_nov_close_cnt_20", gwangju_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            gwangju_dec_close_cnt_20 += 1
            print("gwangju_dec_close_cnt_20", gwangju_dec_close_cnt_20)
    for info in gyeonggi_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeonggi_jan_close_cnt_20 += 1
            print("gyeonggi_jan_close_cnt_20", gyeonggi_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            gyeonggi_feb_close_cnt_20 += 1
            print("gyeonggi_feb_close_cnt_20", gyeonggi_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            gyeonggi_mar_close_cnt_20 += 1
            print("gyeonggi_mar_close_cnt_20", gyeonggi_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            gyeonggi_apr_close_cnt_20 += 1
            print("gyeonggi_apr_close_cnt_20", gyeonggi_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            gyeonggi_may_close_cnt_20 += 1
            print("gyeonggi_may_close_cnt_20", gyeonggi_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            gyeonggi_jun_close_cnt_20 += 1
            print("gyeonggi_jun_close_cnt_20", gyeonggi_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            gyeonggi_jul_close_cnt_20 += 1
            print("gyeonggi_jul_close_cnt_20", gyeonggi_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            gyeonggi_aug_close_cnt_20 += 1
            print("gyeonggi_aug_close_cnt_20", gyeonggi_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            gyeonggi_sep_close_cnt_20 += 1
            print("gyeonggi_sep_close_cnt_20", gyeonggi_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            gyeonggi_oct_close_cnt_20 += 1
            print("gyeonggi_oct_close_cnt_20", gyeonggi_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            gyeonggi_nov_close_cnt_20 += 1
            print("gyeonggi_nov_close_cnt_20", gyeonggi_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            gyeonggi_dec_close_cnt_20 += 1
            print("gyeonggi_dec_close_cnt_20", gyeonggi_dec_close_cnt_20)
    for info in gyeongbuk_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeongbuk_jan_close_cnt_20 += 1
            print("gyeongbuk_jan_close_cnt_20", gyeongbuk_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            gyeongbuk_feb_close_cnt_20 += 1
            print("gyeongbuk_feb_close_cnt_20", gyeongbuk_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            gyeongbuk_mar_close_cnt_20 += 1
            print("gyeongbuk_mar_close_cnt_20", gyeongbuk_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            gyeongbuk_apr_close_cnt_20 += 1
            print("gyeongbuk_apr_close_cnt_20", gyeongbuk_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            gyeongbuk_may_close_cnt_20 += 1
            print("gyeongbuk_may_close_cnt_20", gyeongbuk_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            gyeongbuk_jun_close_cnt_20 += 1
            print("gyeongbuk_jun_close_cnt_20", gyeongbuk_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            gyeongbuk_jul_close_cnt_20 += 1
            print("gyeongbuk_jul_close_cnt_20", gyeongbuk_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            gyeongbuk_aug_close_cnt_20 += 1
            print("gyeongbuk_aug_close_cnt_20", gyeongbuk_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            gyeongbuk_sep_close_cnt_20 += 1
            print("gyeongbuk_sep_close_cnt_20", gyeongbuk_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            gyeongbuk_oct_close_cnt_20 += 1
            print("gyeongbuk_oct_close_cnt_20", gyeongbuk_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            gyeongbuk_nov_close_cnt_20 += 1
            print("gyeongbuk_nov_close_cnt_20", gyeongbuk_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            gyeongbuk_dec_close_cnt_20 += 1
            print("gyeongbuk_dec_close_cnt_20", gyeongbuk_dec_close_cnt_20)
    for info in gyeongnam_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            gyeongnam_jan_close_cnt_20 += 1
            print("gyeongnam_jan_close_cnt_20", gyeongnam_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            gyeongnam_feb_close_cnt_20 += 1
            print("gyeongnam_feb_close_cnt_20", gyeongnam_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            gyeongnam_mar_close_cnt_20 += 1
            print("gyeongnam_mar_close_cnt_20", gyeongnam_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            gyeongnam_apr_close_cnt_20 += 1
            print("gyeongnam_apr_close_cnt_20", gyeongnam_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            gyeongnam_may_close_cnt_20 += 1
            print("gyeongnam_may_close_cnt_20", gyeongnam_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            gyeongnam_jun_close_cnt_20 += 1
            print("gyeongnam_jun_close_cnt_20", gyeongnam_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            gyeongnam_jul_close_cnt_20 += 1
            print("gyeongnam_jul_close_cnt_20", gyeongnam_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            gyeongnam_aug_close_cnt_20 += 1
            print("gyeongnam_aug_close_cnt_20", gyeongnam_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            gyeongnam_sep_close_cnt_20 += 1
            print("gyeongnam_sep_close_cnt_20", gyeongnam_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            gyeongnam_oct_close_cnt_20 += 1
            print("gyeongnam_oct_close_cnt_20", gyeongnam_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            gyeongnam_nov_close_cnt_20 += 1
            print("gyeongnam_nov_close_cnt_20", gyeongnam_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            gyeongnam_dec_close_cnt_20 += 1
            print("gyeongnam_dec_close_cnt_20", gyeongnam_dec_close_cnt_20)
    for info in incheon_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            incheon_jan_close_cnt_20 += 1
            print("incheon_jan_close_cnt_20", incheon_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            incheon_feb_close_cnt_20 += 1
            print("incheon_feb_close_cnt_20", incheon_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            incheon_mar_close_cnt_20 += 1
            print("incheon_mar_close_cnt_20", incheon_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            incheon_apr_close_cnt_20 += 1
            print("incheon_apr_close_cnt_20", incheon_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            incheon_may_close_cnt_20 += 1
            print("incheon_may_close_cnt_20", incheon_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            incheon_jun_close_cnt_20 += 1
            print("incheon_jun_close_cnt_20", incheon_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            incheon_jul_close_cnt_20 += 1
            print("incheon_jul_close_cnt_20", incheon_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            incheon_aug_close_cnt_20 += 1
            print("incheon_aug_close_cnt_20", incheon_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            incheon_sep_close_cnt_20 += 1
            print("incheon_sep_close_cnt_20", incheon_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            incheon_oct_close_cnt_20 += 1
            print("incheon_oct_close_cnt_20", incheon_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            incheon_nov_close_cnt_20 += 1
            print("incheon_nov_close_cnt_20", incheon_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            incheon_dec_close_cnt_20 += 1
            print("incheon_dec_close_cnt_20", incheon_dec_close_cnt_20)
    for info in jeju_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeju_jan_close_cnt_20 += 1
            print("jeju_jan_close_cnt_20", jeju_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            jeju_feb_close_cnt_20 += 1
            print("jeju_feb_close_cnt_20", jeju_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            jeju_mar_close_cnt_20 += 1
            print("jeju_mar_close_cnt_20", jeju_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            jeju_apr_close_cnt_20 += 1
            print("jeju_apr_close_cnt_20", jeju_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            jeju_may_close_cnt_20 += 1
            print("jeju_may_close_cnt_20", jeju_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jeju_jun_close_cnt_20 += 1
            print("jeju_jun_close_cnt_20", jeju_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jeju_jul_close_cnt_20 += 1
            print("jeju_jul_close_cnt_20", jeju_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            jeju_aug_close_cnt_20 += 1
            print("jeju_aug_close_cnt_20", jeju_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            jeju_sep_close_cnt_20 += 1
            print("jeju_sep_close_cnt_20", jeju_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            jeju_oct_close_cnt_20 += 1
            print("jeju_oct_close_cnt_20", jeju_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            jeju_nov_close_cnt_20 += 1
            print("jeju_nov_close_cnt_20", jeju_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            jeju_dec_close_cnt_20 += 1
            print("jeju_dec_close_cnt_20", jeju_dec_close_cnt_20)
    for info in jeonbuk_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeonbuk_jan_close_cnt_20 += 1
            print("jeonbuk_jan_close_cnt_20", jeonbuk_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            jeonbuk_feb_close_cnt_20 += 1
            print("jeonbuk_feb_close_cnt_20", jeonbuk_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            jeonbuk_mar_close_cnt_20 += 1
            print("jeonbuk_mar_close_cnt_20", jeonbuk_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            jeonbuk_apr_close_cnt_20 += 1
            print("jeonbuk_apr_close_cnt_20", jeonbuk_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            jeonbuk_may_close_cnt_20 += 1
            print("jeonbuk_may_close_cnt_20", jeonbuk_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jeonbuk_jun_close_cnt_20 += 1
            print("jeonbuk_jun_close_cnt_20", jeonbuk_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jeonbuk_jul_close_cnt_20 += 1
            print("jeonbuk_jul_close_cnt_20", jeonbuk_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            jeonbuk_aug_close_cnt_20 += 1
            print("jeonbuk_aug_close_cnt_20", jeonbuk_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            jeonbuk_sep_close_cnt_20 += 1
            print("jeonbuk_sep_close_cnt_20", jeonbuk_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            jeonbuk_oct_close_cnt_20 += 1
            print("jeonbuk_oct_close_cnt_20", jeonbuk_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            jeonbuk_nov_close_cnt_20 += 1
            print("jeonbuk_nov_close_cnt_20", jeonbuk_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            jeonbuk_dec_close_cnt_20 += 1
            print("jeonbuk_dec_close_cnt_20", jeonbuk_dec_close_cnt_20)
    for info in jeonnam_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jeonnam_jan_close_cnt_20 += 1
            print("jeonnam_jan_close_cnt_20", jeonnam_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            jeonnam_feb_close_cnt_20 += 1
            print("jeonnam_feb_close_cnt_20", jeonnam_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            jeonnam_mar_close_cnt_20 += 1
            print("jeonnam_mar_close_cnt_20", jeonnam_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            jeonnam_apr_close_cnt_20 += 1
            print("jeonnam_apr_close_cnt_20", jeonnam_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            jeonnam_may_close_cnt_20 += 1
            print("jeonnam_may_close_cnt_20", jeonnam_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jeonnam_jun_close_cnt_20 += 1
            print("jeonnam_jun_close_cnt_20", jeonnam_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jeonnam_jul_close_cnt_20 += 1
            print("jeonnam_jul_close_cnt_20", jeonnam_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            jeonnam_aug_close_cnt_20 += 1
            print("jeonnam_aug_close_cnt_20", jeonnam_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            jeonnam_sep_close_cnt_20 += 1
            print("jeonnam_sep_close_cnt_20", jeonnam_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            jeonnam_oct_close_cnt_20 += 1
            print("jeonnam_oct_close_cnt_20", jeonnam_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            jeonnam_nov_close_cnt_20 += 1
            print("jeonnam_nov_close_cnt_20", jeonnam_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            jeonnam_dec_close_cnt_20 += 1
            print("jeonnam_dec_close_cnt_20", jeonnam_dec_close_cnt_20)
    for info in sejong_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            sejong_jan_close_cnt_20 += 1
            print("sejong_jan_close_cnt_20", sejong_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            sejong_feb_close_cnt_20 += 1
            print("sejong_feb_close_cnt_20", sejong_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            sejong_mar_close_cnt_20 += 1
            print("sejong_mar_close_cnt_20", sejong_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            sejong_apr_close_cnt_20 += 1
            print("sejong_apr_close_cnt_20", sejong_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            sejong_may_close_cnt_20 += 1
            print("sejong_may_close_cnt_20", sejong_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            sejong_jun_close_cnt_20 += 1
            print("sejong_jun_close_cnt_20", sejong_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            sejong_jul_close_cnt_20 += 1
            print("sejong_jul_close_cnt_20", sejong_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            sejong_aug_close_cnt_20 += 1
            print("sejong_aug_close_cnt_20", sejong_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sejong_sep_close_cnt_20 += 1
            print("sejong_sep_close_cnt_20", sejong_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            sejong_oct_close_cnt_20 += 1
            print("sejong_oct_close_cnt_20", sejong_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            sejong_nov_close_cnt_20 += 1
            print("sejong_nov_close_cnt_20", sejong_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            sejong_dec_close_cnt_20 += 1
            print("sejong_dec_close_cnt_20", sejong_dec_close_cnt_20)
    for info in seoul_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            seoul_jan_close_cnt_20 += 1
            print("seoul_jan_close_cnt_20", seoul_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            seoul_feb_close_cnt_20 += 1
            print("seoul_feb_close_cnt_20", seoul_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            seoul_mar_close_cnt_20 += 1
            print("seoul_mar_close_cnt_20", seoul_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            seoul_apr_close_cnt_20 += 1
            print("seoul_apr_close_cnt_20", seoul_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            seoul_may_close_cnt_20 += 1
            print("seoul_may_close_cnt_20", seoul_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            seoul_jun_close_cnt_20 += 1
            print("seoul_jun_close_cnt_20", seoul_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            seoul_jul_close_cnt_20 += 1
            print("seoul_jul_close_cnt_20", seoul_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            seoul_aug_close_cnt_20 += 1
            print("seoul_aug_close_cnt_20", seoul_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            seoul_sep_close_cnt_20 += 1
            print("seoul_sep_close_cnt_20", seoul_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            seoul_oct_close_cnt_20 += 1
            print("seoul_oct_close_cnt_20", seoul_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            seoul_nov_close_cnt_20 += 1
            print("seoul_nov_close_cnt_20", seoul_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            seoul_dec_close_cnt_20 += 1
            print("seoul_dec_close_cnt_20", seoul_dec_close_cnt_20)
    for info in ulsan_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            ulsan_jan_close_cnt_20 += 1
            print("ulsan_jan_close_cnt_20", ulsan_jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            ulsan_feb_close_cnt_20 += 1
            print("ulsan_feb_close_cnt_20", ulsan_feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            ulsan_mar_close_cnt_20 += 1
            print("ulsan_mar_close_cnt_20", ulsan_mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            ulsan_apr_close_cnt_20 += 1
            print("ulsan_apr_close_cnt_20", ulsan_apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            ulsan_may_close_cnt_20 += 1
            print("ulsan_may_close_cnt_20", ulsan_may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            ulsan_jun_close_cnt_20 += 1
            print("ulsan_jun_close_cnt_20", ulsan_jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            ulsan_jul_close_cnt_20 += 1
            print("ulsan_jul_close_cnt_20", ulsan_jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            ulsan_aug_close_cnt_20 += 1
            print("ulsan_aug_close_cnt_20", ulsan_aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            ulsan_sep_close_cnt_20 += 1
            print("ulsan_sep_close_cnt_20", ulsan_sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            ulsan_oct_close_cnt_20 += 1
            print("ulsan_oct_close_cnt_20", ulsan_oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            ulsan_nov_close_cnt_20 += 1
            print("ulsan_nov_close_cnt_20", ulsan_nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            ulsan_dec_close_cnt_20 += 1
            print("ulsan_dec_close_cnt_20", ulsan_dec_close_cnt_20)

    # 시도별 20년 open
    for info in busan_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            busan_jan_open_cnt_20 += 1
            print("busan_jan_open_cnt_20", busan_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            busan_feb_open_cnt_20 += 1
            print("busan_feb_open_cnt_20", busan_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            busan_mar_open_cnt_20 += 1
            print("busan_mar_open_cnt_20", busan_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            busan_apr_open_cnt_20 += 1
            print("busan_apr_open_cnt_20", busan_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            busan_may_open_cnt_20 += 1
            print("busan_may_open_cnt_20", busan_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            busan_jun_open_cnt_20 += 1
            print("busan_jun_open_cnt_20", busan_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            busan_jul_open_cnt_20 += 1
            print("busan_jul_open_cnt_20", busan_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            busan_aug_open_cnt_20 += 1
            print("busan_aug_open_cnt_20", busan_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            busan_sep_open_cnt_20 += 1
            print("busan_sep_open_cnt_20", busan_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            busan_oct_open_cnt_20 += 1
            print("busan_oct_open_cnt_20", busan_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            busan_nov_open_cnt_20 += 1
            print("busan_nov_open_cnt_20", busan_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            busan_dec_open_cnt_20 += 1
            print("busan_dec_open_cnt_20", busan_dec_open_cnt_20)
    for info in chungbuk_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            chungbuk_jan_open_cnt_20 += 1
            print("chungbuk_jan_open_cnt_20", chungbuk_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            chungbuk_feb_open_cnt_20 += 1
            print("chungbuk_feb_open_cnt_20", chungbuk_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            chungbuk_mar_open_cnt_20 += 1
            print("chungbuk_mar_open_cnt_20", chungbuk_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            chungbuk_apr_open_cnt_20 += 1
            print("chungbuk_apr_open_cnt_20", chungbuk_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            chungbuk_may_open_cnt_20 += 1
            print("chungbuk_may_open_cnt_20", chungbuk_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            chungbuk_jun_open_cnt_20 += 1
            print("chungbuk_jun_open_cnt_20", chungbuk_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            chungbuk_jul_open_cnt_20 += 1
            print("chungbuk_jul_open_cnt_20", chungbuk_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            chungbuk_aug_open_cnt_20 += 1
            print("chungbuk_aug_open_cnt_20", chungbuk_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            chungbuk_sep_open_cnt_20 += 1
            print("chungbuk_sep_open_cnt_20", chungbuk_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            chungbuk_oct_open_cnt_20 += 1
            print("chungbuk_oct_open_cnt_20", chungbuk_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            chungbuk_nov_open_cnt_20 += 1
            print("chungbuk_nov_open_cnt_20", chungbuk_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            chungbuk_dec_open_cnt_20 += 1
            print("chungbuk_dec_open_cnt_20", chungbuk_dec_open_cnt_20)
    for info in chungnam_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            chungnam_jan_open_cnt_20 += 1
            print("chungnam_jan_open_cnt_20", chungnam_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            chungnam_feb_open_cnt_20 += 1
            print("chungnam_feb_open_cnt_20", chungnam_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            chungnam_mar_open_cnt_20 += 1
            print("chungnam_mar_open_cnt_20", chungnam_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            chungnam_apr_open_cnt_20 += 1
            print("chungnam_apr_open_cnt_20", chungnam_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            chungnam_may_open_cnt_20 += 1
            print("chungnam_may_open_cnt_20", chungnam_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            chungnam_jun_open_cnt_20 += 1
            print("chungnam_jun_open_cnt_20", chungnam_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            chungnam_jul_open_cnt_20 += 1
            print("chungnam_jul_open_cnt_20", chungnam_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            chungnam_aug_open_cnt_20 += 1
            print("chungnam_aug_open_cnt_20", chungnam_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            chungnam_sep_open_cnt_20 += 1
            print("chungnam_sep_open_cnt_20", chungnam_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            chungnam_oct_open_cnt_20 += 1
            print("chungnam_oct_open_cnt_20", chungnam_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            chungnam_nov_open_cnt_20 += 1
            print("chungnam_nov_open_cnt_20", chungnam_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            chungnam_dec_open_cnt_20 += 1
            print("chungnam_dec_open_cnt_20", chungnam_dec_open_cnt_20)
    for info in daegu_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            daegu_jan_open_cnt_20 += 1
            print("daegu_jan_open_cnt_20", daegu_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            daegu_feb_open_cnt_20 += 1
            print("daegu_feb_open_cnt_20", daegu_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            daegu_mar_open_cnt_20 += 1
            print("daegu_mar_open_cnt_20", daegu_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            daegu_apr_open_cnt_20 += 1
            print("daegu_apr_open_cnt_20", daegu_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            daegu_may_open_cnt_20 += 1
            print("daegu_may_open_cnt_20", daegu_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            daegu_jun_open_cnt_20 += 1
            print("daegu_jun_open_cnt_20", daegu_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            daegu_jul_open_cnt_20 += 1
            print("daegu_jul_open_cnt_20", daegu_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            daegu_aug_open_cnt_20 += 1
            print("daegu_aug_open_cnt_20", daegu_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            daegu_sep_open_cnt_20 += 1
            print("daegu_sep_open_cnt_20", daegu_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            daegu_oct_open_cnt_20 += 1
            print("daegu_oct_open_cnt_20", daegu_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            daegu_nov_open_cnt_20 += 1
            print("daegu_nov_open_cnt_20", daegu_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            daegu_dec_open_cnt_20 += 1
            print("daegu_dec_open_cnt_20", daegu_dec_open_cnt_20)
    for info in daejeon_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            daejeon_jan_open_cnt_20 += 1
            print("daejeon_jan_open_cnt_20", daejeon_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            daejeon_feb_open_cnt_20 += 1
            print("daejeon_feb_open_cnt_20", daejeon_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            daejeon_mar_open_cnt_20 += 1
            print("daejeon_mar_open_cnt_20", daejeon_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            daejeon_apr_open_cnt_20 += 1
            print("daejeon_apr_open_cnt_20", daejeon_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            daejeon_may_open_cnt_20 += 1
            print("daejeon_may_open_cnt_20", daejeon_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            daejeon_jun_open_cnt_20 += 1
            print("daejeon_jun_open_cnt_20", daejeon_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            daejeon_jul_open_cnt_20 += 1
            print("daejeon_jul_open_cnt_20", daejeon_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            daejeon_aug_open_cnt_20 += 1
            print("daejeon_aug_open_cnt_20", daejeon_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            daejeon_sep_open_cnt_20 += 1
            print("daejeon_sep_open_cnt_20", daejeon_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            daejeon_oct_open_cnt_20 += 1
            print("daejeon_oct_open_cnt_20", daejeon_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            daejeon_nov_open_cnt_20 += 1
            print("daejeon_nov_open_cnt_20", daejeon_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            daejeon_dec_open_cnt_20 += 1
            print("daejeon_dec_open_cnt_20", daejeon_dec_open_cnt_20)
    for info in gangwon_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gangwon_jan_open_cnt_20 += 1
            print("gangwon_jan_open_cnt_20", gangwon_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            gangwon_feb_open_cnt_20 += 1
            print("gangwon_feb_open_cnt_20", gangwon_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            gangwon_mar_open_cnt_20 += 1
            print("gangwon_mar_open_cnt_20", gangwon_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            gangwon_apr_open_cnt_20 += 1
            print("gangwon_apr_open_cnt_20", gangwon_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            gangwon_may_open_cnt_20 += 1
            print("gangwon_may_open_cnt_20", gangwon_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            gangwon_jun_open_cnt_20 += 1
            print("gangwon_jun_open_cnt_20", gangwon_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            gangwon_jul_open_cnt_20 += 1
            print("gangwon_jul_open_cnt_20", gangwon_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            gangwon_aug_open_cnt_20 += 1
            print("gangwon_aug_open_cnt_20", gangwon_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            gangwon_sep_open_cnt_20 += 1
            print("gangwon_sep_open_cnt_20", gangwon_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            gangwon_oct_open_cnt_20 += 1
            print("gangwon_oct_open_cnt_20", gangwon_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            gangwon_nov_open_cnt_20 += 1
            print("gangwon_nov_open_cnt_20", gangwon_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            gangwon_dec_open_cnt_20 += 1
            print("gangwon_dec_open_cnt_20", gangwon_dec_open_cnt_20)
    for info in gwangju_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gwangju_jan_open_cnt_20 += 1
            print("gwangju_jan_open_cnt_20", gwangju_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            gwangju_feb_open_cnt_20 += 1
            print("gwangju_feb_open_cnt_20", gwangju_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            gwangju_mar_open_cnt_20 += 1
            print("gwangju_mar_open_cnt_20", gwangju_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            gwangju_apr_open_cnt_20 += 1
            print("gwangju_apr_open_cnt_20", gwangju_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            gwangju_may_open_cnt_20 += 1
            print("gwangju_may_open_cnt_20", gwangju_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            gwangju_jun_open_cnt_20 += 1
            print("gwangju_jun_open_cnt_20", gwangju_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            gwangju_jul_open_cnt_20 += 1
            print("gwangju_jul_open_cnt_20", gwangju_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            gwangju_aug_open_cnt_20 += 1
            print("gwangju_aug_open_cnt_20", gwangju_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            gwangju_sep_open_cnt_20 += 1
            print("gwangju_sep_open_cnt_20", gwangju_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            gwangju_oct_open_cnt_20 += 1
            print("gwangju_oct_open_cnt_20", gwangju_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            gwangju_nov_open_cnt_20 += 1
            print("gwangju_nov_open_cnt_20", gwangju_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            gwangju_dec_open_cnt_20 += 1
            print("gwangju_dec_open_cnt_20", gwangju_dec_open_cnt_20)
    for info in gyeonggi_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeonggi_jan_open_cnt_20 += 1
            print("gyeonggi_jan_open_cnt_20", gyeonggi_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            gyeonggi_feb_open_cnt_20 += 1
            print("gyeonggi_feb_open_cnt_20", gyeonggi_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            gyeonggi_mar_open_cnt_20 += 1
            print("gyeonggi_mar_open_cnt_20", gyeonggi_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            gyeonggi_apr_open_cnt_20 += 1
            print("gyeonggi_apr_open_cnt_20", gyeonggi_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            gyeonggi_may_open_cnt_20 += 1
            print("gyeonggi_may_open_cnt_20", gyeonggi_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            gyeonggi_jun_open_cnt_20 += 1
            print("gyeonggi_jun_open_cnt_20", gyeonggi_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            gyeonggi_jul_open_cnt_20 += 1
            print("gyeonggi_jul_open_cnt_20", gyeonggi_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            gyeonggi_aug_open_cnt_20 += 1
            print("gyeonggi_aug_open_cnt_20", gyeonggi_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            gyeonggi_sep_open_cnt_20 += 1
            print("gyeonggi_sep_open_cnt_20", gyeonggi_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            gyeonggi_oct_open_cnt_20 += 1
            print("gyeonggi_oct_open_cnt_20", gyeonggi_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            gyeonggi_nov_open_cnt_20 += 1
            print("gyeonggi_nov_open_cnt_20", gyeonggi_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            gyeonggi_dec_open_cnt_20 += 1
            print("gyeonggi_dec_open_cnt_20", gyeonggi_dec_open_cnt_20)
    for info in gyeongbuk_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeongbuk_jan_open_cnt_20 += 1
            print("gyeongbuk_jan_open_cnt_20", gyeongbuk_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            gyeongbuk_feb_open_cnt_20 += 1
            print("gyeongbuk_feb_open_cnt_20", gyeongbuk_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            gyeongbuk_mar_open_cnt_20 += 1
            print("gyeongbuk_mar_open_cnt_20", gyeongbuk_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            gyeongbuk_apr_open_cnt_20 += 1
            print("gyeongbuk_apr_open_cnt_20", gyeongbuk_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            gyeongbuk_may_open_cnt_20 += 1
            print("gyeongbuk_may_open_cnt_20", gyeongbuk_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            gyeongbuk_jun_open_cnt_20 += 1
            print("gyeongbuk_jun_open_cnt_20", gyeongbuk_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            gyeongbuk_jul_open_cnt_20 += 1
            print("gyeongbuk_jul_open_cnt_20", gyeongbuk_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            gyeongbuk_aug_open_cnt_20 += 1
            print("gyeongbuk_aug_open_cnt_20", gyeongbuk_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            gyeongbuk_sep_open_cnt_20 += 1
            print("gyeongbuk_sep_open_cnt_20", gyeongbuk_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            gyeongbuk_oct_open_cnt_20 += 1
            print("gyeongbuk_oct_open_cnt_20", gyeongbuk_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            gyeongbuk_nov_open_cnt_20 += 1
            print("gyeongbuk_nov_open_cnt_20", gyeongbuk_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            gyeongbuk_dec_open_cnt_20 += 1
            print("gyeongbuk_dec_open_cnt_20", gyeongbuk_dec_open_cnt_20)
    for info in gyeongnam_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            gyeongnam_jan_open_cnt_20 += 1
            print("gyeongnam_jan_open_cnt_20", gyeongnam_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            gyeongnam_feb_open_cnt_20 += 1
            print("gyeongnam_feb_open_cnt_20", gyeongnam_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            gyeongnam_mar_open_cnt_20 += 1
            print("gyeongnam_mar_open_cnt_20", gyeongnam_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            gyeongnam_apr_open_cnt_20 += 1
            print("gyeongnam_apr_open_cnt_20", gyeongnam_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            gyeongnam_may_open_cnt_20 += 1
            print("gyeongnam_may_open_cnt_20", gyeongnam_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            gyeongnam_jun_open_cnt_20 += 1
            print("gyeongnam_jun_open_cnt_20", gyeongnam_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            gyeongnam_jul_open_cnt_20 += 1
            print("gyeongnam_jul_open_cnt_20", gyeongnam_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            gyeongnam_aug_open_cnt_20 += 1
            print("gyeongnam_aug_open_cnt_20", gyeongnam_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            gyeongnam_sep_open_cnt_20 += 1
            print("gyeongnam_sep_open_cnt_20", gyeongnam_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            gyeongnam_oct_open_cnt_20 += 1
            print("gyeongnam_oct_open_cnt_20", gyeongnam_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            gyeongnam_nov_open_cnt_20 += 1
            print("gyeongnam_nov_open_cnt_20", gyeongnam_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            gyeongnam_dec_open_cnt_20 += 1
            print("gyeongnam_dec_open_cnt_20", gyeongnam_dec_open_cnt_20)
    for info in incheon_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            incheon_jan_open_cnt_20 += 1
            print("incheon_jan_open_cnt_20", incheon_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            incheon_feb_open_cnt_20 += 1
            print("incheon_feb_open_cnt_20", incheon_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            incheon_mar_open_cnt_20 += 1
            print("incheon_mar_open_cnt_20", incheon_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            incheon_apr_open_cnt_20 += 1
            print("incheon_apr_open_cnt_20", incheon_apr_close_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            incheon_may_open_cnt_20 += 1
            print("incheon_may_open_cnt_20", incheon_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            incheon_jun_open_cnt_20 += 1
            print("incheon_jun_open_cnt_20", incheon_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            incheon_jul_open_cnt_20 += 1
            print("incheon_jul_open_cnt_20", incheon_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            incheon_aug_open_cnt_20 += 1
            print("incheon_aug_open_cnt_20", incheon_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            incheon_sep_open_cnt_20 += 1
            print("incheon_sep_open_cnt_20", incheon_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            incheon_oct_open_cnt_20 += 1
            print("incheon_oct_open_cnt_20", incheon_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            incheon_nov_open_cnt_20 += 1
            print("incheon_nov_open_cnt_20", incheon_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            incheon_dec_open_cnt_20 += 1
            print("incheon_dec_open_cnt_20", incheon_dec_open_cnt_20)
    for info in jeju_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeju_jan_open_cnt_20 += 1
            print("jeju_jan_open_cnt_20", jeju_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            jeju_feb_open_cnt_20 += 1
            print("jeju_feb_open_cnt_20", jeju_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            jeju_mar_open_cnt_20 += 1
            print("jeju_mar_open_cnt_20", jeju_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            jeju_apr_open_cnt_20 += 1
            print("jeju_apr_open_cnt_20", jeju_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            jeju_may_open_cnt_20 += 1
            print("jeju_may_open_cnt_20", jeju_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jeju_jun_open_cnt_20 += 1
            print("jeju_jun_open_cnt_20", jeju_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jeju_jul_open_cnt_20 += 1
            print("jeju_jul_open_cnt_20", jeju_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            jeju_aug_open_cnt_20 += 1
            print("jeju_aug_open_cnt_20", jeju_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            jeju_sep_open_cnt_20 += 1
            print("jeju_sep_open_cnt_20", jeju_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            jeju_oct_open_cnt_20 += 1
            print("jeju_oct_open_cnt_20", jeju_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            jeju_nov_open_cnt_20 += 1
            print("jeju_nov_open_cnt_20", jeju_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            jeju_dec_open_cnt_20 += 1
            print("jeju_dec_open_cnt_20", jeju_dec_open_cnt_20)
    for info in jeonbuk_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeonbuk_jan_open_cnt_20 += 1
            print("jeonbuk_jan_open_cnt_20", jeonbuk_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            jeonbuk_feb_open_cnt_20 += 1
            print("jeonbuk_feb_open_cnt_20", jeonbuk_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            jeonbuk_mar_open_cnt_20 += 1
            print("jeonbuk_mar_open_cnt_20", jeonbuk_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            jeonbuk_apr_open_cnt_20 += 1
            print("jeonbuk_apr_open_cnt_20", jeonbuk_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            jeonbuk_may_open_cnt_20 += 1
            print("jeonbuk_may_open_cnt_20", jeonbuk_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jeonbuk_jun_open_cnt_20 += 1
            print("jeonbuk_jun_open_cnt_20", jeonbuk_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jeonbuk_jul_open_cnt_20 += 1
            print("jeonbuk_jul_open_cnt_20", jeonbuk_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            jeonbuk_aug_open_cnt_20 += 1
            print("jeonbuk_aug_open_cnt_20", jeonbuk_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            jeonbuk_sep_open_cnt_20 += 1
            print("jeonbuk_sep_open_cnt_20", jeonbuk_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            jeonbuk_oct_open_cnt_20 += 1
            print("jeonbuk_oct_open_cnt_20", jeonbuk_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            jeonbuk_nov_open_cnt_20 += 1
            print("jeonbuk_nov_open_cnt_20", jeonbuk_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            jeonbuk_dec_open_cnt_20 += 1
            print("jeonbuk_dec_open_cnt_20", jeonbuk_dec_open_cnt_20)
    for info in jeonnam_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jeonnam_jan_open_cnt_20 += 1
            print("jeonnam_jan_open_cnt_20", jeonnam_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            jeonnam_feb_open_cnt_20 += 1
            print("jeonnam_feb_open_cnt_20", jeonnam_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            jeonnam_mar_open_cnt_20 += 1
            print("jeonnam_mar_open_cnt_20", jeonnam_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            jeonnam_apr_open_cnt_20 += 1
            print("jeonnam_apr_open_cnt_20", jeonnam_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            jeonnam_may_open_cnt_20 += 1
            print("jeonnam_may_open_cnt_20", jeonnam_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jeonnam_jun_open_cnt_20 += 1
            print("jeonnam_jun_open_cnt_20", jeonnam_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jeonnam_jul_open_cnt_20 += 1
            print("jeonnam_jul_open_cnt_20", jeonnam_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            jeonnam_aug_open_cnt_20 += 1
            print("jeonnam_aug_open_cnt_20", jeonnam_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            jeonnam_sep_open_cnt_20 += 1
            print("jeonnam_sep_open_cnt_20", jeonnam_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            jeonnam_oct_open_cnt_20 += 1
            print("jeonnam_oct_open_cnt_20", jeonnam_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            jeonnam_nov_open_cnt_20 += 1
            print("jeonnam_nov_open_cnt_20", jeonnam_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            jeonnam_dec_open_cnt_20 += 1
            print("jeonnam_dec_open_cnt_20", jeonnam_dec_open_cnt_20)
    for info in sejong_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            sejong_jan_open_cnt_20 += 1
            print("sejong_jan_open_cnt_20", sejong_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            sejong_feb_open_cnt_20 += 1
            print("sejong_feb_open_cnt_20", sejong_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            sejong_mar_open_cnt_20 += 1
            print("sejong_mar_open_cnt_20", sejong_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            sejong_apr_open_cnt_20 += 1
            print("sejong_apr_open_cnt_20", sejong_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            sejong_may_open_cnt_20 += 1
            print("sejong_may_open_cnt_20", sejong_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            sejong_jun_open_cnt_20 += 1
            print("sejong_jun_open_cnt_20", sejong_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            sejong_jul_open_cnt_20 += 1
            print("sejong_jul_open_cnt_20", sejong_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            sejong_aug_open_cnt_20 += 1
            print("sejong_aug_open_cnt_20", sejong_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sejong_sep_open_cnt_20 += 1
            print("sejong_sep_open_cnt_20", sejong_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            sejong_oct_open_cnt_20 += 1
            print("sejong_oct_open_cnt_20", sejong_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            sejong_nov_open_cnt_20 += 1
            print("sejong_nov_open_cnt_20", sejong_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            sejong_dec_open_cnt_20 += 1
            print("sejong_dec_open_cnt_20", sejong_dec_open_cnt_20)
    for info in seoul_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            seoul_jan_open_cnt_20 += 1
            print("seoul_jan_open_cnt_20", seoul_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            seoul_feb_open_cnt_20 += 1
            print("seoul_feb_open_cnt_20", seoul_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            seoul_mar_open_cnt_20 += 1
            print("seoul_mar_open_cnt_20", seoul_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            seoul_apr_open_cnt_20 += 1
            print("seoul_apr_open_cnt_20", seoul_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            seoul_may_open_cnt_20 += 1
            print("seoul_may_open_cnt_20", seoul_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            seoul_jun_open_cnt_20 += 1
            print("seoul_jun_open_cnt_20", seoul_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            seoul_jul_open_cnt_20 += 1
            print("seoul_jul_open_cnt_20", seoul_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            seoul_aug_open_cnt_20 += 1
            print("seoul_aug_open_cnt_20", seoul_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            seoul_sep_open_cnt_20 += 1
            print("seoul_sep_open_cnt_20", seoul_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            seoul_oct_open_cnt_20 += 1
            print("seoul_oct_open_cnt_20", seoul_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            seoul_nov_open_cnt_20 += 1
            print("seoul_nov_open_cnt_20", seoul_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            seoul_dec_open_cnt_20 += 1
            print("seoul_dec_open_cnt_20", seoul_dec_open_cnt_20)
    for info in ulsan_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            ulsan_jan_open_cnt_20 += 1
            print("ulsan_jan_open_cnt_20", ulsan_jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            ulsan_feb_open_cnt_20 += 1
            print("ulsan_feb_open_cnt_20", ulsan_feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            ulsan_mar_open_cnt_20 += 1
            print("ulsan_mar_open_cnt_20", ulsan_mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            ulsan_apr_open_cnt_20 += 1
            print("ulsan_apr_open_cnt_20", ulsan_apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            ulsan_may_open_cnt_20 += 1
            print("ulsan_may_open_cnt_20", ulsan_may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            ulsan_jun_open_cnt_20 += 1
            print("ulsan_jun_open_cnt_20", ulsan_jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            ulsan_jul_open_cnt_20 += 1
            print("ulsan_jul_open_cnt_20", ulsan_jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            ulsan_aug_open_cnt_20 += 1
            print("ulsan_aug_open_cnt_20", ulsan_aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            ulsan_sep_open_cnt_20 += 1
            print("ulsan_sep_open_cnt_20", ulsan_sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            ulsan_oct_open_cnt_20 += 1
            print("ulsan_oct_open_cnt_20", ulsan_oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            ulsan_nov_open_cnt_20 += 1
            print("ulsan_nov_open_cnt_20", ulsan_nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            ulsan_dec_open_cnt_20 += 1
            print("ulsan_dec_open_cnt_20", ulsan_dec_open_cnt_20)

    my_api = {
        "title": "Location month data",
        "busan": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": busan_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": busan_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": busan_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": busan_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": busan_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": busan_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": busan_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": busan_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": busan_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": busan_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": busan_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": busan_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": busan_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": busan_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": busan_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": busan_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": busan_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": busan_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": busan_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": busan_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": busan_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": busan_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": busan_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": busan_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": busan_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": busan_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": busan_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": busan_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": busan_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": busan_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": busan_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": busan_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": busan_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": busan_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": busan_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": busan_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": busan_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": busan_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": busan_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": busan_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": busan_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": busan_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": busan_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": busan_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": busan_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": busan_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": busan_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": busan_dec_open_cnt_20
                },
            ]
        },
        "chungbuk": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungbuk_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungbuk_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungbuk_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungbuk_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungbuk_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungbuk_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungbuk_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungbuk_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungbuk_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungbuk_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungbuk_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungbuk_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungbuk_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungbuk_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungbuk_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungbuk_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungbuk_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungbuk_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungbuk_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungbuk_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungbuk_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungbuk_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungbuk_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungbuk_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungbuk_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungbuk_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungbuk_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungbuk_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungbuk_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungbuk_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungbuk_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungbuk_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungbuk_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungbuk_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungbuk_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungbuk_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungbuk_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungbuk_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungbuk_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungbuk_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungbuk_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungbuk_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungbuk_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungbuk_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungbuk_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungbuk_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungbuk_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungbuk_dec_open_cnt_20
                },
            ]
        },
        "chungnam": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungnam_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungnam_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungnam_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungnam_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungnam_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungnam_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungnam_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungnam_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungnam_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungnam_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungnam_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungnam_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungnam_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungnam_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungnam_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungnam_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungnam_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungnam_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungnam_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungnam_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungnam_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungnam_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungnam_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungnam_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungnam_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungnam_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungnam_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungnam_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungnam_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungnam_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungnam_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungnam_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungnam_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungnam_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungnam_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungnam_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": chungnam_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": chungnam_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": chungnam_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": chungnam_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": chungnam_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": chungnam_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": chungnam_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": chungnam_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": chungnam_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": chungnam_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": chungnam_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": chungnam_dec_open_cnt_20
                },
            ]
        },
        "daegu": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daegu_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daegu_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daegu_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daegu_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daegu_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daegu_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daegu_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daegu_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daegu_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daegu_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daegu_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daegu_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daegu_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daegu_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daegu_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daegu_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daegu_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daegu_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daegu_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daegu_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daegu_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daegu_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daegu_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daegu_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daegu_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daegu_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daegu_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daegu_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daegu_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daegu_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daegu_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daegu_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daegu_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daegu_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daegu_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daegu_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daegu_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daegu_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daegu_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daegu_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daegu_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daegu_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daegu_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daegu_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daegu_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daegu_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daegu_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daegu_dec_open_cnt_20
                },
            ]
        },
        "daejeon": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daejeon_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daejeon_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daejeon_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daejeon_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daejeon_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daejeon_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daejeon_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daejeon_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daejeon_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daejeon_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daejeon_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daejeon_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daejeon_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daejeon_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daejeon_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daejeon_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daejeon_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daejeon_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daejeon_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daejeon_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daejeon_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daejeon_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daejeon_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daejeon_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daejeon_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daejeon_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daejeon_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daejeon_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daejeon_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daejeon_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daejeon_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daejeon_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daejeon_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daejeon_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daejeon_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daejeon_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": daejeon_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": daejeon_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": daejeon_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": daejeon_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": daejeon_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": daejeon_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": daejeon_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": daejeon_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": daejeon_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": daejeon_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": daejeon_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": daejeon_dec_open_cnt_20
                },
            ]
        },
        "gangwon": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gangwon_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gangwon_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gangwon_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gangwon_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gangwon_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gangwon_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gangwon_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gangwon_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gangwon_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gangwon_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gangwon_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gangwon_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gangwon_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gangwon_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gangwon_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gangwon_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gangwon_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gangwon_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gangwon_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gangwon_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gangwon_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gangwon_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gangwon_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gangwon_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gangwon_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gangwon_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gangwon_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gangwon_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gangwon_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gangwon_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gangwon_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gangwon_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gangwon_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gangwon_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gangwon_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gangwon_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gangwon_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gangwon_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gangwon_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gangwon_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gangwon_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gangwon_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gangwon_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gangwon_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gangwon_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gangwon_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gangwon_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gangwon_dec_open_cnt_20
                },
            ]
        },
        "gwangju": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gwangju_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gwangju_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gwangju_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gwangju_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gwangju_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gwangju_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gwangju_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gwangju_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gwangju_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gwangju_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gwangju_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gwangju_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gwangju_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gwangju_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gwangju_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gwangju_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gwangju_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gwangju_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gwangju_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gwangju_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gwangju_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gwangju_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gwangju_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gwangju_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gwangju_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gwangju_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gwangju_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gwangju_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gwangju_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gwangju_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gwangju_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gwangju_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gwangju_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gwangju_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gwangju_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gwangju_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gwangju_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gwangju_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gwangju_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gwangju_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gwangju_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gwangju_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gwangju_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gwangju_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gwangju_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gwangju_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gwangju_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gwangju_dec_open_cnt_20
                },
            ]
        },
        "gyeonggi": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeonggi_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeonggi_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeonggi_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeonggi_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeonggi_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeonggi_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeonggi_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeonggi_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeonggi_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeonggi_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeonggi_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeonggi_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeonggi_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeonggi_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeonggi_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeonggi_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeonggi_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeonggi_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeonggi_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeonggi_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeonggi_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeonggi_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeonggi_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeonggi_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeonggi_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeonggi_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeonggi_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeonggi_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeonggi_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeonggi_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeonggi_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeonggi_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeonggi_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeonggi_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeonggi_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeonggi_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeonggi_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeonggi_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeonggi_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeonggi_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeonggi_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeonggi_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeonggi_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeonggi_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeonggi_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeonggi_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeonggi_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeonggi_dec_open_cnt_20
                },
            ]
        },
        "gyeongbuk": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongbuk_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongbuk_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongbuk_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongbuk_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongbuk_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongbuk_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongbuk_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongbuk_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongbuk_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongbuk_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongbuk_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongbuk_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongbuk_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongbuk_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongbuk_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongbuk_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongbuk_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongbuk_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongbuk_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongbuk_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongbuk_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongbuk_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongbuk_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongbuk_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongbuk_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongbuk_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongbuk_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongbuk_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongbuk_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongbuk_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongbuk_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongbuk_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongbuk_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongbuk_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongbuk_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongbuk_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongbuk_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongbuk_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongbuk_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongbuk_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongbuk_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongbuk_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongbuk_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongbuk_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongbuk_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongbuk_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongbuk_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongbuk_dec_open_cnt_20
                },
            ]
        },
        "gyeongnam": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongnam_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongnam_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongnam_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongnam_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongnam_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongnam_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongnam_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongnam_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongnam_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongnam_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongnam_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongnam_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongnam_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongnam_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongnam_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongnam_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongnam_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongnam_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongnam_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongnam_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongnam_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongnam_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongnam_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongnam_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongnam_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongnam_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongnam_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongnam_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongnam_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongnam_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongnam_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongnam_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongnam_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongnam_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongnam_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongnam_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": gyeongnam_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": gyeongnam_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": gyeongnam_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": gyeongnam_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": gyeongnam_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": gyeongnam_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": gyeongnam_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": gyeongnam_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": gyeongnam_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": gyeongnam_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": gyeongnam_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": gyeongnam_dec_open_cnt_20
                },
            ]
        },
        "incheon": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": incheon_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": incheon_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": incheon_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": incheon_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": incheon_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": incheon_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": incheon_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": incheon_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": incheon_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": incheon_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": incheon_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": incheon_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": incheon_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": incheon_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": incheon_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": incheon_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": incheon_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": incheon_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": incheon_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": incheon_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": incheon_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": incheon_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": incheon_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": incheon_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": incheon_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": incheon_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": incheon_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": incheon_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": incheon_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": incheon_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": incheon_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": incheon_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": incheon_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": incheon_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": incheon_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": incheon_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": incheon_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": incheon_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": incheon_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": incheon_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": incheon_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": incheon_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": incheon_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": incheon_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": incheon_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": incheon_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": incheon_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": incheon_dec_open_cnt_20
                },
            ]
        },
        "jeju": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeju_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeju_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeju_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeju_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeju_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeju_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeju_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeju_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeju_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeju_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeju_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeju_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeju_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeju_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeju_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeju_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeju_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeju_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeju_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeju_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeju_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeju_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeju_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeju_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeju_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeju_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeju_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeju_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeju_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeju_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeju_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeju_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeju_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeju_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeju_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeju_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeju_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeju_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeju_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeju_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeju_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeju_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeju_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeju_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeju_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeju_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeju_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeju_dec_open_cnt_20
                },
            ]
        },
        "jeonbuk": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonbuk_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonbuk_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonbuk_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonbuk_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonbuk_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonbuk_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonbuk_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonbuk_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonbuk_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonbuk_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonbuk_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonbuk_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonbuk_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonbuk_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonbuk_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonbuk_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonbuk_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonbuk_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonbuk_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonbuk_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonbuk_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonbuk_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonbuk_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonbuk_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonbuk_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonbuk_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonbuk_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonbuk_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonbuk_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonbuk_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonbuk_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonbuk_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonbuk_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonbuk_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonbuk_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonbuk_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonbuk_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonbuk_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonbuk_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonbuk_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonbuk_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonbuk_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonbuk_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonbuk_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonbuk_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonbuk_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonbuk_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonbuk_dec_open_cnt_20
                },
            ]
        },
        "jeonnam": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonnam_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonnam_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonnam_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonnam_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonnam_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonnam_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonnam_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonnam_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonnam_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonnam_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonnam_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonnam_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonnam_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonnam_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonnam_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonnam_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonnam_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonnam_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonnam_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonnam_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonnam_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonnam_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonnam_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonnam_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonnam_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonnam_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonnam_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonnam_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonnam_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonnam_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonnam_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonnam_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonnam_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonnam_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonnam_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonnam_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": jeonnam_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": jeonnam_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": jeonnam_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": jeonnam_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": jeonnam_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": jeonnam_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": jeonnam_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": jeonnam_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": jeonnam_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": jeonnam_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": jeonnam_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": jeonnam_dec_open_cnt_20
                },
            ]
        },
        "sejong": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": sejong_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": sejong_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": sejong_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": sejong_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": sejong_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": sejong_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": sejong_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": sejong_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": sejong_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": sejong_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": sejong_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": sejong_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": sejong_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": sejong_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": sejong_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": sejong_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": sejong_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": sejong_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": sejong_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": sejong_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": sejong_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": sejong_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": sejong_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": sejong_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": sejong_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": sejong_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": sejong_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": sejong_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": sejong_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": sejong_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": sejong_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": sejong_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": sejong_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": sejong_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": sejong_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": sejong_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": sejong_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": sejong_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": sejong_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": sejong_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": sejong_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": sejong_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": sejong_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": sejong_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": sejong_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": sejong_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": sejong_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": sejong_dec_open_cnt_20
                },
            ]
        },
        "seoul": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": seoul_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": seoul_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": seoul_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": seoul_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": seoul_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": seoul_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": seoul_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": seoul_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": seoul_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": seoul_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": seoul_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": seoul_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": seoul_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": seoul_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": seoul_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": seoul_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": seoul_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": seoul_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": seoul_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": seoul_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": seoul_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": seoul_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": seoul_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": seoul_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": seoul_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": seoul_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": seoul_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": seoul_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": seoul_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": seoul_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": seoul_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": seoul_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": seoul_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": seoul_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": seoul_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": seoul_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": seoul_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": seoul_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": seoul_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": seoul_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": seoul_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": seoul_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": seoul_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": seoul_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": seoul_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": seoul_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": seoul_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": seoul_dec_open_cnt_20
                },
            ]
        },
        "ulsan": {
            "month_close_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": ulsan_jan_close_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": ulsan_feb_close_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": ulsan_mar_close_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": ulsan_apr_close_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": ulsan_may_close_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": ulsan_jun_close_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": ulsan_jul_close_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": ulsan_aug_close_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": ulsan_sep_close_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": ulsan_oct_close_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": ulsan_nov_close_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": ulsan_dec_close_cnt_19
                },
            ],
            "month_close_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": ulsan_jan_close_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": ulsan_feb_close_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": ulsan_mar_close_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": ulsan_apr_close_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": ulsan_may_close_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": ulsan_jun_close_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": ulsan_jul_close_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": ulsan_aug_close_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": ulsan_sep_close_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": ulsan_oct_close_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": ulsan_nov_close_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": ulsan_dec_close_cnt_20
                },
            ],
            "month_open_19": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": ulsan_jan_open_cnt_19
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": ulsan_feb_open_cnt_19
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": ulsan_mar_open_cnt_19
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": ulsan_apr_open_cnt_19
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": ulsan_may_open_cnt_19
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": ulsan_jun_open_cnt_19
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": ulsan_jul_open_cnt_19
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": ulsan_aug_open_cnt_19
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": ulsan_sep_open_cnt_19
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": ulsan_oct_open_cnt_19
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": ulsan_nov_open_cnt_19
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": ulsan_dec_open_cnt_19
                },
            ],
            "month_open_20": [
                {
                    "month": "January",
                    "month_str": "01",
                    "month_num": 1,
                    "abbreviations": "Jan.",
                    "count": ulsan_jan_open_cnt_20
                },
                {
                    "month": "February",
                    "month_str": "02",
                    "month_num": 2,
                    "abbreviations": "Feb.",
                    "count": ulsan_feb_open_cnt_20
                },
                {
                    "month": "March",
                    "month_str": "03",
                    "month_num": 3,
                    "abbreviations": "Mar.",
                    "count": ulsan_mar_open_cnt_20
                },
                {
                    "month": "April",
                    "month_str": "04",
                    "month_num": 4,
                    "abbreviations": "Apr.",
                    "count": ulsan_apr_open_cnt_20
                },
                {
                    "month": "May",
                    "month_str": "05",
                    "month_num": 5,
                    "abbreviations": "May",
                    "count": ulsan_may_open_cnt_20
                },
                {
                    "month": "June",
                    "month_str": "06",
                    "month_num": 6,
                    "abbreviations": "Jun.",
                    "count": ulsan_jun_open_cnt_20
                },
                {
                    "month": "July",
                    "month_str": "07",
                    "month_num": 7,
                    "abbreviations": "Jul.",
                    "count": ulsan_jul_open_cnt_20
                },
                {
                    "month": "August",
                    "month_str": "08",
                    "month_num": 8,
                    "abbreviations": "Aug.",
                    "count": ulsan_aug_open_cnt_20
                },
                {
                    "month": "September",
                    "month_str": "09",
                    "month_num": 9,
                    "abbreviations": "Sep.",
                    "count": ulsan_sep_open_cnt_20
                },
                {
                    "month": "October",
                    "month_str": "10",
                    "month_num": 10,
                    "abbreviations": "Oct.",
                    "count": ulsan_oct_open_cnt_20
                },
                {
                    "month": "November",
                    "month_str": "11",
                    "month_num": 11,
                    "abbreviations": "Nov.",
                    "count": ulsan_nov_open_cnt_20
                },
                {
                    "month": "December",
                    "month_str": "12",
                    "month_num": 12,
                    "abbreviations": "Dec.",
                    "count": ulsan_dec_open_cnt_20
                },
            ]
        },
    }
    local_main_api = db['local_data_api']
    print("my_api", my_api)

    my_api_id = local_main_api.insert_one(my_api).inserted_id
    print(my_api_id)


data()
