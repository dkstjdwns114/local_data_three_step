import csv
from multiprocessing import Process
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
localData19 = client['localData19']
localData20 = client['localData20']


def data010101():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_01_P_병원.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010102():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_02_P_의원.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010103():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_03_P_부속의료기관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010104():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_04_P_산후조리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010105():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_05_P_안전상비의약품판매업소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010106():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_06_P_약국.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010107():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_07_P_응급환자이송업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010108():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_08_P_의료법인.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010109():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_01_10_P_의료유사업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010201():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_02_01_P_안경업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010202():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_02_02_P_의료기기수리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010203():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_02_03_P_의료기기판매임대업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data010204():
    f = open('./LOCALDATA_ALL_CSV/fulldata_01_02_04_P_치과기공소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                health_open = localData19.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0120:
                health_open = localData20.health_open
                health_open_id = health_open.insert_one(store).inserted_id
            elif is0319:
                health_close = localData19.health_close
                health_close_id = health_close.insert_one(store).inserted_id
            elif is0320:
                health_close = localData20.health_close
                health_close_id = health_close.insert_one(store).inserted_id


def data020301():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_01_P_동물병원.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020302():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_02_P_동물약국.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020303():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_03_P_동물용의료용구판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020304():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_04_P_동물용의약품도매상.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020305():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_05_P_동물장묘업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020306():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_03_06_P_동물판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_open = localData19.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0120:
                animal_open = localData20.animal_open
                animal_open_id = animal_open.insert_one(store).inserted_id
            elif is0319:
                animal_close = localData19.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id
            elif is0320:
                animal_close = localData20.animal_close
                animal_close_id = animal_close.insert_one(store).inserted_id


def data020401():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_01_P_가축사육업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data020402():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_02_P_가축인공수정소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data020403():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_03_P_도축업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data020404():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_04_P_부화업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data020405():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_05_P_사료제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data020406():
    f = open('./LOCALDATA_ALL_CSV/fulldata_02_04_06_P_종축업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                animal_husbandry_open = localData19.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0120:
                animal_husbandry_open = localData20.animal_husbandry_open
                animal_husbandry_open_id = animal_husbandry_open.insert_one(store).inserted_id
            elif is0319:
                animal_husbandry_close = localData19.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id
            elif is0320:
                animal_husbandry_close = localData20.animal_husbandry_close
                animal_husbandry_close_id = animal_husbandry_close.insert_one(store).inserted_id


def data030501():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_01_P_게임물배급업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030502():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_02_P_게임물제작업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030503():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_03_P_복합영상물제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030504():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_04_P_복합유통게임제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030505():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_05_P_인터넷컴퓨터게임시설제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030506():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_06_P_일반게임제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030507():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_05_07_P_청소년게임제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                game_open = localData19.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0120:
                game_open = localData20.game_open
                game_open_id = game_open.insert_one(store).inserted_id
            elif is0319:
                game_close = localData19.game_close
                game_close_id = game_close.insert_one(store).inserted_id
            elif is0320:
                game_close = localData20.game_close
                game_close_id = game_close.insert_one(store).inserted_id


def data030601():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_06_01_P_공연장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                show_open = localData19.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0120:
                show_open = localData20.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0319:
                show_close = localData19.show_close
                show_close_id = show_close.insert_one(store).inserted_id
            elif is0320:
                show_close = localData20.show_close
                show_close_id = show_close.insert_one(store).inserted_id


def data030602():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_06_02_P_관광공연장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                show_open = localData19.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0120:
                show_open = localData20.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0319:
                show_close = localData19.show_close
                show_close_id = show_close.insert_one(store).inserted_id
            elif is0320:
                show_close = localData20.show_close
                show_close_id = show_close.insert_one(store).inserted_id


def data030603():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_06_03_P_관광극장유흥업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                show_open = localData19.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0120:
                show_open = localData20.show_open
                show_open_id = show_open.insert_one(store).inserted_id
            elif is0319:
                show_close = localData19.show_close
                show_close_id = show_close.insert_one(store).inserted_id
            elif is0320:
                show_close = localData20.show_close
                show_close_id = show_close.insert_one(store).inserted_id


def data030701():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_01_P_관광궤도업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030702():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_02_P_관광사업자.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030703():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_03_P_관광유람선업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030704():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_04_P_국제회의시설업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030705():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_05_P_박물관,미술관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030706():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_06_P_시내순환관광업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030708():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_08_P_유원시설업기타.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030709():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_09_P_일반유원시설업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030710():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_10_P_전문휴양업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030711():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_11_P_전통사찰.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030712():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_12_P_종합유원시설업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030713():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_13_P_종합휴양업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030714():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_07_14_P_지방문화원.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                tourism_open = localData19.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0120:
                tourism_open = localData20.tourism_open
                tourism_open_id = tourism_open.insert_one(store).inserted_id
            elif is0319:
                tourism_close = localData19.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id
            elif is0320:
                tourism_close = localData20.tourism_close
                tourism_close_id = tourism_close.insert_one(store).inserted_id


def data030801():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_08_01_P_국제회의기획업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cultural_planning_open = localData19.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0120:
                cultural_planning_open = localData20.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0319:
                cultural_planning_close = localData19.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id
            elif is0320:
                cultural_planning_close = localData20.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id


def data030802():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_08_02_P_대중문화예술기획업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cultural_planning_open = localData19.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0120:
                cultural_planning_open = localData20.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0319:
                cultural_planning_close = localData19.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id
            elif is0320:
                cultural_planning_close = localData20.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id


def data030803():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_08_03_P_문화예술법인.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cultural_planning_open = localData19.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0120:
                cultural_planning_open = localData20.cultural_planning_open
                cultural_planning_open_id = cultural_planning_open.insert_one(store).inserted_id
            elif is0319:
                cultural_planning_close = localData19.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id
            elif is0320:
                cultural_planning_close = localData20.cultural_planning_close
                cultural_planning_close_id = cultural_planning_close.insert_one(store).inserted_id


def data030901():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_09_01_P_노래연습장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                karaoke_open = localData19.karaoke_open
                karaoke_open_id = karaoke_open.insert_one(store).inserted_id
            elif is0120:
                karaoke_open = localData20.karaoke_open
                karaoke_open_id = karaoke_open.insert_one(store).inserted_id
            elif is0319:
                karaoke_close = localData19.karaoke_close
                karaoke_close_id = karaoke_close.insert_one(store).inserted_id
            elif is0320:
                karaoke_close = localData20.karaoke_close
                karaoke_close_id = karaoke_close.insert_one(store).inserted_id


def data031001():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_10_01_P_비디오물감상실업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                video_open = localData19.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0120:
                video_open = localData20.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0319:
                video_close = localData19.video_close
                video_close_id = video_close.insert_one(store).inserted_id
            elif is0320:
                video_close = localData20.video_close
                video_close_id = video_close.insert_one(store).inserted_id


def data031002():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_10_02_P_비디오물배급업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                video_open = localData19.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0120:
                video_open = localData20.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0319:
                video_close = localData19.video_close
                video_close_id = video_close.insert_one(store).inserted_id
            elif is0320:
                video_close = localData20.video_close
                video_close_id = video_close.insert_one(store).inserted_id


def data031003():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_10_03_P_비디오물소극장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                video_open = localData19.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0120:
                video_open = localData20.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0319:
                video_close = localData19.video_close
                video_close_id = video_close.insert_one(store).inserted_id
            elif is0320:
                video_close = localData20.video_close
                video_close_id = video_close.insert_one(store).inserted_id


def data031004():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_10_04_P_비디오물시청제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                video_open = localData19.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0120:
                video_open = localData20.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0319:
                video_close = localData19.video_close
                video_close_id = video_close.insert_one(store).inserted_id
            elif is0320:
                video_close = localData20.video_close
                video_close_id = video_close.insert_one(store).inserted_id


def data031005():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_10_05_P_비디오물제작업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                video_open = localData19.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0120:
                video_open = localData20.video_open
                video_open_id = video_open.insert_one(store).inserted_id
            elif is0319:
                video_close = localData19.video_close
                video_close_id = video_close.insert_one(store).inserted_id
            elif is0320:
                video_close = localData20.video_close
                video_close_id = video_close.insert_one(store).inserted_id


def data031101():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_01_P_관광숙박업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031102():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_02_P_관광펜션업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031103():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_03_P_숙박업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031104():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_04_P_외국인관광도시민박업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031105():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_05_P_자동차야영장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031106():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_06_P_한옥체험업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031107():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_11_07_P_일반야영장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                accommodation_open = localData19.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0120:
                accommodation_open = localData20.accommodation_open
                accommodation_open_id = accommodation_open.insert_one(store).inserted_id
            elif is0319:
                accommodation_close = localData19.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id
            elif is0320:
                accommodation_close = localData20.accommodation_close
                accommodation_close_id = accommodation_close.insert_one(store).inserted_id


def data031201():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_12_01_P_국내여행업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                travel_open = localData19.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0120:
                travel_open = localData20.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0319:
                travel_close = localData19.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id
            elif is0320:
                travel_close = localData20.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id


def data031202():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_12_02_P_국외여행업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                travel_open = localData19.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0120:
                travel_open = localData20.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0319:
                travel_close = localData19.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id
            elif is0320:
                travel_close = localData20.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id


def data031203():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_12_03_P_일반여행업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                travel_open = localData19.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0120:
                travel_open = localData20.travel_open
                travel_open_id = travel_open.insert_one(store).inserted_id
            elif is0319:
                travel_close = localData19.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id
            elif is0320:
                travel_close = localData20.travel_close
                travel_close_id = travel_close.insert_one(store).inserted_id


def data031301():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_13_01_P_영화배급업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                movie_open = localData19.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0120:
                movie_open = localData20.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0319:
                movie_close = localData19.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id
            elif is0320:
                movie_close = localData20.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id


def data031302():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_13_02_P_영화상영관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                movie_open = localData19.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0120:
                movie_open = localData20.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0319:
                movie_close = localData19.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id
            elif is0320:
                movie_close = localData20.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id


def data031303():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_13_03_P_영화상영업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                movie_open = localData19.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0120:
                movie_open = localData20.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0319:
                movie_close = localData19.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id
            elif is0320:
                movie_close = localData20.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id


def data031304():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_13_04_P_영화수입업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                movie_open = localData19.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0120:
                movie_open = localData20.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0319:
                movie_close = localData19.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id
            elif is0320:
                movie_close = localData20.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id


def data031305():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_13_05_P_영화제작업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                movie_open = localData19.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0120:
                movie_open = localData20.movie_open
                movie_open_id = movie_open.insert_one(store).inserted_id
            elif is0319:
                movie_close = localData19.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id
            elif is0320:
                movie_close = localData20.movie_close
                movie_close_id = movie_close.insert_one(store).inserted_id


def data031401():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_14_01_P_온라인음악서비스제공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                music_open = localData19.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0120:
                music_open = localData20.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0319:
                music_close = localData19.music_close
                music_close_id = music_close.insert_one(store).inserted_id
            elif is0320:
                music_close = localData20.music_close
                music_close_id = music_close.insert_one(store).inserted_id


def data031402():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_14_02_P_음반.음악영상물배급업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                music_open = localData19.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0120:
                music_open = localData20.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0319:
                music_close = localData19.music_close
                music_close_id = music_close.insert_one(store).inserted_id
            elif is0320:
                music_close = localData20.music_close
                music_close_id = music_close.insert_one(store).inserted_id


def data031403():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_14_03_P_음반.음악영상물제작업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                music_open = localData19.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0120:
                music_open = localData20.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0319:
                music_close = localData19.music_close
                music_close_id = music_close.insert_one(store).inserted_id
            elif is0320:
                music_close = localData20.music_close
                music_close_id = music_close.insert_one(store).inserted_id


def data031404():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_14_04_P_음반물배급업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                music_open = localData19.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0120:
                music_open = localData20.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0319:
                music_close = localData19.music_close
                music_close_id = music_close.insert_one(store).inserted_id
            elif is0320:
                music_close = localData20.music_close
                music_close_id = music_close.insert_one(store).inserted_id


def data031405():
    f = open('./LOCALDATA_ALL_CSV/fulldata_03_14_05_P_음반물제작업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                music_open = localData19.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0120:
                music_open = localData20.music_open
                music_open_id = music_open.insert_one(store).inserted_id
            elif is0319:
                music_close = localData19.music_close
                music_close_id = music_close.insert_one(store).inserted_id
            elif is0320:
                music_close = localData20.music_close
                music_close_id = music_close.insert_one(store).inserted_id


def data041501():
    f = open('./LOCALDATA_ALL_CSV/fulldata_04_15_01_P_옥외광고업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                media_open = localData19.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0120:
                media_open = localData20.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0319:
                media_close = localData19.media_close
                media_close_id = media_close.insert_one(store).inserted_id
            elif is0320:
                media_close = localData20.media_close
                media_close_id = media_close.insert_one(store).inserted_id


def data041601():
    f = open('./LOCALDATA_ALL_CSV/fulldata_04_16_01_P_인쇄사.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                media_open = localData19.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0120:
                media_open = localData20.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0319:
                media_close = localData19.media_close
                media_close_id = media_close.insert_one(store).inserted_id
            elif is0320:
                media_close = localData20.media_close
                media_close_id = media_close.insert_one(store).inserted_id


def data041701():
    f = open('./LOCALDATA_ALL_CSV/fulldata_04_17_01_P_출판사.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                media_open = localData19.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0120:
                media_open = localData20.media_open
                media_open_id = media_open.insert_one(store).inserted_id
            elif is0319:
                media_close = localData19.media_close
                media_close_id = media_close.insert_one(store).inserted_id
            elif is0320:
                media_close = localData20.media_close
                media_close_id = media_close.insert_one(store).inserted_id


def data051801():
    f = open('./LOCALDATA_ALL_CSV/fulldata_05_18_01_P_미용업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                salon_open = localData19.salon_open
                salon_open_id = salon_open.insert_one(store).inserted_id
            elif is0120:
                salon_open = localData20.salon_open
                salon_open_id = salon_open.insert_one(store).inserted_id
            elif is0319:
                salon_close = localData19.salon_close
                salon_close_id = salon_close.insert_one(store).inserted_id
            elif is0320:
                salon_close = localData20.salon_close
                salon_close_id = salon_close.insert_one(store).inserted_id


def data051901():
    f = open('./LOCALDATA_ALL_CSV/fulldata_05_19_01_P_이용업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                salon_open = localData19.salon_open
                salon_open_id = salon_open.insert_one(store).inserted_id
            elif is0120:
                salon_open = localData20.salon_open
                salon_open_id = salon_open.insert_one(store).inserted_id
            elif is0319:
                salon_close = localData19.salon_close
                salon_close_id = salon_close.insert_one(store).inserted_id
            elif is0320:
                salon_close = localData20.salon_close
                salon_close_id = salon_close.insert_one(store).inserted_id


def data062001():
    f = open('./LOCALDATA_ALL_CSV/fulldata_06_20_01_P_세탁업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                laundry_open = localData19.laundry_open
                laundry_open_id = laundry_open.insert_one(store).inserted_id
            elif is0120:
                laundry_open = localData20.laundry_open
                laundry_open_id = laundry_open.insert_one(store).inserted_id
            elif is0319:
                laundry_close = localData19.laundry_close
                laundry_close_id = laundry_close.insert_one(store).inserted_id
            elif is0320:
                laundry_close = localData20.laundry_close
                laundry_close_id = laundry_close.insert_one(store).inserted_id


def data062002():
    f = open('./LOCALDATA_ALL_CSV/fulldata_06_20_02_P_의료기관세탁물처리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                laundry_open = localData19.laundry_open
                laundry_open_id = laundry_open.insert_one(store).inserted_id
            elif is0120:
                laundry_open = localData20.laundry_open
                laundry_open_id = laundry_open.insert_one(store).inserted_id
            elif is0319:
                laundry_close = localData19.laundry_close
                laundry_close_id = laundry_close.insert_one(store).inserted_id
            elif is0320:
                laundry_close = localData20.laundry_close
                laundry_close_id = laundry_close.insert_one(store).inserted_id


def data072101():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_21_01_P_위탁급식영업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                school_meals_open = localData19.school_meals_open
                school_meals_open_id = school_meals_open.insert_one(store).inserted_id
            elif is0120:
                school_meals_open = localData20.school_meals_open
                school_meals_open_id = school_meals_open.insert_one(store).inserted_id
            elif is0319:
                school_meals_close = localData19.school_meals_close
                school_meals_close_id = school_meals_close.insert_one(store).inserted_id
            elif is0320:
                school_meals_close = localData20.school_meals_close
                school_meals_close_id = school_meals_close.insert_one(store).inserted_id


def data072102():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_21_02_P_집단급식소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                school_meals_open = localData19.school_meals_open
                school_meals_open_id = school_meals_open.insert_one(store).inserted_id
            elif is0120:
                school_meals_open = localData20.school_meals_open
                school_meals_open_id = school_meals_open.insert_one(store).inserted_id
            elif is0319:
                school_meals_close = localData19.school_meals_close
                school_meals_close_id = school_meals_close.insert_one(store).inserted_id
            elif is0320:
                school_meals_close = localData20.school_meals_close
                school_meals_close_id = school_meals_close.insert_one(store).inserted_id


def data072201():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_01_P_집단급식소식품판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072202():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_02_P_건강기능식품유통전문판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072203():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_03_P_건강기능식품일반판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072204():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_04_P_축산판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072205():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_05_P_축산가공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072206():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_06_P_식육포장처리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072207():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_07_P_식품냉동냉장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072208():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_08_P_식품소분업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072209():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_09_P_식품운반업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072210():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_10_P_식품자동판매기업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072211():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_11_P_식품제조가공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072212():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_12_P_식품첨가물제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072213():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_13_P_식품판매업기타.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072214():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_14_P_옹기류제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072215():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_15_P_용기·포장지제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072216():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_16_P_용기냉동기특정설비.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072217():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_17_P_유통전문판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072218():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_18_P_제과점영업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072219():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_19_P_즉석판매제조가공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072220():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_20_P_집유업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072221():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_21_P_식용얼음판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072224():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_24_P_축산물보관업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072225():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_22_25_P_축산물운반업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                food_open = localData19.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0120:
                food_open = localData20.food_open
                food_open_id = food_open.insert_one(store).inserted_id
            elif is0319:
                food_close = localData19.food_close
                food_close_id = food_close.insert_one(store).inserted_id
            elif is0320:
                food_close = localData20.food_close
                food_close_id = food_close.insert_one(store).inserted_id


def data072301():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_23_01_P_단란주점영업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                entertainment_bar_open = localData19.entertainment_bar_open
                entertainment_bar_open_id = entertainment_bar_open.insert_one(store).inserted_id
            elif is0120:
                entertainment_bar_open = localData20.entertainment_bar_open
                entertainment_bar_open_id = entertainment_bar_open.insert_one(store).inserted_id
            elif is0319:
                entertainment_bar_close = localData19.entertainment_bar_close
                entertainment_bar_close_id = entertainment_bar_close.insert_one(store).inserted_id
            elif is0320:
                entertainment_bar_close = localData20.entertainment_bar_close
                entertainment_bar_close_id = entertainment_bar_close.insert_one(store).inserted_id


def data072302():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_23_02_P_유흥주점영업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                entertainment_bar_open = localData19.entertainment_bar_open
                entertainment_bar_open_id = entertainment_bar_open.insert_one(store).inserted_id
            elif is0120:
                entertainment_bar_open = localData20.entertainment_bar_open
                entertainment_bar_open_id = entertainment_bar_open.insert_one(store).inserted_id
            elif is0319:
                entertainment_bar_close = localData19.entertainment_bar_close
                entertainment_bar_close_id = entertainment_bar_close.insert_one(store).inserted_id
            elif is0320:
                entertainment_bar_close = localData20.entertainment_bar_close
                entertainment_bar_close_id = entertainment_bar_close.insert_one(store).inserted_id


def data072401():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_24_01_P_관광식당.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                restaurant_open = localData19.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0120:
                restaurant_open = localData20.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0319:
                restaurant_close = localData19.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id
            elif is0320:
                restaurant_close = localData20.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id


def data072402():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_24_02_P_관광유흥음식점업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                restaurant_open = localData19.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0120:
                restaurant_open = localData20.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0319:
                restaurant_close = localData19.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id
            elif is0320:
                restaurant_close = localData20.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id


def data072403():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_24_03_P_외국인전용유흥음식점업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                restaurant_open = localData19.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0120:
                restaurant_open = localData20.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0319:
                restaurant_close = localData19.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id
            elif is0320:
                restaurant_close = localData20.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id


def data072404():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_24_04_P_일반음식점.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                restaurant_open = localData19.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0120:
                restaurant_open = localData20.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0319:
                restaurant_close = localData19.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id
            elif is0320:
                restaurant_close = localData20.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id


def data072405():
    f = open('./LOCALDATA_ALL_CSV/fulldata_07_24_05_P_휴게음식점.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                restaurant_open = localData19.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0120:
                restaurant_open = localData20.restaurant_open
                restaurant_open_id = restaurant_open.insert_one(store).inserted_id
            elif is0319:
                restaurant_close = localData19.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id
            elif is0320:
                restaurant_close = localData20.restaurant_close
                restaurant_close_id = restaurant_close.insert_one(store).inserted_id


def data082501():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_25_01_P_대규모점포.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data082601():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_26_01_P_다단계판매업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data082602():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_26_02_P_방문판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data082603():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_26_03_P_전화권유판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data082604():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_26_04_P_통신판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data082605():
    f = open('./LOCALDATA_ALL_CSV/fulldata_08_26_05_P_후원방문판매업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                distribution_open = localData19.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0120:
                distribution_open = localData20.distribution_open
                distribution_open_id = distribution_open.insert_one(store).inserted_id
            elif is0319:
                distribution_close = localData19.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id
            elif is0320:
                distribution_close = localData20.distribution_close
                distribution_close_id = distribution_close.insert_one(store).inserted_id


def data092701():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_27_01_P_목재수입유통업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                wood_open = localData19.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0120:
                wood_open = localData20.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0319:
                wood_close = localData19.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id
            elif is0320:
                wood_close = localData20.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id


def data092702():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_27_02_P_원목생산업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                wood_open = localData19.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0120:
                wood_open = localData20.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0319:
                wood_close = localData19.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id
            elif is0320:
                wood_close = localData20.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id


def data092703():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_27_03_P_제재업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                wood_open = localData19.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0120:
                wood_open = localData20.wood_open
                wood_open_id = wood_open.insert_one(store).inserted_id
            elif is0319:
                wood_close = localData19.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id
            elif is0320:
                wood_close = localData20.wood_close
                wood_close_id = wood_close.insert_one(store).inserted_id


def data092801():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_01_P_계량기수리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092802():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_02_P_계량기수입업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092803():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_03_P_계량기제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092804():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_04_P_계량기증명업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092805():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_05_P_고압가스업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092806():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_06_P_석연탄제조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092807():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_07_P_석유및석유대체연료판매업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092808():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_08_P_석유판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092809():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_09_P_액화석유가스용품제조업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092810():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_10_P_일반도시가스업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092812():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_12_P_전력기술감리업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092813():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_13_P_전력기술설계업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092814():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_28_14_P_특정고압가스업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                energy_open = localData19.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0120:
                energy_open = localData20.energy_open
                energy_open_id = energy_open.insert_one(store).inserted_id
            elif is0319:
                energy_close = localData19.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id
            elif is0320:
                energy_close = localData20.energy_close
                energy_close_id = energy_close.insert_one(store).inserted_id


def data092901():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_29_01_P_지하수시공업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                groundwater_open = localData19.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0120:
                groundwater_open = localData20.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0319:
                groundwater_close = localData19.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id
            elif is0320:
                groundwater_close = localData20.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id


def data092902():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_29_02_P_지하수영향조사기관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                groundwater_open = localData19.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0120:
                groundwater_open = localData20.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0319:
                groundwater_close = localData19.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id
            elif is0320:
                groundwater_close = localData20.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id


def data092903():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_29_03_P_지하수정화업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                groundwater_open = localData19.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0120:
                groundwater_open = localData20.groundwater_open
                groundwater_open_id = groundwater_open.insert_one(store).inserted_id
            elif is0319:
                groundwater_close = localData19.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id
            elif is0320:
                groundwater_close = localData20.groundwater_close
                groundwater_close_id = groundwater_close.insert_one(store).inserted_id


def data093001():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_01_P_가축분뇨수집운반업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093002():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_02_P_가축분뇨배출시설관리업사업장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093003():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_03_P_개인하수처리시설관리업사업장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093004():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_04_P_건물위생관리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
                
                
def data093005():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_05_P_건설폐기물처리업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093006():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_06_P_급수공사대행업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093007():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_07_P_단독정화조오수처리시설설계시공업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093008():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_08_P_대기오염물질배출시설설치사업장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093009():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_09_P_배출가스전문정비사업자확인검사대행자.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093010():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_10_P_분뇨수집운반업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093011():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_11_P_소독업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093012():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_12_P_수질오염원설치시설기타.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093013():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_13_P_쓰레기종량제봉투판매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093014():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_14_P_저수조청소업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093015():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_15_P_환경관리대행기관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093016():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_16_P_환경전문공사업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093017():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_17_P_환경측정대행업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data093018():
    f = open('./LOCALDATA_ALL_CSV/fulldata_09_30_18_P_환경컨설팅회사.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                environmental_management_open = localData19.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0120:
                environmental_management_open = localData20.environmental_management_open
                environmental_management_open_id = environmental_management_open.insert_one(store).inserted_id
            elif is0319:
                environmental_management_close = localData19.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id
            elif is0320:
                environmental_management_close = localData20.environmental_management_close
                environmental_management_close_id = environmental_management_close.insert_one(store).inserted_id


def data103101():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_31_01_P_골프연습장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103102():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_31_02_P_골프장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103103():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_31_03_P_등록체육시설업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103201():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_32_01_P_당구장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103301():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_33_01_P_무도장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103302():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_33_02_P_무도학원업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103401():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_34_01_P_빙상장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103501():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_35_01_P_수영장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103601():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_36_01_P_스키장.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103701():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_37_01_P_종합체육시설업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103801():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_38_01_P_승마장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data103901():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_39_01_P_썰매장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data104001():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_40_01_P_요트장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data104101():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_41_01_P_체육도장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data104201():
    f = open('./LOCALDATA_ALL_CSV/fulldata_10_42_01_P_체력단련장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                physical_education_open = localData19.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0120:
                physical_education_open = localData20.physical_education_open
                physical_education_open_id = physical_education_open.insert_one(store).inserted_id
            elif is0319:
                physical_education_close = localData19.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id
            elif is0320:
                physical_education_close = localData20.physical_education_close
                physical_education_close_id = physical_education_close.insert_one(store).inserted_id


def data104301():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_43_01_P_담배도매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cigarette_open = localData19.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0120:
                cigarette_open = localData20.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0319:
                cigarette_close = localData19.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id
            elif is0320:
                cigarette_close = localData20.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id


def data104302():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_43_02_P_담배소매업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cigarette_open = localData19.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0120:
                cigarette_open = localData20.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0319:
                cigarette_close = localData19.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id
            elif is0320:
                cigarette_close = localData20.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id


def data104303():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_43_03_P_담배수입판매업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                cigarette_open = localData19.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0120:
                cigarette_open = localData20.cigarette_open
                cigarette_open_id = cigarette_open.insert_one(store).inserted_id
            elif is0319:
                cigarette_close = localData19.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id
            elif is0320:
                cigarette_close = localData20.cigarette_close
                cigarette_close_id = cigarette_close.insert_one(store).inserted_id


def data104401():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_44_01_P_목욕장업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                bathhouse_open = localData19.bathhouse_open
                bathhouse_open_id = bathhouse_open.insert_one(store).inserted_id
            elif is0120:
                bathhouse_open = localData20.bathhouse_open
                bathhouse_open_id = bathhouse_open.insert_one(store).inserted_id
            elif is0319:
                bathhouse_close = localData19.bathhouse_close
                bathhouse_close_id = bathhouse_close.insert_one(store).inserted_id
            elif is0320:
                bathhouse_close = localData20.bathhouse_close
                bathhouse_close_id = bathhouse_close.insert_one(store).inserted_id


def data104501():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_45_01_P_물류주선업국제.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                logistics_open = localData19.logistics_open
                logistics_open_id = logistics_open.insert_one(store).inserted_id
            elif is0120:
                logistics_open = localData20.logistics_open
                logistics_open_id = logistics_open.insert_one(store).inserted_id
            elif is0319:
                logistics_close = localData19.logistics_close
                logistics_close_id = logistics_close.insert_one(store).inserted_id
            elif is0320:
                logistics_close = localData20.logistics_close
                logistics_close_id = logistics_close.insert_one(store).inserted_id


def data104502():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_45_02_P_물류창고업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                logistics_open = localData19.logistics_open
                logistics_open_id = logistics_open.insert_one(store).inserted_id
            elif is0120:
                logistics_open = localData20.logistics_open
                logistics_open_id = logistics_open.insert_one(store).inserted_id
            elif is0319:
                logistics_close = localData19.logistics_close
                logistics_close_id = logistics_close.insert_one(store).inserted_id
            elif is0320:
                logistics_close = localData20.logistics_close
                logistics_close_id = logistics_close.insert_one(store).inserted_id


def data104601():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_46_01_P_민방위급수시설.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                civil_defense_open = localData19.civil_defense_open
                civil_defense_open_id = civil_defense_open.insert_one(store).inserted_id
            elif is0120:
                civil_defense_open = localData20.civil_defense_open
                civil_defense_open_id = civil_defense_open.insert_one(store).inserted_id
            elif is0319:
                civil_defense_close = localData19.civil_defense_close
                civil_defense_close_id = civil_defense_close.insert_one(store).inserted_id
            elif is0320:
                civil_defense_close = localData20.civil_defense_close
                civil_defense_close_id = civil_defense_close.insert_one(store).inserted_id


def data104602():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_46_02_P_민방위대피시설.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                civil_defense_open = localData19.civil_defense_open
                civil_defense_open_id = civil_defense_open.insert_one(store).inserted_id
            elif is0120:
                civil_defense_open = localData20.civil_defense_open
                civil_defense_open_id = civil_defense_open.insert_one(store).inserted_id
            elif is0319:
                civil_defense_close = localData19.civil_defense_close
                civil_defense_close_id = civil_defense_close.insert_one(store).inserted_id
            elif is0320:
                civil_defense_close = localData20.civil_defense_close
                civil_defense_close_id = civil_defense_close.insert_one(store).inserted_id


def data104701():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_47_01_P_상조업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                funeral_open = localData19.funeral_open
                funeral_open_id = funeral_open.insert_one(store).inserted_id
            elif is0120:
                funeral_open = localData20.funeral_open
                funeral_open_id = funeral_open.insert_one(store).inserted_id
            elif is0319:
                funeral_close = localData19.funeral_close
                funeral_close_id = funeral_close.insert_one(store).inserted_id
            elif is0320:
                funeral_close = localData20.funeral_close
                funeral_close_id = funeral_close.insert_one(store).inserted_id


def data104801():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_48_01_P_승강기유지관리업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                elevator_open = localData19.elevator_open
                elevator_open_id = elevator_open.insert_one(store).inserted_id
            elif is0120:
                elevator_open = localData20.elevator_open
                elevator_open_id = elevator_open.insert_one(store).inserted_id
            elif is0319:
                elevator_close = localData19.elevator_close
                elevator_close_id = elevator_close.insert_one(store).inserted_id
            elif is0320:
                elevator_close = localData20.elevator_close
                elevator_close_id = elevator_close.insert_one(store).inserted_id


def data104802():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_48_02_P_승강기제조및수입업체.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                elevator_open = localData19.elevator_open
                elevator_open_id = elevator_open.insert_one(store).inserted_id
            elif is0120:
                elevator_open = localData20.elevator_open
                elevator_open_id = elevator_open.insert_one(store).inserted_id
            elif is0319:
                elevator_close = localData19.elevator_close
                elevator_close_id = elevator_close.insert_one(store).inserted_id
            elif is0320:
                elevator_close = localData20.elevator_close
                elevator_close_id = elevator_close.insert_one(store).inserted_id


def data104901():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_49_01_P_요양보호사교육기관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                educational_institutions_open = localData19.educational_institutions_open
                educational_institutions_open_id = educational_institutions_open.insert_one(store).inserted_id
            elif is0120:
                educational_institutions_open = localData20.educational_institutions_open
                educational_institutions_open_id = educational_institutions_open.insert_one(store).inserted_id
            elif is0319:
                educational_institutions_close = localData19.educational_institutions_close
                educational_institutions_close_id = educational_institutions_close.insert_one(store).inserted_id
            elif is0320:
                educational_institutions_close = localData20.educational_institutions_close
                educational_institutions_close_id = educational_institutions_close.insert_one(store).inserted_id


def data104902():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_49_02_P_장례지도사교육기관.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                educational_institutions_open = localData19.educational_institutions_open
                educational_institutions_open_id = educational_institutions_open.insert_one(store).inserted_id
            elif is0120:
                educational_institutions_open = localData20.educational_institutions_open
                educational_institutions_open_id = educational_institutions_open.insert_one(store).inserted_id
            elif is0319:
                educational_institutions_close = localData19.educational_institutions_close
                educational_institutions_close_id = educational_institutions_close.insert_one(store).inserted_id
            elif is0320:
                educational_institutions_close = localData20.educational_institutions_close
                educational_institutions_close_id = educational_institutions_close.insert_one(store).inserted_id


def data105001():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_50_01_P_무료직업소개소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                office_support_open = localData19.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0120:
                office_support_open = localData20.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0319:
                office_support_close = localData19.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id
            elif is0320:
                office_support_close = localData20.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id


def data105002():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_50_02_P_유료직업소개소.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                office_support_open = localData19.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0120:
                office_support_open = localData20.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0319:
                office_support_close = localData19.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id
            elif is0320:
                office_support_close = localData20.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id


def data105003():
    f = open('./LOCALDATA_ALL_CSV/fulldata_11_50_03_P_행정사업.csv', 'r', encoding='cp949')
    firstLine = f.readline()
    rdr = csv.reader(f)

    cnt0119 = 0
    cnt0120 = 0
    cnt0319 = 0
    cnt0320 = 0
    for line in rdr:
        is0119 = False
        is0120 = False
        is0319 = False
        is0320 = False
        if line[7] == "01" and line[5][0:4] == '2019':
            cnt0119 += 1
            is0119 = True
            print(cnt0119, line)

        if line[7] == "01" and line[5][0:4] == '2020':
            cnt0120 += 1
            is0120 = True
            print(cnt0120, line)

        if line[7] == "03" and line[11][0:4] == '2019':
            cnt0319 += 1
            is0319 = True
            print(cnt0319, line)

        if line[7] == "03" and line[11][0:4] == '2020':
            cnt0320 += 1
            is0320 = True
            print(cnt0320, line)

        if is0119 or is0120 or is0319 or is0320:
            store = {
                "open_service": line[1],
                "open_service_id": line[2],
                "control_number": line[4],
                "authorization_date": line[5],
                "cancel_authorization_date": line[6],
                "state_code": line[7],
                "state": line[8],
                "closed_store_date": line[11],
                "postal_code": line[17],
                "address": line[19],
                "store_name": line[21],
                "detailed_classification": line[25],
                "coordinates": {
                    "x": line[26],
                    "y": line[27]
                }
            }

            if is0119:
                office_support_open = localData19.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0120:
                office_support_open = localData20.office_support_open
                office_support_open_id = office_support_open.insert_one(store).inserted_id
            elif is0319:
                office_support_close = localData19.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id
            elif is0320:
                office_support_close = localData20.office_support_close
                office_support_close_id = office_support_close.insert_one(store).inserted_id


'''
if __name__ == "__main__":
    p1 = Process(target=data010101)
    p2 = Process(target=data010102)
    p3 = Process(target=data010103)
    p4 = Process(target=data010104)
    p5 = Process(target=data010105)
    p6 = Process(target=data010106)
    p7 = Process(target=data010107)
    p8 = Process(target=data010108)
    p9 = Process(target=data010109)
    p10 = Process(target=data010201)
    p11 = Process(target=data010202)
    p12 = Process(target=data010203)
    p13 = Process(target=data010204)
    p14 = Process(target=data020301)
    p15 = Process(target=data020302)
    p16 = Process(target=data020303)
    p17 = Process(target=data020304)
    p18 = Process(target=data020305)
    p19 = Process(target=data020306)
    p20 = Process(target=data020401)
    p21 = Process(target=data020402)
    p22 = Process(target=data020403)
    p23 = Process(target=data020404)
    p24 = Process(target=data020405)
    p25 = Process(target=data020406)
    p26 = Process(target=data030501)
    p27 = Process(target=data030502)
    p28 = Process(target=data030503)
    p29 = Process(target=data030504)
    p30 = Process(target=data030505)
    p31 = Process(target=data030506)
    p32 = Process(target=data030507)
    p33 = Process(target=data030601)
    p34 = Process(target=data030602)
    p35 = Process(target=data030603)
    p36 = Process(target=data030701)
    p37 = Process(target=data030702)
    p38 = Process(target=data030703)
    p39 = Process(target=data030704)
    p40 = Process(target=data030705)
    p41 = Process(target=data030706)
    p42 = Process(target=data030708)
    p43 = Process(target=data030709)
    p44 = Process(target=data030710)
    p45 = Process(target=data030711)
    p46 = Process(target=data030712)
    p47 = Process(target=data030713)
    p48 = Process(target=data030714)
    p49 = Process(target=data030801)
    p50 = Process(target=data030802)
    p51 = Process(target=data030803)
    p52 = Process(target=data030901)
    p53 = Process(target=data031001)
    p54 = Process(target=data031002)
    p55 = Process(target=data031003)
    p56 = Process(target=data031004)
    p57 = Process(target=data031005)
    p58 = Process(target=data031101)
    p59 = Process(target=data031102)
    p60 = Process(target=data031103)
    p61 = Process(target=data031104)
    p62 = Process(target=data031105)
    p63 = Process(target=data031106)
    p64 = Process(target=data031107)
    p65 = Process(target=data031201)
    p66 = Process(target=data031202)
    p67 = Process(target=data031203)
    p68 = Process(target=data031301)
    p69 = Process(target=data031302)
    p70 = Process(target=data031303)
    p71 = Process(target=data031304)
    p72 = Process(target=data031305)
    p73 = Process(target=data031401)
    p74 = Process(target=data031402)
    p75 = Process(target=data031403)
    p76 = Process(target=data031404)
    p77 = Process(target=data031405)
    p78 = Process(target=data041501)
    p79 = Process(target=data041601)
    p80 = Process(target=data041701)
    p81 = Process(target=data051801)
    p82 = Process(target=data051901)
    p83 = Process(target=data062001)
    p84 = Process(target=data062002)
    p85 = Process(target=data072101)
    p86 = Process(target=data072102)
    p87 = Process(target=data072201)
    p88 = Process(target=data072202)
    p89 = Process(target=data072203)
    p90 = Process(target=data072204)
    p91 = Process(target=data072205)
    p92 = Process(target=data072206)
    p93 = Process(target=data072207)
    p94 = Process(target=data072208)
    p95 = Process(target=data072209)
    p96 = Process(target=data072210)
    p97 = Process(target=data072211)
    p98 = Process(target=data072212)
    p99 = Process(target=data072213)
    p100 = Process(target=data072214)
    p101 = Process(target=data072215)
    p102 = Process(target=data072216)
    p103 = Process(target=data072217)
    p104 = Process(target=data072218)
    p105 = Process(target=data072219)
    p106 = Process(target=data072220)
    p107 = Process(target=data072221)
    p108 = Process(target=data072224)
    p109 = Process(target=data072225)
    p110 = Process(target=data072301)
    p111 = Process(target=data072302)
    p112 = Process(target=data072401)
    p113 = Process(target=data072402)
    p114 = Process(target=data072403)
    p115 = Process(target=data072404)
    p116 = Process(target=data072405)
    p117 = Process(target=data082501)
    p118 = Process(target=data082601)
    p119 = Process(target=data082602)
    p120 = Process(target=data082603)
    p121 = Process(target=data082604)
    p122 = Process(target=data082605)
    p123 = Process(target=data092701)
    p124 = Process(target=data092702)
    p125 = Process(target=data092703)
    p126 = Process(target=data092801)
    p127 = Process(target=data092802)
    p128 = Process(target=data092803)
    p129 = Process(target=data092804)
    p130 = Process(target=data092805)
    p131 = Process(target=data092806)
    p132 = Process(target=data092807)
    p133 = Process(target=data092808)
    p134 = Process(target=data092809)
    p135 = Process(target=data092810)
    p136 = Process(target=data092812)
    p137 = Process(target=data092813)
    p138 = Process(target=data092814)
    p139 = Process(target=data092901)
    p140 = Process(target=data092902)
    p141 = Process(target=data092903)
    p142 = Process(target=data093001)
    p143 = Process(target=data093002)
    p144 = Process(target=data093003)
    p145 = Process(target=data093004)
    p146 = Process(target=data093005)
    p147 = Process(target=data093006)
    p148 = Process(target=data093007)
    p149 = Process(target=data093008)
    p150 = Process(target=data093009)
    p151 = Process(target=data093010)
    p152 = Process(target=data093011)
    p153 = Process(target=data093012)
    p154 = Process(target=data093013)
    p155 = Process(target=data093014)
    p156 = Process(target=data093015)
    p157 = Process(target=data093016)
    p158 = Process(target=data093017)
    p159 = Process(target=data093018)
    p160 = Process(target=data103101)
    p161 = Process(target=data103102)
    p162 = Process(target=data103103)
    p163 = Process(target=data103201)
    p164 = Process(target=data103301)
    p165 = Process(target=data103302)
    p166 = Process(target=data103401)
    p167 = Process(target=data103501)
    p168 = Process(target=data103601)
    p169 = Process(target=data103701)
    p170 = Process(target=data103801)
    p171 = Process(target=data103901)
    p172 = Process(target=data104001)
    p173 = Process(target=data104101)
    p174 = Process(target=data104201)
    p175 = Process(target=data104302)
    p176 = Process(target=data104303)
    p177 = Process(target=data104401)
    p178 = Process(target=data104501)
    p179 = Process(target=data104502)
    p180 = Process(target=data104601)
    p181 = Process(target=data104602)
    p182 = Process(target=data104701)
    p183 = Process(target=data104801)
    p184 = Process(target=data104802)
    p185 = Process(target=data104901)
    p186 = Process(target=data104902)
    p187 = Process(target=data105001)
    p188 = Process(target=data105002)
    p189 = Process(target=data105003)
    p190 = Process(target=data104301)

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
    p67.start()
    p68.start()
    p69.start()
    p70.start()
    p71.start()
    p72.start()
    p73.start()
    p74.start()
    p75.start()
    p76.start()
    p77.start()
    p78.start()
    p79.start()
    p80.start()
    p81.start()
    p82.start()
    p83.start()
    p84.start()
    p85.start()
    p86.start()
    p87.start()
    p88.start()
    p89.start()
    p90.start()
    p91.start()
    p92.start()
    p93.start()
    p94.start()
    p95.start()
    p96.start()
    p97.start()
    p98.start()
    p99.start()
    p100.start()
    p101.start()
    p102.start()
    p103.start()
    p104.start()
    p105.start()
    p106.start()
    p107.start()
    p108.start()
    p109.start()
    p110.start()
    p111.start()
    p112.start()
    p113.start()
    p114.start()
    p115.start()
    p116.start()
    p117.start()
    p118.start()
    p119.start()
    p120.start()
    p121.start()
    p122.start()
    p123.start()
    p124.start()
    p125.start()
    p126.start()
    p127.start()
    p128.start()
    p129.start()
    p130.start()
    p131.start()
    p132.start()
    p133.start()
    p134.start()
    p135.start()
    p136.start()
    p137.start()
    p138.start()
    p139.start()
    p140.start()
    p141.start()
    p142.start()
    p143.start()
    p144.start()
    p145.start()
    p146.start()
    p147.start()
    p148.start()
    p149.start()
    p150.start()
    p151.start()
    p152.start()
    p153.start()
    p154.start()
    p155.start()
    p156.start()
    p157.start()
    p158.start()
    p159.start()
    p160.start()
    p161.start()
    p162.start()
    p163.start()
    p164.start()
    p165.start()
    p166.start()
    p167.start()
    p168.start()
    p169.start()
    p170.start()
    p171.start()
    p172.start()
    p173.start()
    p174.start()
    p175.start()
    p176.start()
    p177.start()
    p178.start()
    p179.start()
    p180.start()
    p181.start()
    p182.start()
    p183.start()
    p184.start()
    p185.start()
    p186.start()
    p187.start()
    p188.start()
    p189.start()
    p190.start()

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
    p67.join()
    p68.join()
    p69.join()
    p70.join()
    p71.join()
    p72.join()
    p73.join()
    p74.join()
    p75.join()
    p76.join()
    p77.join()
    p78.join()
    p79.join()
    p80.join()
    p81.join()
    p82.join()
    p83.join()
    p84.join()
    p85.join()
    p86.join()
    p87.join()
    p88.join()
    p89.join()
    p90.join()
    p91.join()
    p92.join()
    p93.join()
    p94.join()
    p95.join()
    p96.join()
    p97.join()
    p98.join()
    p99.join()
    p100.join()
    p101.join()
    p102.join()
    p103.join()
    p104.join()
    p105.join()
    p106.join()
    p107.join()
    p108.join()
    p109.join()
    p110.join()
    p111.join()
    p112.join()
    p113.join()
    p114.join()
    p115.join()
    p116.join()
    p117.join()
    p118.join()
    p119.join()
    p120.join()
    p121.join()
    p122.join()
    p123.join()
    p124.join()
    p125.join()
    p126.join()
    p127.join()
    p128.join()
    p129.join()
    p130.join()
    p131.join()
    p132.join()
    p133.join()
    p134.join()
    p135.join()
    p136.join()
    p137.join()
    p138.join()
    p139.join()
    p140.join()
    p141.join()
    p142.join()
    p143.join()
    p144.join()
    p145.join()
    p146.join()
    p147.join()
    p148.join()
    p149.join()
    p150.join()
    p151.join()
    p152.join()
    p153.join()
    p154.join()
    p155.join()
    p156.join()
    p157.join()
    p158.join()
    p159.join()
    p160.join()
    p161.join()
    p162.join()
    p163.join()
    p164.join()
    p165.join()
    p166.join()
    p167.join()
    p168.join()
    p169.join()
    p170.join()
    p171.join()
    p172.join()
    p173.join()
    p174.join()
    p175.join()
    p176.join()
    p177.join()
    p178.join()
    p179.join()
    p180.join()
    p181.join()
    p182.join()
    p183.join()
    p184.join()
    p185.join()
    p186.join()
    p187.join()
    p188.join()
    p189.join()
    p190.join()
'''
