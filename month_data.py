from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]
cluster_collection = db['seoul20']

client = MongoClient("localhost", 27017)

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']


def data():
    # 19년 업종별 close
    animal_close_19 = theoremLocalDataClose19['animal']
    culture_close_19 = theoremLocalDataClose19['culture']
    environment_close_19 = theoremLocalDataClose19['environment']
    food_close_19 = theoremLocalDataClose19['food']
    health_close_19 = theoremLocalDataClose19['health']
    life_close_19 = theoremLocalDataClose19['life']
    other_close_19 = theoremLocalDataClose19['other']
    # 19년 업종별 open
    animal_open_19 = theoremLocalDataOpen19['animal']
    culture_open_19 = theoremLocalDataOpen19['culture']
    environment_open_19 = theoremLocalDataOpen19['environment']
    food_open_19 = theoremLocalDataOpen19['food']
    health_open_19 = theoremLocalDataOpen19['health']
    life_open_19 = theoremLocalDataOpen19['life']
    other_open_19 = theoremLocalDataOpen19['other']

    # 20년 업종별 close
    animal_close_20 = theoremLocalDataClose20['animal']
    culture_close_20 = theoremLocalDataClose20['culture']
    environment_close_20 = theoremLocalDataClose20['environment']
    food_close_20 = theoremLocalDataClose20['food']
    health_close_20 = theoremLocalDataClose20['health']
    life_close_20 = theoremLocalDataClose20['life']
    other_close_20 = theoremLocalDataClose20['other']
    # 20년 업종별 open
    animal_open_20 = theoremLocalDataOpen20['animal']
    culture_open_20 = theoremLocalDataOpen20['culture']
    environment_open_20 = theoremLocalDataOpen20['environment']
    food_open_20 = theoremLocalDataOpen20['food']
    health_open_20 = theoremLocalDataOpen20['health']
    life_open_20 = theoremLocalDataOpen20['life']
    other_open_20 = theoremLocalDataOpen20['other']

    jan_close_cnt_19 = 0
    feb_close_cnt_19 = 0
    mar_close_cnt_19 = 0
    apr_close_cnt_19 = 0
    may_close_cnt_19 = 0
    jun_close_cnt_19 = 0
    jul_close_cnt_19 = 0
    aug_close_cnt_19 = 0
    sep_close_cnt_19 = 0
    oct_close_cnt_19 = 0
    nov_close_cnt_19 = 0
    dec_close_cnt_19 = 0

    jan_close_cnt_20 = 0
    feb_close_cnt_20 = 0
    mar_close_cnt_20 = 0
    apr_close_cnt_20 = 0
    may_close_cnt_20 = 0
    jun_close_cnt_20 = 0
    jul_close_cnt_20 = 0
    aug_close_cnt_20 = 0
    sep_close_cnt_20 = 0
    oct_close_cnt_20 = 0
    nov_close_cnt_20 = 0
    dec_close_cnt_20 = 0

    jan_open_cnt_19 = 0
    feb_open_cnt_19 = 0
    mar_open_cnt_19 = 0
    apr_open_cnt_19 = 0
    may_open_cnt_19 = 0
    jun_open_cnt_19 = 0
    jul_open_cnt_19 = 0
    aug_open_cnt_19 = 0
    sep_open_cnt_19 = 0
    oct_open_cnt_19 = 0
    nov_open_cnt_19 = 0
    dec_open_cnt_19 = 0

    jan_open_cnt_20 = 0
    feb_open_cnt_20 = 0
    mar_open_cnt_20 = 0
    apr_open_cnt_20 = 0
    may_open_cnt_20 = 0
    jun_open_cnt_20 = 0
    jul_open_cnt_20 = 0
    aug_open_cnt_20 = 0
    sep_open_cnt_20 = 0
    oct_open_cnt_20 = 0
    nov_open_cnt_20 = 0
    dec_open_cnt_20 = 0

    for info in animal_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in culture_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in environment_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in food_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in health_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in life_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)
    for info in other_close_19.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_19 += 1
            print("jan_close_cnt_19", jan_close_cnt_19)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_19 += 1
            print("feb_close_cnt_19", feb_close_cnt_19)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_19 += 1
            print("mar_close_cnt_19", mar_close_cnt_19)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_19 += 1
            print("apr_close_cnt_19", apr_close_cnt_19)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_19 += 1
            print("may_close_cnt_19", may_close_cnt_19)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_19 += 1
            print("jun_close_cnt_19", jun_close_cnt_19)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_19 += 1
            print("jul_close_cnt_19", jul_close_cnt_19)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_19 += 1
            print("aug_close_cnt_19", aug_close_cnt_19)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_19 += 1
            print("sep_close_cnt_19", sep_close_cnt_19)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_19 += 1
            print("oct_close_cnt_19", oct_close_cnt_19)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_19 += 1
            print("nov_close_cnt_19", nov_close_cnt_19)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_19 += 1
            print("dec_close_cnt_19", dec_close_cnt_19)

    for info in animal_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in culture_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in environment_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in food_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in health_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in life_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)
    for info in other_close_20.find({}).batch_size(1):
        if info['closed_store_date'][4:6] == '01':
            jan_close_cnt_20 += 1
            print("jan_close_cnt_20", jan_close_cnt_20)
        elif info['closed_store_date'][4:6] == '02':
            feb_close_cnt_20 += 1
            print("feb_close_cnt_20", feb_close_cnt_20)
        elif info['closed_store_date'][4:6] == '03':
            mar_close_cnt_20 += 1
            print("mar_close_cnt_20", mar_close_cnt_20)
        elif info['closed_store_date'][4:6] == '04':
            apr_close_cnt_20 += 1
            print("apr_close_cnt_20", apr_close_cnt_20)
        elif info['closed_store_date'][4:6] == '05':
            may_close_cnt_20 += 1
            print("may_close_cnt_20", may_close_cnt_20)
        elif info['closed_store_date'][4:6] == '06':
            jun_close_cnt_20 += 1
            print("jun_close_cnt_20", jun_close_cnt_20)
        elif info['closed_store_date'][4:6] == '07':
            jul_close_cnt_20 += 1
            print("jul_close_cnt_20", jul_close_cnt_20)
        elif info['closed_store_date'][4:6] == '08':
            aug_close_cnt_20 += 1
            print("aug_close_cnt_20", aug_close_cnt_20)
        elif info['closed_store_date'][4:6] == '09':
            sep_close_cnt_20 += 1
            print("sep_close_cnt_20", sep_close_cnt_20)
        elif info['closed_store_date'][4:6] == '10':
            oct_close_cnt_20 += 1
            print("oct_close_cnt_20", oct_close_cnt_20)
        elif info['closed_store_date'][4:6] == '11':
            nov_close_cnt_20 += 1
            print("nov_close_cnt_20", nov_close_cnt_20)
        elif info['closed_store_date'][4:6] == '12':
            dec_close_cnt_20 += 1
            print("dec_close_cnt_20", dec_close_cnt_20)

    for info in animal_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in culture_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in environment_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in food_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in health_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in life_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)
    for info in other_open_19.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_19 += 1
            print("jan_open_cnt_19", jan_open_cnt_19)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_19 += 1
            print("feb_open_cnt_19", feb_open_cnt_19)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_19 += 1
            print("mar_open_cnt_19", mar_open_cnt_19)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_19 += 1
            print("apr_open_cnt_19", apr_open_cnt_19)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_19 += 1
            print("may_open_cnt_19", may_open_cnt_19)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_19 += 1
            print("jun_open_cnt_19", jun_open_cnt_19)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_19 += 1
            print("jul_open_cnt_19", jul_open_cnt_19)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_19 += 1
            print("aug_open_cnt_19", aug_open_cnt_19)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_19 += 1
            print("sep_open_cnt_19", sep_open_cnt_19)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_19 += 1
            print("oct_open_cnt_19", oct_open_cnt_19)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_19 += 1
            print("nov_open_cnt_19", nov_open_cnt_19)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_19 += 1
            print("dec_open_cnt_19", dec_open_cnt_19)

    for info in animal_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in culture_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in environment_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in food_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in health_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in life_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)
    for info in other_open_20.find({}).batch_size(1):
        if info['authorization_date'][4:6] == '01':
            jan_open_cnt_20 += 1
            print("jan_open_cnt_20", jan_open_cnt_20)
        elif info['authorization_date'][4:6] == '02':
            feb_open_cnt_20 += 1
            print("feb_open_cnt_20", feb_open_cnt_20)
        elif info['authorization_date'][4:6] == '03':
            mar_open_cnt_20 += 1
            print("mar_open_cnt_20", mar_open_cnt_20)
        elif info['authorization_date'][4:6] == '04':
            apr_open_cnt_20 += 1
            print("apr_open_cnt_20", apr_open_cnt_20)
        elif info['authorization_date'][4:6] == '05':
            may_open_cnt_20 += 1
            print("may_open_cnt_20", may_open_cnt_20)
        elif info['authorization_date'][4:6] == '06':
            jun_open_cnt_20 += 1
            print("jun_open_cnt_20", jun_open_cnt_20)
        elif info['authorization_date'][4:6] == '07':
            jul_open_cnt_20 += 1
            print("jul_open_cnt_20", jul_open_cnt_20)
        elif info['authorization_date'][4:6] == '08':
            aug_open_cnt_20 += 1
            print("aug_open_cnt_20", aug_open_cnt_20)
        elif info['authorization_date'][4:6] == '09':
            sep_open_cnt_20 += 1
            print("sep_open_cnt_20", sep_open_cnt_20)
        elif info['authorization_date'][4:6] == '10':
            oct_open_cnt_20 += 1
            print("oct_open_cnt_20", oct_open_cnt_20)
        elif info['authorization_date'][4:6] == '11':
            nov_open_cnt_20 += 1
            print("nov_open_cnt_20", nov_open_cnt_20)
        elif info['authorization_date'][4:6] == '12':
            dec_open_cnt_20 += 1
            print("dec_open_cnt_20", dec_open_cnt_20)

    '''
    my_api = {
        "title": "Month data",
        "month_close_19": [
            {
                "month": "January",
                "month_str": "01",
                "month_num": 1,
                "abbreviations": "Jan.",
                "count": jan_close_cnt_19
            },
            {
                "month": "February",
                "month_str": "02",
                "month_num": 2,
                "abbreviations": "Feb.",
                "count": feb_close_cnt_19
            },
            {
                "month": "March",
                "month_str": "03",
                "month_num": 3,
                "abbreviations": "Mar.",
                "count": mar_close_cnt_19
            },
            {
                "month": "April",
                "month_str": "04",
                "month_num": 4,
                "abbreviations": "Apr.",
                "count": apr_close_cnt_19
            },
            {
                "month": "May",
                "month_str": "05",
                "month_num": 5,
                "abbreviations": "May",
                "count": may_close_cnt_19
            },
            {
                "month": "June",
                "month_str": "06",
                "month_num": 6,
                "abbreviations": "Jun.",
                "count": jun_close_cnt_19
            },
            {
                "month": "July",
                "month_str": "07",
                "month_num": 7,
                "abbreviations": "Jul.",
                "count": jul_close_cnt_19
            },
            {
                "month": "August",
                "month_str": "08",
                "month_num": 8,
                "abbreviations": "Aug.",
                "count": aug_close_cnt_19
            },
            {
                "month": "September",
                "month_str": "09",
                "month_num": 9,
                "abbreviations": "Sep.",
                "count": sep_close_cnt_19
            },
            {
                "month": "October",
                "month_str": "10",
                "month_num": 10,
                "abbreviations": "Oct.",
                "count": oct_close_cnt_19
            },
            {
                "month": "November",
                "month_str": "11",
                "month_num": 11,
                "abbreviations": "Nov.",
                "count": nov_close_cnt_19
            },
            {
                "month": "December",
                "month_str": "12",
                "month_num": 12,
                "abbreviations": "Dec.",
                "count": dec_close_cnt_19
            },
        ],
        "month_open_19": [
            {
                "month": "January",
                "month_str": "01",
                "month_num": 1,
                "abbreviations": "Jan.",
                "count": jan_open_cnt_19
            },
            {
                "month": "February",
                "month_str": "02",
                "month_num": 2,
                "abbreviations": "Feb.",
                "count": feb_open_cnt_19
            },
            {
                "month": "March",
                "month_str": "03",
                "month_num": 3,
                "abbreviations": "Mar.",
                "count": mar_open_cnt_19
            },
            {
                "month": "April",
                "month_str": "04",
                "month_num": 4,
                "abbreviations": "Apr.",
                "count": apr_open_cnt_19
            },
            {
                "month": "May",
                "month_str": "05",
                "month_num": 5,
                "abbreviations": "May",
                "count": may_open_cnt_19
            },
            {
                "month": "June",
                "month_str": "06",
                "month_num": 6,
                "abbreviations": "Jun.",
                "count": jun_open_cnt_19
            },
            {
                "month": "July",
                "month_str": "07",
                "month_num": 7,
                "abbreviations": "Jul.",
                "count": jul_open_cnt_19
            },
            {
                "month": "August",
                "month_str": "08",
                "month_num": 8,
                "abbreviations": "Aug.",
                "count": aug_open_cnt_19
            },
            {
                "month": "September",
                "month_str": "09",
                "month_num": 9,
                "abbreviations": "Sep.",
                "count": sep_open_cnt_19
            },
            {
                "month": "October",
                "month_str": "10",
                "month_num": 10,
                "abbreviations": "Oct.",
                "count": oct_open_cnt_19
            },
            {
                "month": "November",
                "month_str": "11",
                "month_num": 11,
                "abbreviations": "Nov.",
                "count": nov_open_cnt_19
            },
            {
                "month": "December",
                "month_str": "12",
                "month_num": 12,
                "abbreviations": "Dec.",
                "count": dec_open_cnt_19
            },
        ],
        "month_close_20": [
            {
                "month": "January",
                "month_str": "01",
                "month_num": 1,
                "abbreviations": "Jan.",
                "count": jan_close_cnt_20
            },
            {
                "month": "February",
                "month_str": "02",
                "month_num": 2,
                "abbreviations": "Feb.",
                "count": feb_close_cnt_20
            },
            {
                "month": "March",
                "month_str": "03",
                "month_num": 3,
                "abbreviations": "Mar.",
                "count": mar_close_cnt_20
            },
            {
                "month": "April",
                "month_str": "04",
                "month_num": 4,
                "abbreviations": "Apr.",
                "count": apr_close_cnt_20
            },
            {
                "month": "May",
                "month_str": "05",
                "month_num": 5,
                "abbreviations": "May",
                "count": may_close_cnt_20
            },
            {
                "month": "June",
                "month_str": "06",
                "month_num": 6,
                "abbreviations": "Jun.",
                "count": jun_close_cnt_20
            },
            {
                "month": "July",
                "month_str": "07",
                "month_num": 7,
                "abbreviations": "Jul.",
                "count": jul_close_cnt_20
            },
            {
                "month": "August",
                "month_str": "08",
                "month_num": 8,
                "abbreviations": "Aug.",
                "count": aug_close_cnt_20
            },
            {
                "month": "September",
                "month_str": "09",
                "month_num": 9,
                "abbreviations": "Sep.",
                "count": sep_close_cnt_20
            },
            {
                "month": "October",
                "month_str": "10",
                "month_num": 10,
                "abbreviations": "Oct.",
                "count": oct_close_cnt_20
            },
            {
                "month": "November",
                "month_str": "11",
                "month_num": 11,
                "abbreviations": "Nov.",
                "count": nov_close_cnt_20
            },
            {
                "month": "December",
                "month_str": "12",
                "month_num": 12,
                "abbreviations": "Dec.",
                "count": dec_close_cnt_20
            },
        ],
        "month_open_20": [
            {
                "month": "January",
                "month_str": "01",
                "month_num": 1,
                "abbreviations": "Jan.",
                "count": jan_open_cnt_20
            },
            {
                "month": "February",
                "month_str": "02",
                "month_num": 2,
                "abbreviations": "Feb.",
                "count": feb_open_cnt_20
            },
            {
                "month": "March",
                "month_str": "03",
                "month_num": 3,
                "abbreviations": "Mar.",
                "count": mar_open_cnt_20
            },
            {
                "month": "April",
                "month_str": "04",
                "month_num": 4,
                "abbreviations": "Apr.",
                "count": apr_open_cnt_20
            },
            {
                "month": "May",
                "month_str": "05",
                "month_num": 5,
                "abbreviations": "May",
                "count": may_open_cnt_20
            },
            {
                "month": "June",
                "month_str": "06",
                "month_num": 6,
                "abbreviations": "Jun.",
                "count": jun_open_cnt_20
            },
            {
                "month": "July",
                "month_str": "07",
                "month_num": 7,
                "abbreviations": "Jul.",
                "count": jul_open_cnt_20
            },
            {
                "month": "August",
                "month_str": "08",
                "month_num": 8,
                "abbreviations": "Aug.",
                "count": aug_open_cnt_20
            },
            {
                "month": "September",
                "month_str": "09",
                "month_num": 9,
                "abbreviations": "Sep.",
                "count": sep_open_cnt_20
            },
            {
                "month": "October",
                "month_str": "10",
                "month_num": 10,
                "abbreviations": "Oct.",
                "count": oct_open_cnt_20
            },
            {
                "month": "November",
                "month_str": "11",
                "month_num": 11,
                "abbreviations": "Nov.",
                "count": nov_open_cnt_20
            },
            {
                "month": "December",
                "month_str": "12",
                "month_num": 12,
                "abbreviations": "Dec.",
                "count": dec_open_cnt_20
            },
        ]
    }
    local_main_api = db['local_data_api']
    print("my_api", my_api)

    my_api_id = local_main_api.insert_one(my_api).inserted_id
    print(my_api_id)
    '''


data()
