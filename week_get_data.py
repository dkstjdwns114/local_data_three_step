from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from pymongo import MongoClient
import xmltodict, json

client = MongoClient("localhost", 27017)

localWeekData = client['localWeekData']

jsonObj = {}

url = 'http://www.localdata.go.kr/platform/rest/TO0/openDataApi'


def close():
    queryParams = '?' + urlencode({
        quote_plus("authKey"): "uZ98I03VR/zZ3zAvdNIVEl8EWJy6llSwLtDAMDlOYkE=",

        quote_plus("lastModTsBgn"): "20210331",

        quote_plus("lastModTsEnd"): "20210401",

        quote_plus("state"): "03",

        quote_plus("pageSize"): "10000",

        quote_plus("resultType"): "xml"
    })

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'

    response_body = urlopen(request).read()

    dict = xmltodict.parse(response_body)

    jsonString = json.dumps(dict['result']['body'], ensure_ascii=False)

    jsonObj = json.loads(jsonString)

    for item in jsonObj['rows']['row']:
        if item['dcbYmd'] == "20210331":
            print(item)
            print("번호", item['rowNum'])
            print("개방자치단체코드", item['opnSfTeamCode'])
            print("개방서비스ID", item['opnSvcId'])
            print("데이터갱신일자", item['updateDt'])
            print("개방서비스명", item['opnSvcNm'])
            print("사업장명", item['bplcNm'])
            print("도로명주소", item['rdnWhlAddr'])
            print("인허가일자", item['apvPermYmd'])
            print("인허가취소일자", item['apvCancelYmd'])
            print("영업상태코드", item['trdStateGbn'])
            print("영업상태명", item['trdStateNm'])
            print("폐업일자", item['dcbYmd'])
            print("업태구분명", item['uptaeNm'])
            print("-------------------------")


def today_open():
    queryParams = '?' + urlencode({
        quote_plus("authKey"): "uZ98I03VR/zZ3zAvdNIVEl8EWJy6llSwLtDAMDlOYkE=",

        quote_plus("bgnYmd"): "20210330",

        quote_plus("endYmd"): "20210330",

        quote_plus("state"): "01",

        quote_plus("pageSize"): "10000",

        quote_plus("resultType"): "xml"
    })

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'

    response_body = urlopen(request).read()

    dict = xmltodict.parse(response_body)

    jsonString = json.dumps(dict['result']['body'], ensure_ascii=False)

    jsonObj = json.loads(jsonString)

    for item in jsonObj['rows']['row']:
        print(item)
        print("번호", item['rowNum'])
        print("개방자치단체코드", item['opnSfTeamCode'])
        print("개방서비스ID", item['opnSvcId'])
        print("데이터갱신일자", item['updateDt'])
        print("개방서비스명", item['opnSvcNm'])
        print("사업장명", item['bplcNm'])
        print("도로명주소", item['rdnWhlAddr'])
        print("인허가일자", item['apvPermYmd'])
        print("인허가취소일자", item['apvCancelYmd'])
        print("영업상태코드", item['trdStateGbn'])
        print("영업상태명", item['trdStateNm'])
        print("폐업일자", item['dcbYmd'])
        print("업태구분명", item['uptaeNm'])
        print("-------------------------")


close()
# today_open()
