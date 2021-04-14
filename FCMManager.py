from pyfcm import FCMNotification

APIKEY = "AAAAsLhtlp8:APA91bF7A7f_Rr0tBhpZmgBAzZ5wAIGifzAyMtLJgerJyR-uX6t6bdpjyZ6dNE1IDOk22wm3vItH9xx4mZwzzI_4lcbGBJ-ZBi8kHh9Cxwf_2Kb14SUAnDPkCFPZhHGEP-pdYEeucLfS"

# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(APIKEY)


def sendMessage(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }

    # topic을 이용해 다수의 구독자에게 푸시알림을 전송함
    result = push_service.notify_topic_subscribers(topic_name="generalTopic", data_message=data_message)

    # 전송 결과 출력
    print(result)


sendMessage("TEST Message", "데이터 업데이트 알림")
