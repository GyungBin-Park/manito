import bs4
from urllib.request import urlopen
import datetime as dt


def date_format(date):
    d = str(date).replace('-', '.')
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])
    return dt.date(yyyy, mm, dd)


def kospi_now():
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSPI&page=1"
    source = urlopen(url).read()
    source = bs4.BeautifulSoup(source, 'html.parser')

    # date
    date = source.find_all("td", {"class": "date"})
    date = date_format(date[0].text)

    # 전일 비교 값 차이
    # 문제 생기면 rate_up일 가능성, try_exception
    diff = source.find_all("td", {"class": "rate_down"})
    diff = str.strip(diff[0].text)

    # 실시간 코스피 가격, 전일 비교 퍼센트
    obj = source.find_all("td", {"class": 'number_1'})
    per = str.strip(obj[1].text)
    kospi_dict = {'date' : date, 'now_price' : obj[0].text, 'diff' : diff, 'plus_minus' : per[0], 'per' : per[1:]}
    # print(price[2].text)
    # print(date, price[0].text, str.strip(price[1].text))
    print(kospi_dict)
    return kospi_dict

def kosdaq_now():
    url = "https://finance.naver.com/sise/sise_index_day.nhn?code=KOSDAQ&page=1"
    source = urlopen(url).read()
    source = bs4.BeautifulSoup(source, 'html.parser')

    # date
    date = source.find_all("td", {"class": "date"})
    date = date_format(date[0].text)

    # 전일 비교 값 차이
    diff = source.find_all("td", {"class": "rate_down"})
    diff = str.strip(diff[0].text)

    # 실시간 KOSDAQ 가격, 전일 비교 퍼센트
    obj = source.find_all("td", {"class": 'number_1'})
    per = str.strip(obj[1].text)
    kosdaq_dict = {'date': date, 'now_price': obj[0].text, 'diff': diff, 'plus_minus': per[0], 'per': per[1:]}

    print(kosdaq_dict)
    return kosdaq_dict


def nasdaq_now():
    url = "https://finance.naver.com/world/sise.naver?symbol=NAS@IXIC"
    source = urlopen(url).read()
    source = bs4.BeautifulSoup(source, 'html.parser')

    # NASDAQ 실시간 현재가
    price = source.find_all("p", {"class": 'no_today'})
    price = str.strip(price[0].text)

    # up은 class : no_up
    # down은 class : no_down
    obj = source.find_all("em", {"class": 'no_up'})

    try:
        # 에러가 발생할 가능성이 있는 코드
        # no_up은 up 상태일 때만 발생, 그래서 down일 상태에는 IndexError이 생김.
        diff = str.strip(obj[1].text)
        per = str.strip(obj[2].text)
    except IndexError:  # 에러 종류
        obj = source.find_all("em", {"class": 'no_down'}) # 나스닥 전일 기준 down!
        diff = str.strip(obj[1].text)
        per = str.strip(obj[2].text)
    per = per.strip('()')           # 괄호 지우기
    per = per.replace("\n", "")     # str 안의 엔터 지우기

    nasdaq_dict = {'now_price' : price, 'diff' : diff, 'plus_minus' : per[0], 'per' : per[1:]}
    # print(price, diff, per)
    print(nasdaq_dict)
    return nasdaq_dict


def kospi200_now():
    url = "https://finance.naver.com/sise/sise_index_day.naver?code=KPI200"
    source = urlopen(url).read()
    source = bs4.BeautifulSoup(source, 'html.parser')

    # date = source.find_all("td", {"class": "date"})
    # date = date_format(date[0].text)
    #
    # price = source.find_all("td", {"class": 'number_1'})
    # dict3 = {'date': date, 'now_price': price[0].text, 'yes_price': price[1].text}

    # date
    date = source.find_all("td", {"class": "date"})
    date = date_format(date[0].text)

    # 전일 비교 값 차이
    diff = source.find_all("td", {"class": "rate_down"})
    diff = str.strip(diff[0].text)

    # 실시간 kospi200 가격, 전일 비교 퍼센트
    obj = source.find_all("td", {"class": 'number_1'})
    per = str.strip(obj[1].text)
    kospi200_dict = {'date': date, 'now_price': obj[0].text, 'diff': diff, 'plus_minus': per[0], 'per': per[1:]}

    #print(date, price[0].text, str.strip(price[1].text))
    print(kospi200_dict)
    return kospi200_dict
