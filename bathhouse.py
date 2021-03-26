from pymongo import MongoClient
from multiprocessing import Process

client = MongoClient('localhost', 27017)

localData19 = client['localData19']
localData20 = client['localData20']

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']

theoremLocalDataLocationClose19 = client['theoremLocalDataLocationClose19']
theoremLocalDataLocationOpen19 = client['theoremLocalDataLocationOpen19']
theoremLocalDataLocationClose20 = client['theoremLocalDataLocationClose20']
theoremLocalDataLocationOpen20 = client['theoremLocalDataLocationOpen20']


def bathhouse_close_19():
    data = localData19['bathhouse_close']
    culture = theoremLocalDataClose19.life

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)


def bathhouse_open_19():
    data = localData19['bathhouse_open']
    culture = theoremLocalDataOpen19.life

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)


def bathhouse_close_20():
    data = localData20['bathhouse_close']
    culture = theoremLocalDataClose20.life

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)


def bathhouse_open_20():
    data = localData20['bathhouse_open']
    culture = theoremLocalDataOpen20.life

    cnt = 0
    for store in data.find({}).batch_size(1):
        cnt += 1
        print(cnt, "/", data.count_documents({}), store)
        insert_data = culture.insert_one(store)


'''
if __name__ == "__main__":
    p1 = Process(target=bathhouse_close_19)
    p2 = Process(target=bathhouse_open_19)
    p3 = Process(target=bathhouse_close_20)
    p4 = Process(target=bathhouse_open_20)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
'''
