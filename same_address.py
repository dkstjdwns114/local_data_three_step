from pymongo import MongoClient
from multiprocessing import Process

client = MongoClient('localhost', 27017)

localSameAddress = client['localSameAddress']

theoremLocalDataLocationClose19 = client['theoremLocalDataLocationClose19']
theoremLocalDataLocationClose20 = client['theoremLocalDataLocationClose20']


def busan():
    prev_data = theoremLocalDataLocationClose19['busan']
    current_data = theoremLocalDataLocationClose20['busan']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def chungbuk():
    prev_data = theoremLocalDataLocationClose19['chungbuk']
    current_data = theoremLocalDataLocationClose20['chungbuk']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def chungnam():
    prev_data = theoremLocalDataLocationClose19['chungnam']
    current_data = theoremLocalDataLocationClose20['chungnam']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def daegu():
    prev_data = theoremLocalDataLocationClose19['daegu']
    current_data = theoremLocalDataLocationClose20['daegu']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def daejeon():
    prev_data = theoremLocalDataLocationClose19['daejeon']
    current_data = theoremLocalDataLocationClose20['daejeon']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def gangwon():
    prev_data = theoremLocalDataLocationClose19['gangwon']
    current_data = theoremLocalDataLocationClose20['gangwon']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def gwangju():
    prev_data = theoremLocalDataLocationClose19['gwangju']
    current_data = theoremLocalDataLocationClose20['gwangju']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def gyeongbuk():
    prev_data = theoremLocalDataLocationClose19['gyeongbuk']
    current_data = theoremLocalDataLocationClose20['gyeongbuk']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def gyeongnam():
    prev_data = theoremLocalDataLocationClose19['gyeongnam']
    current_data = theoremLocalDataLocationClose20['gyeongnam']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def gyeonggi():
    prev_data = theoremLocalDataLocationClose19['gyeonggi']
    current_data = theoremLocalDataLocationClose20['gyeonggi']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def incheon():
    prev_data = theoremLocalDataLocationClose19['incheon']
    current_data = theoremLocalDataLocationClose20['incheon']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def jeju():
    prev_data = theoremLocalDataLocationClose19['jeju']
    current_data = theoremLocalDataLocationClose20['jeju']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def jeonbuk():
    prev_data = theoremLocalDataLocationClose19['jeonbuk']
    current_data = theoremLocalDataLocationClose20['jeonbuk']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def jeonnam():
    prev_data = theoremLocalDataLocationClose19['jeonnam']
    current_data = theoremLocalDataLocationClose20['jeonnam']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def sejong():
    prev_data = theoremLocalDataLocationClose19['sejong']
    current_data = theoremLocalDataLocationClose20['sejong']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def seoul():
    prev_data = theoremLocalDataLocationClose19['seoul']
    current_data = theoremLocalDataLocationClose20['seoul']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)


def ulsan():
    prev_data = theoremLocalDataLocationClose19['ulsan']
    current_data = theoremLocalDataLocationClose20['ulsan']

    total_cnt = prev_data.count_documents({})

    cnt = 0
    for store1 in prev_data.find({}).batch_size(1):
        cnt += 1
        stores_info = []
        is_same = False
        for store2 in current_data.find({"address": store1['address']}).batch_size(1):
            is_same = True
            stores_info.append({
                "store_name": store2['store_name'],
                "open_service": store2['open_service'],
                "detailed_classification": store2['detailed_classification'],
                "closed_store_date": store2['closed_store_date']
            })

        if is_same:
            same_address = {
                "address": store1['address'],
                "coordinates": {
                    "x": store1['coordinates']['x'],
                    "y": store1['coordinates']['y']
                },
                "stores_info": stores_info
            }
            address = localSameAddress.same_address
            address_id = address.insert_one(same_address).inserted_id
            print(cnt, "/", total_cnt, same_address)



if __name__ == "__main__":
    p1 = Process(target=busan)
    p2 = Process(target=chungbuk)
    p3 = Process(target=chungnam)
    p4 = Process(target=daegu)
    p5 = Process(target=daejeon)
    p6 = Process(target=gangwon)
    p7 = Process(target=gwangju)
    p8 = Process(target=gyeongbuk)
    p9 = Process(target=gyeongnam)
    p10 = Process(target=gyeonggi)
    p11 = Process(target=incheon)
    p12 = Process(target=jeju)
    p13 = Process(target=jeonbuk)
    p14 = Process(target=jeonnam)
    p15 = Process(target=sejong)
    p16 = Process(target=seoul)
    p17 = Process(target=ulsan)

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

