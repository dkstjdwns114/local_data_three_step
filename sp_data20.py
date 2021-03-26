from pymongo import MongoClient
from multiprocessing import Process

client = MongoClient('localhost', 27017)

localData20 = client['localData20']

theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']

theoremLocalDataLocationClose20 = client['theoremLocalDataLocationClose20']
theoremLocalDataLocationOpen20 = client['theoremLocalDataLocationOpen20']


def accommodation_close():
    data = localData20['accommodation_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def accommodation_open():
    data = localData20['accommodation_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def animal_close():
    data = localData20['animal_close']
    culture = theoremLocalDataClose20.animal
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def animal_open():
    data = localData20['animal_open']
    culture = theoremLocalDataOpen20.animal
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def animal_husbandry_close():
    data = localData20['animal_husbandry_close']
    culture = theoremLocalDataClose20.animal
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def animal_husbandry_open():
    data = localData20['animal_husbandry_open']
    culture = theoremLocalDataOpen20.animal
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def bathhouse_close():
    data = localData20['bathhouse_close']
    culture = theoremLocalDataClose20.life
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def bathhouse_open():
    data = localData20['bathhouse_open']
    culture = theoremLocalDataOpen20.life
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def cigarette_close():
    data = localData20['cigarette_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def cigarette_open():
    data = localData20['cigarette_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def civil_defense_close():
    data = localData20['civil_defense_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def civil_defense_open():
    data = localData20['civil_defense_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def cultural_planning_close():
    data = localData20['cultural_planning_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def cultural_planning_open():
    data = localData20['cultural_planning_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def distribution_close():
    data = localData20['distribution_close']
    culture = theoremLocalDataClose20.life
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def distribution_open():
    data = localData20['distribution_open']
    culture = theoremLocalDataOpen20.life
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def educational_institutions_close():
    data = localData20['educational_institutions_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def educational_institutions_open():
    data = localData20['educational_institutions_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def elevator_close():
    data = localData20['elevator_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def elevator_open():
    data = localData20['elevator_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def energy_close():
    data = localData20['energy_close']
    culture = theoremLocalDataClose20.environment
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def energy_open():
    data = localData20['energy_open']
    culture = theoremLocalDataOpen20.environment
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def entertainment_bar_close():
    data = localData20['entertainment_bar_close']
    culture = theoremLocalDataClose20.food
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def entertainment_bar_open():
    data = localData20['entertainment_bar_open']
    culture = theoremLocalDataOpen20.food
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def environmental_management_close():
    data = localData20['environmental_management_close']
    culture = theoremLocalDataClose20.environment
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def environmental_management_open():
    data = localData20['environmental_management_open']
    culture = theoremLocalDataOpen20.environment
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def food_close():
    data = localData20['food_close']
    culture = theoremLocalDataClose20.food
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def food_open():
    data = localData20['food_open']
    culture = theoremLocalDataOpen20.food
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def funeral_close():
    data = localData20['funeral_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def funeral_open():
    data = localData20['funeral_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def game_close():
    data = localData20['game_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def game_open():
    data = localData20['game_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def groundwater_close():
    data = localData20['groundwater_close']
    culture = theoremLocalDataClose20.environment
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def groundwater_open():
    data = localData20['game_open']
    culture = theoremLocalDataOpen20.environment
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def health_close():
    data = localData20['health_close']
    culture = theoremLocalDataClose20.health
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def health_open():
    data = localData20['health_open']
    culture = theoremLocalDataOpen20.health
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def karaoke_close():
    data = localData20['karaoke_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def karaoke_open():
    data = localData20['karaoke_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def laundry_close():
    data = localData20['laundry_close']
    culture = theoremLocalDataClose20.life
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def laundry_open():
    data = localData20['laundry_open']
    culture = theoremLocalDataOpen20.life
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def logistics_close():
    data = localData20['logistics_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def logistics_open():
    data = localData20['logistics_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def media_close():
    data = localData20['media_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def media_open():
    data = localData20['media_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def movie_close():
    data = localData20['movie_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def movie_open():
    data = localData20['movie_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def music_close():
    data = localData20['music_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def music_open():
    data = localData20['music_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def office_support_close():
    data = localData20['office_support_close']
    culture = theoremLocalDataClose20.other
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def office_support_open():
    data = localData20['office_support_open']
    culture = theoremLocalDataOpen20.other
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def physical_education_close():
    data = localData20['physical_education_close']
    culture = theoremLocalDataClose20.life
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def physical_education_open():
    data = localData20['physical_education_open']
    culture = theoremLocalDataOpen20.life
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def salon_close():
    data = localData20['salon_close']
    culture = theoremLocalDataClose20.life
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def salon_open():
    data = localData20['salon_open']
    culture = theoremLocalDataOpen20.life
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def school_meals_close():
    data = localData20['school_meals_close']
    culture = theoremLocalDataClose20.food
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def school_meals_open():
    data = localData20['school_meals_open']
    culture = theoremLocalDataOpen20.food
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def show_close():
    data = localData20['show_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def show_open():
    data = localData20['show_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def tourism_close():
    data = localData20['tourism_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def tourism_open():
    data = localData20['tourism_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def travel_close():
    data = localData20['travel_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def travel_open():
    data = localData20['travel_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def video_close():
    data = localData20['video_close']
    culture = theoremLocalDataClose20.culture
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def video_open():
    data = localData20['video_open']
    culture = theoremLocalDataOpen20.culture
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def wood_close():
    data = localData20['wood_close']
    culture = theoremLocalDataClose20.environment
    busan = theoremLocalDataLocationClose20.busan
    chungbuk = theoremLocalDataLocationClose20.chungbuk
    chungnam = theoremLocalDataLocationClose20.chungnam
    daegu = theoremLocalDataLocationClose20.daegu
    daejeon = theoremLocalDataLocationClose20.daejeon
    gangwon = theoremLocalDataLocationClose20.gangwon
    gwangju = theoremLocalDataLocationClose20.gwangju
    gyeonggi = theoremLocalDataLocationClose20.gyeonggi
    gyeongbuk = theoremLocalDataLocationClose20.gyeongbuk
    gyeongnam = theoremLocalDataLocationClose20.gyeongnam
    incheon = theoremLocalDataLocationClose20.incheon
    jeju = theoremLocalDataLocationClose20.jeju
    jeonbuk = theoremLocalDataLocationClose20.jeonbuk
    jeonnam = theoremLocalDataLocationClose20.jeonnam
    sejong = theoremLocalDataLocationClose20.sejong
    seoul = theoremLocalDataLocationClose20.seoul
    ulsan = theoremLocalDataLocationClose20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


def wood_open():
    data = localData20['wood_open']
    culture = theoremLocalDataOpen20.environment
    busan = theoremLocalDataLocationOpen20.busan
    chungbuk = theoremLocalDataLocationOpen20.chungbuk
    chungnam = theoremLocalDataLocationOpen20.chungnam
    daegu = theoremLocalDataLocationOpen20.daegu
    daejeon = theoremLocalDataLocationOpen20.daejeon
    gangwon = theoremLocalDataLocationOpen20.gangwon
    gwangju = theoremLocalDataLocationOpen20.gwangju
    gyeonggi = theoremLocalDataLocationOpen20.gyeonggi
    gyeongbuk = theoremLocalDataLocationOpen20.gyeongbuk
    gyeongnam = theoremLocalDataLocationOpen20.gyeongnam
    incheon = theoremLocalDataLocationOpen20.incheon
    jeju = theoremLocalDataLocationOpen20.jeju
    jeonbuk = theoremLocalDataLocationOpen20.jeonbuk
    jeonnam = theoremLocalDataLocationOpen20.jeonnam
    sejong = theoremLocalDataLocationOpen20.sejong
    seoul = theoremLocalDataLocationOpen20.seoul
    ulsan = theoremLocalDataLocationOpen20.ulsan

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)

        if store['address'].split(' ')[0] == "부산광역시":
            insert_data = busan.insert_one(store)
        elif store['address'].split(' ')[0] == "충청북도":
            insert_data = chungbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "충청남도":
            insert_data = chungnam.insert_one(store)
        elif store['address'].split(' ')[0] == "대구광역시":
            insert_data = daegu.insert_one(store)
        elif store['address'].split(' ')[0] == "대전광역시":
            insert_data = daejeon.insert_one(store)
        elif store['address'].split(' ')[0] == "강원도":
            insert_data = gangwon.insert_one(store)
        elif store['address'].split(' ')[0] == "광주광역시":
            insert_data = gwangju.insert_one(store)
        elif store['address'].split(' ')[0] == "경기도":
            insert_data = gyeonggi.insert_one(store)
        elif store['address'].split(' ')[0] == "경상북도":
            insert_data = gyeongbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "경상남도":
            insert_data = gyeongnam.insert_one(store)
        elif store['address'].split(' ')[0] == "인천광역시":
            insert_data = incheon.insert_one(store)
        elif store['address'].split(' ')[0] == "제주특별자치도":
            insert_data = jeju.insert_one(store)
        elif store['address'].split(' ')[0] == "전라북도":
            insert_data = jeonbuk.insert_one(store)
        elif store['address'].split(' ')[0] == "전라남도":
            insert_data = jeonnam.insert_one(store)
        elif store['address'].split(' ')[0] == "세종특별자치시":
            insert_data = sejong.insert_one(store)
        elif store['address'].split(' ')[0] == "서울특별시":
            insert_data = seoul.insert_one(store)
        elif store['address'].split(' ')[0] == "울산광역시":
            insert_data = ulsan.insert_one(store)


'''
if __name__ == "__main__":
    p1 = Process(target=accommodation_close)
    p2 = Process(target=accommodation_open)
    p3 = Process(target=animal_close)
    p4 = Process(target=animal_open)
    p5 = Process(target=animal_husbandry_close)
    p6 = Process(target=animal_husbandry_open)
    p7 = Process(target=bathhouse_close)
    p8 = Process(target=bathhouse_open)
    p9 = Process(target=cigarette_close)
    p10 = Process(target=cigarette_open)
    p11 = Process(target=civil_defense_close)
    p12 = Process(target=civil_defense_open)
    p13 = Process(target=cultural_planning_close)
    p14 = Process(target=cultural_planning_open)
    p15 = Process(target=distribution_close)
    p16 = Process(target=distribution_open)
    p17 = Process(target=educational_institutions_close)
    p18 = Process(target=educational_institutions_open)
    p19 = Process(target=elevator_close)
    p20 = Process(target=elevator_open)
    p21 = Process(target=energy_close)
    p22 = Process(target=energy_open)
    p23 = Process(target=entertainment_bar_close)
    p24 = Process(target=entertainment_bar_open)
    p25 = Process(target=environmental_management_close)
    p26 = Process(target=environmental_management_open)
    p27 = Process(target=food_close)
    p28 = Process(target=food_open)
    p29 = Process(target=funeral_close)
    p30 = Process(target=funeral_open)
    p31 = Process(target=game_close)
    p32 = Process(target=game_open)
    p33 = Process(target=groundwater_close)
    p34 = Process(target=groundwater_open)
    p35 = Process(target=health_close)
    p36 = Process(target=health_open)
    p37 = Process(target=karaoke_close)
    p38 = Process(target=karaoke_open)
    p39 = Process(target=laundry_close)
    p40 = Process(target=laundry_open)
    p41 = Process(target=logistics_close)
    p42 = Process(target=logistics_open)
    p43 = Process(target=media_close)
    p44 = Process(target=media_open)
    p45 = Process(target=movie_close)
    p46 = Process(target=movie_open)
    p47 = Process(target=music_close)
    p48 = Process(target=music_open)
    p49 = Process(target=office_support_close)
    p50 = Process(target=office_support_open)
    p51 = Process(target=physical_education_close)
    p52 = Process(target=physical_education_open)
    p53 = Process(target=salon_close)
    p54 = Process(target=salon_open)
    p55 = Process(target=school_meals_close)
    p56 = Process(target=school_meals_open)
    p57 = Process(target=show_close)
    p58 = Process(target=show_open)
    p59 = Process(target=tourism_close)
    p60 = Process(target=tourism_open)
    p61 = Process(target=travel_close)
    p62 = Process(target=travel_open)
    p63 = Process(target=video_close)
    p64 = Process(target=video_open)
    p65 = Process(target=wood_close)
    p66 = Process(target=wood_open)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    p21.start()
    p22.start()
    p23.start()
    p24.start()
    p25.start()
    p26.start()
    p27.start()
    p28.start()
    p29.start()
    p30.start()
    p31.start()
    p32.start()
    p33.start()
    p34.start()
    p35.start()
    p36.start()
    p37.start()
    p38.start()
    p39.start()
    p40.start()
    p41.start()
    p42.start()
    p43.start()
    p44.start()
    p45.start()
    p46.start()
    p47.start()
    p48.start()
    p49.start()
    p50.start()
    p51.start()
    p52.start()
    p53.start()
    p54.start()
    p55.start()
    p56.start()
    p57.start()
    p58.start()
    p59.start()
    p60.start()
    p61.start()
    p62.start()
    p63.start()
    p64.start()
    p65.start()
    p66.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    p19.join()
    p20.join()
    p21.join()
    p22.join()
    p23.join()
    p24.join()
    p25.join()
    p26.join()
    p27.join()
    p28.join()
    p29.join()
    p30.join()
    p31.join()
    p32.join()
    p33.join()
    p34.join()
    p35.join()
    p36.join()
    p37.join()
    p38.join()
    p39.join()
    p40.join()
    p41.join()
    p42.join()
    p43.join()
    p44.join()
    p45.join()
    p46.join()
    p47.join()
    p48.join()
    p49.join()
    p50.join()
    p51.join()
    p52.join()
    p53.join()
    p54.join()
    p55.join()
    p56.join()
    p57.join()
    p58.join()
    p59.join()
    p60.join()
    p61.join()
    p62.join()
    p63.join()
    p64.join()
    p65.join()
    p66.join()
'''
